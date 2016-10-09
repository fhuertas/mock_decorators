#!/bin/bash -e

BASEDIR=`dirname $0`/..

mkdir -p dist

echo "Building wheel..."
"$BASEDIR/env/bin/python" setup.py bdist_wheel

echo "Building egg..."
"$BASEDIR/env/bin/python" setup.py sdist

VERSION=`cat $BASEDIR/VERSION`
