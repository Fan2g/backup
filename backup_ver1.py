#Filename:backup_ver1.py
import os 
import time

#需要备份的文件或目录
source =[r'F:\wallpaper']

#目标目录
target_dir = [r'D:\wallpaper\wallpapers']

#备份成压缩文件
target = ''.join(target_dir) 
# + time.strftime('%Y%m%d%H%M%S') + '.zip'

#压缩文件实现
rar_command = "rar a -ag -r  %s %s"%(target,''.join(source))

#运行备份
if os.system(rar_command)==0:
	print('Successful backup to',target)
else:
	print('Backup FAllED')