[![Build Status](https://travis-ci.org/fhuertas/mock_decorators.svg?branch=master)](https://travis-ci.org/fhuertas/mock_decorators)
[![Coverage Status](https://coveralls.io/repos/github/fhuertas/mock_decorators/badge.svg?branch=master)](https://coveralls.io/github/fhuertas/mock_decorators?branch=master)
# Python decorators for mocking

This module contains a set of decorators that allow to mock functions. (Replacing the behavior of a method, attribute, object or class)

## Requisites

This module has been created using python 3.4 and tested in python 2.7, 3.4 and 3,5. This should works in python 2.7 and higher. If you want to know if this module works
in a concrete python version, download the project and execute:

`make test PYTHON_VERSION=<python-version>`

where <python-version> is the version to test. Note: you must be installed that version. 

## Change log: 

**1.0**:

* Created the mocks, documentation.

**1.0.1**:

* Revise compatibility of ClassMock in python 2.7
* Update with coverage report

**1.0.2-1.0.4**
* Improved python 2 compatibility
* Adapted to Pypi public repository

**1.0.5**
* Added Mocks for dictionaries
* FIX: now ClassMock is reported correctly that it doesn't work in python 2

**1.0.6**
* Added mock for check if a function is called
* FIX: `make test-versions` makes tests for python 2 and 3

**1.0.7**
* FunctionMockCheckCall can return a value instead invoke the function

**1.0.9**
* FunctionMockCheckCall now check 0 invocations
* Fix: FunctionMockCheckCall checks if the value to return is None and not a condition
* Fix: the checks in the FunctionMockCheckCall

**1.1.0**
* New Mock. MockSysOutput catch the system output in a Stream 
* Fix documentation of FunctionMockCheckCall

## Installation

This module can be installed using the following options:
* From Pypi, using the following command `pip install mock_decorators`
* From respository: `pip install git+https://github.com/fhuertas/mock_decorators (for master version)`

## Usage

The tests contain examples to use this library but here there are the more useful examples: 

### FunctionMock

This mock replace a function for other. [Example](https://github.com/fhuertas/mock_decorators/blob/1.1.0/tests/mock_decorators/test_function_mock.py#L18) 

The parameters are the following: 

* **entity**: The module, class or object that you can replace the function. 
* **function_name**: The name string of the function to replace.
* **mocked_function**: The function that you can use. 
* **check_signature**: (*optional, true by default*) Check if the signature of the original function and the mocked mock function is the same
 
### FunctionMockResult

This mock replace a function for a result value. [Example](https://github.com/fhuertas/mock_decorators/blob/1.1.0/tests/mock_decorators/test_function_mock.py#L167)

The parameters are the following: 

* **entity**: The module, class or object that you can replace the function.
* **function_name**: The name string of the function to replace.
* **result**: The result of the mocked function 
* **checkExists**: (*optional, True by default*): Check if the original function exists 

### FunctionMockChangeResult

This mock modify the result of a function. i.e. if Add 2 to a result of a function. 
[Example](https://github.com/fhuertas/mock_decorators/blob/1.1.0/tests/mock_decorators/test_function_mock.py#L220)

The parameters are the following:
* **entity**: The module, class or object where the function is.
* **function_name**: The function where you can modify the result 
* **fn**: The function to apply to the original function

### FunctionMockCheckCall

This mock checks if a function is called or not and optionally the times that it is called. By default the function is invoked but instead a value can be returned
[Example](https://github.com/fhuertas/mock_decorators/blob/1.1.0/tests/mock_decorators/test_function_mock.py#L18)

The parameters are the following:
* **entity**: The module, class or object where the function is.
* **function_name**: The function where you can modify the result 
* **expected_times** (*optional, None by default*): Expected number times that the function should be called. None checks if the function is called but not the times that it is invoked
* **return_value** (*optional, None by default*): Return a value instead call to the function, if None, the function is called

## AttributeMock

This mock change the value of a attribute for other. [Example](https://github.com/fhuertas/mock_decorators/blob/1.1.0/tests/mock_decorators/test_attribute_mock.py#L8)

The parameters are the following: 

* **entity**: The module, class or object that you can replace the attribute.  
* **attribute_name**: The name of the attribute 
* **value**: New value


## ClassMock

This mock only work in python 3 and higher. This mock replace a class or object by other. [Example](https://github.com/fhuertas/mock_decorators/blob/1.1.0/tests/mock_decorators/test_class_mock.py#L24) 

The parameters are the following:
* **old_class_name**: The original object/class that you can replace
* **new_class**: The new object/class


## DictMock

This mock replace a value in a map by other value. [Example](https://github.com/fhuertas/mock_decorators/blob/1.1.0/tests/mock_decorators/test_dict_mock.py#L7) 

The parameters are the following:
* **entity_dict**: The original dictionary
* **key**: The key to replace the value
* **value**: The new value
* **check**: (*optional, false by default*) Check if the dictionary has the value of the key

## MockIoRedirect

This mock catch the system output in a Stream. It is desirable that it is a StringIO. [Example](https://github.com/fhuertas/mock_decorators/blob/1.1.0/tests/mock_decorators/test_mock_sys_output.py#L27) 
 
The parameters are the following:
* **text_io_wrapper**: The stream where the output will be saved
