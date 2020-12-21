'''
1065364716404-bthmosciopfvjhu5jj3tevvel8r5eieq.apps.googleusercontent.com
B1paKv1Vqm1bV3ax83qsOG1A
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
'''
import requests
from requests.exceptions import ConnectionError
import logging
import os
import time
from pyzbar.pyzbar import decode #raspberry Pi
import RPi.GPIO as GPIO #raspberry Pi
import sys
global prev_touch
prev_touch =False
from bash import bash  #raspberry Pi
import sys
global selector
global mouse
global last_check_point
last_check_point='index'
#os.system("sudo rmmod uvcvideo")
#os.system("sudo modprobe uvcvideo nodrop=1 timeout=5000 quirks=0x80")
#{"E: ID_VENDOR_ID=1908\n": "web", "E: ID_VENDOR_ID=b666\n": "dental"}

os.chdir("/home/pi/Dent2/")

def restart_uvc():
    pass
    '''
    print('[34]')
    try:
        bash('sudo modprobe bcm2835-v4l2')
    except:
        print('[ERROR AT 34]')
    '''

import requests
import glob
import pyrebase
from imutils.video import WebcamVideoStream
from imutils.video import FPS
import argparse
import imutils
import json
import io
import time
import os
import pyqrcode
import base64
import imutils
import eel
import cv2
from os import path
import shutil
from keyboard import is_pressed
import shutil
from time import sleep
from datetime import datetime
import threading
global disease_index
global list_cancer_images,list_fluorosis_images

global list_periodontis_images
global list_ginivitis_images
global list_maloccusion_images
global list_hairry_tounge_images
global list_carries_cavities_images
list_cancer_images =[]
list_fluorosis_images =[]
list_periodontis_images=[]
list_ginivitis_images=[]
list_maloccusion_images=[]
list_hairry_tounge_images=[]
list_carries_cavities_images=[]
global file_ptr
file_ptr =0
disease_index =0
global disease_dict
disease_dict ={}
global queue_index
queue_index =[]
now = datetime.now()
timestamp = datetime.timestamp(now)
import  sys, os
from pathlib import Path
global ideal_folder
ideal_folder=''
import eel.browsers
#eel.browsers.set_path('electron', '/home/pi/Dent2/node_modules/electron/dist/electron')
rootdir = 'Patients'
global co
co=0
web_options = {



}
eel.init('web')
sub=['carries','cavities','cancer','flurosis']
global TOUCH
TOUCH = 17



GPIO.setmode(GPIO.BCM) # Use BCM GPIO numbers #raspberry Pi
GPIO.setup(TOUCH, GPIO.IN) #raspberry Pi
global cap

global camera
camera=0
global WhichCamera
WhichCamera =0
global vs0,vs2
global web_cam,dental_cam
global web_cam_cap,dental_cam_cap
configpatient = {
  "apiKey": "AIzaSyAuwb5XgCRiuIJBHnS48MXhPbSuOqIdK_c",
  "authDomain": "denta-operator.firebaseapp.com",
  "databaseURL": "https://denta-operator.firebaseio.com/",
  "storageBucket": "denta-operator.appspot.com"
}
firebase_p = pyrebase.initialize_app(configpatient)
dbp = firebase_p.database()

configdoctor = {
  "apiKey": "AIzaSyCnCXtZArTi1V_YITbOVDiaAteKBXcbQ6k",
  "authDomain": "dental-3edb0.firebaseio.com",
  "databaseURL": "https://dental-3edb0.firebaseio.com",
  "storageBucket": "dental-3edb0.appspot.com"
}
firebase_d = pyrebase.initialize_app(configdoctor)
global dbdr
dbdr = firebase_d.database()
global authdr
authdr = firebase_d.auth()
global init_cam_flag
init_cam_flag = 0
global running_diagnostics
running_diagnostics =0
global is_it_first_time_vs0 , is_it_first_time_vs2
is_it_first_time_vs0 =0
is_it_first_time_vs2 =0
import sys
import subprocess
@eel.expose()
def restart_prog():
    cmd = 'python3 dentaLitev3.py'
    subprocess.run('lxterminal -e ' + cmd, shell=True)
    time.sleep(0.2)
    quit()
@eel.expose()
def init_cam(temp =0,err=0):
    global init_cam_flag
    print('[INIT_CAM FUNCTION]')
    camera_dic={}
    try:
        with open('camera_list.json', 'r') as openfile:
            camera_dic = json.load(openfile)
    except:

        print("file not found")
    t1 = time.time()
    print("file function done")
    global is_it_first_time_vs2 ,is_it_first_time_vs0




    global running_diagnostics
    running_diagnostics =1

    #global init_cam_flag
    if init_cam_flag == 0:
        init_cam_flag =1
        #try:

        global cap
        global camera
        camera=0
        global WhichCamera
        WhichCamera =0
        global vs0,vs2
        global web_cam,dental_cam
        global web_cam_cap,dental_cam_cap
        web_cam = 0
        dental_cam =0

        global web_cam_index
        if(True):
            flag1 =0
            flag2 = 0
            web_cam =0
            dental_cam =0
            webcam_flag =0
            dental_flag=0

            for i in range(30):
                try:
                    c  = list(os.popen("sudo udevadm info --query=all /dev/video{}| grep 'VENDOR_ID\|MODEL_ID\|SERIAL_SHORT'".format(i)))[1]
                except:
                    c=['','']
                #try:
                print(c)
                try:

                    if(camera_dic[c] == "web" and c!=['',''] and webcam_flag ==0):
                        print("webcam found")
                        if(is_it_first_time_vs0 !=0):
                            prev_vs0 = vs0
                        #vs0 = WebcamVideoStream(src=i).start()
                        #vs0_s=vs0.start()
                        if(is_it_first_time_vs0 !=0):
                            del prev_vs0
                        is_it_first_time_vs0 =1
                        web_cam_index = i
                        flag1 =i
                        #cap=vs0
                        WhichCamera =i
                        camera=i
                        web_cam = i
                        #web_cam_cap =vs0
                        webcam_flag =1
                except:
                    print("error")
                # except:
                #     if(c[0]=='E'):
                #         choice =input("New Camera is Identified Please Type its type (web/dental)")

                #         if(choice =="web"):
                #             vs0 = WebcamVideoStream(src=i).start()
                #             web_cam_index = i
                #             flag1 =i
                #             cap=vs0
                #             WhichCamera =i
                #             camera=i
                #             web_cam = i
                #             web_cam_cap =vs0
                #             webcam_flag=1
                #         elif(choice =="dental"):
                #             vs2 = WebcamVideoStream(src=i).start()
                #             flag2 =i
                #             dental_cam =i
                #             dental_cam_cap =vs2
                #             dental_flag=1


                #         dic = {
                #         c : choice,
                #         }
                #         camera_dic[c] = choice
                #         with open("camera_list.json", "w") as outfile:
                #             outfile.write(json.dumps(dic))


                try:

                    if(camera_dic[c] == "dental" and c!=['',''] and dental_flag==0):
                        print("dental found")
                        if(is_it_first_time_vs2!=0):
                            prev_vs2 = vs2
                        #vs2 = WebcamVideoStream(src=i).start()
                        #vs2_s = vs2.start()
                        if(is_it_first_time_vs2!=0):
                            del prev_vs2
                        is_it_first_time_vs2 =1
                        flag2 =i
                        dental_cam =i
                        #dental_cam_cap =vs2
                        dental_flag=1
                except:
                    print("error")
                #     if(c[0]=='E'):
                #         choice =input("New Camera is Identified Please Type its type (web/dental)")
                #         if(choice =="web"):
                #             vs0 = WebcamVideoStream(src=i).start()
                #             web_cam_index = i
                #             flag1 =i
                #             cap=vs0
                #             WhichCamera =i
                #             camera=i
                #             web_cam = i
                #             web_cam_cap =vs0
                #             webcam_flag=1
                #         elif(choice =="dental"):
                #             vs2 = WebcamVideoStream(src=i).start()
                #             flag2 =i
                #             dental_cam =i
                #             dental_cam_cap =vs2
                #             dental_flag=1
                #         dic = {
                #         c : choice,
                #         }
                #         camera_dic[c] = choice
                #         with open("camera_list.json", "w") as outfile:
                #             outfile.write(json.dumps(dic))
                if(webcam_flag==1 and dental_flag==1):
                    print('camera diagnostics over')
                    running_diagnostics =0

                    break
            print('--------[camera diagnostics over]------')
            #set_camera(0)
            running_diagnostics =0







        # except:
        #     print('[ERROR AT 198]')
    else:
        init_cam_flag =1

