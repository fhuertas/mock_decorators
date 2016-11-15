#!/bin/bash -e

BASEDIR=`dirname $0`/..

TEST_DIR=${BASEDIR}/env-test2
echo "$TEST_DIR"
if [ ! -d "$TEST_DIR" ]; then
    virtualenv -p python3 -q $TEST_DIR
    echo "New virtualenv for UT created."

    source $TEST_DIR/bin/activate
    echo "New virtualenv for UT activated."
    pip install -r $BASEDIR/requirements.txt
    pip install -e $BASEDIR

fi

$TEST_DIR/bin/nosetests --verbosity=3 --with-coverage --cover-erase --cover-package=mock_decorators tests

TEST_DIR=${BASEDIR}/env-test3
echo "$TEST_DIR"
if [ ! -d "$TEST_DIR" ]; then
    virtualenv -p python2 -q $TEST_DIR
    echo "New virtualenv for UT created."

    source $TEST_DIR/bin/activate
    echo "New virtualenv for UT activated."
    pip install -r $BASEDIR/requirements.txt
    pip install -e $BASEDIR

fi


export COVERAGE_FILE=.coverage
$TEST_DIR/bin/nosetests --verbosity=3 --with-coverage --cover-package=mock_decorators tests
$TEST_DIR/bin/coverage xml
rm .coverage
