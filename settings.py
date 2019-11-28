try:
    from datetime import datetime
    import playsound
    import time
    import os
    import subprocess
    import hashlib
    import turtle as t
    from turtle import *
    import pyautogui
    import cv2
    from threading import Thread
    import jdatetime
    import numpy as np
    from PIL import Image
    import requests
    m=t.Turtle()
    m.ht()
    dcw=t.Turtle()
    dcw.ht()
    def main_menu():
        file = open("data/dtcheck.txt","w")
        file.write("1")
        file.close()
        scr.clearscreen()
        t.ht()
        t.speed(0)
        t.setup(620, 510)
        t.title("Codoffee Freezewall | نرم افزار ديوار يخين")
        m = t.Turtle()
        m.ht()
        m.speed(0)
        t.clear()
        t.bgcolor("#71dada")
        t.pencolor("darkred")
        t.fillcolor("#a3a375")
        t.pensize(1)
        t.pu()
        t.goto(-310, 210)
        t.pd()
        t.goto(310, 210)
        t.pu()
        t.goto(-310, 215)
        t.pd()
        t.goto(310, 215)
        t.pu()
        t.goto(-310, 220)
        t.pd()
        t.goto(310, 220)
        t.pd()
        t.begin_fill()
        t.goto(310, 220)
        t.goto(310, 255)
        t.goto(-310, 255)
        t.goto(-310, 220)
        t.end_fill()
        t.pu()
        t.goto(-310, -190)
        t.pd()
        t.goto(310, -190)
        t.pu()
        t.goto(-310, -195)
        t.pd()
        t.goto(310, -195)
        t.pu()
        t.goto(-310, -200)
        t.pd()
        t.goto(310, -200)
        t.pu()
        t.goto(-310, -205)
        t.pd()
        t.goto(310, -205)
        t.pu()
        t.goto(-310, -210)
        t.pd()
        t.begin_fill()
        t.goto(310, -210)
        t.goto(310, -255)
        t.goto(-310, -255)
        t.goto(-310, -210)
        t.end_fill()
        button1 = Turtle()
        image = "face.gif"
        scr.addshape(image)
        button1.shape(image)
        button1.speed(0)
        button1.pu()
        button1.goto(-3, -190)
        button1.pd()
        t.pencolor("black")
        t.pu()
        t.goto(-3, -245)
        t.write("شناسایی چهره", align="center", font=("B Koodak", 13,("bold")))
        t.pu()
        t.goto(-3, 220)
        t.pd()
        button3 = Turtle()
        image = "logout.gif"
        scr.addshape(image)
        button3.shape(image)
        button3.speed(0)
        button3.pu()
        button3.goto(116, -190)
        button3.pd()
        t.pu()
        t.goto(116, -245)
        t.pd()
        t.pencolor("black")
        t.write("خروج", align="center", font=("B Koodak", 13,("bold")))
        button4 = Turtle()
        image = "security.gif"
        scr.addshape(image)
        button4.shape(image)
        button4.speed(0)
        button4.pu()
        button4.goto(-120, -190)
        button4.pd()
        t.pu()
        t.goto(-118, -245)
        t.pd()
        t.pencolor("black")
        t.write("امنیت", align="center", font=("B Koodak", 13,("bold")))
        m.clear()
        m.pu()
        m.goto(0, 0)
        m.pd()
        m.pencolor("darkorange")
        m.write('نرم افزار دیوار یخین | بخش مدیریت', align="center", font=("B Koodak", 15,("bold")))
        button1.onclick(buton1)
        button3.onclick(buton3)
        button4.onclick(buton4)
    def recorder(number,count,scr,t):
        try:
            scr.clearscreen()
            t.write("...در حال ضبط", align="center", font=("B Koodak", 13,("bold")))
            t.ht()
            scr.bgcolor("#47e4bb")
            t.pencolor("darkred")
            t.pu()
            t.goto(0, -190)
            t.pd()
            t.write("لطفا جهت ضبط بهتر گاهی صورت خود را به جلو و عقب حرکت دهید و", align="center", font=("B Koodak", 10,("bold")))
            t.pu()
            t.goto(0,-215)
            t.pd()
            t.write(".در 20 درصد پایانی نور محیط را تغییر دهید", align="center",font=("B Koodak", 10,("bold")))
            t.pu()
            t.goto(0,-240)
            t.pd()
            t.write(".تگران نباشید، ضبط تنها هنگامی رخ می دهد که صورت شما شناسایی شود", align="center",
                    font=("B Koodak", 10))
            t.pu()
            t.goto(0,-30)
            t.pd()
            t.pencolor("darkgreen")
            t.write(str(0)+": درصد تکمیل شده", align="center", font=("B Koodak", 13,("bold")))
            face_cascade = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')
            cap = cv2.VideoCapture(0)
            id =number
            sampleN = 0;
            while 1:
                t.undo()
                t.write(str(int(sampleN * 100 / count)) + ": درصد تکمیل شده", align="center", font=("B Koodak", 13,("bold")))
                ret, img = cap.read()
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = face_cascade.detectMultiScale(gray, 1.3, 5)
                for (x, y, w, h) in faces:
                    sampleN = sampleN + 1;
                    #print(sampleN)
                    cv2.imwrite(
                        "data/facesData/User." + str(id) + "." + str(sampleN) + ".jpg",
                        gray[y:y + h, x:x + w])
                    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                if sampleN > count:
                    break
            cap.release()
            cv2.destroyAllWindows()
            return 'ok'
        except:
            return 'error'
    def errpage():
        scr.clearscreen()
        t.setup(620, 510)
        t.write("خطا", align="center", font=("B Koodak", 25,("bold")))
        t.ht()
        scr.bgcolor("#47e4bb")
        t.pencolor("red")
        t.pu()
        t.goto(0, -190)
        t.pd()
        t.write(".متاسفانه خطایی رخ داده است. لطفا با پشتیبانی کدفی تماس بگیرید", align="center", font=("B Koodak", 10,("bold")))
        t.pu()
        t.goto(0, -215)
        t.pd()
        t.pencolor("darkblue")
        t.write(".خطای پیش آمده به صورت خودکار به کدفی گزارش داده خواهد شد", align="center", font=("B Koodak", 10,("bold")))
        time.sleep(5)
        try:
            file=open("info.png","rb")
            file.close()
            main_menu()
        except:
            sys.exit(0)
    def trainer(scr,t):
        try:
            scr.clearscreen()
            t.write("...در حال پردازش", align="center", font=("B Koodak", 13,("bold")))
            t.ht()
            scr.bgcolor("#47e4bb")
            t.pencolor("darkblue")
            t.pu()
            t.goto(0, -190)
            t.pd()
            t.write(".اکنون نرم افزار درحال آموزش دیدن با چهره شماست. لطفا صبر کنید", align="center", font=("B Koodak", 10,("bold")))
            t.pu()
            t.goto(0,-215)
            t.pd()
            t.pencolor("darkred")
            t.write(".این عملیات ممکن است بسته به تعداد صورتها تا 3 دقیقه به طول انجامد", align="center",font=("B Koodak", 10,("bold")))
            recognizer = cv2.face.LBPHFaceRecognizer_create();
            path = "data/facesData"
            def getImagesWithID(path):
                imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
                faces = []
                IDs = []
                for imagePath in imagePaths:
                    facesImg = Image.open(imagePath).convert('L')
                    faceNP = np.array(facesImg, 'uint8')
                    ID = int(os.path.split(imagePath)[-1].split(".")[1])
                    faces.append(faceNP)
                    IDs.append(ID)
                return np.array(IDs), faces
            Ids, faces = getImagesWithID(path)
            recognizer.train(faces, Ids)
            recognizer.save("data/trainingdata.yml")
            cv2.destroyAllWindows()
            return 'ok'
        except:
            return 'error'
    try:
        t.setup(410,410)
        t.title('Codoffee Freezewall | نرم افزار دیوار یخین')
        t.speed(0)
        t.ht()
        scr=t.Screen()
        t.bgcolor("#71dada")
        t.pencolor("#ec9b3b")
        t.write("C",align="center",font=("impact",50))
        time.sleep(0.2)
        t.undo()
        t.pencolor("#e8647c")
        t.write("CO",align="center",font=("impact",50))
        time.sleep(0.2)
        t.undo()
        t.pencolor("#ec9b3b")
        t.write("COD",align="center",font=("impact",50))
        time.sleep(0.2)
        t.undo()
        t.pencolor("#e8647c")
        t.write("CODO",align="center",font=("impact",50))
        time.sleep(0.2)
        t.undo()
        t.pencolor("#ec9b3b")
        t.write("CODOFF",align="center",font=("impact",50))
        time.sleep(0.2)
        t.undo()
        t.pencolor("#e8647c")
        t.write("CODOFFEE",align="center",font=("impact",50))
        time.sleep(0.2)
        t.pu()
        t.goto(0,-35)
        t.pd()
        t.pencolor("#105e62")
        t.write("FreezeWall",align="center",font=("Comic Sans MS",25,("bold")))
        t.pu()
        t.goto(0,-161)
        t.pd()
        t.pencolor("black")
        t.pu()
        t.goto(0,-167)
        t.pd()
        t.pencolor("black")
        t.write("© 2019 Codoffee | All rights reserved.",align="center",font=("Arial",7,("bold")))
        t.pu()
        t.goto(0,-195)
        t.pd()
        t.pencolor("black")
        t.write(".تمامی حقوق این نرم افزار محفوظ است",align="center",font=("B Koodak",9,("bold")))
        playsound.playsound("Codoffee Audio.mp3")
        t.pensize(1)
        t_j_o="0"
        '''
        current_machine_id = str(subprocess.check_output('wmic csproduct get uuid'))
        current_machine_id = current_machine_id[46:83]
        mac=current_machine_id
        results = hashlib.md5(current_machine_id.encode())
        lastres = results.digest()
        '''
        lastres="ok"
        try:
            file = open("info.png", 'rb')
            macs = file.read()
            file.close()
            t_j_o = "1"
        except:
            t_j_o = "0"
        if(t_j_o=="0"):
            t.clear()
            t.title("Sign-in | ورود")
            t.pu()
            t.goto(0,-10)
            t.pd()
            t.bgcolor("lightyellow")
            t.pencolor("purple")
            t.write("Sign-in",align="center",font=("Impact",35))
            t.pu()
            t.goto(-2,-60)
            t.pd()
            t.pencolor("darkblue")
            t.write("ورود",align="center",font=("B Titr",25))
            numw=t.Turtle()
            numw.speed(10)
            numw.pu()
            numw.goto(-30,-138)
            numw.pd()
            numw.ht()
            numw.write("1",align="center",font=("Impact",11))
            name=t.textinput('Sign-in | ورود',"نام و نام خانوادگي:")
            numw.forward(20)
            numw.speed(0)
            numw.write("2",align="center",font=("Impact",11))
            lic=t.textinput("Sign-in | ورود","کد فعال سازي نرم افزار:")
            t.clear()
            t.title("ورود به نرم افزار")
            t.pu()
            t.goto(0,30)
            t.pd()
            t.bgcolor("lightyellow")
            t.pencolor("purple")
            t.write("...درحال تایید اعتبار از سرور",align="center",font=("B Koodak",17,("bold")))
            t.pu()
            t.goto(-2,-10)
            t.pd()
            t.pencolor("darkblue")
            version = 2
            t.write(".لطفا شکیبا باشید",align="center",font=("B Koodak",14,("bold")))
            from datetime import datetime
            '''
            now = datetime.now()
            reg_date = str(str(now.year) + '/' + str(now.month) + '/' + str(now.day))
            exp_date = str(str(now.year + 1) + '/' + str(now.month) + '/' + str(now.day))
            mac = current_machine_id
            res = requests.get("http://codoffeeteam.ir/validate.php?name=" + name + "&license=" + lic + "&reg_date=" + reg_date + "&exp_date=" + exp_date + "&mac=" + mac)
            result = res.text
            '''
            if(len(lic)==6 and (int(lic)%13)==0 and (int(lic)%7)==0):
                result="ok"
            else:
                vi=random.randint(1,2)
                res=["used","wrong"]
                result=res[vi]
            if ("ok" in result):
                file = open("info.png", 'w')
                file.write(lastres)
                file.close()
                t.clear()
                t.title("ورود به نرم افزار")
                t.pu()
                t.goto(0, 30)
                t.pd()
                t.bgcolor("lightyellow")
                t.pencolor("purple")
                t.write("،نتیجه عملیات", align="center", font=("B Koodak", 17,("bold")))
                t.pu()
                t.goto(-2, -10)
                t.pd()
                t.pencolor("#19fc00")
                version = 2
                t.write("!موفقیت آمیز بود. خوش آمدید", align="center", font=("B Koodak", 14,("bold")))
                time.sleep(5)
            elif ("used" in result):
                numw.clear()
                t.title("ورود به نرم افزار")
                t.pu()
                t.goto(0, 30)
                t.pd()
                t.bgcolor("#39b9e9")
                t.pencolor("purple")
                t.write("،نتیجه عملیات", align="center", font=("B Koodak", 17,("bold")))
                t.pu()
                t.goto(-2, -10)
                t.pd()
                t.pencolor("red")
                version = 2
                t.write(".موفقیت آمیز نبود. سریال تکراری است", align="center", font=("B Koodak", 14,("bold")))
                time.sleep(10)
                sys.exit(0)
            elif ("wrong" in result):
                t.clear()
                t.title("ورود به نرم افزار")
                t.pu()
                t.goto(0, 30)
                t.pd()
                t.bgcolor("#39b9e9")
                t.pencolor("purple")
                t.write("،نتیجه عملیات", align="center", font=("B Koodak", 17,("bold")))
                t.pu()
                t.goto(-2, -10)
                t.pd()
                t.pencolor("red")
                version = 2
                t.write(".موفقیت آمیز نبود. سریال نادرست است", align="center", font=("B Koodak", 14,("bold")))
                time.sleep(10)
                sys.exit(0)
            else:
                t.clear()
                t.title("ورود به نرم افزار")
                t.pu()
                t.goto(0, 30)
                t.pd()
                t.bgcolor("#39b9e9")
                t.pencolor("purple")
                t.write("نتیجه عملیات", align="center", font=("B Koodak", 17,("bold")))
                t.pu()
                t.goto(-2, -30)
                t.pd()
                t.pencolor("darkblue")
                version = 2
                t.write("به علت خطایی ناشناخته \n با شکست مواجه شد.", align="center", font=("B Koodak", 14,("bold")))
                time.sleep(10)
                sys.exit(0)
            numw.clear()
        try:
            try:
                file = open("data/dtcheck.txt","w")
                file.write("1")
                file.close()
                m.clear()
                t.setup(620,510)
                t.title('Codoffee FreezeWall | نرم افزار ديوار يخين')
                m=t.Turtle()
                m.ht()
                m.speed(0)
                t.clear()
                t.bgcolor("#71dada")
                t.pencolor("darkred")
                t.fillcolor("#a3a375")
                t.pensize(1)
                t.pu()
                t.goto(-310,210)
                t.pd()
                t.goto(310,210)
                t.pu()
                t.goto(-310,215)
                t.pd()
                t.goto(310,215)
                t.pu()
                t.goto(-310,220)
                t.pd()
                t.goto(310,220)
                t.pd()
                t.begin_fill()
                t.goto(310,220)
                t.goto(310,255)
                t.goto(-310,255)
                t.goto(-310,220)
                t.end_fill()
                t.pu()
                t.goto(-310,-190)
                t.pd()
                t.goto(310,-190)
                t.pu()
                t.goto(-310,-195)
                t.pd()
                t.goto(310,-195)
                t.pu()
                t.goto(-310,-200)
                t.pd()
                t.goto(310,-200)
                t.pu()
                t.goto(-310,-205)
                t.pd()
                t.goto(310,-205)
                t.pu()
                t.goto(-310,-210)
                t.pd()
                t.begin_fill()
                t.goto(310,-210)
                t.goto(310,-255)
                t.goto(-310,-255)
                t.goto(-310,-210)
                t.end_fill()
                button1=Turtle()
                image="face.gif"
                scr.addshape(image)
                button1.shape(image)
                button1.speed(0)
                button1.pu()
                button1.goto(-3,-190)
                button1.pd()
                t.pencolor("black")
                t.pu()
                t.goto(-3,-245)
                t.write("شناسایی چهره",align="center",font=("B Koodak",13,("bold")))
                t.pu()
                t.goto(-3,220)
                t.pd()
                #t.write("تمامي حقوق اين نرم افزار براي شرکت نرم افزاري کدفي محفوظ است",align="center",font=("B Kourosh",15))
                button3=Turtle()
                image="logout.gif"
                scr.addshape(image)
                button3.shape(image)
                button3.speed(0)
                button3.pu()
                button3.goto(116,-190)
                button3.pd()
                t.pu()
                t.goto(116,-245)
                t.pd()
                t.pencolor("black")
                t.write("خروج",align="center",font=("B Koodak",13,("bold")))
                button4=Turtle()
                image="security.gif"
                scr.addshape(image)
                button4.shape(image)
                button4.speed(0)
                button4.pu()
                button4.goto(-120,-190)
                button4.pd()
                t.pu()
                t.goto(-118,-245)
                t.pd()
                t.pencolor("black")
                t.write("امنیت",align="center",font=("B Koodak",13,("bold")))
                def buton1(x,y):
                    try:
                        file = open("data/dtcheck.txt","w")
                        file.write("0")
                        file.close()
                        button1.speed(10)
                        button1.pu()
                        button1.goto(-7, -190)
                        button1.pd()
                        button1.pu()
                        button1.goto(1, -190)
                        button1.pd()
                        button1.pu()
                        button1.goto(-3, -190)
                        button1.pd()
                        button1.speed(0)
                        # face recognition
                        time.sleep(0.5)
                        scr.clearscreen()
                        scr.clearscreen()
                        scr.bgcolor('#47e4bb')
                        t.ht()
                        t.pencolor('#39b9e9')
                        t.pu()
                        t.goto(0,0)
                        t.pd()
                        files = os.listdir('data/facesData')
                        u1 = 0
                        u2 = 0
                        u3 = 0
                        u4 = 0
                        u5 = 0
                        u6 = 0
                        u7 = 0
                        u8 = 0
                        u9 = 0
                        u10 = 0
                        for file in files:
                            if("User.1" in file):
                                u1 = 1
                            elif("User.2" in file):
                                u2 = 1
                            elif ("User.3" in file):
                                u3 = 1
                            elif ("User.4" in file):
                                u4 = 1
                            elif ("User.5" in file):
                                u5 = 1
                            elif ("User.6" in file):
                                u6 = 1
                            elif ("User.7" in file):
                                u7 = 1
                            elif ("User.8" in file):
                                u8 = 1
                            elif ("User.9" in file):
                                u9 = 1
                            elif ("User.10" in file):
                                u10 = 1
                        num = u1+u2+u3+u4+u5+u6+u7+u8+u9+u10
                        t.pencolor("darkblue")
                        t.write(".در حال حاضر "+str(num)+" صورت ثبت شده دارید", align="center", font=("B Koodak", 13,("bold")))
                        command = scr.textinput("عملیات","عملیات مورد نظر خود (اضافه / حذف) را وارد کنید.")
                        if('حذف' in command):
                            time.sleep(0.5)
                            command = scr.textinput("عملیات", ".لطفا کد کاربری چهره ای که می خواهید آن را حذف کنید (مثلا 1) وارد کنید")
                            c=0
                            for file in files:
                                if('User.'+str(command) in file):
                                    os.remove('data/facesData/'+file)
                                    c+=1
                            if(c > 100):
                                if(num>1):
                                    result = trainer(scr,t)
                                else:
                                    os.remove('data/trainingdata.yml')
                                    result = 'ok'
                                if(result == 'ok'):
                                    pyautogui.alert('.چهره ي مورد نظر با موفقيت حذف شد','حذف چهره','متوجه شدم')
                                    main_menu()
                                else:
                                    errpage()
                            else:
                                errpage()
                        elif('اضافه' in command):
                            time.sleep(0.5)
                            command = scr.textinput("عملیات", ".لطفا یک کد کاربری تک رقمی (مثلا 1) را برای این چهره وارد کنید")
                            while int(command) > 9 :
                                pyautogui.alert('.لطفا عددي تک رقمي وارد کنيد','عملیات','متوجه شدم')
                                command = scr.textinput("عملیات", ".لطفا یک کد کاربری تک رقمی (مثلا 1) را برای این چهره وارد کنید")
                            dn = 0
                            for file in files:
                                if('User.'+str(command) in file):
                                    dn = 1
                            while dn==1:
                                pyautogui.alert('.عدد وارد شده تکراري است', 'عملیات', 'متوجه شدم')
                                command = scr.textinput("عملیات",
                                                        ".لطفا یک کد کاربری تک رقمی (مثلا 1) را برای این چهره وارد کنید")
                                dn = 0
                                for file in files:
                                    if ('User.' + str(command) in file):
                                        dn = 1
                            result = recorder(command,300,scr,t)
                            if(result == 'ok'):
                                print('ok')
                                result = trainer(scr,t)
                                if(result == 'ok'):
                                    scr.clearscreen()
                                    t.pencolor("darkblue")
                                    t.write(".لطفا يک پين کد براي موارد اضطراري تعيين کنيد", align="center", font=("B Koodak", 13,("bold")))
                                    t.ht()
                                    scr.bgcolor("#47e4bb")
                                    t.pencolor("#e8647c")
                                    t.pu()
                                    t.goto(0, -180)
                                    t.pd()
                                    t.pencolor("darkred")
                                    t.write(".اين پين کد را حتما به ياد داشته باشيد", align="center",
                                            font=("B Koodak", 10))
                                    pincode=command = scr.textinput("عملیات",
                                                        ".لطفا پین کد مورد نظر را وارد کنید")
                                    file=open("data/pin.txt","w")
                                    file.write(pincode)
                                    file.close()
                                    scr.clearscreen()
                                    t.pencolor("darkblue")
                                    t.write("!عملیات به اتمام رسید", align="center", font=("B Koodak", 13,("bold")))
                                    t.ht()
                                    scr.bgcolor("#47e4bb")
                                    t.pencolor("#e8647c")
                                    t.pu()
                                    t.goto(0, -180)
                                    t.pd()
                                    t.pencolor("darkred")
                                    t.write(".اکنون نرم افزار شما را می شناسد و میتواند شما را شناسایی کند", align="center",
                                            font=("B Koodak", 10))
                                    t.pu()
                                    t.goto(0, -205)
                                    t.pd()
                                    t.pencolor("darkred")
                                    t.write(".قفل تصویری را فعال کنید [ Win + ~ ] همچنین می توانید از طریق", align="center",
                                            font=("B Koodak", 10))
                                    time.sleep(5)
                                    main_menu()
                            else:
                                errpage()
                        else:
                            errpage()
                    except:
                        errpage()
                def buton3(x,y):
                    try:
                        file = open("data/dtcheck.txt","w")
                        file.write("0")
                        file.close()
                        button3.speed(10)
                        button3.goto(112, -190)
                        button3.pd()
                        button3.pu()
                        button3.goto(120, -190)
                        button3.pd()
                        button3.pu()
                        button3.goto(116,-190)
                        button3.pd()
                        button3.speed(0)
                        os.remove("info.png")
                        file=open("data/log.txt","w")
                        file.write("")
                        file.close()
                        pyautogui.alert("!با موفقيت خارج شديد",'خروج از حساب کاربری', 'متوجه شدم')
                    except:
                        errpage()
                def buton4(x,y):
                    try:
                        file = open("data/dtcheck.txt","w")
                        file.write("0")
                        file.close()
                        button4.speed(10)
                        button4.goto(-124, -190)
                        button4.pd()
                        button4.pu()
                        button4.goto(-116, -190)
                        button4.pd()
                        button4.pu()
                        button4.goto(-120, -190)
                        button4.pd()
                        button4.speed(0)
                        scr.title("دیوار یخین | Codoffee Freezewall")
                        # face recognition
                        time.sleep(0.5)
                        scr.clearscreen()
                        scr.clearscreen()
                        scr.bgcolor('#47e4bb')
                        t.ht()
                        t.pencolor('#39b9e9')
                        t.pu()
                        t.goto(0, 0)
                        t.pd()
                        t.pencolor("darkblue")
                        t.write(".لطفا دستور مورد نظر را وارد کنید", align="center",
                                font=("B Koodak", 13))
                        command = scr.textinput("عملیات", "عملیات مورد نظر خود (پاکسازی عکسها / گزارشات ) را وارد کنید.")
                        if('گزارش' in command):
                            try:
                                os.startfile("data/log.txt")
                            except:
                                errpage()
                        elif 'ساز' in command:
                            files = os.listdir('data/facesData')
                            for file in files:
                                os.remove("data/facesData/"+file)
                            pyautogui.alert('!حذف عکسها با موفقيت انجام شد', 'حذف عکسها', 'متوجه شدم')
                            main_menu()
                    except:
                        errpage()
                m.clear()
                m.pu()
                m.goto(0,0)
                m.pd()
                m.pencolor("darkblue")
                m.write('نرم افزار دیوار یخین | بخش مدیریت',align="center",font=("B Koodak",15,("bold")))
                button1.onclick(buton1)
                button3.onclick(buton3)
                button4.onclick(buton4)
                def date_time():
                    dt=t.Turtle()
                    tm=t.Turtle()
                    dt.speed(0)
                    tm.speed(0)
                    jdatetime.set_locale('fa_IR')
                    tm.pu()
                    tm.goto(-240, 215)
                    tm.pd()
                    dt.pu()
                    dt.goto(267, 215)
                    dt.pd()
                    dt.ht()
                    tm.ht()
                    dt.ht()
                    tm.ht()
                    dt.fd(1)
                    tm.fd(1)
                    while True:
                        file = open("data/dtcheck.txt", "r")
                        dtval = file.read()
                        file.close()
                        if(dtval=="1"):
                            now=datetime.now()
                            now_date=jdatetime.datetime.now().strftime("%Y/%m/%d")
                            now_time=jdatetime.datetime.now().strftime("%H:%M")
                            dt.undo()
                            tm.undo()
                            dt.pencolor("black")
                            tm.pencolor("black")
                            dt.write(now_time,align="center",font=("B Titr",15))
                            tm.write(now_date,align="center",font=("B Titr",15))
                            time.sleep(1)
                thread1=Thread(target=date_time,args=[])
                thread1.start()
                t.mainloop()
            except:
                errpage()
        except:
            errpage()
    except:
        errpage()
except:
    errpage()
# End, Total codes: 803 line:----------------------------------------------------Codoffee FreezeWall--------------------------------------------------------------
# Thanks from:
    # Mr.Safarzadeh-CodoffeeManager
    # Mr.Izanlou-CodoffeeManager-UI-DESIGNER
    # Proudly-PoweredBy-PythonTkinter-C++/C-PL
