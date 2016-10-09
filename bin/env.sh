#!/bin/bash -e

BASEDIR=`dirname $0`/..

virtualenv -p python3 -q $BASEDIR/env

source $BASEDIR/env/bin/activate

pip install -r $BASEDIR/requirements.txt
pip install -e $BASEDIR

