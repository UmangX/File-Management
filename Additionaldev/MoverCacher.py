from os import path


def checker():
    file = open('cache.txt', 'r') 
    data = file.readlines(1)
    if data != []:
        print('File Has Some Shit')
        file.close()
    else:
        file = open('cache.txt','a+') 
        file.write("data is here")
        file.close()

if path.exists('cache.txt') == False:
    filec = open('cache.txt','w+')
    filec.close()
    checker()
else:
    checker()   
       


