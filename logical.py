# and operator
#example 1
x = 5 
print(x > 3 and x < 10)#true, coz both are true
#Example 2
y = 12
print(y > 11 and y % 5 ==1 ) #false, coz the second one is false

#or operator
s = 6
print(s < 4 or s > 11) #False, coz both are false

d = 8
print(d < 5 or d % 2 == 0) #True, coz second condition is true

#not operator
e = 5
print(not(x > 2 and x < 9)) #False, coz the condition inside the not is true

f = 9
print (not(f < 11 or f % 5 ==0)) #False, coz the condition inside the not is true

