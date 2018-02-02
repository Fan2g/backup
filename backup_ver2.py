#备份文件版本二
import os
import time

source = [r'F:\wallpaper',r'F:\tools']

target_dir = r'D:\wallpaper' + os.sep

today = target_dir + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

if not os.path.exists(today):
	os.mkdir(today)
	print('successfully created directory',today)

target = today + os.sep + now

rar_command = "rar a %s %s"%(target,' '.join(source))

if os.system(rar_command) == 0:
	print('Successful back up to',target)
else:
	print('Backup Falled')