global existing
existing=1
fold="dummy"
subfold=''
current_dir_fold=''
current_dir_subfold=''
count=0
image=0
global ids_replace
ids_replace=0
current_patient=""
path_of_cancer=[]
global ids
ids=0
global after_id
after_id=1
ideal_folder=os.getcwd()+'/web'
global  download_thread
import hashlib
class signin:
    def __init__(self,uid,pssd):
        print('[240]')
        t1 = time.time()
        self.userid=uid
        self.password = pssd
        self.userid_sha =''
        self.password_sha =''
        self.token_id=''
        self.local_id=''
        self.dr_id =''
        self.pat_id =''
        print('[Time Taken ]',time.time()-t1)

    def cnvrtUserId_Psswd_to_sha265(self):
        print('[251]')
        t1 = time.time()
        try:
            self.userid_sha =hashlib.sha256(self.userid.encode()).hexdigest()
            self.password_sha = hashlib.sha256(self.password.encode()).hexdigest()
        except:
            print('[ERROR AT 251]')
        print('[Time Taken ]',time.time()-t1)



    def check_sign_in_machine(self):
        print('[259]')
        t1 = time.time()

        data ={}
        with open('hash.json', 'r') as openfile:
            data =json.load(openfile)
        #print(data)
        if(self.userid_sha == data['userID'] and self.password_sha == data['password']):
            init_cam()
            return 1
        else:
            return 0
        print(['Time Taken '],time.time()-t1)
    def auth_dr_db(self,dr_id):
        print('[273]')
        t1 = time.time()
        try:
            dr_id = dr_id.upper()
            if(dr_id ==''):
                self.dr_id =''
                return 1
            try:
                global authdr,dbdr
                #print('Check1')
                user = authdr.sign_in_with_email_and_password(self.userid, self.password)
                #print('check2')
                self.token_id = user['idToken']
                self.local_id = user['localId']
                #print(self.local_id)
                dr_id_check = dbdr.child('operator_users').child('{}'.format(self.local_id)).get(self.token_id).val()
                #print(dr_id_check)
                if(dr_id_check == self.dr_id ):
                    self.dr_id = dr_id
                    return 1


            except:
                print('[ERROR AT 275]')
                return 0
            print('[Time Taken ]',time.time()-t1)
        except:
            print('[ERROR AT 273]')





global signin_ob
@eel.expose
def check_signin(u,p):
    print('[309]')
    t1 = time.time()
    #print(u,p)
    global signin_ob
    signin_ob = signin(u,p)
    signin_ob.cnvrtUserId_Psswd_to_sha265()
    return(signin_ob.check_sign_in_machine())

    print('[Time Taken ]',time.time()-t1)


@eel.expose
def check_dr_id(dr_id):
    print('[322]')
    t1 = time.time()
    try:
        global signin_ob
        dr_id = dr_id.upper()
        signin_ob.dr_id = dr_id
        if(dr_id != ''):
            with open('dr_list.json', 'r') as openfile:
                json_object = json.loads(openfile)
                N = len(json_object)
                if(N == 0):
                    return 0
                elif(dr_id in json_object):
                    signin_ob.dr_id = dr_id
                    return 1
                else:
                    return 2
        else:
            return 1
    except:
        print('[ERROR AT 322]')
    print('[Time Taken ]',time.time()-t1)


@eel.expose
def add_dr_id(dr_id):
    print('[346]')
    t1 = time.time()
    try:
        dr_id = dr_id.upper()
        #print('[DR_ADDED : ]' , dr_id)
        if(dr_id != ''):
            L = []

            global dbp
            global list_of_dr_id
            if(dr_id in list_of_dr_id):
                try:

                    with open('dr_list.json', 'r') as openfile:
                        dat= json.load(openfile)
                        if(dr_id in dat):
                            #print('[EXIST]')
                            L=dat
                        else:
                            dat.append(dr_id)
                            L =dat
                        #print('[LIST OF DR ID IN FILE]',L)

                except :
                    L.append(dr_id)
                    #print('[FILE ERROR]')
                with open("dr_list.json", "w") as outfile:
                    outfile.write(json.dumps(L))
                #print('[ADDED SUCESSFULLY]')
                return 1
            else:
                #print('[EDIT DENIED]')
                return 0
        else:
            #print('CANT BE EMPTY')
            return 2
    except:
        print('[ERROR AT 346]')
    print('[Time Taken ]',time.time()-t1)

@eel.expose
def remove_dr_id(dr_id):
    print('[386]')
    t1 = time.time()
    try:
        dr_id = dr_id.upper()

        L=[]
        with open('dr_list.json', 'r') as openfile:
            L = json.load(openfile)
        if(dr_id in L):
            L.remove(dr_id)
            #print('[REMOVED]')

        with open("dr_list.json", "w") as outfile:
            outfile.write(json.dumps(L))
        return 1
    except:
        print('[ERROR AT 386]')
    print('[Time Taken ]',time.time()-t1)

@eel.expose
def return_dr_list():
    print('[406]')
    t1 = time.time()
    try:
        dat =[]
        with open('dr_list.json', 'r') as openfile:
            dat= json.load(openfile)
        code ='<option value=" " >Doctor Ids</option>'
        for i in dat:
            code =code + '<option value="{}" >{}</option>'.format(i,i)
        return code
    except:
        print('[ERROR AT 416]')
    print('[Time Taken ]',time.time()-t1)

@eel.expose
def return_dr_list_autocomplete():
    print('[420]')
    t1 = time.time()
    try:
        dat =[]
        with open('dr_list.json', 'r') as openfile:
            dat= json.load(openfile)
        code =dat

        code =dat
        return code
    except:
        print('[ERROR AT 430]')
    print('[Time Taken ]',time.time()-t1)
@eel.expose
def return_dr_list_for_index():
    print('[433]')
    t1 = time.time()
    try:
        dat =[]
        with open('dr_list.json', 'r') as openfile:
            dat= json.load(openfile)
        code =''
        for i in dat:
            code =code + '<option value="{}">{}</option>'.format(i,i)
        code  = code + '<option value="{}">{}</option>'.format('Null','Null')
        return code
    except:
        print('[ERROR At 444]')
    print('[Time Taken ]',time.time()-t1)
@eel.expose
def dr_id_thread():
    #print('[DR_ID_THREAD]')
    print('[432]')
    t1 = time.time()
    try:
        tn = threading.Thread(target=fetch_dr, args=())
        tn.start()
    except:
        print('[ERROR AT 432]')
    print('[Time Taken ]',time.time()-t1)


