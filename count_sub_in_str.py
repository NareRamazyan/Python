def count_sub_in_str(string_obj, substring):
    count = 0

    for i in range(len(string_obj)):
        if string_obj[i:i+len(substring)] == substring:
            count = count + 1
    return count

string_obj = "hihihihihi"
substring = "hi"

result = count_sub_in_str(string_obj, substring)
print(result)
