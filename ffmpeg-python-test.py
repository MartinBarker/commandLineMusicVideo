import ffmpeg
print('test')

#stream = ffmpeg.input('in.mp4')
#stream = ffmpeg.hflip(stream)
#stream = ffmpeg.output(stream, 'output.mp4')
#ffmpeg.run(stream)

#ffmpeg -loop 1 -framerate 2 -i img.jpg -i song.mp3 -vf "scale=2*trunc(iw/2):2*trunc(ih/2),setsar=1,format=yuv420p" -c:v libx264 -preset medium -tune stillimage -crf 18 -c:a aac -b:a 320k -shortest -vf scale=1920:1080 -pix_fmt yuv420p out.mp4"

import ffmpeg
print('test')

audioInput = ffmpeg.input('fighter.mp3')
imageInput = ffmpeg.input('front.jpg')
(
    ffmpeg
    .filter([audioInput, imageInput], 'overlay', 10, 10)
    .output('out.mp4')
    .run()
)