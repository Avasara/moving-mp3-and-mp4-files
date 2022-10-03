#This program will move mp3 or mp4 files from a similar folder to the same or different ones depending on the one you specify.

#Importing the pathlib and shutil modules
from pathlib import Path
import shutil

#Telling the program to search the downloads folder.
downloads = Path("C:\\Users\\USER\\Downloads") #CHANGE THIS IF YOU HAVE TO

#Searching for 'mp3' and 'mp4' files and storing them.
mp3files = list(downloads.glob('**/*.mp3'))
mp4files = list(downloads.glob('**/*.mp4'))

#Getting the number of items in the mp3 and mp4 file lists
no_of_mp3 = len(mp3files)
no_of_mp4 = len(mp4files)

#Making a function to automatically move files from a given source and destination
def move_files(source, destination):
    
    shutil.move(source, destination)
    print('Successfully moved',str(source),'to',str(destination))

#The for loop creates a variable 'index' which will run in the range of numbers the no_of_mp3/mp4 value holds and pass that
#as the index for mp3/mp4files. Because we used no_of_music to get the number of files, we don't need to increment the value ourselves.
    
#If we tried incrementing directly with the for loop, we would get a windows path error.

#The mp3 movement function
def move_mp3():
    print("--------------------------------------------------------------------------------------------------")    
    print("Moving MP3 files...")
    print("--------------------------------------------------------------------------------------------------")

    if(no_of_mp3 != 0):
        
        for index in range(no_of_mp3):
            move_files(mp3files[index] , 'C:\\Users\\USER\\Music') #CHANGE THIS DESTINATION OR LEAVE AS IS.
            
        print("ALL MP3 FILES HAVE BEEN SUCCESSFULLY MOVED")
        
    else:
        print("Sorry, there are no MP3 files in your downloads folder.")

#The mp4 movement function
def move_mp4():
    print("--------------------------------------------------------------------------------------------------")
    print("Moving MP4 files...")
    print("--------------------------------------------------------------------------------------------------")

    if(no_of_mp4 != 0):

        for index in range(no_of_mp4):
            move_files(mp4files[index] , 'C:\\Users\\USER\\Music') # CHANGE DESTINATION OR LEAVE AS IS

        print("ALL MP4 FILES HAVE BEEN SUCCESSFULLY MOVED")

    else:
        print("Sorry, there are no MP4 files in your downloads folder")

move_mp4()
move_mp3()

#HOLY SHIT IT WORKED!
