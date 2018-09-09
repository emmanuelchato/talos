import subprocess
import time
from win32 import win32api
import win32con

p = subprocess.Popen(r'E:\ALPHA\TALOS\ffmpeg\bin\ffmpeg -ss 00:00:25 -t 00:00:00.04 -i E:\ALPHA\TALOS\captura_video\muestra.mp4 -r 30.000030 E:\ALPHA\TALOS\captura_frames\frame%4d.png')
time.sleep(20)
print ("ENVIANDO CTRL+C")
print ("FINALIZANDO CAPTURAS DE FRAMES")
try:
    win32api.GenerateConsoleCtrlEvent(win32con.CTRL_C_EVENT, 0)
    p.wait()
except KeyboardInterrupt:
    print ("CAPTURA FINALIZADA COMPARE VERSION DE FW")