import cv2
fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
video = cv2.VideoWriter('video1.mp4', fourcc, 10.0, (4000, 2226))

# 在生成每一帧后可以执行这个
for i in range(0, 500):
    img = cv2.imread('./output/generated{}.png'.format(i))
    print('./output/generated{}.png'.format(i))
    video.write(img)

# 在生成每一帧后，并且打开 ./WaifuPainter.ipynb 生成 './output/generated{}_{}.png' 才可以这个
# for i in range(0, 500):
#     img = cv2.imread('./output/generated{}.png'.format(i))
#     print('./output/generated{}.png'.format(i))
#     video.write(img)
#     if i in list(range(249, 270)):
#         for j in range(0, 72):
#             img = cv2.imread('./output/generated{}_{}.png'.format(i, j))
#             print('./output/generated{}_{}.png'.format(i, j))
#             video.write(img)

video.release()