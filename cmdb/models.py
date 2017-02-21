from django.db import models

# Create your models here.

class User(models.Model):
	'''
	用户名密码
	'''
	login_name = models.CharField(max_length=20,verbose_name='用户名')
	login_passwd = models.CharField(max_length=30,verbose_name='密码')
	
	class Meta:
		verbose_name_plural = "账号"
	def __str__(self):
		return self.login_name

class ServerList(models.Model):
	'''
	服务器列表
	'''
	host_name = models.CharField(max_length=100, verbose_name='主机名')
	os = models.CharField(max_length=100, verbose_name='操作系统')
	public_ip = models.CharField(max_length=100, verbose_name='公网IP')
	intranet_ip = models.CharField(max_length=100, verbose_name='内网IP')
	cpu_num = models.CharField(max_length=100, verbose_name='CPU个数')
	memory_size = models.CharField(max_length=50, verbose_name='内存')
	disk_size = models.CharField(max_length=50, verbose_name='磁盘')
	installed_software = models.CharField(max_length=100,verbose_name='已安装软件')

	class Meta:
		verbose_name_plural = '服务器列表'
	def __str__(self):
		return self.host_name

class NginxLog(models.Model):
	'''
	nginx 访问日志 前十
	'''
	access_ip = models.CharField(max_length=100, verbose_name='请求IP')
	access_url = models.CharField(max_length=100, verbose_name='请求url')
	status = models.CharField(max_length=100, verbose_name='状态')
	num = models.CharField(max_length=100, verbose_name='请求次数')

	class Meta:
		verbose_name_plural = 'nginx访问日志'
	def __str__(self):
		return self.host_name

class Host(models.Model):
    hostname = models.CharField(max_length=128,unique=True)
    key = models.TextField()
    status_choices = ((0,'Waiting Approval'),
                      (1,'Accepted'),
                      (2,'Rejected'))


    os_type_choices =(
        ('redhat','Redhat\CentOS'),
        ('ubuntu','Ubuntu'),
        ('suse','Suse'),
        ('windows','Windows'),
    )

    os_type = models.CharField(choices=os_type_choices,max_length=64,default='redhat')
    status = models.SmallIntegerField(choices=status_choices,default=0)

    def __str__(self):
        return self.hostname
class HostGroup(models.Model):
    name =  models.CharField(max_length=64,unique=True)
    hosts = models.ManyToManyField(Host,blank=True)

    def __str__(self):
        return self.name
