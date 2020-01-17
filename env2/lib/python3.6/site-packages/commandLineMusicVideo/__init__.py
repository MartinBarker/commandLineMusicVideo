import os
import sys


def renderVideo(sourceAudioFilepath, filename, imageFilepath, resolution, outputFilename):
    print('renderVideo()')



    if filename.endswith('mp3'):

        #ffmpeg -loop 1 -framerate 2 -i "../../../Soulseek Downloads/complete/illjarn93/J - Hidefumi Toki - City Fumi (1978)//front.jpeg" -i "../../../Soulseek Downloads/complete/illjarn93/J - Hidefumi Toki - City Fumi (1978)/06 Pumpkin Doll.mp3" -vf "scale=2*trunc(iw/2):2*trunc(ih/2),setsar=1" -c:v libx264 -preset medium -tune stillimage -crf 18 -c:a copy -b:a 320k -shortest -vf scale=1920:1080 -pix_fmt yuv420p "../../../Soulseek Downloads/complete/illjarn93/J - Hidefumi Toki - City Fumi (1978)//Pumpkin Doll.mp4"

        ffmpegCommand = 'ffmpeg -loop 1 -framerate 2 -i "'+ imageFilepath +'" -i "'+ sourceAudioFilepath +'" -vf "scale=2*trunc(iw/2):2*trunc(ih/2),setsar=1" -c:v libx264 -preset medium -tune stillimage -crf 18 -c:a copy -b:a 320k -shortest -vf scale=' + resolution + ' -pix_fmt yuv420p "'+ outputFilename  +'.mp4"'

        print("\n**********\n"+ffmpegCommand+"\n**********\n")
        os.system(ffmpegCommand)

    elif filename.endswith('flac'):
        ffmpegCommand = 'ffmpeg -loop 1 -framerate 2 -i "' + imageFilepath + '" -i "' + sourceAudioFilepath + '" -vf "scale=2*trunc(iw/2):2*trunc(ih/2),setsar=1,format=yuv420p" -c:v libx264 -preset medium -tune stillimage -crf 18 -c:a aac -b:a 320k -shortest -vf '+ 'scale=' + resolution + ' -pix_fmt yuv420p "' + outputFilename  +'.mp4"'

        print("\n**********\n"+ffmpegCommand+"\n**********\n")
        os.system(ffmpegCommand)

    else:
        print("file format not supported (yet), please tweet at me @martinradio_ or email me ")

def fullAlbum(songsFilepath, audioFormat, imageFilepath, outputResolution):
    if audioFormat == 'mp3':
        print("concat audio mp3")
        concatString = "concat:"
        arr = os.listdir(songsFilepath)
        for filename in arr:
            if filename.endswith(audioFormat):
                songLocation = songsFilepath + '/' + filename
                concatString = concatString + songLocation + '|'

        #create concatAudio string     "concat:fighter.mp3|03life.mp3"
        #render concatAudio.mp3    ffmpeg -i "concat:fighter.mp3|03life.mp3" -acodec copy concatAudio.mp3
        print('concatString = ', concatString)
        os.system('ffmpeg -i "' + concatString + '" -acodec copy "' + songsFilepath + '/concatAudio.mp3"')

        renderVideo(songsFilepath+'/concatAudio.mp3', 'concatAudio.mp3', imageFilepath, outputResolution, songsFilepath+'/fullAlbum.mp4')
        os.system('rm "'+ songsFilepath + '/concatAudio.mp3"')

    elif audioFormat == 'flac':
        #os.system('rm inputs.txt')
        #os.system('rm "'+ songsFilepath + '/concatAudio.mp3"')
        os.system('touch songinputs.txt')
        arr = os.listdir(songsFilepath)
        for filename in arr:
            if filename.endswith(audioFormat):
                songLocation = songsFilepath + '/' + filename
                with open("songinputs.txt", "a") as myfile:
                    songLocationString = songLocation.replace("'", "'\\''")   #   '\''
                    myfile.write("file '" + songLocationString +"' \n")

        os.system("ffmpeg -f concat -safe 0 -i songinputs.txt -safe 0 '" + songsFilepath + "/concatAudio.mp3'")
        #os.system('rm inputs.txt')
        renderVideo(songsFilepath+'/concatAudio.mp3', 'concatAudio.mp3', imageFilepath, outputResolution, songsFilepath+'/fullAlbum.mp4')
        #os.system('rm "'+ songsFilepath + '/concatAudio.mp3"')

def outputFilenameParse(outputFilename):

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

    return outputFilename

def renderEachSong(songsFilepath, imageFilepath, audioFormat, outputResolution):
    #renderEachSong(songsFilepath, imageFilepath, audioFormat, outputResolution)
        #for each song
    arr = os.listdir(songsFilepath)
    print(arr)
    for filename in arr:
        if filename.endswith(audioFormat):
            outputFilename = filename[:-len(audioFormat)-1]

            outputFilename = outputFilenameParse(outputFilename)

            print('outputFilename = [', outputFilename, ']')
            outputFilename = songsFilepath + '/' + outputFilename            
            print('outputFilename = [', outputFilename, ']')

            renderVideo(songsFilepath+''+filename, filename, imageFilepath, outputResolution, outputFilename)

    
    print('')
    

#set default args
outputFilename = None
outputResolution = "1920:1080"
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
    songsIndex = sys.argv.index('-songs')
    #get songsFilepath
    songsFilepath = sys.argv[songsIndex+1]
    print("songsFilepath = ", songsFilepath)

    #get audioFormat
    audioFormat = sys.argv[songsIndex+2]
    print("audioFormat = ", audioFormat)

    #get imageFilename from same folder
    imageFilename = sys.argv[songsIndex+3]
    print("imageFilename = ", imageFilename)
    imageFilepath = songsFilepath + '/' + imageFilename
    print("imageFilepath = ", imageFilepath)

    if '-fullAlbumOnly' in sys.argv:
        fullAlbum(songsFilepath, audioFormat, imageFilepath, outputResolution)

    elif '-fullAlbum' in sys.argv: # and sys.argv.index('-fullalbum') < sys.argv.index('-songs'):
        print('fullAlbum') #comesfirst')
        renderEachSong(songsFilepath, imageFilepath, audioFormat, outputResolution)
        fullAlbum(songsFilepath, audioFormat, imageFilepath, outputResolution)
    else:
        print("outputResolution = ", outputResolution)
        renderEachSong(songsFilepath, imageFilepath, audioFormat, outputResolution)
