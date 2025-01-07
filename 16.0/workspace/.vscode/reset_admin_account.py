#!/usr/bin/env python3
"""
Odoo Admin Account Reset Script
------------------------------

This script provides functionality to reset admin or other user accounts in Odoo.
It supports customizing credentials and includes safety features like dry-run mode.

Usage:
    python reset_admin_account.py --database your_db [options]

Options:
    --user-id: ID of the user to reset (default: 2 for admin)
    --login: New login (default: 'admin')
    --password: New password (default: 'admin')
    --name: New display name (default: 'Admin')
    --dry-run: Show what would be changed without making changes
    --force: Skip confirmation prompt
    --reset-2fa-only: Only reset 2FA settings
    --reset-password-only: Only reset password
"""

import logging
from typing import Any, Tuple

import click
import click_odoo

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
_logger = logging.getLogger(__name__)


class AdminAccountResetter:
    """
    Handles resetting of user accounts.
    """

    def __init__(self, env: Any):
        """
        Initialize the resetter with Odoo environment.

        Args:
            env: Odoo environment
        """
        self.env = env

    def check_user_status(self, user_id: int) -> Tuple[bool, str]:
        """
        Check current status of user account.
        
        Args:
            user_id: ID of the user to check
            
        Returns:
            Tuple of (is_ok, message)
        """
        user = self.env['res.users'].browse(user_id)
        if not user.exists():
            return False, f"User ID {user_id} not found in database"
            
        status_messages = []
        
        if not user.active:
            status_messages.append("Account is currently inactive")
            
        if user.totp_secret:
            status_messages.append("2FA is currently enabled")
            
        if user.login_date:
            status_messages.append(f"Last login: {user.login_date}")
            
        return True, " | ".join(status_messages) if status_messages else "Account status OK"

    def reset_user(
        self,
        user_id: int,
        login: str = 'admin',
        password: str = 'admin',
        name: str = 'Admin',
        dry_run: bool = False,
        reset_2fa_only: bool = False,
        reset_password_only: bool = False
    ) -> bool:
        """
        Reset user account with specified settings.
        
        Args:
            user_id: ID of the user to reset
            login: New login
            password: New password
            name: New display name
            dry_run: If True, only show what would be changed
            reset_2fa_only: If True, only reset 2FA settings
            reset_password_only: If True, only reset password
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            user = self.env['res.users'].browse(user_id)
            if not user.exists():
                _logger.error(f"User (ID: {user_id}) not found in database")
                return False

            # Check current status
            status_ok, status_msg = self.check_user_status(user_id)
            _logger.info(f"Current user status: {status_msg}")

            # Prepare changes based on reset type
            changes = {}
            
            if reset_2fa_only:
                changes = {'totp_secret': ''}
            elif reset_password_only:
                changes = {'password': password}
            else:
                changes = {
                    'name': name,
                    'login': login,
                    'password': password,
                    'active': True,
                    'totp_secret': '',
                }

            # Show changes in dry run mode
            if dry_run:
                _logger.info("DRY RUN - Would make these changes:")
                for key, value in changes.items():
                    if key == 'password':
                        _logger.info(f"  {key}: ***")
                    else:
                        _logger.info(f"  {key}: {value}")
                return True

            # Apply changes
            user.write(changes)
            self.env.cr.commit()
            
            # Log changes
            _logger.info(f"Successfully reset user account (ID: {user_id})")
            return True

        except Exception as e:
            _logger.exception(f"Failed to reset user account: {str(e)}")
            return False


@click.command()
@click.option('--user-id', default=2, help='ID of the user to reset (default: 2 for admin)')
@click.option('--login', default='admin', help='New login')
@click.option('--password', default='admin', help='New password')
@click.option('--name', default='Admin', help='New display name')
@click.option('--dry-run', is_flag=True, help='Show what would be changed without making changes')
@click.option('--force', is_flag=True, help='Skip confirmation prompt')
@click.option('--reset-2fa-only', is_flag=True, help='Only reset 2FA settings')
@click.option('--reset-password-only', is_flag=True, help='Only reset password')
@click_odoo.env_options(default_log_level="info")
def main(
    env: Any,
    user_id: int,
    login: str,
    password: str,
    name: str,
    dry_run: bool,
    force: bool,
    reset_2fa_only: bool,
    reset_password_only: bool
) -> None:
    """
    Entry point for the user account reset script.

    Args:
        env: Odoo environment
        user_id: ID of the user to reset
        login: New login
        password: New password
        name: New display name
        dry_run: If True, only show what would be changed
        force: If True, skip confirmation prompt
        reset_2fa_only: If True, only reset 2FA settings
        reset_password_only: If True, only reset password
    """
    try:
        # Disable tracking and notifications
        context = env.context.copy()
        context["tracking_disable"] = True
        context["mail_create_nolog"] = True
        context["mail_create_nosubscribe"] = True
        context["mail_notrack"] = True
        env = env(context=context)

        resetter = AdminAccountResetter(env)
        
        # Check user status first
        status_ok, status_msg = resetter.check_user_status(user_id)
        if not status_ok:
            _logger.error(status_msg)
            return
        
        _logger.info(f"Current status: {status_msg}")

        # Confirm action unless --force is used
        if not force and not dry_run:
            if not click.confirm(f"Are you sure you want to reset user {user_id}?"):
                _logger.info("Operation cancelled by user")
                return

        success = resetter.reset_user(
            user_id=user_id,
            login=login,
            password=password,
            name=name,
            dry_run=dry_run,
            reset_2fa_only=reset_2fa_only,
            reset_password_only=reset_password_only
        )

        if not success:
            _logger.error("Failed to reset user account")
            return

    except Exception as e:
        _logger.exception(f"Reset process failed: {str(e)}")
        raise


if __name__ == "__main__":
    main()
