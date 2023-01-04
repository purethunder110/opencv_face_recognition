import cv2 as cv
import tkinter as tk
from tkinter import filedialog

file_path='None'

def file_handle():
    #calling the file functionality from tkinter libs
    root=tk.Tk()
    root.withdraw()
    path=filedialog.askopenfilename()
    return path

def image_rec(path,opt):
    #using opencv for detecting image
    img=cv.imread(path)#loading image
    gray_img=cv.cvtColor(img,cv.COLOR_RGB2GRAY)#changing the color of img to gray for less computational use

    #classifier loading file for loading data set againdt witch image will be recognised.
    if opt==1:
        classify=cv.CascadeClassifier(f"{cv.data.haarcascades}haarcascade_frontalface_alt.xml")
        processed=classify.detectMultiScale(gray_img,minSize=(50,50))
    elif opt==2:
        classify=cv.CascadeClassifier(f"{cv.data.haarcascades}haarcascade_eye.xml")
        processed=classify.detectMultiScale(gray_img,minSize=(50,50))
    else:
        classify=cv.CascadeClassifier(f"{cv.data.haarcascades}haarcascade_smile.xml")
        processed=classify.detectMultiScale(gray_img,minSize=(200,200))
    
    #the detectMultiScale() function return the number of positive cases from the dataset

    #drawing box for the positive regions
    if len(processed)!=0:
        for (x,y,width,hight) in processed:
                cv.rectangle(img,(x,y),(x+hight,y+width),(0,255,0),2)
    else:
        print(">>>>Not recognised")
        return 0
    #window for opening the final image
    while True:
        cv.imshow("image recognition",img)
        if cv.waitKey(1)==ord('q'):
            cv.destroyWindow("image recognition")
            return 0


#main fnction loop
while True:
    print('-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
    print("image recognition:-")
    print('image pointer path=',file_path)
    print('enter your choice:')
    print('1.enter image pointer path')
    print('2.detect faces in image')
    print('3.detect eyes in image')
    print('4.detect smile in image')
    print('5.exit')
    choice=int(input('enter your choice=>>'))
    print('-*-*-*-*-*-*')
    if choice==1:
        file_path=file_handle()
    else:
        if file_path=='None':
            print('>>>>file pointing to none, run 1st command first')
        elif choice==2:
            image_rec(file_path,1)
        elif choice==3:
            image_rec(file_path,2)
        elif choice==4:
            image_rec(file_path,3)
        elif choice==5:
            exit()
        else:
            print(">>>>wrong input")