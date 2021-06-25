#Personal Project By Umangx.cf
#for all the files Requires custom input
from os import listdir
from os import chdir
from os import system
from getpass import getuser
from os import path 


user = getuser()

def makefolders(nameoffolder):
	if path.exists('/home/'+user+'/'+nameoffolder) == False:
		chdir('/home/'+user)
		system('mkdir '+ nameoffolder) 

makefolders('Software')
makefolders('Zips')


#gets the username for Linux
user = getuser()


#the download directory 
Download = ('/home/'+user+'/Downloads/')

#changes the pwd to the Download directory 
chdir(Download)


#the main directory to mv to //user-specific where the images should be stored 
picture = ('/home/'+user+'/Pictures') 
software = ('/home/'+user+'/Software')
docs =('/home/'+user+'/Documents')
vids = ('/home/'+user+'/Videos')
zips = ('/home/'+user+'/Zips')
Music = ('/home/'+user+'/Music')


#gets the list of files
files = listdir()


def mvimages(i):
	#checks for file extension
	if i[-3:len(i)] == "jpg":
	   #print(i)
	   #print("Image Found")
	   system("mv " + i +" " + picture)
	if i[-3:len(i)] == "png":
	   #print(i)
	   #print("Image Found")
	   system("mv " + i +" " + picture)
	if i[-3:len(i)] == "deb" or i[-3:len(i)] == "exe":
	   #print(i)
	   #print("Image Found")
	   system("mv " + i +" " + software)
	if i[-3:len(i)] == "pdf":
	   #print(i)
	   #print("Image Found")
	   system("mv " + i +" " + docs)
	if i[-3:len(i)] == "doc":
	   #print(i)
	   #print("Image Found") 
	   system("mv " + i +" " + docs)
	if i[-3:len(i)] == "mp3":
	   #print(i)
	   #print("Image Found")
	   system("mv " + i +" " + Music)	   
	if i[-3:len(i)] == "wav":
	   #print(i)
	   #print("Image Found")
	   system("mv " + i +" " + Music)		     
	if i[-3:len(i)] == "zip":
	   #print(i)
	   #print("Image Found")
	   system("mv " + i +" " + zips)	   	
	if i[-3:len(i)] == "iso":
	   #print(i)
	   #print("Image Found")
	   system("mv " + i +" " + zips)
	if i[-3:len(i)] == "rar":
	   #print(i)
	   #print("Image Found")
	   system("mv " + i +" " + zips)	         
	if i[-3:len(i)] == "mp4":
	   #print(i)
	   #print("Image Found")
	   system("mv " + i +" " + vids)
	if i[-3:len(i)] == "mkv":
	   #print(i)
	   #print("Image Found")
	   system("mv " + i +" " + vids)	   
	   
	 
def mainloop():
    for i in files:mvimages(i)


#execute the main Search and mv Loops 
mainloop()

