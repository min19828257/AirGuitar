import os
import sys
import cv2

def pose_detection():
    img_path = './media/COCO_val2014_000000000474.jpg'
    
    dir_path = os.path.dirname(os.path.realpath(__file__))
    sys.path.append(dir_path + '/python/openpose/Release');
    os.environ['PATH']  = os.environ['PATH'] + ';' + dir_path + '/x64/Release;' +  dir_path + '/bin;'
    import pyopenpose as op

    params = dict()
    params["model_folder"] = "./models/"
    #params["face"] = True
    params["hand"] = True


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
        left = datum.handKeypoints[0]
        right = datum.handKeypoints[1]

        leftX = []
        leftY = []
        rightX = []
        rightY = []
        for l in left[0]:
            leftX.append(l[0])
            leftY.append(l[1])
        for r in right[0]:
            rightX.append(r[0])
            rightY.append(r[1])

        cv2.imshow("Pose and Hand", datum.cvOutputData)
        cv2.waitKey(0)

    except Exception as e:
        sys.exit(-1)

    return leftX, leftY, rightX, rightY
