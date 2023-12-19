import cv2 
import uuid
import os
import time

IMAGES_PATH = 'Tensorflow/workspace/images/collectedimages'

labels = ['hello', 'thanks', 'iloveyou', 'yes', 'no']
number_imgs = 10

for label in labels:
    os.makedirs(os.path.join(IMAGES_PATH, label), exist_ok=True) 
    cap = cv2.VideoCapture(1)
    print('Collecting images for {}'.format(label))
    time.sleep(5)
    
    for imgnum in range(number_imgs):
        print('Collecting image {}'.format(imgnum))
        ret, frame = cap.read()
        imgname = os.path.join(IMAGES_PATH, label, label + '.' + '{}.jpg'.format(str(uuid.uuid1())))
        cv2.imwrite(imgname, frame)
        cv2.imshow('frame', frame)
        time.sleep(2)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()

cv2.destroyAllWindows()  
