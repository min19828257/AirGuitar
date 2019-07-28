import os
import sys
import cv2

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path + '/python/openpose/Release');
os.environ['PATH']  = os.environ['PATH'] + ';' + dir_path + '/x64/Release;' +  dir_path + '/bin;'
import pyopenpose as op

params = dict()
params["model_folder"] = "./models/"
#params["face"] = True
params["hand"] = True

img_path = './media/COCO_val2014_000000000474.jpg'

try:
    opWrapper = op.WrapperPython()
    opWrapper.configure(params)
    opWrapper.start()

    datum = op.Datum()
    imageToProcess = cv2.imread(img_path)
    datum.cvInputData = imageToProcess

    opWrapper.emplaceAndPop([datum])

    #body = str(datum.poseKeypoints)
    #face = str(datum.faceKeypoints)
    hand_L = str(datum.handKeypoints[0])
    hand_R = str(datum.handKeypoints[1])

    cv2.imshow("Pose and Hand", datum.cvOutputData)
    cv2.waitKey(0)

except Exception as e:
    sys.exit(-1)
