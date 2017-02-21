from django.shortcuts import render,render_to_response
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect,Http404
from django.core.urlresolvers import reverse
from .nginx_log import *
from .models import User,ServerList,NginxLog
import json
import os
# Create your views here.

def login(request):
	'''
	这里定义了一个登陆视图

	'''
	if request.method != 'POST':
		return render(request,"cmdb/login.html")
	else:
		login_name = request.POST['login_name']
		login_passwd = request.POST['login_passwd']
		print(login_name)
		i = 1
		while i <= len(User.objects.all()):
			if login_name == User.objects.get(id=i).login_name and login_passwd == User.objects.get(id=i).login_passwd:
				return HttpResponseRedirect(reverse('cmdb:index'))
				#return render(request,'cmdb/index.html')
				break
			else:
				while i == len(User.objects.all()):
					return HttpResponseRedirect(reverse('cmdb:login'))
				i += 1

def logout(request):
	"""
	注销视图，点击注销就返回到登陆页面
	"""
	return HttpResponseRedirect(reverse('cmdb:login'))


def index(request):
	'''
	这是首页，也是仪表盘显示页
	'''
	nginx_analyse()
	access = NginxLog.objects.all()
	
	return render(request,'cmdb/index.html',{'access':access})

def server_info(request):
	'''
	服务器列表
	'''
	server_list = ServerList.objects.all()
	context = {"server_list":server_list}
	return render(request,'cmdb/server_info.html',context)

def del_server(request,*args):
	'''
		删除服务器
	'''
	del_id = request.POST['del_id']
	print(del_id)
	ServerList.objects.all().filter(id=del_id).delete()
	return HttpResponseRedirect(reverse('cmdb:index'))

def add_server(request,*args):
	'''
        增加服务器
    '''
	add_host = request.POST['add_host']
	add_os = request.POST['add_os']
	add_puip = request.POST['add_puip']
	add_inip = request.POST['add_inip']
	add_cpu = request.POST['add_cpu']
	add_memory = request.POST['add_memory']
	add_disk = request.POST['add_disk']
	add_soft = request.POST['add_soft']
	print(add_host,add_os,add_puip,add_cpu)

	add_server = ServerList(host_name=add_host,os=add_os,public_ip=add_puip,intranet_ip=add_inip,cpu_num=add_cpu,memory_size=add_memory,disk_size=add_disk,installed_software=add_soft)
	add_server.save()
#	return HttpResponseRedirect(reverse('cmdb:server_info'))
	return HttpResponseRedirect('/server_info/')


def execute_cmd(request):
	return render(request,'cmdb/execute_cmd.html')

def cmd_result(request,*args):
	'''
	命令执行的返回结果
	'''
	host = request.POST['host']
	cmd = request.POST['cmd']
	print(host,cmd)
	result = os.popen(cmd)
	text = result.read()
	result.close()
	print(text)
	text = {'text':text}
	return JsonResponse(text)

