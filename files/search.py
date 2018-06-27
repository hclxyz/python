# -*- coding: utf-8 -*-

import os,re,sys,time,shutil

count = 0
counter = 1
start = time.time()
txtfile = "list.txt"
rootdir = os.getcwd()+"\\"
sourcedir = "source\\"
resultdir = "result\\"
typelist = ['self','home','friend']
typedict = {'self':{'index':0, 'name':'self'}, 'home':{'index':1, 'name':'home'}, 'friend': {'index': 2, 'name':'friend'}}

# print(rootdir)
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

# 查找最新的序号
def find(path,word):
	if not(os.path.exists(resultsubdir)):
		print('目录为空:'+resultsubdir)
		return 1
	list2 = []
	lists = os.listdir(path)
	for list in lists:
		if word in list:
			list2.append(list)

	list3 = []
	for ll in list2:
		list3.append(int(ll.split(".")[0].split("-")[2]))

	if len(list3) :
		print(list3)
		return max(list3)+1
	else:
		print('列表为空:')
		return 1

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

#统计文件夹下的文件数量
def folder_count(path):
	count = 0
	if os.path.exists(path):
		print("目录："+path)
		for fn in os.listdir(path): #fn 表示的是文件名
			count = count + 1
	return count


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
		source = search(rootdir+sourcedir,istring)
		if source:
			print("符合条件的手机号:"+istring)
			# newdir = rootdir+resultdir+istring+"\\"+itype['name']+"-"+istring
			newdir = rootdir + resultdir + string[0]
			re = mkdir(newdir)
			if re==False:
				print('创建目录失败:'+newdir)
				pass

			oldname = rootdir+sourcedir+"\\"+source
			source = str(source)
			# print(type(source))
			# mobile = source.split('_cc')[0].split('_9')[1];
			# print(mobile)
			# number = folder_count(newdir)
			resultsubdir = rootdir+resultdir+string[0]
			if os.path.exists(resultsubdir):
				number = find(resultsubdir, istring)

			print("文件数量:"+str(number))
			# number = (number if (number) else 1)
			# print(rootdir+resultdir+istring+',number:'+str(number))
			newfilename = source[0:8]+'-'+istring+'-'+str(number)+'.mp3'
			print(source)
			# print(newfilename)
			newname = newdir+"\\"+newfilename
			shutil.copyfile(oldname,newname)
			count += 1
			# print('源：'+oldname+'，新'+newname)
file.close()


end = time.time()
c = end - start
print("共找到 %d 个文件"%count)
print('程序运行耗时：%0.2f'%(c)+'秒，8秒后自动退出')
time_remain(8)
