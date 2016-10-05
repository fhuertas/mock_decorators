#!/bin/bash -e

BASEDIR=`dirname $0`/..

if [ ! -d "$BASEDIR/env" ]; then
    virtualenv -p python3 -q $BASEDIR/env

    source $BASEDIR/env/bin/activate

    pip install -r $BASEDIR/requirements.txt
    pip install -e $BASEDIR
else
    source $BASEDIR/env/bin/activate
    echo "Virtualenv activated."

    pip install -r $BASEDIR/requirements.txt
    pip install -e $BASEDIR
fi
