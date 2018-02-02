#备份文件版本四
#将输入的路径下文件备份到相应路径下（文件名是当时日期）
#!/usr/bin/python
import os
import time

source = []

while True:
	all_source = input('please input file path:')
	source.append(all_source)
	flag = input('Do you want to continue add file path(1/0):')
	if int(flag)==0:
		break
		
		
		
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
rar_command = "rar a %s %s"%(target,' '.join(source))

if os.system(rar_command) == 0:
	print('Successful back up to',target)
else:
	print('Backup Falled')