def fetch_dr():
    print('[442]')
    t1 = time.time()
    try:
        global dbp
        global list_of_dr_id
        list1=[]
        for i in dbp.child('Doctor_ID').get().each():
            #print(i.key(),'[LIST OF DR ID]')
            list1.append(i.key())
        list_of_dr_id =list1
    except:
        print('[ERROR AT 442]')
    print('[Time Taken ]',time.time()-t1)
    #print(list_of_dr_id)

global DR_ID

@eel.expose
def dr_id_selected(dr_id):
    print('[459]')
    t1 = time.time()
    try:
        global DR_ID
        if(dr_id == 'Null'):
            DR_ID = ''
        else:
            DR_ID = dr_id
    except:
        print('[ERROR AT 459]')
    print('[Time Taken ]',time.time()-t1)
    #print('[DR-ID SELECTED]',DR_ID)




class patientDetails:
    def __init__(self,name,phoneNo,yob,address,list_cancer_img_path,list_fluorosis_img_path):
        print('[488]')
        t1 = time.time()
        try:
            self.name =name
            self.phoneNo =phoneNo
            self.yob=yob
            self.address=address
            self.cancer_images = list_cancer_img_path
            self.fluorosis_img = list_fluorosis_img_path
            self.url = 'https://python-e1e83.firebaseio.com/python.json'
        except:
            print('[ERROR AT 488]')
        print('[Time Taken ]',time.time()-t1)

    def post_to_database(self):
        print('[501]')
        t1 = time.time()
        try:
            list_encode =[]
            dic_cancer={}
            dic_fluorosis={}
            img =[]
            temp=''
            for i in range(len(self.cancer_images)):
                image = cv2.imread(self.cancer_images[i])
                _,img=cv2.imencode('.png',image)
                dic_cancer['{}'.format(i)]=base64.b64encode(img)

            for i in range(len(self.fluorosis_img)):
                image = cv2.imread(self.fluorosis_img[i])
                _,img=cv2.imencode('.png',image)
                dic_fluorosis['{}'.format(i)]=base64.b64encode(img)


            data = {
            'name':'{}'.format(self.name),
            'phoneNo':'{}'.format(self.phoneNo),
            'yob':'{}'.format(self.yob),
            'address':'{}'.format(self.address),
            'cancer_images':'{}'.format(dic_cancer),
            'fluorosis_images':'{}'.format(dic_fluorosis),

            }
            x = requests.Session().post(self.url, data = json.dumps(data),timeout = 50)
        except:
            print('[ERROR AT 501]')
        print('[Time Taken ]',time.time()-t1)
        #print(x.json())


class ExtractInfo:
    def __init__(self,text):
        print('[538]')
        t1 = time.time()
        try:
            self.text = text
            self.name=''
            self.yob=''
            self.aadharNo=''
            self.gender=''
            self.street=''
            self.district=''
            self.state=''
            self.pincode=''
            self.address =''
        except:
            print('[ERROR AT 538]')
        print('[Time Taken ]',time.time()-t1)


    def extractName(self):
        print('[555]')
        t1 = time.time()
        try:

        #print('name')
            ptr = self.text.find('name=',0,len(self.text)+1)
            ptr +=6
            while(self.text[ptr]!='"'):
                self.name = self.name+self.text[ptr]
                ptr+=1
            #print(self.name)
            return(self.name)
        except:
            print('[ERROR AT 555]')
        print('[Time Taken ]',time.time()-t1)


    def extractyob(self):
        print('[571]')
        t1 = time.time()
        try:
            #print('yob')
            ptr = self.text.find('yob=',0,len(self.text)+1)
            ptr +=5
            while(self.text[ptr]!='"'):
                self.yob = self.yob+self.text[ptr]
                ptr+=1
            return(self.yob)
        except:
            self.yob =None
        print('[Time Taken ]',time.time()-t1)
        #print(self.yob)

    def extractgender(self):
        print('[585]')
        t1 = time.time()
        try:
            ptr = self.text.find('gender=',0,len(self.text)+1)
            ptr +=8
            while(self.text[ptr]!='"'):
                self.gender = self.gender+self.text[ptr]
                ptr+=1
            if(self.gender == 'M'):
                self.gender = 'Male'
                return self.gender
            elif(self.gender == 'F'):
                self.gender ='Female'
                return self.gender

        except:
            self.gender =None
        print('[Time Taken ]',time.time()-t1)
        #print(self.gender)

    def extractAadharNo(self):
        print('[604]')
        t1 = time.time()
        try:
            ptr = self.text.find('uid=',0,len(self.text)+1)
            ptr +=5
            while(self.text[ptr]!='"' and ptr<len(self.text)):
                if(len(self.aadharNo)==4 or len(self.aadharNo)==9):
                    self.aadharNo =self.aadharNo+' '
                self.aadharNo = self.aadharNo+self.text[ptr]
                ptr+=1
            return(self.aadharNo)
        except:
            self.aadharNo=None
        print('[Time Taken ]',time.time()-t1)

    def extractAddress(self):
        print('[618]')
        t1 = time.time()
        try:
            ptr = self.text.find('street=',0,len(self.text)+1)
            ptr +=8
            while(self.text[ptr]!='"' and ptr<len(self.text)):
                self.street = self.street+self.text[ptr]
                ptr+=1
            ptr = self.text.find('dist=',0,len(self.text)+1)
            ptr +=6
            while(self.text[ptr]!='"' and ptr<len(self.text)):
                self.district = self.district+self.text[ptr]
                ptr+=1
            ptr = self.text.find('state=',0,len(self.text)+1)
            ptr +=7
            while(self.text[ptr]!='"' and ptr<len(self.text)):
                self.state = self.state+self.text[ptr]
                ptr+=1
            ptr = self.text.find('pc=',0,len(self.text)+1)
            ptr +=4
            while(self.text[ptr]!='"' and ptr<len(self.text)):
                self.pincode = self.pincode+self.text[ptr]
                ptr+=1


            self.address = self.street+' '+self.district+' '+self.state+' '+self.pincode
            return(self.address)
        except:
            self.aadharNo=None
        print('[Time Taken ]',time.time()-t1)
        #print(self.aadharNo)






class QrCodeScannner:
    global cap

    def __init__(self,image,WhichCamera=1):
        #print('[657]')
        try:
            self.image=image
            self.qrCode=None
            self.WhichCamera = WhichCamera
        except:
            print('[ERROR AT 657]')
        #self.vid = cap#cv2.VideoCapture(self.WhichCamera)
        #....
        #self.image =cv2.imread('test_qr_1.PNG')

    def imageCapture(self):
        #print('[669]')
        global init_cam_flag
        try:
            self.image = cap.read()
        except:
            print('[ERROR AT 669]')
            print('[Calling 34...]')

            init_cam_flag = 0
            #restart_uvc()
            print('[Calling INIT_CAM_Function...]')
            init_cam()




    def qrDecoder(self):
        #print('[683]')
        try:

            self.qrCode = decode(self.image)
            return(self.ShowImage())
        except:
            print('[ERROR AT 683]')

    def ShowImage(self):
        #print('[692]')
        try:
            for qr in self.qrCode:
                (x, y, w, h) = qr.rect
                cv2.rectangle(self.image, (x, y), (x + w, y + h), (0, 0, 255), 2)
                barcodeData = qr.data.decode("utf-8")
                barcodeType = qr.type
                text = "{} ({})".format(barcodeData, barcodeType)
                cv2.putText(self.image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,0.5, (0, 0, 255), 2)
                #print("[INFO] Found {} barcode: {}".format(barcodeType, barcodeData))
                if(barcodeType == 'QRCODE'):
                    #self.vid.release()
                    return (barcodeData)
                else:
                    print('[ERROR CHECK]')
                    return ('Null') #ERROR CAN BE IN THIS LINE
                    #self.vid.release()
        except:
            print('[ERROR AT 692]')

