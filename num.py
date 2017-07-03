#!/usr/bin/python
import subprocess, re
PIPE = subprocess.PIPE
keyboard = subprocess.check_output(['skb', '-now']).strip()
keyboard = str(keyboard)
if keyboard == 'b\'Eng\'':
	print ("${image USA.png -p 145,755 -s 80x60 }") # -p - положение в коньках, -s размер картинки
else:
	print ("${image RUS.png -p 145,755 -s 80x60 }")
#---------------------------------------------
num = subprocess.Popen("xsetleds -show |awk '{print $6}'|tr -d '\n'", stderr=None, stdout=PIPE, shell=PIPE)
num = str(num.stdout.read())
if num == 'b\'on\'':
	print ("${image num-on.png -p 158,820 -s 60x20 }")
else:
	print ("${image num-off.png -p 158,820 -s 60x20 }")
#---------------------------------------------
caps = subprocess.Popen("xsetleds -show |awk '{print $4}'|tr -d '\n'", stderr=None, stdout=PIPE, shell=PIPE)
caps = str(caps.stdout.read())
if caps == 'b\'on\'':
	print ("${image caps-on.png -p 153,850 -s 70x20 }")
else:
	print ("${image caps-off.png -p 153,850 -s 70x20 }")

