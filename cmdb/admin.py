from django.contrib import admin
from cmdb.models import User,ServerList,NginxLog,Host,HostGroup
# Register your models here.
admin.site.register(User)
admin.site.register(ServerList)
admin.site.register(NginxLog)
admin.site.register(Host)
admin.site.register(HostGroup)