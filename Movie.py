import time
import os

frameList = ['''
 \ /                                        
 (∞)                                    __/ /
 {()}                                  (____/
  ▼                                      U
 ''',
 '''


\ /
(x)
{()}
''']  
while True:
	os.system("cls")
	for frame in frameList:
		print(frame)
		time.sleep(.5)
		os.system("cls")