# Python decorators for mocking

This module contains a set of decorators that allow to mock functions. (Replacing the behavior of a method, attribute, object or class)

## Requisites

This module has been created using python 3.4 and tested in python 2.7, 3.4 and 3,5. This should works in python 2.7 and higher. If you want to know if this module works
in a concrete python version, download the project and execute:

`make test PYTHON_VERSION=2.6`

you can replace 2.6 for the version as you want to test. Note that you must be installed this version. 

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
* FIX: now ClassMock is reperted correctly that it doesn't work in python 2

## Installation

This module can be installed using the following options:
* From Pypi, using the following command `pip install mock_decorators`
* From respository: `pip install git+https://github.com/fhuertas/mock_decorators (for master version)`

## Usage

The tests contain examples to use this library but here there are the more useful examples: 

### FunctionMock

This mock replace a function for other. [Example](https://github.com/fhuertas/mock_decorators/blob/1.0.5/tests/mock_decorators/test_function_mock.py#L18) 

The parameters are the following: 

* **entity**: The module, class or object that you can replace the function. 
* **function_name**: The name string of the function to replace.
* **mocked_function**: The function that you can use. 
* **check_signature**: (*optional, true by default*) Check if the signature of the original function and the mocked mock function is the same
 
### FunctionMockResult

This mock replace a function for a result value. [Example](https://github.com/fhuertas/mock_decorators/blob/1.0.5/tests/mock_decorators/test_function_mock.py#L114)

The parameters are the following: 

* **entity**: The module, class or object that you can replace the function.
* **function_name**: The name string of the function to replace.
* **result**: The result of the mocked function 
* **checkExists**: (*optional, True by default*): Check if the original function exists 

### FunctionMockChangeResult

This mock modify the result of a function. i.e. if Add 2 to a result of a function. 
[Example](https://github.com/fhuertas/mock_decorators/blob/1.0.5/tests/mock_decorators/test_function_mock.py#L18)

The parameters are the following:
* **entity**: The module, class or object where the function is.
* **function_name**: The function where you can modify the result 
* **fn**: The function to apply to the original function

## AttributeMock

This mock change the value of a attribute for other. [Example](https://github.com/fhuertas/mock_decorators/blob/1.0.5/tests/mock_decorators/test_attribute_mock.py#L8)

The parameters are the following: 

* **entity**: The module, class or object that you can replace the attribute.  
* **attribute_name**: The name of the attribute 
* **value**: New value


## ClassMock

This mock only work in python 3 and higher. This mock replace a class or object by other. [Example](https://github.com/fhuertas/mock_decorators/blob/1.0.5/tests/mock_decorators/test_class_mock.py#L24) 

The parameters are the following:
* **old_class_name**: The original object/class that you can replace
* **new_class**: The new object/class


## DictMock

This mock replace a value in a map by other value. [Example](https://github.com/fhuertas/mock_decorators/blob/1.0.5/tests/mock_decorators/test_dict_mock.py#L7) 

The parameters are the following:
* **entity_dict**: The original dictionary
* **key**: The key to replace the value
* **value**: The new value
* **check**: (*optional, false by default*) Check if the dictionaty has the value of the key
