"""
Task 4: Petya, Katya and Seryozha make cranes out of paper. Together they made S cranes.
How many cranes did each child make, if it is known that Petya and Seryozha made the same number of cranes,
and Katya made twice as many cranes as Petya and Seryozha together?
"""
"""
s = int(input("Enter a number: "))
x = s // 6

p = x
k = (x + x) * 2
c = x

print(p, k, c)
"""
"""
Task 2: Find the sum of the digits of a three-digit number.
"""

"""
n = int(input("Enter a three digit number: "))
a = n // 100
b = (n % 100) // 10
c = n % 10

sum = a + b + c
print(sum)
"""

"""
Task 6: Do you use public transport? You probably paid for the fare and received a ticket with a number. 
A lucky ticket is a ticket with a six–digit number, where the sum of the first three digits is equal to the sum of the last three. 
I.e., a ticket with the number 385916 is a lucky one, because 3+8+5=9+1+6. 
You need to write a program that checks the ticket's happiness.
"""

"""
n = input (("Enter a number: "))
s1 = int(n[0]) + int(n[1]) + int(n[2])
s2 = int(n[3]) + int(n[4]) + int(n[5])
if s1 == s2:
    print("Yes")
else:
    print("No")
"""


"""
Task 8: It is required to determine whether it is possible to break off k lobules from a chocolate bar with a size of n × m lobules, 
if it is allowed to make one break in a straight line between the lobules (that is, to break the chocolate bar into two rectangles).
"""

"""
n = int(input("Enter length: "))
m = int(input("Enter width: "))
k = int(input("Enter a number of slices: "))
if k % n == 0 or k % m == 0:
    print("Yes")
else: 
    print("No")
"""









