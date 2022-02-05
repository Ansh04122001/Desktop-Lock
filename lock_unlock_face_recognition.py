import cv2
import sys
import numpy as np
import pyautogui
import ctypes
import os
import datetime
import time


def assure_path_exists(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)


counter_correct = 0  # counter variable to count number of times loop runs
counter_wrong = 0

now = datetime.datetime.now()  # extract current time
now = now.second  # we need only seconds

recognizer = cv2.face.LBPHFaceRecognizer_create()

assure_path_exists("dataset/")  # add path to the folder where all the files are saved

recognizer.read('trainer.yml')  # load training model

cascadePath = ("haarcascade_frontalface_default.xml")  # cascade path

faceCascade = cv2.CascadeClassifier(cascadePath);  # load cascade

font = cv2.FONT_HERSHEY_COMPLEX_SMALL  # Set the font style

cam = cv2.VideoCapture(0)

while True:

    ret, im = cam.read()

    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:

        cv2.rectangle(im, (x - 20, y - 20), (x + w + 20, y + h + 20), (0, 255, 0), 4)

        Id, confidence = recognizer.predict(gray[y:y + h, x:x + w])  # Recognize the face belongs to which ID

        if (confidence > 80):  # confidence usually comes greater than 80 for strangers
            counter_wrong += 1
            print("Wrong")
            Id = "Unknown + {0:.2f}%".format(round(100 - confidence, 2))
            print(confidence)
            print("counter_wrong - " + str(counter_wrong))
            cv2.rectangle(im, (x - 22, y - 90), (x + w + 22, y - 22), (0, 0, 255), -1)
            cv2.putText(im, str(Id), (x, y - 40), font, 1, (0, 0, 0), 2)
        else:  # confidence usually comes less than 80 for correct user(s)
            Id = "Ansh + {0:.2f}%".format(round(100 - confidence, 2))
            print("Verified")
            print(confidence)
            counter_correct += 1
            print("counter_correct - " + str(counter_correct))
            cv2.rectangle(im, (x - 22, y - 90), (x + w + 22, y - 22), (255, 255, 255), -1)
            cv2.putText(im, str(Id), (x, y - 40), font, 1, (0, 0, 0), 2)

        if (counter_wrong == 3):
            pyautogui.moveTo(48, 748)
            pyautogui.click(48, 748)
            cam.release()
            cv2.destroyAllWindows()
            ctypes.windll.user32.LockWorkStation()
            sys.exit()

    cv2.imshow('Webcam', im)

    if cv2.waitKey(10) & 0xFF == ord('*'):  # If '*' is pressed, terminate the  program
        break

cam.release()

cv2.destroyAllWindows()
