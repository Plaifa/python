#force First letter of Name to uppercase and show it
def get_init(name,force_upper= True):
    if force_upper :
        init = name[0:1].upper()
    else:
        init = name[0:1]
    return init

def display(msg,Is_P):
    if Is_P:
        print ('First letter Is P!')
    else:
        print(msg)


Name = input ('Enter Name :')
InitName = get_init(Name)
if InitName == 'P':
    Is_P = True
else:
    Is_P = False
display(InitName,Is_P)
    

