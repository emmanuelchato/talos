import subprocess as sp
import time

# 2018-2019  Emmanuel Santiago Carrillo, STB tester basado en Python & OpenCV
# Scripts basicos de captura de video, fotogramas & validación 
# Configure el path definitivo para implementación en producción

def captura_video():
    print ("\n,")
    print ("************************************************")
    print ("*****2018-2019  EMMANUEL SANTIAGO CARRILLO******")
    print ("******************TALOS IA**********************")
    print ("************************************************")
    print ("************************************************, \n")
    print ("CAPTURANDO VIDEO, \n ")
    

    sp.Popen(r"ffmpeg -y -f v4l2 -r 30.000030 -s 720x480  -rtbufsize 300M -i /dev/video0 /home/emmanuel/Escritorio/git/video/muestra.mp4", shell=True)
    time.sleep(30)
    print ("OTORGANDO PERMISOS, \n ")
    sp.Popen(r"chmod 777 /home/emmanuel/Escritorio/git/video/muestra.mp4", shell=True)
    print ("ENVIANDO CTRL+C, \n ")
    sp.Popen(r"killall ffmpeg", shell=True)
    time.sleep(10)
captura_video()

def captura_frames():
    print ("CAPTURANDO FOTOGRAMAS, \n ")
    sp.Popen(r"ffmpeg -ss 00:00:25 -t 00:00:00.04 -i /home/emmanuel/Escritorio/git/video/muestra.mp4 -r 30.000030 /home/emmanuel/Escritorio/git/video/captura_frames/frame%4d.png", shell=True)
    time.sleep(5)
    print ("OTORGANDO PERMISOS, \n ")
    sp.Popen(r"chmod 777 -R /home/emmanuel/Escritorio/git/video/captura_frames", shell=True)    
captura_frames()

def video_integridad():
    print ("VALIDANDO INTEGRIDAD, \n ")
    sp.Popen(r"ffmpeg -v debug -i /home/emmanuel/Escritorio/git/video/muestra.mp4 -f null - > /home/emmanuel/Escritorio/git/video/log.txt 2>&1", shell=True)
    time.sleep(5)
    print ("OTORGANDO PERMISOS, \n ")
    sp.Popen(r"chmod 777 /home/emmanuel/Escritorio/git/video/log.txt", shell=True)    
video_integridad()


