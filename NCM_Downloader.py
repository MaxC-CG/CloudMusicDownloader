import cloudmusic
import time
import re
import urllib.request
import os
import sys

#Handling the problem of Windows reserved words in file names
intab = "?*/\|.:><\""
outtab = "          "
trantab = str.maketrans(intab, outtab)

If_End = False
while not If_End:
    If_Download = False
    while not If_Download:
        Music_List_ID = input("Please enter the ID of the Netease cloud music playlist that you wish to download:\n")
        musiclist = cloudmusic.getPlaylist(Music_List_ID)
        #Display the number of songs in the playlist and confirm whether to download
        print("The playlist you wish to download contains ",len(musiclist)," songs. Do you want to download?    Y/N")
        Check_Download = input()
        if Check_Download == "Y" or Check_Download == "y":
            If_Download = True
    If_Path = False
    while not If_Path:
        Download_Addrass = input("Please enter the path where you want to store the song:\n")
        if os.path.isdir(Download_Addrass):
            If_Path = True
        else:
            print("The path you entered is illegal! Please re-enter!")
    #Make sure the quality of music（standard by default
    Music_Quality = input("Please enter the quality of the song you wish to download: (standard/higher/exhigh/lossless)\n")
    Music_ID = int(input("Please enter the initial number of the music:\n"))
    for music in musiclist:
        music.name = music.name.translate(trantab)
        music.download(Download_Addrass, Music_Quality)
        File_Names = os.listdir(Download_Addrass)
        path = Download_Addrass
        for Name in File_Names:
            for C in Name:
                if C == '-':
                    os.rename(os.path.join(Download_Addrass, Name), os.path.join(Download_Addrass, str(Music_ID).rjust(3,'0')+Name[Name.rindex('.'):]))
                    break
        urllib.request.urlretrieve(music.picUrl , filename=Download_Addrass+'/'+str(Music_ID).rjust(3,'0')+'.png')
        Txt_File = open(r""+Download_Addrass + "/" + str(Music_ID).rjust(3,'0') + ".txt", mode='w', encoding="utf-8")
        Txt_File.write("Music Name: "+music.name+"\n"+"Artist Name: ")
        for artist in music.artist:
            Txt_File.write(artist + " ")
        Txt_File.write("\nAlbum Name: " + music.album + "\nLyrics:\n")
        for lyrics in music.getLyrics():
            if not lyrics is None:
                Txt_File.write(lyrics)
        Txt_File.write("Hot Comments:\n")
        for comments in music.getHotComments():
            if not comments is None:
                Txt_File.write(comments['content']+"\n")
        Txt_File.close()
        print("NO."+str(Music_ID).rjust(3,'0')+" "+ music.name +" Download successful!")
        Music_ID+=1
    print("Do you want to continue running this program?    Y/N")
    Check_End = input()
    if Check_End == "n" or Check_End == "N":
        If_End = True