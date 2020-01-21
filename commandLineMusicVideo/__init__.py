import os
import sys


def renderVideo(sourceAudioFilepath, filename, imageFilepath, resolution, outputFilename):
    print('renderVideo()')

    if filename.endswith('mp3'):
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

        print('concatString = ', concatString)
        os.system('ffmpeg -i "' + concatString + '" -acodec copy "' + songsFilepath + '/concatAudio.mp3"')

        renderVideo(songsFilepath+'/concatAudio.mp3', 'concatAudio.mp3', imageFilepath, outputResolution, songsFilepath+'/fullAlbum')
        os.system('rm "'+ songsFilepath + '/concatAudio.mp3"')

    elif audioFormat == 'flac':
        os.system('touch songinputs.txt')
        arr = os.listdir(songsFilepath)
        for filename in arr:
            if filename.endswith(audioFormat):
                songLocation = songsFilepath + '/' + filename
                with open("songinputs.txt", "a") as myfile:
                    songLocationString = songLocation.replace("'", "'\\''")   #   '\''
                    myfile.write("file '" + songLocationString +"' \n")

        os.system("ffmpeg -f concat -safe 0 -i songinputs.txt -safe 0 '" + songsFilepath + "/concatAudio.mp3'")
        renderVideo(songsFilepath+'/concatAudio.mp3', 'concatAudio.mp3', imageFilepath, outputResolution, songsFilepath+'/fullAlbum')
        os.system('rm "'+ songsFilepath + '/concatAudio.mp3"')

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
    #for each file in filepath
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

if '-h' in sys.argv:
    print('Welcome to the commandLineMusicVideo pip3 package.')
    print('\n~General Flags~\n')
    print('-songs "folderFilepath/" "audioFormat" "imageName.jpeg"   //render each audioFormat file in the folderFilepath, using the imageName also found in the folderFilepath      ')
    print(' -fullAlbum                                               //render full album with these songs as well')
    print(' -fullAlbumOnly                                           //only render the full album')
    print('-outputResolution 1920:1080                               //set output resolution for video')
    print('\n~Filename Output Flags~\n')
    print('-removeFirst 3                                            //remove first # chars from song filename for output filename')
    print('-removeUpTo "-"                                           //remove up to and including this char') 
    print('-removeAfter "-"                                          //remove everything after and including this char')
    print('-titleize                                                 //capitalize first letter of each word of output filename')    

if '-test' in sys.argv:
    #test your ffmpeg installation
    print("You should see the 'ffmpeg version' command output, if you have ffmpeg installed correctly then it will output something like 'ffmpeg version x.x.x...'. If you don't see this then install ffmpeg with 'sudo apt-get install ffmpeg'. \n\n ")
    os.system('ffmpeg -version')
    

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

    elif '-fullAlbum' in sys.argv:
        print('fullAlbum')
        renderEachSong(songsFilepath, imageFilepath, audioFormat, outputResolution)
        fullAlbum(songsFilepath, audioFormat, imageFilepath, outputResolution)
    else:
        print("outputResolution = ", outputResolution)
        renderEachSong(songsFilepath, imageFilepath, audioFormat, outputResolution)
