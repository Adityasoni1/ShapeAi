import hashlib

# initializing string

str2hash = "Hello adi"

# encoding using encode()

# then sending to md5()

result = hashlib.md5(str2hash.encode())

# printing the equivalent hexadecimal value

print("The hash is : ", end ="")

print(result.hexdigest())
