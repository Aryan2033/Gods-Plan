# normal list function

def normal_numbers():

    normal=[]

    for i in range(10):
        normal.append(i)

    return normal

# generator function

def generator_numbers():

    for i in range(10):
        yield i

#normal list function

print("normal numbers:")
result= normal_numbers()
print(result)


# generator function

print("generator numbers:")

output= generator_numbers()

for value in output:
    print(value)
