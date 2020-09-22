import cloudmusic
import time
import re
import urllib.request
import os
import sys
import pngquant
from pydub import AudioSegment
from PIL import Image
from os.path import join, getsize

#Handling the problem of Windows reserved words in file names
intab = "?*/\\|.:><\"\'"
outtab = "           "
trantab = str.maketrans(intab, outtab)
Error_List = "\n----------------------------------------------------\n"

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
    Check_Process = input("Do you want to transcode audio files, slice them and compress the images?    Y/N\n")
    for music in musiclist:
        music.name = music.name.translate(trantab)
        if not music.type is None:
            try:
                music.download(r""+Download_Addrass, Music_Quality)
            except:
                Error_List += "ID." + str(Music_ID) + "\n"
                print("###Music ID " + str(music.id) + " has error, pass!")
                continue
        else:
            Error_List += "ID." + str(music.id) + "\n"
            print("###Music ID " + str(music.id) +" has error, pass!")
            continue
        try:
            File_Names = os.listdir(Download_Addrass)
            path = Download_Addrass
            for Music_Name in File_Names:
                for C in Music_Name:
                    if C == '-':
                        os.rename(os.path.join(Download_Addrass, Music_Name), os.path.join(Download_Addrass, str(Music_ID).rjust(3, '0') + '.'+music.type))
                        break
            print("NO." + str(Music_ID).rjust(3, '0') + " " + music.name + " download successful!")
            if Check_Process == "Y" or Check_Process == "y":
                #Process audio files
                Music_Process = AudioSegment.from_file(r"" + Download_Addrass + "/" + str(Music_ID).rjust(3,'0') + '.'+music.type, music.type)
                one_minute = 60 * 1000
                Music_Save = Music_Process[:one_minute]
                Music_Save.export(r""+Download_Addrass + "/" +str(Music_ID).rjust(3,'0')+".mp3",format ="mp3")
                if music.type != "mp3":
                    os.remove(os.path.join(Download_Addrass, str(Music_ID).rjust(3,'0') + '.'+music.type))
            Img_Name = Download_Addrass+'/'+str(Music_ID).rjust(3,'0')+'.png'
            urllib.request.urlretrieve(music.picUrl , filename=Img_Name)
            #pngquant.quant_image(Img_Name)
            while getsize(Img_Name) > 1000000:
                Img_Re = Image.open(Img_Name)
                Img_Re = Img_Re.resize((int(Img_Re.size[0]/2),int(Img_Re.size[1]/2)))
                Img_Re.save(Img_Name)
            print("NO." + str(Music_ID).rjust(3, '0') + " processing completed!")
            Txt_File = open(r""+Download_Addrass + "/" + str(Music_ID).rjust(3,'0') + ".txt", mode='w', encoding="utf-8")
            Txt_File.write("Music Name: "+music.name+"\n\n"+"Artist Name: ")
            for artist in music.artist:
                Txt_File.write(artist + " ")
            Txt_File.write("\n\nAlbum Name: " + music.album + "\n\nLyrics:\n")
            for lyrics in music.getLyrics():
                if not lyrics is None:
                    Txt_File.write(lyrics)
            Txt_File.write("\nHot Comments:\n")
            for comments in music.getHotComments():
                if not comments is None:
                    Txt_File.write(comments['content']+"\n------------------------------\n")
            Txt_File.close()
            print("NO."+str(Music_ID).rjust(3,'0')+" .png and .txt file generated successful!")
        except:
            Error_List += "ID." + str(Music_ID) + "\n"
            print("###Music ID " + str(music.id) + " has error, pass!")
            continue
        Music_ID+=1
    print(Error_List+"has errors!\nThe last ID is "+str(Music_ID-1)+"\n----------------------------------------------------")
    print("Do you want to continue running this program?    Y/N")
    Check_End = input()
    if Check_End == "n" or Check_End == "N":
        If_End = True