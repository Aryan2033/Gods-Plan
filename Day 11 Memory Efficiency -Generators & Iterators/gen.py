numbers=[x*x for x in range(10)] #list comprehension
print(numbers)

numbers=(x*x for x in range(10)) #generator expression
print(numbers)
for number in numbers:
    print(number)


#if range is large like 1000000, list will consume a lot of memory while generator will not as it generates one value at a time