def upload_images(image_category,pat_id,data,case_no):
    print('[716]')
    t1 = time.time()
    try:
        global dbp
        dbp.child(image_category).child(pat_id).child(case_no).set(data)
    except:
        print('[ERROR AT 716]')
    print('[Time Taken ]',time.time()-t1)

global upload_status
upload_status = 0

def update_upload_status(no):
    print('[727]')
    t1 = time.time()
    try:
        global upload_status
        upload_status = no
    except:
        print('[ERROR AT 727]')
    print('[Time Taken ]',time.time()-t1)
@eel.expose
def get_upload_status():
    print('[738]')
    t1 = time.time()
    try:
        global upload_status
        return int(upload_status)
    except:
        print('[ERROR AT 738]')
    print('[Time Taken ]',time.time()-t1)

import socket
@eel.expose
def is_connected():
    print('[748]')
    t1 = time.time()
    try:
        try:
            socket.create_connection(("1.1.1.1", 53))
            return True
        except OSError:
            pass
        return False
    except:
        print('[ERROR AT 748]')
        return True
    print('[Time Taken ]',time.time()-t1)

def uploadToFirebaseThread():
    print('[762]')
    t1 = time.time()
    update_upload_status(1)

    global list_cancer_images
    global list_fluorosis_images
    global list_periodontis_images
    global list_ginivitis_images
    global list_maloccusion_images
    global list_hairry_tounge_images
    global list_carries_cavities_images
    #url = 'https://python-e1e83.firebaseio.com/Patient.json'
    url = 'https://denta-operator.firebaseio.com/Patients.json'
    #/home/pi/Desktop/Dent1
    list_files = os.listdir('/home/pi/Dent2/web/Patient/upload')
    #print('[INFO] Files uploading in Thread')
    for i in list_files:
        if(i!='.DS_Store'):
            #print('[INFO] [THREAD] {} file uploading'.format(i))
            with open(os.path.join('/home/pi/Dent2/web/Patient/upload/',i)) as json_file:
                    data = json.load(json_file)
                    len_cancer_images = len(data['Cancer_image'])
                    len_fluorosis_images = len(data['Fluorosis'])
                    len_periodontis_images = len(data['Periodontis_images'])
                    len_ginivitis_images = len(data['Ginivitis_images'])
                    len_maloccusion_images = len(data['Maloccusion_images'])
                    len_hairry_tounge_images = len(data['Hairry_tounge_images'])
                    len_carries_cavities_images = len(data['Carries_cavities_images'])

                    if(len_fluorosis_images ==1):
                        try:
                            #print(data['Flurosis'])
                            if(data['Fluorosis']['None'] == 'None'):
                                len_fluorosis_images =0
                                #print('Nooooo     Images')
                        except:
                            print(' ')
                    if(len_cancer_images==1):
                        try:
                            #print(data['Flurosis'])
                            if(data['Cancer_image']['None'] == 'None'):
                                len_cancer_images =0
                                #print('Nooooo     Images')
                        except:
                            print(' ')
                    if(len_ginivitis_images==1):
                        try:
                            #print(data['Flurosis'])
                            if(data['Ginivitis_images']['None'] == 'None'):
                                len_ginivitis_images =0
                                #print('Nooooo     Images')
                        except:
                            print(' ')
                    if(len_periodontis_images==1):
                        try:
                            #print(data['Flurosis'])
                            if(data['Periodontis_images']['None'] == 'None'):
                                len_periodontis_images =0
                                #print('Nooooo     Images')
                        except:
                            print(' ')
                    if(len_maloccusion_images==1):
                        try:
                            #print(data['Flurosis'])
                            if(data['Maloccusion_images']['None'] == 'None'):
                                len_maloccusion_images =0
                                #print('Nooooo     Images')
                        except:
                            print(' ')
                    if(len_hairry_tounge_images==1):
                        try:
                            #print(data['Flurosis'])
                            if(data['Hairry_tounge_images']['None'] == 'None'):
                                len_hairry_tounge_images=0
                                #print('Nooooo     Images')
                        except:
                            print(' ')
                    if(len_carries_cavities_images==1):
                        try:#
                            #print(data['Flurosis'])
                            if(data['Carries_cavities_images']['None'] == 'None'):
                                len_carries_cavities_images=0
                                #print('Nooooo     Images')
                        except:
                            print(' ')
                    st = data['PhoneNo']
                    uid_pat = hashlib.sha256(st.encode()).hexdigest()

                    global signin_ob
                    dic = {
                        'Name' :'{}'.format(data['Name']),
                        'PhoneNo' : '{}'.format(data['PhoneNo']),
                        'yob' :'{}'.format(data['yob']),
                        'Address':'{}'.format(data['Address']),
                        'Status': '{}'.format(data['Status']),
                        'Doctor_id': '{}'.format(data['Doctor_id']),
                        'Question' : '{}'.format(data['Question']),
                        'Gender' :'{}'.format(data['Gender']),
                        'Date' :'{}'.format(data['Date']),
                        'Assigned_Date':'{}'.format('---'),
                        'No_of_cancer_images' :'{}'.format(len_cancer_images),
                        'No_of_fluorosis_images' :'{}'.format(len_fluorosis_images),
                        'No_of_periodontis_images' :'{}'.format(len_periodontis_images),
                        'No_of_ginivitis_images' :'{}'.format(len_ginivitis_images),
                        'No_of_maloccusion_images' :'{}'.format(len_maloccusion_images),
                        'No_of_hairry_tounge_images' :'{}'.format(len_hairry_tounge_images),
                        'No_of_carries_cavities_images' :'{}'.format(len_carries_cavities_images),
                        'Operator_id':'{}'.format(signin_ob.userid),

                    }
                    if(True):
                        #x =requests.Session().post(url, data = json.dumps(dic),timeout = 50)
                        global dbp
                        global dbdr
                        case_no=0
                        l = []
                        try:
                            for k in dbp.child('Patient').child(uid_pat).shallow().get().val():
                                l.append(k)
                        except:
                            print('')
                        dic_temp ={}
                        if(len(l)==0):
                            dic_temp[0]=dic
                            case_no=0
                            x = dbp.child("Patient").child(uid_pat).set(dic_temp)
                        else:
                            history_no = len(l)
                            dic_temp[history_no] = dic
                            x = dbp.child("Patient").child(uid_pat).child(history_no).set(dic)
                            case_no=history_no

                        ct=threading.Thread(target=upload_images, args=('CancerImages',uid_pat,data['Cancer_image'],case_no))
                        ft=threading.Thread(target=upload_images, args=('FluorosisImages',uid_pat,data['Fluorosis'],case_no))
                        pt=threading.Thread(target=upload_images, args=('PeriodontisImages',uid_pat,data['Periodontis_images'],case_no))
                        gt=threading.Thread(target=upload_images, args=('GinivitisImages',uid_pat,data['Ginivitis_images'],case_no))
                        mt=threading.Thread(target=upload_images, args=('MaloccusionImages',uid_pat,data['Maloccusion_images'],case_no))
                        ht=threading.Thread(target=upload_images, args=('Hairry_toungeImages',uid_pat,data['Hairry_tounge_images'],case_no))
                        cct=threading.Thread(target=upload_images, args=('Carries_cavitiesImages',uid_pat,data['Carries_cavities_images'],case_no))
                        ct.start()
                        ft.start()
                        pt.start()
                        gt.start()
                        mt.start()
                        ht.start()
                        cct.start()


                        if(True):

                            if(data['private']=='False' or data['DrId']==''):
                                try:
                                    pen=dbp.child("Pending").child(uid_pat).get().val()
                                    if(pen!=None):
                                        pen = str(pen) + ' ' + str(case_no)
                                        dbp.child("Pending").update({uid_pat:pen})
                                    else:
                                        dbp.child("Pending").child(uid_pat).set(str(case_no))

                                except:
                                   print('')
                            else:
                                #print('[Assigning To Doctor in Private Mode]',data['DrId'])
                                u_id =dbdr.child('Dr_id_ID').child(data['DrId']).get().val()
                                dbdr.child('Doctors').child(u_id).child('Accepted_Patients').child(uid_pat).update({str(case_no):'Private'})
                            ct.join()
                            ft.join()
                            pt.join()
                            gt.join()
                            mt.join()
                            ht.join()
                            cct.join()
                            os.remove(os.path.join('/home/pi/Dent2/web/Patient/upload/',i)) #macbook
                            print('[INFO] [THREAD] {} file UPLOADED'.format(i))
                            update_upload_status(2)



                        else:
                            #print('[INFO] upload failed files saved properly , no worries it will be uploaded next time when internet connection is proper')
                            update_upload_status(2)

                    else:
                        #print('[INFO] Upload Failed , Due To one od the images didnt upload properly')
                        update_upload_status(0)
    print('[Time Taken ]',time.time()-t1)




