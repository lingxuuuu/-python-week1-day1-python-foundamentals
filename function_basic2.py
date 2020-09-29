#1
def countDown (num):
    for i in range (num, -1, -1):
        print(i)
countDown(5)

#2
def print_and_return(a):
    print(a[0])
    return(a[1])
print_and_return([1,2])

#3
def first_plus_length(a):
    var_sum = 0
    var_sum = a[0] + len(a)
    #print(var_sum)
    return var_sum
first_plus_length([1,2,3,4,5])    

#4
def values_greater_than_second(list):
    count = 0
    new_list = []
    if len(list) < 2:
        #print("False")
        return False
    for i in (list):
        if i > list[1]:
            count = count + 1
            new_list.append(i)
    print(count)
    #print(new_list)
    return new_list
values_greater_than_second([5,2,3,2,1,4])
values_greater_than_second([3]) 

#5
arr = []
def  length_and_value (size, value):
    for i in range (0, size, 1):
        arr.append(value)
    #print(arr)
    return arr
length_and_value(4,7)
