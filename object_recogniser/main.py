from time import sleep

import cv2

from object_recogniser.telegram import send_last_photo_to_admins

done = False
while not done:
    try:
        send_last_photo_to_admins()
        done = True
    except Exception as e:
        print('waiting' + str(e))
        done = False
        sleep(2)
cam = cv2.VideoCapture(0)
cv2.namedWindow('test')
img_counter = 0
c = 0
while True:
    c += 1
    print(c)
    ret, frame = cam.read()
    resize = cv2.resize(frame, (768, 480))
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("test", resize)
    k = cv2.waitKey(1)
    if k % 256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k % 256 == 32:
        # SPACE pressed
        img_name = "last_photo.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1
        send_last_photo_to_admins()

    if c % 150 == 0:
        img_name = "last_photo.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        send_last_photo_to_admins()
cam.release()

cv2.destroyAllWindows()
