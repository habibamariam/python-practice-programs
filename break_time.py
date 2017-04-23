import webbrowser
import time

count = 0

while count <3:
    time.sleep(60*60*2)
    if count == 0:
        webbrowser.open("http://www.GOOGLE.com")
    if count == 1:
        webbrowser.open("http://www.yahoo.com")
    if count == 2:
        webbrowser.open("http://www.youtube.com")
    count=count+1         
