#Countdown
def countdown(start):
    array=[]
    for i in range(start,-1,-1):
        array.append(i)
    print(array)
countdown(5)
#Print and Return
def print_return(num1,num2):
    print(num1)
    return num2
print_return(1,2)
#First Plus Length
def first_plus_length(array):
    sum = 0
    for i in range(0,len(array)-1,1):
        sum=array[0]+len(array)
    print(sum)
first_plus_length([1,2,3,4,5])
#Values Greater than Second
def values_greater_than_second(array):  
    if len(array)<2 :
        return False
    newlist=[]
    for i in range(0,len(array)):
        if array[i] > array[1]:
            newlist.append(array[i])
    return len(newlist)
print(values_greater_than_second([5,5,8,9,8,7,1]))
#This Length, That Value
def length_and_value(size,value):
    return [value]*size
print(length_and_value(4,7))