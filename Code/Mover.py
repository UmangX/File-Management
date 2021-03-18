#Personal Project By Umangx.cf


from os import listdir 
from os import chdir
from os import system
from getpass import getuser


#gets the username for windows
user = getuser()


#the download directory 
Download = ('C:/Users/'+user+'/Downloads/')

#changes the pwd to the Download directory 
chdir(Download)


#the main directory to move to //user-specific where the images should be stored 
des = ('d:/os') 

#gets the list of files
files = listdir()


def moveimages(i):
	#checks for file extension 
	if i[-3:len(i)] == "jpg":
	   #print(i)
	   #print("Image Found")
	   system("move " + i +" " + des)
	if i[-3:len(i)] == "png":
	   #print(i)
	   #print("Image Found")
	   system("move " + i +" " + des)





def mainloop():
    for i in files:moveimages(i)


#exexute the main Search and Move Loops 
mainloop()

