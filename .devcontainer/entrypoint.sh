#!/usr/bin/env bash

find /workspace -name "requirements.txt" -exec pip3 install -r {} \;

sleep infinity