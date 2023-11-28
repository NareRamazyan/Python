def ends_with(str_obj, sub_string):
    if len(sub_string) > len(str_obj):
        return False
    if str_obj[-len(sub_string):] == sub_string:
        return True
    return False

string = "Hello World"
print("string =", string)
substring = input("substring = ")

result = ends_with(string, substring)

print(result)
