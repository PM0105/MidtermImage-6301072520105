#import library
import cv2 
import numpy as np
import matplotlib.pyplot as plt

#import image
img = cv2.imread("med.jpg") 
img1 = cv2.imread("black.jpg")
name = cv2.imread("background.jpg")
img = cv2.resize(img,(600,600)) #ปรับขนาดภาพ (x,y)
img1 = cv2.resize(img1,(600,40))
B1 = cv2.resize(img1,(250,40))
B2 = cv2.resize(img1,(200,40))
B3 = cv2.resize(img1,(225,40))
B4 = cv2.resize(img1,(175,40))
B5 = cv2.resize(img1,(225,40))
name = cv2.resize(name,(600,600))

#delete noise
blur = cv2.GaussianBlur(img, (9,9), 0) #เบลอภาพเพื่อลบ noise

#med 1 gold
lower_1 = np.array([33,85,85]) #detect color [B,G,R]
upper_1 = np.array([98,230,255])
mask = cv2.inRange(blur, lower_1, upper_1) #กำหนดช่วงของค่าสีให้เป็นขาวดำ โดยถ้าเป็นค่าที่อยู่ในช่วง upper lower จะเป็นสีขาว ส่วนอื่นที่ไม่อยู่ช่วงค่าที่กำหนดจะเป็นสีดำ
color1 = cv2.bitwise_and(blur,blur,mask=mask) #เติมสี
#med 2 blue
lower_2 = np.array([65,55,65])
upper_2 = np.array([189,158,131])
mask = cv2.inRange(blur, lower_2, upper_2)
color2 = cv2.bitwise_and(blur,blur,mask=mask)
#med 3 black
lower_3 = np.array([41,37,36])
upper_3 = np.array([105,105,105])
mask = cv2.inRange(blur, lower_3, upper_3)
color3 = cv2.bitwise_and(blur,blur,mask=mask)
#med 4 pink
lower_4 = np.array([60,65,55])
upper_4 = np.array([188,171,251])
mask = cv2.inRange(blur, lower_4, upper_4)
color4 = cv2.bitwise_and(blur,blur,mask=mask)
#med 5 cream
lower_5 = np.array([140,155,176])
upper_5 = np.array([174,193,214])
mask = cv2.inRange(blur, lower_5, upper_5)
color5 = cv2.bitwise_and(blur,blur,mask=mask)

#Crop
#med 1
crop_img1 = color1[184:53+184, 370:68+370] # Crop จาก x, y, w, h คือ img[y: h + y, x: w + x]
m1 = cv2.resize(crop_img1,(50,40))
crop_img2 = color1[228:42+228, 450:73+450]
m2 = cv2.resize(crop_img2,(50,40))
#med 2
crop_img3 = color2[368:45+368, 235:18+235]
m3 = cv2.resize(crop_img3,(50,40))
crop_img4 = color2[285:35+285, 178:27+178]
m4 = cv2.resize(crop_img4,(50,40))
crop_img5 = color2[204:25+204, 129:30+129]
m5 = cv2.resize(crop_img5,(50,40))
crop_img6 = color2[122:35+122, 182:20+182]
m6 = cv2.resize(crop_img6,(50,40))
#med 3
crop_img7 = color3[329:60+329, 95:50+95]
m7 = cv2.resize(crop_img7,(50,40))
crop_img8 = color3[281:55+281, 218:50+218]
m8 = cv2.resize(crop_img8,(50,40))
crop_img9 = color3[181:35+181, 313:50+313]
m9 = cv2.resize(crop_img9,(50,40))
#med 4
crop_img10 = color4[172:35+172, 66:30+66]
m10 = cv2.resize(crop_img10,(50,40))
crop_img11 = color4[229:38+229, 199:28+199]
m11 = cv2.resize(crop_img11,(50,40))
crop_img12 = color4[464:42+464, 118:35+118]
m12 = cv2.resize(crop_img12,(50,40))
crop_img13 = color4[368:33+368, 348:28+348]
m13 = cv2.resize(crop_img13,(50,40))
crop_img14 = color4[423:40+423, 347:28+347]
m14 = cv2.resize(crop_img14,(50,40))
#med 5
crop_img15 = color5[143:48+143, 117:42+117]
m15 = cv2.resize(crop_img15,(50,40))
crop_img16 = color5[256:52+256, 368:42+368]
m16 = cv2.resize(crop_img16,(50,40))
crop_img17 = color5[327:60+327, 458:36+458]
m17 = cv2.resize(crop_img17,(50,40))

