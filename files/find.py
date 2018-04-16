# -*- coding: utf-8 -*-

import os,re,sys,time,shutil

count = 0
start = time.time()
txtfile = "list.txt"
rootdir = os.getcwd()+"\\"
sourcedir = "source\\"
resultdir = "result\\"
typelist = ['self','home','friend']
typedict = {'self':{'index':0, 'name':'self'}, 'home':{'index':1, 'name':'home'}, 'friend': {'index': 2, 'name':'friend'}}

print(rootdir)
# input_str = 'self'
input_str = input('please input handle type:')
if input_str not in typelist:
	print("输入错误，只支持输入3种类型，如：'self','home','friend'")
	time.sleep(3)
	exit(0)#无错误退出,1为有错误退出

itype = typedict[input_str]
print(itype)

# 查找文件
def search(path,word):
	for filename in os.listdir(path):
		# re_filename = re.findall('.\w+', str(filename))#去除文件后缀名
		# if word in re_filename[0]:
		if word in filename:
			# print(re_filename[0])
			# print(word+'=>'+filename)
			return filename

# 创建文件夹
def mkdir(path):
	folder = os.path.exists(path)
	if not folder:
		os.makedirs(path)
		return True
	else:
		return True

# 倒计时
def time_remain(mins):
	count1 = 0
	length = len(str(mins))
	sys.stdout.write(" " * length,)
	while (count1 < mins):
		count1 += 1
		n = mins - count1
		time.sleep(1)
		sys.stdout.write(('\b' * length) + str(n),)
		sys.stdout.flush()
		if not n:
			return 'completed'


# 根据文件内容进行查找拷贝
file = open(rootdir+txtfile,'r')
while 1:
	lines = file.readlines(10000)
	if not lines:
		break
	# print(lines)
	for line in lines:
		# print(line)
		string = line.split( )
		# print(string)
		istring = string[itype['index']]
		result = search(rootdir+sourcedir,istring)
		if result:
			print("符合条件的手机号:"+istring)
			newdir = rootdir+resultdir+istring+"\\"+itype['name']+"-"+istring
			re = mkdir(newdir)
			if re==False:
				print('创建目录失败:'+newdir)
				pass

			oldname = rootdir+sourcedir+"\\"+result
			newname = newdir+result
			shutil.copyfile(oldname,newname)
			count += 1
			# print('源：'+oldname+'，新'+newname)
file.close()


end = time.time()
c = end - start
print("共找到 %d 个文件"%count)
print('程序运行耗时：%0.2f'%(c)+'秒，8秒后自动退出')
time_remain(8)
