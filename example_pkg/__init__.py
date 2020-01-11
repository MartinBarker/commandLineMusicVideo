import os
import sys

print("inside martin's test pip package")

def renderSingle():
    os.system('ffmpeg -loop 1 -framerate 2 -i "front.png" -i "testWAVfile.wav" -vf "scale=2*trunc(iw/2):2*trunc(ih/2),setsar=1,format=yuv420p" -c:v libx264 -preset medium -tune stillimage -crf 18 -c:a aac -shortest -vf scale=1920:1080  "outputVideoPy.mp4"')

print("the script has the name %s" % (sys.argv[0]))

#set default args
outputFilename = None
outputResolution = None

#get option flags

if '-outputResolution' in sys.argv:
    print("-outputResolution")

if '-outputFilename' in sys.argv:
    print("-outputFilename")

#get requirerd flags

if '-img' in sys.argv:
    print("-img")

if '-song' in sys.argv:
    print('-song')
    #get songFilepath
    songFilepathIndex = sys.argv.index('-song')+1
    songFilepath = sys.argv[songFilepathIndex]
    print("songFilepath = ", songFilepath)

    #get fileFormat from songFilepath
    indexOfLastPeriod = songFilepath.rfind(".")
    fileFormat = songFilepath[indexOfLastPeriod:]
    print("fileFormat = ", fileFormat)

    #render single
    renderSingle()

elif '-songs' in sys.argv:
    print("-songs (multiple)")




'''
ffmpeg 
    -loop 1 
    -framerate 2 
    -i "front.png" 
    -i "testWAVfile.wav" 
    -vf "scale=2*trunc(iw/2):2*trunc(ih/2),setsar=1,format=yuv420p" 
    -c:v libx264 
    -preset medium 
    -tune stillimage 
    -crf 18 
    -c:a aac 
    -shortest 
    -vf scale=1920:1080  
    "outputVideo.mp4"


#mp3
ffmpeg 
    -loop 1 
    -framerate 2 
    -i "front.png" 
    -i "testmp3file.MP3" 
    -vf "scale=2*trunc(iw/2):2*trunc(ih/2),setsar=1" 
    -c:v libx264 
    -preset medium 
    -tune stillimage 
    -crf 18 
    -c:a copy 
    -shortest 
    -pix_fmt yuv420p "$2/$5.mp4"  

#flac
ffmpeg 
    -loop 1 
    -framerate 2 
    -i "$2/$3" 
    -i "$2/$4" 
    -vf "scale=2*trunc(iw/2):2*trunc(ih/2),setsar=1" 
    -c:v libx264 
    -preset medium 
    -tune stillimage 
    -crf 18 
    -c:a copy 
    -shortest 
    -pix_fmt yuv420p 
    -strict -2 "$2/$5.mp4"

#wav
ffmpeg -loop 1 -framerate 2 -i "front.png" -i "testWAVfile.wav" -vf "scale=2*trunc(iw/2):2*trunc(ih/2),setsar=1,format=yuv420p" -c:v libx264 -preset medium -tune stillimage -crf 18 -c:a aac -shortest -vf scale=1920:1080  "outputVideo.mp4"




'''


print("\n\n\n")