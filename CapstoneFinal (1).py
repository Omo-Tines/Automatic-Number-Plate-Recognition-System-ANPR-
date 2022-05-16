#import pytesseract
#pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
#print(pytesseract.image_to_string(r'C:\Users\HP\Desktop\download.jfif'))
import cv2
import imutils
import numpy as np
from PIL import Image
import pytesseract
from PIL import Image
from picamera.array import PiRGBArray
from picamera import PiCamera
import smtplib
import getpass
import ssl
import mysql.connector as MySQLdb
import string, secrets
from datetime import datetime
from gpiozero import LED
from time import sleep
import re

red= LED(22)
amber = LED(27)
green= LED(17)


red.on()

#sleep(2)#wait 2seconds before changing capturing plate

server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login("tinesebun@gmail.com","tolusele")
#img = cv2.imread('licenseplate2.jpg',cv2.IMREAD_COLOR)
camera= PiCamera()
print('s')
camera.resolution = (640,480)
print('o')
camera.framerate = 30
print('m')
rawCapture = PiRGBArray(camera,size=(640,480))#640,480
print('p')
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    print('m')
    img = frame.array
    cv2.imshow("Frame",img)
    key = cv2.waitKey(1) & 0xFF
    rawCapture.truncate(0)
    if key == ord("s"):
        img = cv2.resize(img, (640,480) )
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #convert to grey scale
        gray = cv2.bilateralFilter(gray, 11, 17, 17) #Blur to reduce noise
        edged = cv2.Canny(gray, 30, 200) #Perform Edge detection
        # find contours in the edged image, keep only the largest
        # ones, and initialize our screen contour
        cnts = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:10]
        screenCnt = None
        # loop over our contours
        for c in cnts:
            # approximate the contour
            peri = cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, 0.018 * peri, True)
            # if our approximated contour has four points, then
            # we can assume that we have found our screen
            if len(approx) == 4:
                screenCnt = approx
                break
        if screenCnt is None:
            detected = 0
            print ("No contour detected")
        else:
            detected = 1
        if detected == 1:
            cv2.drawContours(img, [screenCnt], -1, (0, 255, 0), 3)
        # Masking the part other than the number plate
        mask = np.zeros(gray.shape,np.uint8)
        new_image = cv2.drawContours(mask,[screenCnt],0,255,-1,)
        new_image = cv2.bitwise_and(img,img,mask=mask)
        # Now crop
        (x, y) = np.where(mask == 255)
        (topx, topy) = (np.min(x), np.min(y))
        (bottomx, bottomy) = (np.max(x), np.max(y))
        Cropped = gray[topx:bottomx+1, topy:bottomy+1]
        #Read the number plate
        #pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
        #text = pytesseract.image_to_string(r'C:\Users\HP\Desktop\licenseplate2.jpg')
        plate =pytesseract.image_to_string(Cropped,config='--psm 11')
        print("Detcted Number is:",plate)
        print(plate)
        cv2.imshow('image',img)
        cv2.imshow('Cropped',Cropped)
        #database connect
        
        text=plate
        
        text=re.sub(r'[^\w]', '',text)#to remove any non alphanumeric charactwers from the string 
        text=re.sub(r'_', '',text)#to remove underscores
        text=text.strip()#to remove leading or trailing spacess
        print(text)
        
        now = datetime.now()
        print("database connection")
        db=MySQLdb.connect("localhost","root","password","capstone",3301)
        print("connection established")
        insertrec=db.cursor()
        sqlselect= "select * from driver where license_plate = %s "
        insertrec.execute(sqlselect,(text,))
        records = insertrec.fetchall()

        for row in records:
            Id=row[0]
            
        sqlname= "select fname,lname,email from person where person_id= %s"
        insertrec.execute(sqlname,(Id,))
        person= insertrec.fetchall()
        for i in person:
            name= i[0] +" "+i[1]
            email= i[2]
        rand = "DRF"+secrets.choice(string.ascii_letters)#for the offence code
        date = now.strftime('%Y-%m-%d %H:%M:%S')

        sqlquery="insert into violator(person_id,offence_code,date_time_created,payment,paid) values(%s,%s,%s,'100.50','0')"
        que=(Id,rand,date)
        insertrec.execute(sqlquery,que)
        db.commit()
        print("Record saved successfully...!")
        db.close()
        server.sendmail("tinesebun@gmail.com","olasenitowobola@gmail.com",plate+" "+name+" "+email)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        break
        
cv2.destroyAllWindows()

sleep(1)
print('redon')
red.off()
print('redoff')
amber.on()
sleep(3)
amber.off()

green.on()
sleep(3)
green.off()
#database connec
# import pyodbc
# server = '<server>.database.windows.net'
# database = '<database>'
# username = '<username>'
# password = '{<password>}'   
#EMAIL PORTION
# Get email ID and password from user
#email = input("Enter email ID: ")
#password = getpass.getpass("Enter password: ")

# Set SMTP host and port
#if "gmail" in email:
#  host = "smtp.gmail.com"
#   port = 587
#elif "outlook" in email:
#    host = "smtp-mail.outlook.com"
#   port = 587
#else:
#    print("Invalid email ID, please try again")
#    exit(0)

# Create SMTPLib object and contact server
#server = smtplib.SMTP(host, port)
#check = server.ehlo()
#if check[0] == 250:
#    print("Successfully contacted mail server")
#else:
#    print("Unable to contact server")
#    exit(0)

# Start TLS encryption (only to be done if conencting to port 587 i.e. TLS)
#server.starttls()

# Logging into the server
#try:
#    server.login(email, password)
#    print("Login successful")
#except smtplib.SMTPAuthenticationError as ex:
#    print("Exception:", ex)#
#    exit(0)

# Get email details from user
#sender_mail = email
#receiver_email =input("Enter email subject: ")
#subject = input("Enter email subject: ")
#content = text #input("Enter email content: ")

# Create email body by merging emails object and content
#body = "Subject: " + subject + '\n' + content

# Send the mail
#output = server.sendmail(sender_mail, receiver_email, body)
#if not len(output):
#    print("Send mail successfully")
#else:
#    print("Unable to send mail, please try again")
#    exit(0)