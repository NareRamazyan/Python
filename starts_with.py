"""
ex.7
write function for the following string operation
startswith(str_obj, sub_string)
this function should do the same as a builtin string function do
"""
def starts_with(str_obj, sub_string):
    if len(sub_string) > len(str_obj):
        return False
    if str_obj[:len(sub_string)] == sub_string: 
        return True
    return False

string = "Hello World"
print("string = ", string)
substring = input("substring = ")

result = starts_with(string, substring)

print(result)  

