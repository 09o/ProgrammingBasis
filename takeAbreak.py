'''
设计一个程序每隔两个小时提醒一次，一共三次
'''
import time
import webbrowser

total_breaks = 3
break_count = 0

print("This program started on " + time.ctime())

while (break_count < total_breaks):
    time.sleep(2*60*60)
    webbrowser.open("https://www.youtube.com/watch?v=l1yPgCiJut0")
    break_count += 1