def Main_program():
    try:
            @eel.expose
            def upload_to_firebase():
                print('[962]')
                t0 = time.time()
                try:
                    t1 = threading.Thread(target=uploadToFirebaseThread, args=())
                    t1.start()
                except:
                    print('[ERROR AT 962]')
                #t1.join()
                #quit()
                #print('Thread Started')
                print('[Time Taken ]',time.time()-t0)



            @eel.expose
            def save_file_txt(name,phoneNo,yob,address,gender):
                print('[976]')
                t1 = time.time()
                try:
                    global list_cancer_images
                    global list_fluorosis_images
                    global list_periodontis_images
                    global list_ginivitis_images
                    global list_maloccusion_images
                    global list_hairry_tounge_images
                    global list_carries_cavities_images
                    global file_ptr
                    date = str(time.asctime( time.localtime(time.time())) )
                    dic_cancer={} #
                    dic_fluorosis={} #
                    dic_periodontis={} #
                    dic_ginivitis={} #
                    dic_maloccusion={} #
                    dic_hairry_tounge={} #
                    dic_carries_cavities={}
                    if(len(list_cancer_images) == 0):
                        dic_cancer = {'None':'None'}
                    else:

                        for i in range(len(list_cancer_images)):

                            image = cv2.imread(list_cancer_images[i])
                            try:
                                _,img=cv2.imencode('.png',image)
                                dic_cancer[str(i)]=str(base64.b64encode(img))
                            except:
                                continue
                    if(len(list_fluorosis_images) ==0):
                        dic_fluorosis = {'None':'None'}
                    else:
                        for i in range(len(list_fluorosis_images)):
                            image = cv2.imread(list_fluorosis_images[i])
                            try:
                                _,img=cv2.imencode('.png',image)
                                dic_fluorosis[str(i)]=str(base64.b64encode(img))
                            except:
                                continue

                    if(len(list_periodontis_images) ==0):
                        dic_periodontis = {'None':'None'}
                    else:
                        for i in range(len(list_periodontis_images)):
                            image = cv2.imread(list_periodontis_images[i])
                            try:
                                _,img=cv2.imencode('.png',image)
                                dic_periodontis[str(i)]=str(base64.b64encode(img))
                            except:
                                continue

                    if(len(list_ginivitis_images) ==0):
                        dic_ginivitis = {'None':'None'}
                    else:
                        #print(list_ginivitis_images,'=============List of ginivitis')
                        for i in range(len(list_ginivitis_images)):
                            image = cv2.imread(list_ginivitis_images[i])
                            try:
                                _,img=cv2.imencode('.png',image)
                                dic_ginivitis[str(i)]=str(base64.b64encode(img))
                            except:
                                continue
                    if(len(list_maloccusion_images) ==0):
                        dic_maloccusion = {'None':'None'}
                    else:
                        for i in range(len(list_maloccusion_images)):
                            image = cv2.imread(list_maloccusion_images[i])
                            try:
                                _,img=cv2.imencode('.png',image)
                                dic_maloccusion[str(i)]=str(base64.b64encode(img))
                            except:
                                continue
                    if(len(list_hairry_tounge_images) ==0):
                        dic_hairry_tounge = {'None':'None'}
                    else:
                        for i in range(len(list_hairry_tounge_images)):
                            image = cv2.imread(list_hairry_tounge_images[i])
                            try:
                                _,img=cv2.imencode('.png',image)
                                dic_hairry_tounge[str(i)]=str(base64.b64encode(img))
                            except:
                                continue

                    if(len(list_carries_cavities_images) ==0):
                        dic_carries_cavities = {'None':'None'}
                    else:
                        for i in range(len(list_carries_cavities_images)):
                            image = cv2.imread(list_carries_cavities_images[i])
                            try:
                                _,img=cv2.imencode('.png',image)
                                dic_carries_cavities[str(i)]=str(base64.b64encode(img))
                            except:
                                continue


                    global signin_ob
                    flag='False'
                    global DR_ID
                    if(DR_ID !=''):
                        flag = 'True'


                    dic ={
                        'Name' :'{}'.format(name),
                        'PhoneNo' : '{}'.format(phoneNo),
                        'yob' :'{}'.format(yob),
                        'Address':'{}'.format(address),
                        'Cancer_image': dic_cancer,
                        'Fluorosis': dic_fluorosis,
                        'Periodontis_images': dic_periodontis,
                        'Ginivitis_images': dic_ginivitis,
                        'Maloccusion_images': dic_maloccusion,
                        'Hairry_tounge_images': dic_hairry_tounge,
                        'Carries_cavities_images': dic_carries_cavities,
                        'Status': '{}'.format('onGoing'),
                        'Doctor_id': '{}'.format('null'),
                        'Question' : '{}'.format('under deveopment'),
                        'Gender' :'{}'.format(gender),
                        'Date' :'{}'.format(date),
                        'Doctor_Name':'{}'.format('---'),
                        'Assigned_Date':'{}'.format('---'),
                        'private' : flag,
                        'DrId' : DR_ID,



                    }
                    dic = json.dumps(dic)
                    pth = os.path.join("/home/pi/Dent2/web/Patient/upload","upload{}.json".format(file_ptr))
                    with open(pth,"w") as f:
                        f.write(dic)
                        f.close()
                        file_ptr+=1
                        list_cancer_images=[]
                        list_fluorosis_images =[]
                except:
                    print('[ERROR AT 976]')
                print('[Time Taken ]',time.time()-t1)



            @eel.expose
            def upload_patient(name,phoneNo,yob,address):
                print('[1119]')
                t1 = time.time()
                try:
                    global list_cancer_images
                    global list_fluorosis_images
                    ob = patientDetails(name,phoneNo,yob,address,list_cancer_images,list_fluorosis_images)
                    #print(list_cancer_images)
                    ob.post_to_database()
                except:
                    print('[ERROR AT 1119]')
                print('[Time Taken ]',time.time()-t1)

            @eel.expose
            def makeDir(name,gender,yob,district,categoryCreated):
                print('[1177]')
                t1 = time.time()
                try:
                    yob = yob.replace('/','_')
                    #print(yob)
                    date = list(time.asctime( time.localtime(time.time()) ).split())[:3]
                    date = date[2]+' '+date[0]+' '+date[1]
                    yob = yob.replace('/','_')



                    if(os.path.exists('web/Patient/'+date+'/'+name+'_'+yob+'/'+categoryCreated)):
                        return 1
                    else:
                        os.makedirs('web/Patient/'+date+'/'+name+'_'+yob+'/'+categoryCreated)
                        return 0
                except:
                    print('[ERROR AT 1178]')
                print('[Time Taken ]',time.time()-t1)

            @eel.expose
            def get_path_to_preview(ame,date,gender,yob,district,categoryCreated):
                print('[1198]')
                t1 = time.time()
                try:
                    global disease_index
                    global disease_dict
                except:
                    print('[ERROR AT 1198]')
                print('[Time Taken ]',time.time()-t1)
            @eel.expose
            def append_previous_images(name,gender,yob,district,categoryCreated):
                print('[1206]')
                t1 = time.time()
                try:
                    date = list(time.asctime( time.localtime(time.time()) ).split())[:3]
                    date = date[2]+' '+date[0]+' '+date[1]
                    yob = yob.replace('/','_')
                    path = 'web/Patient/'+date+'/'+name+'_'+yob+'/'+categoryCreated
                    global disease_index
                    global disease_dict
                    global queue_index
                    global list_cancer_images
                    global list_fluorosis_images
                    global list_periodontis_images
                    global list_ginivitis_images
                    global list_maloccusion_images
                    global list_hairry_tounge_images
                    global list_carries_cavities_images
                    code =''
                    try:
                        list_of_images = os.listdir(path)
                        #print(list_of_images ,'[LIST Of IMGAES]')
                        list_of_images.sort()
                        code =''
                        for i in list_of_images:
                            try:
                                if(i[-4:] == ".png"):
                                    #print('[IMAGE FILE NAME ]',i)
                                    res = [str(j) for j in i if j.isdigit()]
                                    #print('res',res)
                                    index = ''
                                    index =index.join(res)
                                    #print('idex',index)
                                    index= int(index)
                                    #print('[INDEX OF THE IMAGE]',index)
                                    try :
                                        disease_dict[categoryCreated].append(int(index))
                                        if(len(disease_dict[categoryCreated])==5):
                                            #os.remove(os.path.join(path,'test_image'+str(disease_dict[categoryCreated][-1])+'.png'))
                                            disease_dict[categoryCreated].pop(0)

                                    except:
                                        disease_dict[categoryCreated] = [index]
                                    image_path =os.path.join(path[3:],i)
                                    #print('[IMAGE PATH]',image_path)
                                    code =code+ "<div class=\"col-4\" id=\"{}\"><a href = \"{}\" data-lightbox=\"image-1\" data-title= \"<div id='{}' onclick = 'del(this)'> <div class='btn btn-info'>delete</div></div>\"><img src =\"{}\" height=\"100\"></a></div>".format('_'+str(categoryCreated)+str(disease_dict[categoryCreated][-1]),image_path,str(categoryCreated)+str(disease_dict[categoryCreated][-1]),image_path)
                                    if(categoryCreated == 'cancer'):
                                        #print('Cancer __________')
                                        list_cancer_images.append(os.path.join(path,i))
                                    elif(categoryCreated == 'Flurosis'):
                                        p#rint('Fll______________')
                                        list_fluorosis_images.append(os.path.join(path,i))
                                    elif(categoryCreated == 'Gingivitis'):
                                        #print('Gingivitis')
                                        list_ginivitis_images.append(os.path.join(path,i))

                                    elif(categoryCreated == 'Periodontis'):
                                        #print('Periodontis______________')
                                        list_periodontis_images.append(os.path.join(path,i))

                                    elif(categoryCreated == 'Malocclusion'):
                                        #print('Malocclusion______________')
                                        list_maloccusion_images.append(os.path.join(path,i))

                                    elif(categoryCreated == 'Hairry Tongue'):
                                        #print('Hairry Tongue______________')
                                        list_hairry_tounge_images.append(os.path.join(path,i))

                                    elif(categoryCreated == 'Carries&Cavities'):
                                        #print('Carries&Cavities______________')
                                        list_carries_cavities_images.append(os.path.join(path,i))

                            except :
                                print('')
                    except :
                        print('')
                    return code
                except:
                    print('[ERROR AT 1206]')
                print('[Time Taken ]',time.time()-t1)


            @eel.expose
            def save_image_in_path(name,gender,yob,district,categoryCreated):
                print('[1286]')
                t1 = time.time()
                try:
                    global disease_index
                    global disease_dict
                    global queue_index
                    global list_cancer_images
                    global list_fluorosis_images
                    global list_periodontis_images
                    global list_ginivitis_images
                    global list_maloccusion_images
                    global list_hairry_tounge_images
                    global list_carries_cavities_images
                    date = list(time.asctime( time.localtime(time.time()) ).split())[:3]
                    date = date[2]+' '+date[0]+' '+date[1]
                    yob = yob.replace('/','_')

                    #path =os.path.join(os.getcwd(),'web/Patient',date,name+'_'+gender+'_'+yob,categoryCreated)
                    eel.alerti(os.getcwd())

                    #print(yob)
                    path= 'web/Patient/'+date+'/'+name+'_'+yob+'/'+categoryCreated
                    try :
                        disease_dict[categoryCreated].append(disease_dict[categoryCreated][-1]+1)
                        if(len(disease_dict[categoryCreated])==5):
                            #os.remove(os.path.join(path,'test_image'+str(disease_dict[categoryCreated][-1])+'.png'))
                            disease_dict[categoryCreated].pop(0)

                    except:
                        disease_dict[categoryCreated] = [0]


                    image,_ =returnImageFrame(0,1)
                    #print('TEST')
                    #print(os.path.join(path,'test_image'+str(disease_dict[categoryCreated][-1])+'.png'))
                    #print('[ddsf]',os.getcwd())
                    if(categoryCreated == 'cancer'):
                        #print('Cancer __________')
                        list_cancer_images.append(os.path.join(path,'test_image'+str(disease_dict[categoryCreated][-1])+'.png'))
                    elif(categoryCreated == 'Flurosis'):
                        #print('Fll______________')
                        list_fluorosis_images.append(os.path.join(path,'test_image'+str(disease_dict[categoryCreated][-1])+'.png'))
                    elif(categoryCreated == 'Gingivitis'):
                        #print('Gingivitis')
                        list_ginivitis_images.append(os.path.join(path,'test_image'+str(disease_dict[categoryCreated][-1])+'.png'))

                    elif(categoryCreated == 'Periodontis'):
                        #print('Periodontis______________')
                        list_periodontis_images.append(os.path.join(path,'test_image'+str(disease_dict[categoryCreated][-1])+'.png'))

                    elif(categoryCreated == 'Malocclusion'):
                        #print('Malocclusion______________')
                        list_maloccusion_images.append(os.path.join(path,'test_image'+str(disease_dict[categoryCreated][-1])+'.png'))

                    elif(categoryCreated == 'Hairy Tongue'):
                        #print('Hairry Tongue______________')
                        list_hairry_tounge_images.append(os.path.join(path,'test_image'+str(disease_dict[categoryCreated][-1])+'.png'))

                    elif(categoryCreated == 'Carries&Cavities'):
                        #print('Carries&Cavities______________')
                        list_carries_cavities_images.append(os.path.join(path,'test_image'+str(disease_dict[categoryCreated][-1])+'.png'))

                    #print(path,os.getcwd())
                    #print(os.path.exists(path),os.getcwd())
                   # print(os.path.join(path,'test_image'+str(disease_dict[categoryCreated][-1])+'.png'))
                    s=cv2.imwrite(os.path.join(path,'test_image'+str(disease_dict[categoryCreated][-1])+'.png'),image)
                    image_path =os.path.join(path[3:],'test_image'+str(disease_dict[categoryCreated][-1])+'.png')
                   # print(s)
                    #print(image_path)
                    disease_index+=1
                    text = "<div class=\"col-4\" id=\"{}\"><a href = \"{}\" data-lightbox=\"image-1\" data-title= \"<div id='{}' onclick = 'del(this)'> <div class='btn btn-info'>delete</div></div>\"><img src =\"{}\" height=\"100\"></a></div>".format('_'+str(categoryCreated)+str(disease_dict[categoryCreated][-1]),image_path,str(categoryCreated)+str(disease_dict[categoryCreated][-1]),image_path)
                    return text
                except:
                    print('[ERROR AT 1286]')
                print('[Time Taken ]',time.time()-t1)
            global return0img_check
            return0img_check =0
            @eel.expose
            def returnImageFrame(wc =0,imageOrqr =0):
                            #
                            # txt = os.popen()
                            # if(txt!=''):
                            #     print('[Shell]',txt)
                            global return0img_check
                            global init_cam_flag
                            if(return0img_check ==0):
                                t1 = time.time()

                            global running_diagnostics
                            if running_diagnostics ==0:

                                #print('[1368]')
                                try: #call this function in loop in html to get frames ok now that button is responding
                                    global cap
                                    global image
                                    global WhichCamera
                                    #WhichCamera = wc

                                    try:
                                        ob = QrCodeScannner(None,WhichCamera)
                                        #cap = cv2.VideoCapture(WhichCamera)
                                        ob.imageCapture()
                                        #_,image =cap.read()
                                        image1 =ob.image.copy()
                                        #print('test')

                                        #print('test1')
                                        image1=imutils.rotate_bound(image1, 270) #rotates the image by 270 degree but none is cutoff during this process
                                        image1=cv2.resize(image1,(250,350),cv2.INTER_AREA)
                                        retval, buffer = cv2.imencode('.png', image1)
                                        jpg_as_text = base64.b64encode(buffer).decode("ascii")
                                        #print('test')
                                        #return image1
                                        ob =None
                                        if(imageOrqr ==0):
                                            return("data:image/png;base64, " + jpg_as_text)
                                        else:
                                            return (image1,"data:image/png;base64, " + jpg_as_text)

                                    except:
                                        #cap.release()
                                        #cap = cv2.VideoCapture(WhichCamera)
                                        if(WhichCamera ==0):
                                            cap = vs0
                                        else:
                                            cap =vs2
                                        #cap.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc('M','J','P','G'))
                                        try:
                                            print('[1428]')
                                            try:
                                                _,image1=cap.read()
                                            except:
                                                print('[Error at 1428]')
                                                print('[Calling 34...]')

                                                init_cam_flag = 0
                                                #restart_uvc()
                                                print('[Calling INIT_CAM_Function...]')
                                                init_cam()


                                            image1=imutils.rotate_bound(image1, 270) #rotates the image by 270 degree but none is cutoff during this process
                                            image1=cv2.resize(image1,(250,350),cv2.INTER_AREA)
                                            retval, buffer = cv2.imencode('.png', image1)
                                            jpg_as_text = base64.b64encode(buffer).decode("ascii")
                                            #print('test')
                                            #return image1
                                            ob =None
                                            if(imageOrqr ==0):
                                                if(return0img_check ==0):
                                                    print('[Time Taken ]',time.time()-t1)
                                                    return0img_check =1
                                                return("data:image/png;base64, " + jpg_as_text)
                                            else:
                                                if(return0img_check ==0):
                                                    print('[Time Taken ]',time.time()-t1)
                                                    return0img_check =1
                                                return (image1,"data:image/png;base64, " + jpg_as_text)
                                        except:
                                            print('[ERROR AT 1428]')
                                except:
                                    print('[ERROR AT 1368]')
                                    #print('[Error at 1428]')
                                    print('[Calling 34...]')

                                    init_cam_flag = 0
                                    #restart_uvc()
                                    print('[Calling INIT_CAM_Function...]')
                                    init_cam()

                                    #return (image1,"data:image/png;base64, " + jpg_as_text)
                            else:
                                print("[waiting for diagnostics to finish]")
                                if(return0img_check ==0):
                                    print('[Time Taken ]',time.time()-t1)
                                    return0img_check =1
                                return 0



            @eel.expose
            def ExtractDetailsFromQr(wc= 0):
                            #print('[1426]')
                            try:
                                global WhichCamera

                                try:
                                    (image,retimage) =returnImageFrame(WhichCamera,1)
                                    #print('check')
                                    caP = QrCodeScannner(image,WhichCamera)
                                    dic ={}


                                    text =caP.qrDecoder()
                                    l=[]
                                    #print('Check')

                                    if(text!=None):
                                        print('check+++++++++',text)
                                        extracted = ExtractInfo(text)
                                        l.append( extracted.extractName())
                                        #print(l)
                                        l.append(extracted.extractgender())
                                        l.append(extracted.extractyob())
                                        l.append('') #dummy for phone noe
                                        l.append(extracted.extractAddress()) #ADDRESS
                                        #dic['AadharNo'] = extracted.extractAadharNo()





                                        return(l)
                                    else:
                                        return [1]

                                except:
                                    #print('Error')
                                    return [1]
                            except:
                                print('[ERROR AT 1426]')


            global camera_order
            camera_order=[]



            @eel.expose
            def go_back():
                os.chdir('../')
                global fold
                fold=''
            @eel.expose
            def press_f11():
                print('change f11 later')
                os.popen("sudo xdotool key F11")
            '''
            @eel.expose
            def check_connectivity():
                import requests
                url='http://www.google.com/'
                timeout=5
                try:
                    _ = requests.get(url, timeout=timeout) #checking whether it can connect dummy website google.com
                    download_thread = threading.Thread(target=upload_()) #if connection is there then we upload wholel files to DropBox
                    download_thread.start() #starts the thread of uploaging .start can be callled only once for the particular thread
                    return

                except requests.ConnectionError
                    return False
            '''
            #should check from here <day 1 >
            @eel.expose #added this line
            def selection_of_images(path): #light box
              path=path
              global fold
              global co

              global ids
              global subfold
              global after_id
              ids=ids+1
              #print("the current dir ",os.getcwd())
              #print("the thumbnail ",path)
              text1= '<div id=__'+str(ids)+'><a name='+str(ids) +' class="lightbox" href=#'+str(ids)+'><img src='+str(path)+'/></a>'
              text2='<div class="lightbox-target" id='+str(ids)+'><img src='+str(path)+'/><a  class="lightbox-close" href="#"><button type="button" style="margin-top:85%;background-color:teal;Color:white" class="btn btn-teal">Close</button></a><div id="DELETE"><button type="button" style="margin-top:120.7%; z-index: 500;margin-left:81%;position:absolute" class="btn btn-danger" onclick=get_deleted("{}","{}")>Delete</button></div></div>'.format(str(path),'#__'+str(ids))
              text=text1+text2
              eel.append_the_images(text)#html
              if ids>4:
                 eel.delete_the_images('#__'+str(after_id))
                 after_id=after_id+1

            @eel.expose
            def python_get_deleted(pah):
                global list_cancer_images
                global list_fluorosis_images
                #print(os.getcwd())
                if(path.exists('web/'+pah)):
                    os.remove('web/'+pah)
                    #print("removed")
                    return "yes"
                else:
                    #print("file dont exist to be removed") #file dont exist to remove can we use this in the current code?yea. ok should we try?ha
                    return "no" #added this line



            @eel.expose
            def stop_camera():
                global cap
                #print('something')
                try:
                    print("stop_cam")
                except e as Exception:
                      print(e)

            @eel.expose
            def check_touch(actually_called=0):
                #print('[1695]')
                try:
                    global TOUCH
                    global  prev_touch
                    var1= GPIO.input(TOUCH)
                    time.sleep(0.1)
                    var =GPIO.input(TOUCH)
                    if(var1==var): #raspberry pi
                        if((var==1) and  (prev_touch == False)):
                            prev_touch = True
                            print('[touched]')
                            return 1
                        elif(var==1):
                            prev_touch=True
                            return 0
                        else:
                            #print('[not touched]')
                            prev_touch =False
                            return 0
                    else:
                        print('Noise')
                        return 0
                except:
                    print('[ERROR AT 1695]')

            @eel.expose
            def connect_to_wifi(ssid,password):
                print(ssid+" "+password)
                connect_command='sudo nmcli d wifi connect "{}" password {} '.format(str(ssid),str(password))
                print(connect_command)
                os.system(connect_command)
                #print(os.system(connect_command))

            @eel.expose
            def disconnect_from_wifi():
                global iface
                global wifi
                iface = wifi.interfaces()[0]
                iface.disconnect()
                time.sleep(.5)#giving it time to disconnect ideal time:1s
            @eel.expose
            def scan_wifi_():
                html_code=''
                command="sudo iwlist wlan0 scanning | egrep 'ESSID'"
                #connect_command="sudo nmcli d wifi connect Mr.Krishna password global122 "
                iresults=list(os.popen(command))
                #os.system(connect_command)

                for i in iresults:

                    ptr1 = i.index('"')
                    ptr2 = ptr1 +i[ptr1+1:].index('"')
                    print(i[ptr1+1:ptr2+1])
                    j =i[ptr1+1:ptr2+1]

                    html_code = html_code+ '<li onclick=\"wifi_cred(\'{}\')\"id="{}">{}</a></li>'.format(j,j,j)
                if(len(iresults)!=0):
                    return html_code
                else:
                    return '<li onclick="wifi_cred("{}")"id="{}">{}</a></li>'.format('None','Nonei','No Wifi found')
            @eel.expose
            def dummy(ssid,pswd):
                print(ssid)
                print(pswd)

    except SystemExit as e:
           print(e)
