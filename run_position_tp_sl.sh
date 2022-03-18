#!/bin/bash
PATH=$(dirname "$0")

cd $PATH &&
source crypto/bin/activate &&
python postition_tp_sl.py