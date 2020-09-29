#1
#def biggie_size (list):
    #for i in list:
        #print(i)
        #if i > 0:
            #i = "big"
#biggie_size([-1, 3, 5, -5])
#this solution does not work and I do not know why

def biggie_size (list):
    for i in range (len(list)):
        if list[i] > 0:
            list [i] = "big"
    print(list)
biggie_size([-1, 3, 5, -5])

#2
def count_positives(list):
    count = 0
    for i in range(len(list)):
        if list[i] > 0:
            count = count+1
    list[-1] = count
    print(list)
count_positives([1,6,-4,-2,-7,-2])
count_positives([-1,1,1,1])

#3
def sum_total(list):
    sum = 0
    for i in range(len(list)):
        sum = sum + list[i]
    print(sum)
sum_total([1,2,3,4])

#4
def average(arr):
    sum = 0
    for i in range(len(arr)):
        sum = sum + arr[i]
    print(sum / float(len(arr))) #float() is important to get the decimal
average([1,2,3,4])

#5
def length(arr):
    return len(arr)

#6
def minimum (arr):
    if len(arr) == 0:
        print("False")
        return False
    for i in range(len(arr)):
        if arr[i]<arr[0]:
            arr[0]=arr[i]
    print(arr[0])
minimum([37,2,1,-9])
minimum([]) 

#7
def maximum (arr):
    if len(arr) == 0:
        print("False")
        return False
    for i in range(len(arr)):
        if arr[i]>arr[0]:
            arr[0]=arr[i]
    print(arr[0])
maximum([37,2,1,-9])
maximum([]) 

#8
def ultimate_analysis(arr):
    dict = {
        'sumTotal' : sum_total(arr),
        'average' : average(arr),
        'minimum' : minimum(arr),
        'maximum' : maximum(arr),
        'length' : length(arr)
    }
    print(dict)
    return(dict)

#9
#list_elements[startAt:endBeforeThisPosition:skipInterval] 

# startAt -> if not provided, it starts at 0 
# endBeforeThisPosition -> if not provided, it is the last index 
# skipInterval -> if not provided, default is 1 (jump interval) 
def reverse_list(arr):
    arr = arr[::-1]
    print(arr)
reverse_list([37,2,1,-9])

    

