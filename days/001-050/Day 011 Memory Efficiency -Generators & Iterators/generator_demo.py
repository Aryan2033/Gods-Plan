# normal list function

def normal_numbers():

    normal=[]

    for i in range(10):
        normal.append(i)

    return normal

# generator function

def generator_numbers():

    for i in range(10):
        yield i #python pauses the state of the function and returns the value, when the next value is requested it continues from where it left off

#normal list function

print("normal numbers:")
result= normal_numbers()
print(result)


# generator function

print("generator numbers:")

output= generator_numbers()

for value in output:
    print(value)