@eel.expose
def set_camera(c,tem=0):
    t1 = time.time()
    print('[1550]')
    try:
        #c =1 then dental
        #c =0 then web cam
        global cap
        #print(cap,"____________________________________")
        global camera
        global WhichCamera
        global vs2,vs0
        global web_cam,dental_cam,web_cam_cap,dental_cam_cap
        global camera_order

        if(c ==0):
            if(len(camera_order)==0):
                print('check 1')
                vs0=WebcamVideoStream(src=web_cam).start()
                #vs0.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc('M','J','P','G'))
            elif(camera_order[-1]==1):
                print('check 2')
                vs0=WebcamVideoStream(src=web_cam).start()


            camera =web_cam
            WhichCamera=web_cam
            cap =vs0
            try:
                if(camera_order[-1]==1):
                    vs2.stop()
                    del vs2
            except:
                pass
            camera_order.append(0)

        else:
            if(len(camera_order)==0):
                print('check 3')
                vs2=WebcamVideoStream(src=dental_cam).start()
            elif(camera_order[-1]==0):
                print('check 4')
                vs2=WebcamVideoStream(src=dental_cam).start()



            camera =dental_cam
            WhichCamera=dental_cam
            cap =vs2
            try:
                if(camera_order[-1]==0):
                    vs0.stop()
                    del vs0
            except:
                pass
            camera_order.append(1)
        if(len(camera_order)==5):
            camera_order.pop(0)
    except:
        print('[ERROR AT 1550]')
    print('[Time Taken ]',time.time()-t1)

    #print(cap)



