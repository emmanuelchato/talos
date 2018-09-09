import subprocess
import time
from win32 import win32api
import win32con

p = subprocess.Popen(r'E:\ALPHA\TALOS\ffmpeg\bin\ffmpeg -y -f vfwcap -r 30.000030 -s 720x480 -rtbufsize 100M -i 0 E:\ALPHA\TALOS\captura_video\muestra.mp4')
time.sleep(120)
print ("ENVIANDO CTRL+C")
print ("FINALIZANDO CAPTURA DE VIDEO")
try:
    win32api.GenerateConsoleCtrlEvent(win32con.CTRL_C_EVENT, 0)
    p.wait()
except KeyboardInterrupt:
     print ("VIDEO GUARDADO EXTRAIGA FRAMES")