# นำภาพมาเรียงกันในแนวนอน
med1 = np.hstack((B1,m1,m2,B1)) 
med2 = np.hstack((B2,m3,m4,m5,m6,B2))
med3 = np.hstack((B3,m7,m8,m9,B3))
med4 = np.hstack((B4,m10,m11,m12,m13,m14,B4))
med5 = np.hstack((B5,m15,m16,m17,B5))

# นำภาพมาเรียงกันในแนวตั้ง
Final = np.vstack((img1,img1,img1,med1,img1,med3,img1,med5,img1,med2,img1,med4,img1,img1,img1))

#สร้างกรอบสี่เหลี่ยม
cv2.rectangle(Final, (240,110), (362,170), (0,255,255), 1) #(ชื่อตัวแปร,(ตำแหน่งมุมซ้ายบน(x,y)),(ตำแหน่งมุมขวาล่าง(x,y)),(ค่าสี(B,G,R)), ความหนาเส้น)
cv2.rectangle(Final, (218,190), (385,250), (192,192,192), 1)
cv2.rectangle(Final, (218,270), (385,330), (153,204,255), 1)
cv2.rectangle(Final, (190,350), (405,410), (204,204,0), 1)
cv2.rectangle(Final, (165,430), (430,490), (178,102,255), 1)

#ใส่ข้อความในภาพ
cv2.putText(Final,"Med1:GOLD  = 2 ea",(5,145),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,255),1) #(ชื่อตัวแปร,"ข้อความ",(ตำแหน่ง(x,y)),ฟ้อน,ขนาดข้อความ,(ค่าสี(B,G,R)), ความหนาเส้น)
cv2.putText(Final,"Med2:BLCAK = 3 ea",(5,225),cv2.FONT_HERSHEY_SIMPLEX,0.5,(192,192,192),1)
cv2.putText(Final,"Med3:CREAM = 3 ea",(5,305),cv2.FONT_HERSHEY_SIMPLEX,0.5,(153,204,255),1)
cv2.putText(Final,"Med4:BLUE  = 4 ea",(5,385),cv2.FONT_HERSHEY_SIMPLEX,0.5,(204,204,0),1)
cv2.putText(Final,"Med5:PINK  = 5 ea",(5,465),cv2.FONT_HERSHEY_SIMPLEX,0.5,(178,102,255),1)

#Copy image
Original = img.copy()
cv2.putText(Original,"ORIGINAL",(165,70),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255),5)
Result = Final.copy()
cv2.putText(Result,"RESULT",(187,70),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255),5)

#My Information
cv2.putText(name,"My Information",(130,150),cv2.FONT_HERSHEY_SIMPLEX,1.5,(0,150,255),5)
cv2.putText(name,"Name : Phattharaphon Muenphon",(30,250),cv2.FONT_HERSHEY_SIMPLEX,1,(0,150,255),2)
cv2.putText(name,"ID : 6301072520105",(30,300),cv2.FONT_HERSHEY_SIMPLEX,1,(0,150,255),2)
cv2.putText(name,"Section : 1",(30,350),cv2.FONT_HERSHEY_SIMPLEX,1,(0,150,255),2)

#เปรียบเทียบ
Compare = np.hstack((Original,Result))

#show
cv2.imshow("Information",name)
#cv2.imshow("Original Image",img)
#cv2.imshow("mask",mask)
#cv2.imshow("med1",color1)
#cv2.imshow("med2",color2)
#cv2.imshow("med3",color3)
#cv2.imshow("med4",color4)
#cv2.imshow("med5",color5)
#cv2.imshow("am1",med1)
#cv2.imshow("am2",med2)
#cv2.imshow("am3",med3)
#cv2.imshow("am4",med4)
#cv2.imshow("am5",med5)
#cv2.imshow("img1",img1)
#cv2.imshow("Final Image",Final)
cv2.imshow("Compare Image",Compare)

#plt.subplot(121),plt.imshow(img)
#plt.subplot(122),plt.imshow(Final)
#plt.show()


#close window
cv2.waitKey(0)
cv2.destroyAllWindows
