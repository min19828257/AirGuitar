import cv2
import math

pose_protoFile = "./pose/pose_deploy_linevec.prototxt"
pose_weightsFile = "./pose/pose_iter_440000.caffemodel"
pose_net = cv2.dnn.readNetFromCaffe(pose_protoFile, pose_weightsFile)

hand_protoFile = "hand/pose_deploy.prototxt"
hand_weightsFile = "hand/pose_iter_102000.caffemodel"
hand_net = cv2.dnn.readNetFromCaffe(hand_protoFile, hand_weightsFile)


def line_len(p1, p2):
    x = p2[0] - p1[0]
    y = p1[1] - p2[1]
    return int(math.sqrt((x * x) + (y * y))), x, y

def pose_detection(img_path):

    image = cv2.imread(img_path)
    imageHeight, imageWidth, _ = image.shape     
    inpBlob = cv2.dnn.blobFromImage(image, 1.0 / 255, (imageWidth, imageHeight), (0, 0, 0), swapRB=False, crop=False)
     
    pose_net.setInput(inpBlob)
    output = pose_net.forward()

    H = output.shape[2]
    W = output.shape[3]

    points = []
    for i in range(0, 15):
        probMap = output[0, i, :, :]
        minVal, prob, minLoc, point = cv2.minMaxLoc(probMap)

        x = (imageWidth * point[0]) / W
        y = (imageHeight * point[1]) / H
  
        if prob > 0.1:    
            cv2.circle(image, (int(x), int(y)), 3, (0, 255, 255), thickness=-1, lineType=cv2.FILLED)
            cv2.putText(image, "{}".format(i), (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, lineType=cv2.LINE_AA)
            points.append((int(x), int(y)))
        else :
            points.append(None)

    elbow_l = points[3]
    hand_l = points[4]
    elbow_r = points[6]
    hand_r = points[7]

    cv2.imshow('Output-Keypoints', image)
    cv2.imwrite('./test.jpg', image)
    cv2.waitKey(0)    

    return [elbow_l, hand_l], [elbow_r, hand_r]


def hand_detection(img_path, center):

    #elbow = center[0]
    hand = center[1]
    #l, horizon, vertical = line_len(elbow, hand)

    l = 100

    left = hand[0] - l
    right = hand[0] + l
    bottom = hand[1] - l
    top = hand[1] + l
     
    image = cv2.imread(img_path)
    imageHeight, imageWidth, _ = image.shape
    image = image[bottom:top, left:right]
    image = cv2.resize(image, dsize=(200, 200), interpolation=cv2.INTER_LINEAR)

    imageHeight, imageWidth, _ = image.shape
    threshold = 0.1
    nPoints = 22

    inpBlob = cv2.dnn.blobFromImage(image, 1.0 / 255, (imageWidth, imageHeight), (0, 0, 0), swapRB=False, crop=False) 
    hand_net.setInput(inpBlob) 
    output = hand_net.forward()
    points = []
    imageCopy = image

    for i in range(nPoints):
        probMap = output[0, i, :, :]
        probMap = cv2.resize(probMap, (imageWidth, imageHeight))
        minVal, prob, minLoc, point = cv2.minMaxLoc(probMap)

        if prob > threshold :
            cv2.circle(imageCopy, (int(point[0]), int(point[1])), 8, (0, 255, 255), thickness=-1, lineType=cv2.FILLED)
            cv2.putText(imageCopy, "{}".format(i), (int(point[0]), int(point[1])), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, lineType=cv2.LINE_AA)
            points.append((int(point[0]), int(point[1])))
        else :
            points.append(None)

    cv2.imshow('Output-Keypoints', imageCopy)
    cv2.waitKey(0)

img_path = "media/COCO_val2014_000000000294.jpg"

hands = pose_detection(img_path)
for hand in hands:
    hand_detection(img_path, hand)