'''Please-Pass-the-Coded-Messages
==============================
You need to pass a message to the bunny prisoners, but to avoid detection, the code you agreed to use is… 
obscure, to say the least. The bunnies are given food on standard-issue prison plates that are stamped with the 
numbers 0-9 for easier sorting, and you need to combine sets of plates to create the numbers in the code. The signal 
that a number is part of the code is that it is divisible by 3. You can do smaller numbers like 15 and 45 easily, 
but bigger numbers like 144 and 414 are a little trickier. Write a program to help yourself quickly create large numbers
for use in the code, given a limited number of plates to work with.

You have L, a list containing some digits (0 to 9). Write a function answer(L) which finds the largest number that can be 
made from some or all of these digits and is divisible by 3. If it is not possible to make such a number, return 0 as the answer.
L will contain anywhere from 1 to 9 digits. The same digit may appear multiple times in the list, but each element in the list
may only be used once.


Languages
==========
To provide a Python solution, edit solution.py To provide a Java solution, edit solution.java

Test cases
==========
Inputs:
    (int list) l = [3, 1, 4, 1]
Output:
    (int) 4311

Inputs:
    (int list) l = [3, 1, 4, 1, 5, 9]
Output:
    (int) 94311
   
 SOLUTION:'''
 
 def answer(l):
    i=0
    sum=0
    for i in range(len(l)):
        sum=sum+l[i]
    remainder=sum%3
    ans=0
    if(remainder==0):
        l.sort(reverse=True)
        for i in range(len(1)):
            ans=ans*10+l[i]
        return(ans)
    if(remainder==1):
        if(1 in l):
            l.remove(1)
        elif(4 in l):
            l.remove(4)
        elif(7 in l):
            l.remove(7)
        elif(l.count(2)>=2):
            l.remove(2)
            l.remove(2)
        elif(2 in l and 5 in l):
            l.remove(2)
            l.remove(5)
        elif(l.count(5)>=2):
            l.remove(5)
            l.remove(5)
        elif(2 in l and 8 in l):
            l.remove(2)
            l.remove(8)
        elif(5 in l and 8 in l):
            l.remove(5)
            l.remove(8)
        elif(l.count(8)>=2):
            l.remove(8)
            l.remove(8)
        else:
            return (0)
        l.sort(reverse=True)
        for i in range(len(1)):
            ans=ans*10+l[i]
        return(ans)
    if(remainder==2):
        if(2 in l):
            l.remove(2)
        elif(5 in l):
            l.remove(5)
        elif(8 in l):
            l.remove(8)
        elif(l.count(1)>=2):
            l.remove(1)
            l.remove(1)
        elif(1 in l and 4 in l):
            l.remove(1)
            l.remove(4)
        elif(l.count(4)>=2):
            l.remove(4)
            l.remove(4)
        elif(1 in l and 7 in l):
            l.remove(1)
            l.remove(7)
        elif(4 in l and 7 in l):
            l.remove(4)
            l.remove(7)
        elif(l.count(7)>=2):
            l.remove(7)
            l.remove(7)
        else:
            return(0)
        l.sort(reverse=True)
        for i in range(len(l)):
            ans=ans*10+l[i]
        return(ans)



