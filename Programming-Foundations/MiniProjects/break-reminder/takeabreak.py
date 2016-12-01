import webbrowser
import time

breaks = 3
print('This program started on',time.ctime())
for i in range(breaks):
	time.sleep(1800)
	webbrowser.open("http://www.youtube.com/watch?v=dQw4w9WgXcQ")

