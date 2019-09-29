#different ways to import another module from another file 
import helper
from helper2 import * # or use -- from helper2 import is_lessthan -- for specific used

msg = 'I said Warning'

helper.display (msg,True) #from helper
num1 = int(input('Number 1 : '))
num2 = int(input('Number 2 : '))

boool= is_lessthan(num1,num2) #from helper 2 
print(str(num1)+' is less than '+ str(num2) +' = '+ str(boool))


