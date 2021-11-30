#Personal Project By Umangx.cf
#for all the files Requires custom input
from os import listdir
from os import chdir
from os import system
from getpass import getuser
from os import path 

user = getuser()
def makefolders(nameoffolder):
	if path.exists('c:/Users/'+user+'/'+nameoffolder) == False:
		chdir('C:/Users/'+user)
		system('mkdir '+ nameoffolder) 
makefolders('Software')
makefolders('Zips')
#gets the username for windows
user = getuser()

#the download directory 
Download = ('C:/Users/'+user+'/Downloads/')
#changes the pwd to the Download directory 
chdir(Download)

#the main directory to move to //user-specific where the images should be stored 
picture = ('C:/Users/'+user+'/Pictures') 
software = ('C:/Users/'+user+'/Software')
docs =('C:/Users/'+user+'/Documents')
vids = ('C:/Users/'+user+'/Videos')
zips = ('C:/Users/'+user+'/Zips')
Music = ('C:/Users/'+user+'/Music')

#gets the list of files
files = listdir()
def moveimages(i):
	#checks for file extension
	if i[-3:len(i)] == "jpg":
	   #print(i)
	   #print("Image Found")
	   system("move " + i +" " + picture)
	if i[-3:len(i)] == "png":
	   #print(i)
	   #print("Image Found")
	   system("move " + i +" " + picture)
	if i[-3:len(i)] == "exe" or i[-3:len(i)] == "msi":
	   #print(i)
	   #print("Image Found")
	   system("move " + i +" " + software)
	if i[-3:len(i)] == "pdf":
	   #print(i)
	   #print("Image Found")
	   system("move " + i +" " + docs)
	if i[-3:len(i)] == "doc":
	   #print(i)
	   #print("Image Found") 
	   system("move " + i +" " + docs)
	if i[-3:len(i)] == "mp3":
	   #print(i)
	   #print("Image Found")
	   system("move " + i +" " + Music)	   
	if i[-3:len(i)] == "wav":
	   #print(i)
	   #print("Image Found")
	   system("move " + i +" " + Music)		     
	if i[-3:len(i)] == "zip":
	   #print(i)
	   #print("Image Found")
	   system("move " + i +" " + zips)	   	
	if i[-3:len(i)] == "iso":
	   #print(i)
	   #print("Image Found")
	   system("move " + i +" " + zips)
	if i[-3:len(i)] == "rar":
	   #print(i)
	   #print("Image Found")
	   system("move " + i +" " + zips)	         
	if i[-3:len(i)] == "mp4":
	   #print(i)
	   #print("Image Found")
	   system("move " + i +" " + vids)
	if i[-3:len(i)] == "mkv":
	   #print(i)
	   #print("Image Found")
	   system("move " + i +" " + vids)	   
	   	 
def mainloop():
    for i in files:moveimages(i)
#exexute the main Search and Move Loops 
mainloop()
