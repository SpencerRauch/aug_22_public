def add(num2,num1=3):
    # if num1 > 5:
    #     return "too big Idk"
    print(f"adding {num1} and {num2}")
    return num1+num2
#parameters are in the definition
#arguments are in the call
x = 3
y = 8
sum = add(x)
print(sum)
add(4,num1=8)

#default parameters must come after others

