#Basics
for i in range(151):
    print(i)
#Multiples of Five
for x in range(5,1001,5):
    print(x)
#Counting, the Dojo Way
for y in range(1,101):
    if y % 10 == 0:
        print("Coding Dojo")
    elif y % 5 == 0:
        print("Coding")
    else: 
        print(y)
#Whoa. That Sucker's Huge
sum = 0
for s in range(0,500001,2):
    sum+= s
print(sum)
#Countdown by Fours
for p in range(2018,-1,-4):
    print(p)
#Flexible Counter
lowNum = 2
highNum = 9
mult = 3
for k in range(lowNum, highNum + 1):
    if k % mult == 0:
        print(k)