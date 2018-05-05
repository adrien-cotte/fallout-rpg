#!/bin/bash

path=$(realpath ${BASH_SOURCE})
dir=${path/env.sh}
export PATH=$dir:$PATH
export PYTHONPATH=$dir/../lib:$PYTHONPATH
