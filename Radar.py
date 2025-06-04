import cv2
import time
import math
import serial
arduino = serial.Serial('COM3',9600) #replace "COM3" with your arduino COM-port
think = 1 #thinkness of light-green radar lines
print("connect")
radar = cv2.imread("Radar.png") #replace the location of "Radar.png" file
cv2.imshow("Radar", radar)
time.sleep(1)
x1 = 0
y1 = 0
count1 = 0
alert = 0
def text(xy, text1, scale, color, thin): #better function for text.
    cv2.putText(radar, str(text1), xy, cv2.FONT_HERSHEY_DUPLEX, scale, color, thin)
def update(): #creating static lines and text
    cv2.rectangle(radar, (0, 0), (800, 600), (0, 0, 0), -1)
    cv2.putText(radar, "Made by KaK_TyZz", (50, 300), cv2.FONT_HERSHEY_PLAIN, 5, (20, 20, 20), 3)
    cv2.line(radar, (400, 520), (int(-100000 * math.cos(math.radians(15))), int(-100000 * math.sin(math.radians(15)))), (51, 245, 21), think)
    cv2.line(radar, (400, 520), (int(-100000 * math.cos(math.radians(30))), int(-100000 * math.sin(math.radians(30)))), (51, 245, 21), think)
    cv2.line(radar, (400, 520), (int(-100000 * math.cos(math.radians(45))), int(-100000 * math.sin(math.radians(45)))), (51, 245, 21), think)
    cv2.line(radar, (400, 520), (int(-100000 * math.cos(math.radians(60))), int(-100000 * math.sin(math.radians(60)))), (51, 245, 21), think)
    cv2.line(radar, (400, 520), (int(-100000 * math.cos(math.radians(75))), int(-100000 * math.sin(math.radians(75)))), (51, 245, 21), think)
    cv2.line(radar, (400, 520), (int(-100000 * math.cos(math.radians(105))), int(-100000 * math.sin(math.radians(105)))), (51, 245, 21), think)
    cv2.line(radar, (400, 520), (int(-100000 * math.cos(math.radians(120))), int(-100000 * math.sin(math.radians(120)))), (51, 245, 21), think)
    cv2.line(radar, (400, 520), (int(-100000 * math.cos(math.radians(135))), int(-100000 * math.sin(math.radians(135)))), (51, 245, 21), think)
    cv2.line(radar, (400, 520), (int(-100000 * math.cos(math.radians(150))), int(-100000 * math.sin(math.radians(150)))), (51, 245, 21), think)
    cv2.line(radar, (400, 520), (int(-100000 * math.cos(math.radians(165))), int(-100000 * math.sin(math.radians(165)))), (51, 245, 21), think)
    cv2.line(radar, (400, 520), (400, 0), (51, 245, 21), think)
    cv2.ellipse(radar, (400, 520), (110, 110), 0, 180, 360, (51, 245, 21), think)
    cv2.ellipse(radar, (400, 520), (165, 165), 0, 180, 360, (51, 245, 21), think)
    cv2.ellipse(radar, (400, 520), (220, 220), 0, 180, 360, (51, 245, 21), think)
    cv2.ellipse(radar, (400, 520), (275, 275), 0, 180, 360, (51, 245, 21), think)
    cv2.ellipse(radar, (400, 520), (330, 330), 0, 180, 360, (51, 245, 21), think)
    cv2.ellipse(radar, (400, 520), (385, 385), 0, 180, 360, (51, 245, 21), think)
    cv2.ellipse(radar, (400, 520), (440, 440), 0, 180, 360, (51, 245, 21), think)
    cv2.ellipse(radar, (400, 520), (495, 495), 0, 180, 360, (51, 245, 21), think)
    cv2.ellipse(radar, (400, 520), (550, 550), 0, 180, 360, (51, 245, 21), think)
    text((30, 580), "alert status:", 2.3, (51, 245, 21), 1)
    text((515, 513), "10cm", 0.5, (51, 245, 21), 1)
    text((567, 513), "15cm", 0.5, (51, 245, 21), 1)
    text((623, 513), "20cm", 0.5, (51, 245, 21), 1)
    text((678, 513), "25cm", 0.5, (51, 245, 21), 1)
    text((735, 513), "30cm", 0.5, (51, 245, 21), 1)
    cv2.rectangle(radar, (0, 0), (800, 600), (51, 245, 21), think * 2)
    cv2.line(radar, (0, 520), (800, 520), (51, 245, 21), think)
update()
while True:
    box = arduino.readline().decode('utf-8').strip() #decode distance and degrees
    qq = list(map(int, box.split()))
    dist = int(qq[1]) * 11
    grad = math.radians(int(qq[0])+ 45) #convert to radians
    print(dist, grad)
    if 0 <= grad <= 45 : #for left half of radar
        x1 = int(400 - (dist * math.cos(grad)))
        y1 = int(520 - (dist * math.sin(grad)))
    elif 45 < grad <= 90 : # for right half radar
        x1 = int(400 + (dist * math.cos(grad)))
        y1 = int(520 - (dist * math.sin(grad)))
    if dist <= 500: #start the alert if somthing is closer to radar
        alert = 1
        text((480, 580), "DANGER!", 2.3, (0, 0, 170), 3)
    elif dist > 600:
        alert = 0 #\/ drawing alert and empty radar lines
    cv2.line(radar, (400, 520), (int(400 - (1000 * math.cos(grad))), int(520 - (1000 * math.sin(grad)))), (14, 64, 0), 1)
    cv2.line(radar, (x1, y1), (int(400 - (1000 * math.cos(grad))), int(520 - (1000 * math.sin(grad)))), (0, 0, 255), 2)
    cv2.imshow("Radar", radar)
    count1 += 1
    if count1 % 89 == 0: #update lines  every cycle, if there is no alert
        if alert == 0:
            update()
        else:
            pass
    if cv2.waitKey(10) == ord("q"): #to close program press "q"
        cv2.destroyAllWindows()
        break
