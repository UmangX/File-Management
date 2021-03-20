#Personal Project By Umangx.cf
#for all the files Requires custom input
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
des = ('C:/Users/'+user+'/Pictures/') 
des2 = ('D:\Softies')
des3 =('D:\Books')


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
	if i[-3:len(i)] == "exe" or i[-3:len(i)] == "msi":
	   #print(i)
	   #print("Image Found")
	   system("move " + i +" " + des2)
	if i[-3:len(i)] == "pdf":
	   #print(i)
	   #print("Image Found")
	   system("move " + i +" " + des3)



	



def mainloop():
    for i in files:moveimages(i)


#exexute the main Search and Move Loops 
mainloop()

