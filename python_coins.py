counter = 0
coins = "yes"
while coins == "yes":
    print('You have %d coins' % counter)
    coins = input('Do you want another? ''(yes/no) ')
    counter += 1
if coins == "no":
    print('Bye')

         
