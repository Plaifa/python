#print("hello")
#x = 1
#y = x+5
#z = y
#print (z)
#x = z*1.0
#print(type(x))
#y = True
#print(type(y))
#x = 'string ja'
#print (x)
#print(type(x))
#y = 'This is'
#print (y,x)
#x = y +' '+ x
#print (x)
#name = input('Enter your name:')
#print('your name is : '+name)
#print ('enter sth :',end='')
#sth=input()
#print('this is '+sth)
#print(type(sth))
#sth=int(input('enter num :'))
#print(sth)
#print(type(sth))
#x = 5
#print('The number is ' + str(x))
i=1
while(i<6):
    print('------round'+str(i)+'-----')
    x=int(input ('input num 1 :'))
    y=int(input ('input num 2 :'))
    z=input('choose one operator ( + - * /)  You choose : ')
    if (z=='+'):
        sum=x+y
    elif (z=='-'):
        sum=x-y
    elif (z=='*'):
        sum=x*y
    elif (z=='/'):
        sum=x/y
    else:
            sum = 'can\'t calculate '
    print (sum)
    i=i+1