#!/bin/bash
 
if [ "$1" = "--help" ]; then
    echo -b "This command execute the tests of a python file. The tests are find using prefix and postfix indicated. This"
    echo "command need a special package in feora it is named inotify-tools."
    echo ""
    echo "Usage:"
    echo "    continous-test.sh [--env[ <path-activate-virtualenv>]] [--src <path-to-source>] [--test <path-to-test>]"
    echo "        [--prefix <test-prefix>] [--postfix <test-postfix> [--filter <test-filter>] [--check]"
    echo "    continous-test.sh --check"
    echo "    continous-test.sh --help"
fi
if [ "$1" = "--check" ]; then
  if ! rpm -qa | grep -qw inotify-tools; then
    echo "Installing requisites"
    sudo dnf install inotify-tools
  fi
  exit 0
fi
 
 
if [[ $# == 1 ]]
then
  if [[ "$1" == "-h" ]]
  then
    echo -n " $0 [--env[ <path-activate-virtuaenv>]] [--src <path-to-source>] [--test <path-to-test>] "
    echo "[--prefix <test-prefix>] [--postfix <test-postfix> [--filter <test-filter>]"
    exit 0
  fi
fi
 
 
# Colores
RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m'
 
# fichero de fuentes para inspeccionar
SOURCE_DIR='.'
# ficheros de test para buscar el test
TEST_DIR='.'
# prefijo y postfijo del test
PREFIX="test_"
POSTFIX=""
# comando del test %s irá el nombre del test
TEST_COMMAND="python -m unittest %s"
# Filtro posix para ignorar ficheros. Este esta puesto para ignorar los ficheros temporales de intellij
FILTER="___$"
# Operaciones a observar, 'attrib,modify' para intellij
WATCH_OP='attrib,modify'
 
n_arg=$#
for ((n_arg=1; n_arg<=$#;n_arg++))
do
  arg=${!n_arg}
  case ${arg} in
    --env)
      ((n_arg++))
      arg=${!n_arg}
      if [[ "$arg" == --* ]]
      then
        env=env/bin/activate
        ((n_arg--))
      else
        env=${arg}/bin/activate
      fi
      printf "Activating virtual env: "
      printf "$env\n"
      set -e
      source ${env}
      set +e
      ;;
    --src)
      ((n_arg++))
      SOURCE_DIR=${!n_arg}
      ;;
    --test)
      ((n_arg++))
      TEST_DIR=${!n_arg}
      ;;
    --prefix)
      ((n_arg++))
      PREFIX=${!n_arg}
      ;;
    --postfix)
      ((n_arg++))
      PREFIX=${!n_arg}
      ;;
    --filter)
      ((n_arg++))
      PREFIX=${!n_arg}
      ;;
  esac
 
done
 
echo "Configuration: "
if [ -n "$env" ]; then
  echo " * Virtualenv: $env"
fi
echo " * source dir: $SOURCE_DIR"
echo " * test dir: $TEST_DIR"
echo " * file name test prefix: $PREFIX"
echo " * file name test postfix: $POSTFIX"
echo " * file filter: $FILTER"
# Cheking requisites
if [ ! -d ${TEST_DIR} -o ! -d ${SOURCE_DIR} ]; then
  echo "Some configuration is not correct (Source or test dir)"
  exit 1
fi
 
 
function test_src (){
 
  while :;do
      #Waiting to modifcation
      inotify_results=$(inotifywait -r -e ${WATCH_OP} --exclude ${FILTER} ${SOURCE_DIR} 2>/dev/null)
      results=$(echo ${inotify_results} | grep py$ | cut -d ' ' -f 3 | rev | cut -d '/' -f 1 | cut -d '.' -f 2- | rev )
      n_test=0
      n_test_failed=0
      tests_failed=()
      for file_name in $results
      do
          test_file_name=$PREFIX$file_name$POSTFIX".py"
          test_path=$(find ${TEST_DIR} | grep ${test_file_name}$ )
          if [ "$test_path" != "" ]; then
              echo ""
              echo " * File modified: '$file_name', searching tests with the name '$test_file_name'"
              echo " * Running tests: "
              printf '%s\n' "${test_path[@]}"
              echo ""
              echo "--------------START TESTS----------------"
              echo ""
 
              for test_file in $test_path
              do
                  my_test_file=${test_file#./}
                  test_command=$(printf "$TEST_COMMAND\n" "${my_test_file}")
                  echo "---------------------"
                  echo "TEST: '$test_command'"
                  echo "---------------------"
                  eval ${test_command}
                  result=$?
                  n_test=$((n_test+1))
                  sleep 0.1
                  if [ ${result} -ne 0 ]; then
                      n_test_failed=$((n_test_failed+1))
                      tests_failed+=($test_file)
                  fi
              done
 
              echo ""
              echo "--------------END TESTS----------------"
          fi
      done
 
      if [ ${n_test} -ne 0 ]; then
          echo "Results: "
          DATE=`date +"%Y-%m-%dT%H:%M:%S"`
          echo "Tests faileds: $n_test_failed/$n_test"
          if [ ${n_test_failed} -eq 0 ]; then
              printf "${GREEN}TESTS: OK${NC} (${DATE})\n"
          else
              printf ' %s\n' "${tests_failed[@]}"
              printf "${RED}TESTS: FAIL${NC} (${DATE})\n"
          fi
 
      fi
  done
}
 
 
function test_tests {
 
  while :;do
      #Waiting to modifcation
      inotify_results=$(inotifywait -r -e ${WATCH_OP} --exclude ${FILTER} ${TEST_DIR} 2>/dev/null)
      echo $inotify_results
      results=$(echo ${inotify_results} | cut -d ' ' --output-delimiter='' -f 1,3)
      results=$(echo ${results} | grep py$)
      n_test=0
      n_test_failed=0
      tests_failed=()
      for file_name in $results
      do
          if [ "$file_name" != "" ]; then
              echo ""
              echo " * File modified: '$file_name', Running test:"
              echo ""
              echo "--------------START TESTS----------------"
              echo ""
 
              test_command=$(printf "$TEST_COMMAND\n" "${file_name}")
              echo "---------------------"
              echo "TEST: '$test_command'"
              echo "---------------------"
              eval ${test_command}
              result=$?
              n_test=$((n_test+1))
              if [ ${result} -ne 0 ]; then
                  n_test_failed=$((n_test_failed+1))
                  tests_failed+=(${test_file})
              fi
              echo ""
              echo "--------------END TESTS----------------"
          fi
      done
 
      if [ ${n_test} -ne 0 ]; then
          echo "Results: "
          DATE=`date +"%Y-%m-%dT%H:%M:%S"`
          echo "Tests faileds: $n_test_failed/$n_test"
          sleep 0.1
          if [ ${n_test_failed} -eq 0 ]; then
              printf "${GREEN}TESTS: OK${NC} (${DATE})\n"
          else
              printf ' %s\n' "${tests_failed[@]}"
              printf "${RED}TESTS: FAIL${NC} (${DATE})\n"
          fi
 
      fi
  done
}
 
function input {
  while :;do
    read input
    if [ "$input" == "exit" ];
    then
      file=$(echo $0 | rev | cut -d '/' -f1 | rev)
      $(killall ${file} inotifywait)
      exit 0
    elif [ "$input" == "test" ];
    then
      test_path="$TEST_DIR/$PREFIX*$POSTFIX"
      temp="/"
      test_path=${test_path/\/\//${temp}}
      echo $test_path
      cmd=$(printf "$TEST_COMMAND\n" "${test_path}")
      eval ${cmd}
 
    fi
  done
}
test_src &
test_tests &
input

