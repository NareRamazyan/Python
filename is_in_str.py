def is_in_str(str_obj, sub_string):
    if sub_string in str_obj:
        return True
    return False

string = "Hello World"
print("string =", string)
substring = input("substring = ")

result = is_in_str(string, substring)

print(result)
