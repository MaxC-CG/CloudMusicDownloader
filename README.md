# Netease Cloud Music  Automatic Downloader
## For Digital Asset Management Course in ZJU
***
* ___This program is based on the python package called [cloudmusic], you can visit the github home page of the package via the URL. Special thanks to the contributors of the package.___
* ___This program also uses the [pydub] package, which you also need to install ahead of time. In particular, in order to use some of the features in the pydub package, you need to install [ffmpeg] or [libav] in your environment.___
* ___In order to achieve the image compression function, we uses [pngquant] and [pillow]. So you will need to download the pngquant library and install the python wrapper and the pillow package.___

###Functions realized in this program

> * According to the __ID__ of Netease Cloud Music playlist, automatically download all songs in the  playlist to the specified local folder
> * Download album cover images of songs to the same directory
> * Automatically creates txt files to save the song's name, authors, lyrics, hot comments and other information
> * Automatically renames all files in sequence based on the initial number specified by the user
> * Automatically convert audio files to __.mp3__ format and slice the first minute of the audio
> * Automatically compress images larger than 1MB

###How to use this program

> * Configure your Python environment
> * install [pngquant] on your OS
> * install [ffmpeg] or [libav] on your OS
> * install [pillow] according to the [document of pillow]
> * install the [python wrapper of pngquant] using the command `pip install pngquant`
> * install [pydub] package using the command `pip install pydub`
> *  Install the [cloudmusic] package using the command `pip install cloudmusic`
> *  Run the ___NCM_Downloader.py___ file
> *  Follow the input prompt

###Tips 

> * You can get the ID of the playlist from the URL of the Netease Cloud Music playlist
> For example, in URL https://music.163.com/#/playlist?Id=4895239160, ___4895239160___ is the id of the playlist
> * Try to make sure that the folder which you want to save musics is empty before you run the program, otherwise the program may report an error due to duplicate naming
> * Some songs may fail to download, and the program will automatically skip and display an error list at the end of the run
> *  This program is only tested in a Windows environment, and it is uncertain whether it will run successfully in other OS



[cloudmusic]: https://github.com/p697/cloudmusic
[pydub]: https://github.com/jiaaro/pydub
[ffmpeg]: http://www.ffmpeg.org/
[libav]: https://libav.org/
[pngquant]: https://pngquant.org/
[python wrapper of pngquant]: https://pypi.org/project/pngquant/
[pillow]: https://python-pillow.org/
[document of pillow]: https://pillow.readthedocs.io/en/latest/installation.html