_a_global = 10

def a_function():
    _a_global = 5
    _a_local = 4
    print("Inside the function, the value is ",_a_global)
    print("Outside the function, the value is ", _a_local)
    return None

a_function()

print("Outside the function, the value is ", _a_global)