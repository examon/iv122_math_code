rm -f img/mandelbrot/*.*
rm -f out.mp4
python3 mandelbrot.py
mogrify -format jpeg img/mandelbrot/*.bmp
rm img/mandelbrot/*.bmp
cat img/mandelbrot/*.jpeg | ffmpeg -f image2pipe -framerate 10 -vcodec mjpeg -i - -vcodec libx264 out.mp4
