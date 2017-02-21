#/usr/bin/env python3
#-*- coding:utf-8 -*-

import pymysql
def nginx_analyse():
	db = pymysql.connect('localhost','root','123456','cmdb')
	cursor = db.cursor()
	cursor.execute("truncate table cmdb_nginxlog")

	f = open('/nginx/logs/access.log')
	res = {}
	for l in f:
		arr = l.split(' ')
		ip = arr[0]
		url = arr[6]
		status = arr[8]
		res[(ip,url,status)] = res.get((ip,url,status),0)+1
	#res 是字典，python3字典没有iteritems()，所以先转换成列表,再用sorted根据最后一个参数进行排序
	res_list = [(k[0],k[1],k[2],v) for k,v in res.items()]
	for k in sorted(res_list,key=lambda x:x[3],reverse=True)[:10]:
	#	print(k)
		sql = " INSERT INTO cmdb_nginxlog(access_ip,access_url,status,num) VALUES('%s','%s','%s','%s');"%(k[0],k[1],k[2],k[3])
	#	print(sql)
		try:
			cursor.execute(sql)
			db.commit()
		except:
			db.rollback()
	cursor.execute("SELECT * FROM cmdb.cmdb_nginxlog")
	result = cursor.fetchall()
	#print(result)
	db.close()
