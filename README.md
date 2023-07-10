# Facial-Recognition-Attendance-System
## A project to try and automate the attendance system using different techniques of Facial Recognition and Detection.

Managing attendance can be a tedious job when implemented by traditional 
methods like calling out roll calls or taking a student's signature. A smart and 
authenticated attendance system needs to be implemented to solve this issue. 

The face is a unique identification of humans due to their distinct facial 
features. Face recognition systems are helpful in many real-life applications. 

In the proposed method, all the students will initially be enrolled by storing 
their facial images with a unique ID. At the time of attendance, real-time 
images will be captured, and the faces in those images will be matched with 
the faces in database.

The Haar cascade algorithm is used for face 
detection. The local Binary Patterns Histogram (LBPH) algorithm is used for 
face recognition and training of the stored dataset, which generates the 
histogram for stored and real-time images. The difference between histograms 
of real-time images & dataset images is calculated for face recognition. This
difference gives the best match, displaying that student's name & roll 
number. 
Attendance of the student is automatically updated in the excel sheet.


## Aims and Objectives
The objective of this project is to develop a face recognition attendance system. Expected 
achievements to fulfill the objectives are:
1- To detect the face segment from the video frame.
2- To extract the useful features from the face detected.
3- To classify the features in order to recognize the face
detected.
4- To record the attendance of the identified student.
![image](https://user-images.githubusercontent.com/67535635/169953181-d9e3214d-de9d-488a-bad9-9ff5d7a443fc.png)

![image](https://user-images.githubusercontent.com/67535635/169953323-002e2179-22e8-43f2-91db-188f4e27c3d4.png)



## Scope of the project:

For the initial development phase, i have divided the project into three 
modules. First, I experimented with some facial detection and recognition 
techniques discussed in different research papers to study and find the best approach for 
our final model.

In the second module, i developed the project using the Haar 
cascade technique for facial detection and LBPH for facial recognition.

In the third module, i have used transfer learning to develop a more accurate model. 

The project presents a prototype of the main idea, which is to take real-time 
attendance using facial recognition. So currently, i have used the laptop's 
inbuilt camera, which can later be replaced with CCTV cameras and other camera 
modules. For the GUI, I have used Tkinter to make it easier for the user to test the model while experimenting. 
Apart from that, an excel sheet is created automatically for the present day (which shows the students attendance) and is directly 
mailed to the respected faculty using YAGMAIL in python.

## GUI

![image](https://user-images.githubusercontent.com/67535635/169953350-6977d0b3-17e0-46f4-ae99-eabcd42e41f1.png)

## Face Detection
![image](https://user-images.githubusercontent.com/67535635/169953368-a0387b0f-2efc-4bcc-8186-3e89cfa516d3.png)
![image](https://user-images.githubusercontent.com/67535635/169953379-bf822319-a273-4110-b512-dfa37347f7b5.png)
![image](https://user-images.githubusercontent.com/67535635/169953390-81a0b90c-4cf6-4d52-8471-eee78b620e77.png)

## Database
![image](https://user-images.githubusercontent.com/67535635/169954517-7d0b69d2-7115-4c9b-8478-6372b09a004c.png)


## Face Recognition
![image](https://user-images.githubusercontent.com/67535635/169953428-d57e6646-7725-45e4-a67d-260007daf806.png)
![image](https://user-images.githubusercontent.com/67535635/169953572-fec38fd5-7874-4799-8e8b-39a2517c2ded.png)
![image](https://user-images.githubusercontent.com/67535635/169953634-74f7f8ac-9418-4888-8d7a-f5f264ad6737.png)
![image](https://user-images.githubusercontent.com/67535635/169953648-ca37260b-66ff-4a9c-bb76-7445783b48fa.png)
![image](https://user-images.githubusercontent.com/67535635/169953664-bb8611c2-7a37-448d-9199-f5611bda1f5d.png)
![image](https://user-images.githubusercontent.com/67535635/169953670-a2870952-55ed-46ac-ad86-1574bce7fbab.png)

## Attendance

![image](https://user-images.githubusercontent.com/67535635/169953469-9066db7d-dbb6-4fda-a27f-b116fb4f77a7.png)

## Auto Mail
![image](https://user-images.githubusercontent.com/67535635/169954591-16c1620f-4d64-4156-94bc-873a9da4c75c.png)







## CONCLUSION 

Module 1-

![image](https://user-images.githubusercontent.com/67535635/169953759-492ed478-6064-47dd-b6c0-77ac65a2cd6a.png)
 
                     
The LBPH algorithm can recognize the front face as well as side face with approximate accuracy of 
90% .
This process is able to detect multiple faces with an accuracy of 91.67%. 

Module 2-

For detection, Paul–Viola Jones algorithm is used and for face recognition Linear Binary 
Pattern Histogram (LPBH) algorithm is applied. 
In the result, the unique ID and name of the student is displayed along with the confidence percentage. 
Confidence percentage represents the distance 
between the histogram of the stored image and histogram of the real time image , and is calculated 
by using Euclidean distance. Lower is the distance, higher is the recognition rate. 

Modeule 3-
I tried to explore transfer learning and see the accuracy obtained on using pretrained models 
by using MediaPipe in dlib library for face detection and the openCV Face_Recognition 
library  for face recognition respectively .
It was observed that though the frame rate was considerably less but the accuracy increased immensely. 

## FUTURE SCOPE

1-To increase the accuracy further of the model trained in module 2 we can experiment with other classifiers such as KNN ,SVM, apart 
from the distance classifier used in the project.
 
2- Integrate the software with the hardware components using proper camera modules such as ESP32 , and TinyML for model deployment .

3- For database ,we can use solutions such as Cloud FireStore and other real time databases.
Additionally, an android application can also be developed .
