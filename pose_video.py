import os
import sys
import cv2

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path + '/python/openpose/Release');
os.environ['PATH']  = os.environ['PATH'] + ';' + dir_path + '/x64/Release;' +  dir_path + '/bin;'
import pyopenpose as op

params = dict()
params["model_folder"] = "./models/"

img_path = './media/COCO_val2014_000000000474.jpg'
video_path = './media/video.mp4'

try:
    opWrapper = op.WrapperPython()
    opWrapper.configure(params)
    opWrapper.start()

    datum = op.Datum()

    cap = cv2.VideoCapture(0)

    while True:
        ret, imageToProcess = cap.read()
        imageToProcess = cv2.resize(imageToProcess, dsize=(0, 0), fx=0.3, fy=0.3, interpolation=cv2.INTER_LINEAR)

        datum.cvInputData = imageToProcess

        opWrapper.emplaceAndPop([datum])

        #points = datum.poseKeypoints

        cv2.imshow("Pose", datum.cvOutputData)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except Exception as e:
    sys.exit(-1)
