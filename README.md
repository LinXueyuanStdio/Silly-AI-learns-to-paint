# Silly-AI-learns-to-paint

人工智障学画画

来，给我画个老婆~

## 使用

生成每一帧
```
$ python model/test.py --max_step=100 --actor=actor.pkl --renderer=renderer.pkl --img=./2.png --divide=4
```

如果安装了ffmpeg，运行
```
$ ffmpeg -r 10 -f image2 -i output/generated%d.png -s 512x512 -c:v libx264 -pix_fmt yuv420p video2.mp4 -q:v 0 -q:a 0
```
没安装ffmpeg就运行（需要在里面改参数）
```
$ python png2mp4
```

## 使作画过程更真实

参考 notebook 文件：`./WaifuPainter.ipynb`


