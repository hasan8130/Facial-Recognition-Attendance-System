# Facial-Recognition-Attendance-System
## A project to try and automate the attendance system using different techniques of Facial Recognition and Detection.

Managing attendance can be a tedious job when implemented by traditional 
methods like calling out roll calls or taking a student's signature. A smart and 
authenticated attendance system needs to be implemented to solve this issue. 
Generally, biometrics such as face recognition, fingerprint, DNA, retina, iris 
recognition, hand geometry, etc. are used to execute smart attendance systems. 
The face is a unique identification of humans due to their distinct facial 
features. Face recognition systems are helpful in many real-life applications. 
In the proposed method, all the students will initially be enrolled by storing 
their facial images with a unique ID. At the time of attendance, real-time 
images will be captured, and the faces in those images will be matched with 
the faces in the pre-trained dataset. The Haar cascade algorithm is used for face 
detection. The local Binary Patterns Histogram (LBPH) algorithm is used for 
face recognition and training of the stored dataset, which generates the 
histogram for stored and real-time images. The difference between histograms 
of real-time images & dataset images is calculated for face recognition. The 
lower difference gives the best match, displaying that student's name & roll 
number. Attendance of the student is automatically updated in the excel sheet.


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
The main intention of this project is to solve the issues encountered in the old attendance system 
while reproducing a brand new innovative smart system that can provide convenience to the 
institution.
For the initial development phase, i have divided the project into three 
modules. First, we experimented with some facial detection and recognition 
techniques discussed in research papers to study and find the best approach for 
our final model. In the second module, i developed the project using the Haar 
cascade technique for facial detection and LBPH for facial recognition. In the 
third module, i have used transfer learning to develop a more accurate model. 
The project presents a prototype of the main idea, which is to take real-time 
attendance using facial recognition. So currently, i have used the laptop's 
inbuilt camera, which can later be replaced with CCTV cameras and other camera 
modules. For the GUI, we have used Tkinter to make it easier for the user to go 
through the model while experimenting with the model. 
Apart from that, an excel sheet is created which shows the students attendance and is directly 
mailed to the respected faculty .

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
The proposed method uses face detection and face recognition that helps to maintain the 
automated attendance system. 
Module 1-

![image](https://user-images.githubusercontent.com/67535635/169953759-492ed478-6064-47dd-b6c0-77ac65a2cd6a.png)
 
                     
The LBPH algorithm can recognize the front face as well as side face with approximate accuracy of 
90% This process is able to detect multiple faces with an accuracy of 91.67%. 

In Module 2 for detection, Paul–Viola Jones algorithm is used and for face recognition Linear Binary 
Pattern Histogram (LPBH) algorithm is applied. In the result, the unique ID and name of the student 
is displayed along with the confidence percentage. Confidence percentage represents the distance 
between the histogram of the stored image and histogram of the real time image and is calculated 
by using Euclidean distance. Lower is the distance, higher is the recognition rate. 
We tried to explore transfer learning and see the accuracy obtained on using pretrained models in 
module 3. MediaPipe in dlib library was used for face detection and the openCV Face_Recognition 
library was used for face recognition .It was observed that though the frame rate was considerably 
less but the accuracy increased immensly. 
## FUTURE SCOPE
To increase the accuracy further we can experiment with other classifiers such as KNN ,SVM apart 
from the distance classifier used in the project.Further we can also train our model to adjust as per 
different lightning conditions and detect side faces as well. 
The future scope of the project is to integrate the software with the hardware components for 
example CCTV cameras and better Cam modules through which a monthly list of the defaulter 
students can be sent to the mentor. Additionally, an application can be developed to help students 
to maintain a track of their attendance which is capable of recognising the identity of each 
individuals and eventually record down the data into a database system.It can also be used in offices 
where a large group of employees sit in a hall and their attendance will be marked automatically by 
capturing a video 
