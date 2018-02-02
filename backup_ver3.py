#备份文件版本三
import os
import time

source = [r'F:\wallpaper']

target_dir = r'D:\wallpaper' + os.sep

today = target_dir + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

#用户对压缩文件做注释
comment = input('Enter a comment:')
if len(comment) == 0:
	target = today + os.sep + now
else:
	target = today + os.sep + now + '_' +\
	comment.replace(' ','_')


if not os.path.exists(today):
	os.mkdir(today)
	print('successfully created directory',today)

#执行备份
rar_command = "rar a %s %s"%(target,''.join(source))

if os.system(rar_command) == 0:
	print('Successful back up to',target)
else:
	print('Backup Falled')