@eel.expose
def swi_cam():
    t1 = time.time()

    print('[1484]')
    global web_cam_index
    global dental
    global web_cam,dental_cam
    global camera_order
    if(camera_order[-1]==0):
        set_camera(1)
    else:
        set_camera(0)
    # try:
    #     #switiching Camera from 0 to 1
    #     global cap
    #     #print(cap,"____________________________________")
    #     global camera
    #     global WhichCamera
    #     global vs2,vs0
    #     #changed the logic for switiching the camera
    #     if(camera == web_cam):
    #         vs2.start()
    #         print("[switching to dental_cam]")
    #         camera =dental_cam
    #         WhichCamera=dental_cam
    #         cap =vs2
    #         vs0.stop()
    #     else:
    #         vs0.start()
    #         print("[switching to web_cam]")
    #         camera = web_cam
    #         WhichCamera= web_cam
    #         cap =vs0
    #         vs2.stop()
    # except:
    #     print('[1484]')
    print('[time taken]',time.time()-t1)
    time.sleep(1)
@eel.expose
def create_log(name,gender,phoneNo,yob,address):
    data = {
        'name': name,
        'phoneNo' : phoneNo,
        'yob' : yob,
        'address' : address,
        'gender' : gender,
        'satus' : ''
    }
    with open('log.txt', 'w') as outfile:
        json.dump(data, outfile)
        #print('[LOG FILE CREATED]')
    #print(os.getcwd())

