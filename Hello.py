##Functions Principles
 # Functionds only do one job
 # Functions should be unitary
 # Functions should do the above so they're testable
 # DO NOT PRINT inside functions. you return.
 # Functions need to be called to run.

# Unit tests
# these are tests, that test 1 function

# TDD - Test Driven Development
# write your tests, according to specs
# Then folow the errors and iterate until test pass.

def say_hello():
    return 'hello'

def say_hello_personal(name_arg):
    return 'hello ' + name_arg.capitalize()
    # This is a block of code

print(say_hello())
print(say_hello_personal('Isabella Jones'))

## Testing
# has two main sections: Setup and Evaluation
# you give it controlled input and test for expected outcomes

## Test 1 - test say hello function
# spec - when call should return string 'hello'
print("test say hello function, when call should return string 'hello'")
setup_result = say_hello()
print(setup_result == 'hello')

##Test 2 - testing  say hello perosnalise function
print("test say hello function, when call should take in on argument and return string 'hello' + argument")
print('testing with isabella')

print(say_hello_personal('isabella') == 'Hello Isabella')



### Test 3 - testing function full name hello
print("calling function full_name_hello() with Isabella jones, expect'hello Isabella Jones' to be printed")

print(full_name_hello('isabella', ''))








