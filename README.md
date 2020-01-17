# commandLineMusicVideo

This is a [pip3 package](https://pypi.org/project/commandLineMusicVideo) that uses ffmpeg to render videos using an image and audio file as inputs.

Example video rendered using this package: https://www.youtube.com/watch?v=5SqLD4GEVHc&t=911s

## Quickstart
* Make sure you have ffmpeg installed on your command line, ensure ffmpeg is downloaded by running the command:

  ```ffmpeg```
  Which should give you an output with info on the version of ffmpeg installed.

* Download the commandLineMusicVideo package with this command: ```pip3 install commandLineMusicVideo==0.1.1```
* Run the installed package with ```python3 -m commandLineMusicVideo -h -t``` to view the help page and test your ffmpeg.

## Examples

### Rendering individual videos and a full album video for a folder.

``` python3 -m commandLineMusicVideo -songs "../../../Infernal Love/Violet Eves - Promenade [1988, IRA]/" mp3 "front.jpg" -fullAlbum -removeFirst 19```

This command will get 'front.jpg' and all the mp3 files located in the specified folder:
![step1](https://i.imgur.com/0l2YIJZ.png)

The ```-removeFirst 19``` tag will format the individual song output filenames based on their input filename, for example, the filename ```Violet Eves - 04 - Fiaba di Sale``` after having its first 19 chars removed, would be: ```Fiaba di Sale```

After running the full commandLineMusicVideo command, the folder output (with all the individual songs AND the fullAlbum) will look like this:
![step1](https://i.imgur.com/xDm7Ps9.png)

The output videos will keep the image's aspect ratio.
![step1](https://i.imgur.com/KA7xfhT.png)


## Flags

```-h``` Display help.

```-test``` Test your ffmpeg.

```-songs "folderFilepath/" "audioFormat" "imageName.jpeg"``` Render each audioFormat file in the folderFilepath, using the imageName also found in the folderFilepath.

```-fullAlbum``` Render full album with these songs as well.

```-fullAlbumOnly``` Only render the full album.

```-outputResolution 1920:1080``` Set output resolution for video.

* Output Filename Formatting Flags:

```-removeFirst #``` Remove first # chars from song filename for output filename.

```-removeUpTo "-"``` Remove everything up to and including the first instance of this char.

```-removeAfter "-"``` Remove everything after and including this char.

```-titleize``` Capitalize first letter of each word of output filename')    
