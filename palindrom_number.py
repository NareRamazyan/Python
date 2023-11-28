number = int(input("number = "))

num_str = str(number)

if num_str == num_str[::-1]:
    print("the number is palondrom")
else:
    print("the number is not palindrom")
