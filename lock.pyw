import os
from pynput.keyboard import Key, Listener
import playsound
import pyautogui
import jdatetime
import turtle as t 
import time
from random import randint
import keyboard
from threading import Thread
pyautogui.FAILSAFE = False
stop = "no"
import screeninfo
try:
    def lock():
        while True:
            pyautogui.moveTo(5,5)
            if(stop == "yes"):
                break
    thread1=Thread(target=lock,args=[])
    thread1.start()
    def on_press(key):
        key_press = key
        if ("ctrl" in str(key_press)):
            os.system("shutdown /p /f")
        if ("cmd" in str(key_press)):
            #os.system("shutdown /p /f")
            pass
        if ("esc" in str(key_press)):
            os.system("shutdown /p /f")
    def listen():
        with Listener(on_press=on_press) as listener:
            listener.join()
    thread2=Thread(target=listen,args=[])
    thread2.start()
    import screeninfo
    import numpy as np
    import cv2
    def slides():
        screen_id = 2
        is_color = False
        screen = screeninfo.get_monitors()[0]
        width, height = screen.width, screen.height
        window_name = 'FreezeWall;'
        cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)
        cv2.moveWindow(window_name, screen.x - 1, screen.y - 1)
        cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN,
                              cv2.WINDOW_FULLSCREEN)
        file2=open("data/dtcheck2.txt","w")
        file2.write("0")
        file2.close()
        file2=open("data/dtcheck2.txt","r")
        rdf=file2.read()
        file2.close()
        while rdf=="0":
            files = os.listdir("pic")
            num = randint(1,len(files))
            try:
                image = cv2.imread("pic/Slide"+str(num)+".JPG")
                cv2.imshow(window_name, image)
                key = cv2.waitKey(2000)# pauses for 3 seconds before fetching next image
                file2=open("data/dtcheck2.txt","r")
                rdf=file2.read()
                file2.close()
                if(rdf=="1"):
                    break
            except Exception as e:
                pass
        cv2.destroyAllWindows()
    thread3=Thread(target=slides,args=[])
    thread3.start()
    face_cascade = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')
    smileCascade = cv2.CascadeClassifier('data/haarcascade_smile.xml')
    eyeCascade = cv2.CascadeClassifier('data/haarcascade_eye.xml')
    playsound.playsound("data/activated.mp3")
    time.sleep(0.1)
    playsound.playsound("data/locked.mp3")
    rec = cv2.face.LBPHFaceRecognizer_create();
    rec.read("data/trainingdata.yml")
    cap = cv2.VideoCapture(0)
    id = 0
    stop = "no"
    fontFace = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 1
    fontColor = (255, 255, 255)
    playsound.playsound("data/start.mp3")
    times =0
    afk=0
    file=open("data/pin.txt")
    bpin=file.read()
    file.close()
    file=open("data/dtcheck2.txt",'w')
    file.write("1")
    file.close() 
    while True:
        screen_id = 2
        is_color = False
        screen = screeninfo.get_monitors()[0]
        width, height = screen.width, screen.height
        window_name = 'Face Recognizer;'
        cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)
        cv2.moveWindow(window_name, screen.x - 1, screen.y - 1)
        cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN,
                              cv2.WINDOW_FULLSCREEN)
        times +=1
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.5, 5)
        if keyboard.is_pressed("p")or keyboard.is_pressed("P"):
            ppin=pyautogui.password(text='کنيد وارد را کد پين.', title='پين کد اضطراري', default='', mask='*')
            if(ppin==bpin):
                break
        for (x, y, w, h) in faces:
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
            eyes = eyeCascade.detectMultiScale(
                roi_gray,
                scaleFactor= 1.5,
                minNeighbors=10,
                minSize=(5, 5),
                )
            smile = smileCascade.detectMultiScale(
                roi_gray,
                scaleFactor= 1.5,
                minNeighbors=15,
                minSize=(25, 25),
                )
            qx=x+w//2
            qy=y+h//2
            id, conf = rec.predict(gray[y:y + h, x:x + w])
            print(conf)
            if(conf<=48):
                cv2.rectangle(img, (x, y), (x + w, y + h), (50,255,50), 2)
                #cv2.circle(img,(qx, qy),(w+h)//4,(50,255,50),1.5)
                for (xx, yy, ww, hh) in smile:
                    cv2.rectangle(roi_color, (xx, yy), (xx + ww, yy + hh), (50, 255, 50), 2)
                for (ex, ey, ew, eh) in eyes:
                    qqx=ex+ew//2
                    qqy=ey+eh//2
                    cv2.circle(roi_color,(qqx, qqy),(ew+eh)//4,(50,255,50),2)
                    #cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (50,255,50), 2)       
                ido="User Detected_Access Granted;"
                stop = "yes"
            else:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0,0,255), 2)
                #cv2.circle(img,(qx, qy),(w+h)//4,(0,0,255),1)
                for (xx, yy, ww, hh) in smile:
                    cv2.rectangle(roi_color, (xx, yy), (xx + ww, yy + hh), (0, 0, 255), 2)
                for (ex, ey, ew, eh) in eyes:
                    qqx=ex+ew//2
                    qqy=ey+eh//2
                    cv2.circle(roi_color,(qqx, qqy),(ew+eh)//4,(0, 0, 255),2)
                    #cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 0, 255), 2)       
                ido="Unknown_Access Denied;"
                afk+=1
            if(afk>=200):
                ppin=pyautogui.password(text='کنيد وارد را کد پين.', title='پين کد اضطراري', default='', mask='*')
                if(ppin==bpin):
                    stop = "yes"
            cv2.putText(img, ido, (x+5,y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1)
            cv2.putText(img, str(int(conf)//1), (x+5,y+h-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1)  
            cv2.imshow(window_name, img)
            cv2.waitKey(1)
            if(stop=="yes"):
                break
        if(stop == "yes"):
            break
    file=open("data/log.txt",'r')
    files=file.read()
    file.close()
    file=open("data/log.txt",'w')
    from datetime import datetime
    now = datetime.now()
    jdatetime.set_locale('fa_IR')
    now_date=jdatetime.datetime.now().strftime("%Y/%m/%d")
    now_time=jdatetime.datetime.now().strftime("%H:%M")
    reg_date =  str(now_date)+str(now_time)
    if(files !=""):
        file.write(files+"\n id "+str(id)+" logged on with confidence of "+str(conf*2)+" at "+str(reg_date))
    else:
        file.write("id " + str(id) + " logged on with confidence of " + str(conf * 2) + " at " + str(reg_date))
    file.close()
    cap.release()
    playsound.playsound("data/done.mp3")
    playsound.playsound("data/unlocked.mp3")
    os._exit(0)
except:
    pass
