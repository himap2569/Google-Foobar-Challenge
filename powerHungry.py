'''Power Hungry
============

Commander Lambda's space station is HUGE. And huge space stations take a LOT of power. Huge space stations with doomsday devices take even more power. To help meet the station's power needs, Commander Lambda has installed solar panels on the station's outer surface. But the station sits in the middle of a quasar quantum flux field, which wreaks havoc on the solar panels. You and your team of henchmen have been assigned to repair the solar panels, but you'd rather not take down all of the panels at once if you can help it, since they do help power the space station and all!

You need to figure out which sets of panels in any given array you can take offline to repair while still maintaining the maximum amount of power output per array, and to do THAT, you'll first need to figure out what the maximum output of each array actually is. Write a function solution(xs) that takes a list of integers representing the power output levels of each panel in an array, and returns the maximum product of some non-empty subset of those numbers. So for example, if an array contained panels with power output levels of [2, -3, 1, 0, -5], then the maximum product would be found by taking the subset: xs[0] = 2, xs[1] = -3, xs[4] = -5, giving the product 2*(-3)*(-5) = 30.  So solution([2,-3,1,0,-5]) will be "30".

Each array of solar panels contains at least 1 and no more than 50 panels, and each panel will have a power output level whose absolute value is no greater than 1000 (some panels are malfunctioning so badly that they're draining energy, but you know a trick with the panels' wave stabilizer that lets you combine two negative-output panels to produce the positive output of the multiple of their power values). The final products may be very large, so give the solution as a string representation of the number.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit Solution.java

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Python cases --
Input:
solution.solution([2, 0, 2, 2, 0])
Output:
    8

Input:
solution.solution([-2, -3, 4, -5])
Output:
    60

-- Java cases --
Input:
Solution.solution({2, 0, 2, 2, 0})
Output:
    8

Input:
Solution.solution({-2, -3, 4, -5})
Output:
    60

SOLUTION:'''
	
def solution(xs):
    # Your code here
    n=len(xs)
    pro=1
    count=0
    k=0
    xs.sort(reverse=True)
    while(k<n):
        if(xs[k]==0):
            k+=1
        else:
            break
    if(k==n):
        return str(0)
            
    for i in range(n):
        if xs[i]<=0:
            break
        else:
            pro*=xs[i]
    for j in range(n-1,i-1,-1):
        if(xs[j]<0):
            count+=1
    if(count==1 and xs[i]==0 and xs[0]==0):
        return str(0)
    
    if(count==1 and xs[i-1]>0 and xs[0]>0):
        return str(pro)
        
    if(count%2==0 and count!=0):
        for i in range(n-1,i-1,-1):
            if(xs[i]<0):
                pro*=xs[i]
                count-=1 
            if(count==0):
                break
    if(count%2!=0):
        for i in range(n-1,i-1,-1):
            if(xs[i]<0):
                pro*=xs[i]
                count-=1 
            if(count==1):
                break
    return str(pro)
