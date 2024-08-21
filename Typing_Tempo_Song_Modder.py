

#Mod Tool for Typing Tempo custom music
#21 Aug 2024, written by @dachmikin.org


import os
import time
import webbrowser

print("created by dachmikin, 2024")

#establish some basic variables thru user input and opens browser to search for the song name
#the "\" symbol is an escape character, so we need to double it here to avoid it being read as an escape character
parent_dir = "E:\\SteamLibrary\\steamapps\\common\\Typing Tempo\\res\\songs\\Practice Mode"     #EDIT THIS PATH TO POINT TO YOUR GAME FILE LOCATION

sname = input('Song Name? (Input the exact name) ')
webbrowser.open('https://tunebat.com/Search?q='+sname)
webbrowser.open('https://www.youtube.com/') #for some reason, opening youtube to a search seems to be unable to work. Perhaps an anti-bot feature in youtube?

artist = input('Artist? ') 
genre = input('Genre? ')
bpm = input("BPM? (Input a integer number, e.g. \"120\") ")

os.system('cls')

#creates path for directory to be made later, by appending the song name to the end of the parent directory
path = os.path.join(parent_dir, sname)

#confirm everything is right before proceeding further
print("Song Name: ", sname)
print("Artist: ",artist)
print("Genre: ",genre)
print("BPM: ",bpm)
print()
print("Confirm this is correct before proceeding.")

print( "\"title\": \"", sname, "\",", sep = '')

os.system("pause")

#creates the directory
os.mkdir(path)
print("Created Directory: ", path)

#defines the filename and path for the json file to feed into the script below
fname = path+"\\songinfo.json"
print(fname)
os.system("pause")

#creates the song json file
#because f.write only accepts 1 input (string), we have to format the multiple strings and sname variable into one string and feed that in.
f = open(fname, "x")
f.write("{\n")
f.write( "{}{}{}\n".format("\"title\": \"", sname, "\","))
f.write( "{}{}{}\n".format("\"artist\": \"", artist, "\","))
f.write( "{}{}{}\n".format("\"genre\": \"", genre, "\","))
f.write( "{}{}{}\n".format("\"music\": \"", sname, ".mp3\","))
f.write( "{}{}{}\n".format("\"coverart\": \"", sname, ".jpg\","))
f.write( "{}{}{}\n".format("\"bpmtext\": \"", bpm, "\","))
f.write( "\"musicPreviewStart\": 0.0,\n")
f.write( "\"musicPreviewStop\": 15.0\n")
f.write("}")
f.close()
print("Created json file: ", sname, ".json", sep = "")


#opens file explorer to the newly created path and a seperate window for the downloads folder
os.system('cls')
os.startfile(path)
os.startfile("C:\\Users\\Admin\\Downloads\\")   #EDIT THIS PATH TO POINT TO YOUR DEFAULT DOWNLOAD LOCATION
print("Download a song cover and audio! Name them exactly the same name as your initial song name input, and ensure they are in the correct file format (jpg and mp3 respectively). Then move them into the newly created song folder.")
print("Then move them into the newly created song folder and refresh the game's song list via settings.")

os.system("pause")