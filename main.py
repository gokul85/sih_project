import cv2
from cvzone.HandTrackingModule import HandDetector
import pyautogui
from simple_facerec import SimpleFacerec

# Variables
width, height = 1280, 720
gesture = ""
names = []

#encode faces
sfr = SimpleFacerec()
names = sfr.load_encoding_images("Image/")

#hand detector
detector = HandDetector(detectionCon=0.8,maxHands=1)



#camera setup
cap = cv2.VideoCapture(0)
cap.set(3, width)
cap.set(4, height)

while True:
    #import img
    success, img = cap.read()

    # img = cv2.flip(img, 1)

    hands, img = detector.findHands(img)

    # detect face
    face_locations, face_names = sfr.detect_known_faces(img)
    # print(names)
    # print(face_names)
    if hands:
        hand = hands[0]
        fingers = detector.fingersUp(hand)
        # print(fingers)

        if fingers == [1,0,0,0,0] and gesture != "esc":
            for i in face_names:
                if i in names:
                    gesture = "esc"
                    pyautogui.press('esc')
                    print("esc")

        if fingers == [1,1,1,1,1] and gesture != "initial":
            for i in face_names:
                if i in names:
                    gesture = "initial"
                    print("initial")

        if fingers == [0,1,0,0,0] and gesture != "right":
            for i in face_names:
                if i in names:
                    gesture = "right"
                    pyautogui.press('right')
                    print("right")

        if fingers == [0,1,1,0,0] and gesture != "left":
            for i in face_names:
                if i in names:
                    gesture = "left"
                    pyautogui.press('left')
                    print("left")

        if fingers == [1,1,0,0,0] and gesture != "presentation":
            for i in face_names:
                if i in names:
                    gesture = "presentation"
                    pyautogui.press('f5')
                    print("presentation")

        if fingers == [0,1,0,0,1] and gesture != "Print":
            for i in face_names:
                if i in names:
                    gesture = "Print"
                    with pyautogui.hold('ctrl'):
                        pyautogui.press('p')
                    print("Print")

        if fingers == [0,0,0,0,0] and gesture != "Closed":
            for i in face_names:
                if i in names:
                    gesture = "Closed"
                    with pyautogui.hold('alt'):
                        pyautogui.press('f4')
                    print("Closed")
    for face_loc, name in zip(face_locations, face_names):
        y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

        cv2.putText(img, name, (x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 200, 0), 2)
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 200, 0), 4)
    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break