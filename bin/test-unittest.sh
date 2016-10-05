#!/usr/bin/env bash

BASEDIR=`dirname $0`/..

if [ ! -f "$BASEDIR/env/bin/activate" ]; then
    echo a
else
    echo b
fi