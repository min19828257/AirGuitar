import os
import sys
import cv2
import hand

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path + '/python/openpose/Release');
os.environ['PATH']  = os.environ['PATH'] + ';' + dir_path + '/x64/Release;' +  dir_path + '/bin;'
import pyopenpose as op

params = dict()
params["model_folder"] = "./models/"
#params["face"] = True
params["hand"] = True

img_path = './media/COCO_val2014_000000000474.jpg'
video_path = './media/video.mp4'

try:
    opWrapper = op.WrapperPython()
    opWrapper.configure(params)
    opWrapper.start()

    cap = cv2.VideoCapture(video_path)
    while True:
        ret, imageToProcess = cap.read()
        imageToProcess = cv2.resize(imageToProcess, dsize=(0, 0), fx=1.0, fy=1.0, interpolation=cv2.INTER_LINEAR)
        
        datum = op.Datum()
        datum.cvInputData = imageToProcess
        opWrapper.emplaceAndPop([datum])  

        #body = str(datum.poseKeypoints)
        #face = str(datum.faceKeypoints)
        hand_L = datum.handKeypoints[0]
        hand_R = datum.handKeypoints[1]

        os.system('cls')
        print(hand_L)

        cv2.imshow("Pose and Hand", datum.cvOutputData) 
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except Exception as e:
    sys.exit(-1)
