#!/bin/bash
PATH=$(dirname "$0")

cd $PATH &&
source crypto/bin/activate &&
python entry_checker.py