@eel.expose
def check_log():
    with open('log.txt') as json_file:
        data = json.load(json_file)
        if('status' == 'FAIL'):
            return [data['name'],data['phoneNo'],data['yob'],data['address']] #to prompt operator to continue with same patient
        else:
            return 0
@eel.expose
def bad_exit(name,gender,phoneNo,yob,address):
    data = {
        'name': name,
        'phoneNo' : phoneNo,
        'yob' : yob,
        'address' : address,
        'gender' : gender,
        'satus' : 'FAIL',
    }
    with open('log.txt', 'w') as outfile:
        json.dump(data, outfile)
        #print('[LOG FILE CREATED]')


#index->_index->capture_disease
@eel.expose
def register_last_checkpoint(check_point):
    global last_check_point
    last_check_point = check_point



@eel.expose
def get_ssid():
    command = "(iwgetid -r)"
    ssid =os.system(command)
    command1 ="sudo nmcli con down '{}'".format(ssid)
    #return ssid
@eel.expose
def give_loc(x):
    global location_present
    location_present=x

def check_websocket_open():
    while (True):
        a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        location = ("127.0.0.1", 9000)
        result_of_check = a_socket.connect_ex(location)
        if result_of_check == 0:
            a_socket.close()
            return 1
        else:
            a_socket.close()
            return 0


if (__name__=="__main__"):
    global pth
    # global last_check_point
    # last_check_point = "index"
    # alert on the JS side , indication of uploading to cloud
    print('[MAIN FUNCTION]')
    pth=os.getcwd()+"/web/Patient"
    #global  download_thread
    #download_thread = threading.Thread(target=upload) #threading upload funciton
    Main_program()
    logging.basicConfig(
    level=logging.ERROR,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.FileHandler("vish.log",'w'),logging.StreamHandler()])
    eel.start('index.html',options=web_options,suppress_error=True,)
