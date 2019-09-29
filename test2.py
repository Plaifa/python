from datetime import datetime , timedelta

current = datetime.now()

print('Today is '+ str(current))
oneday = timedelta(days=1)
ytd = current - oneday
print ('Yesterday is '+ str(ytd))

oneweek = timedelta(weeks=1)
lastw = current - oneweek
print ('last week is '+ str(lastw))

print('-------------------------')

print('Day : '+ str(current.day) )
print('Month : '+ str(current.month))
print('Year : '+ str(current.year))
print('Time : '+ str(current.hour) +':'+str(current.minute))

birth = input('Enter birthday (dd/mm/yyy) :')
birthday = datetime.strptime(birth,'%d/%m/%Y')
print('Birth = '+str(birthday))