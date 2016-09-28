'''
Created on Sep 28, 2016

@author: cgabhane
'''
print "Enter age"
a=input()
print "Enter M/F"
b=raw_input( )
print "Marital staus (Y|N)"
c=raw_input( )
if b == "F" and a>=20 and a<=60:
    print "Urban areas only"
elif b=="M" and a>=20 and a<=40:
    print "work anywhere"
elif b=="M"and a>=40 and a<=60:
    print "Men urban areas only"
else:
    print "ERROR"
