'''
Created on Sep 28, 2016
Reverse no
@author: cgabhane
'''
print "Enter 4 digit no:"
n=input()
print "Number is",n

# example n=1234
#1234/1000=1
#1234%1000=234

f=n/1000 #1234/1000=1
rem=n%1000 #1234%1000=234

s=rem/100 #234/100=2
rem=n%100 #234%100=34

t=rem/10 #34/10=3
d=rem%10 #34%10=4


new_number = (f)+(s*10)+(t*100)+(d*1000)
#new_number = 4+30+200+1000=1234
#so 1*1 + 2*10+3*100+4*1000=4321
print "reverse no. is", new_number  