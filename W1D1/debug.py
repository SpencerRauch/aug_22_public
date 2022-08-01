def multiply(num_list, num):
    # print(num_list,num)
    for index in range(len(num_list)):
        # print(x)
        num_list[index] *= num
        # print(num_list)
    return num_list
a = [2,4,10,16]
b = multiply(a,5)
print(b)