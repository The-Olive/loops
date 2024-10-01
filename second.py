a = True
b = False
c = False

if not a or b:
    print(1)
elif not a or not b and c:
    print(2)
elif not a or b or not b and a:
    print(3)
else:
    print(4)

print('')

def menu(choice):
    var1 = 'Me'
    var2 = 'You'
    if(choice == 1):
        return var1
    else:
        return var2

print(menu(3))