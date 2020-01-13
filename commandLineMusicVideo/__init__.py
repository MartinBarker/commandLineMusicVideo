import os
import sys
import glob

print("inside martin's test pip package")
print("the script has the name %s" % (sys.argv[0]))

def renderVideo(sourceAudioFilepath, filename, imageFilepath, resolution, outputFilename):
    print('renderVideo()')


    if filename.endswith('mp3'):

        ffmpegCommand = 'ffmpeg -loop 1 -framerate 2 -i "' + imageFilepath + '" -i "' + sourceAudioFilepath + '" -vf "scale=2*trunc(iw/2):2*trunc(ih/2),setsar=1,format=yuv420p" -c:v libx264 -preset medium -tune stillimage -crf 18 -c:a aac -b:a 320k -shortest -vf '+ 'scale=' + resolution + ' -pix_fmt yuv420p "' + outputFilename + '.mp4"' 

        print("\n**********\n"+ffmpegCommand+"\n**********\n")

    os.system(ffmpegCommand)

def renderSingle():
    os.system('ffmpeg -loop 1 -framerate 2 -i "front.png" -i "testWAVfile.wav" -vf "scale=2*trunc(iw/2):2*trunc(ih/2),setsar=1,format=yuv420p" -c:v libx264 -preset medium -tune stillimage -crf 18 -c:a aac -shortest -vf scale=1920:1080  "outputVideoPy.mp4"')

'''
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
'''


#set default args
outputFilename = None
outputResolution = None
imgFilepath = None

#get option flags

if '-outputResolution' in sys.argv:
    print("-outputResolution")
    outputResolutionIndex = sys.argv.index('-outputResolution')
    outputResolution = sys.argv[outputResolutionIndex+1]

if '-outputFilename' in sys.argv:
    print("-outputFilename")

if '-songs' in sys.argv:
    print('-songs')
    songIndex = sys.argv.index('-songs')
    #get songFilepath
    songFilepath = sys.argv[songIndex+1]
    print("songFilepath = ", songFilepath)

    #get audioFormat
    audioFormat = sys.argv[songIndex+2]
    print("audioFormat = ", audioFormat)

    #get imageFilepath
    imageFilepath = sys.argv[songIndex+3]
    print("imageFilepath = ", imageFilepath)

    #files = os.listdir(songFilepath)
    #zero = []

    arr = os.listdir(songFilepath)
    print(arr)
    for filename in arr:
        if filename.endswith(audioFormat):
            outputFilename = filename[:-len(audioFormat)-1]

            if '-removeFirst' in sys.argv:
                removeFirstIndex = sys.argv.index('-removeFirst')
                removeFirst = sys.argv[removeFirstIndex+1]
                outputFilename = outputFilename[int(removeFirst):]

            if '-removeUpTo' in sys.argv:
                removeUpToIndex = sys.argv.index('-removeUpTo')
                removeUpToChar = sys.argv[removeUpToIndex+1]
                removeAfterChar = sys.argv[removeUpToIndex+2] #optional, can be zero
                removeUpToCharIndex = outputFilename.index(removeUpToChar)
                outputFilename = outputFilename[int(removeUpToCharIndex)+int(removeAfterChar)+1:] 

            if '-removeAfter' in sys.argv:
                removeAfterIndex = sys.argv.index('-removeAfter')
                removeAfterChar = sys.argv[removeAfterIndex+1]
                removeAfterCharIndex = outputFilename.index(removeAfterChar)
                outputFilename = outputFilename[:int(removeAfterCharIndex)]

            if '-titleize' in sys.argv:
                outputFilename = outputFilename.title()


            print('outputFilename = [', outputFilename, ']')
            outputFilename = songFilepath + '/' + outputFilename            
            print('outputFilename = [', outputFilename, ']')

            renderVideo(songFilepath+''+filename, filename, imageFilepath, outputResolution, outputFilename)




    #render single
    #renderSingle()

#elif '-songs' in sys.argv:
#    print("-songs (multiple)")

'''
outputFilepath = songFilepath[:indexOfLastPeriod] 
outputFilepath = outputFilepath + '.mp4'
print("outputFilepath = ", outputFilepath)

ffmpegCommand = 'ffmpeg -loop 1 -framerate 2 -i "' + imgFilepath + '" -i "' + songFilepath + '" -vf "scale=2*trunc(iw/2):2*trunc(ih/2),setsar=1,format=yuv420p" -c:v libx264 -preset medium -tune stillimage -crf 18 -c:a aac -shortest -vf scale=1920:1080 -pix_fmt yuv420p -strict -2 "' + outputFilepath + '"' 

print("\n**********\n"+ffmpegCommand+"\n**********\n")

os.system(ffmpegCommand)

'''




'''
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



#wav
ffmpeg -loop 1 -framerate 2 -i "front.png" -i "testWAVfile.wav" -vf "scale=2*trunc(iw/2):2*trunc(ih/2),setsar=1,format=yuv420p" -c:v libx264 -preset medium -tune stillimage -crf 18 -c:a aac -shortest -vf scale=1920:1080  "outputVideo.mp4"




'''


print("\n\n\n")