#!/usr/bin/env python3
import pymysql.cursors
import datetime
from datetime import timedelta

connection = pymysql.connect(host='localhost', port=1433 ,user='root', password='Free4lamas', db='scrapy', charset='utf8mb4',  cursorclass=pymysql.cursors.DictCursor)

try:
	with connection.cursor() as cursor:
        # Read a single record
		models = ["Trexx", "Wolfer", "Morxes%sport", "Kickbike%race%28"]
		today = datetime.date.today()
		yesterday = datetime.date.today() - timedelta(days=1)
		week_old = datetime.date.today() - timedelta(days=7)
		print(today, yesterday, week_old)
		for model in models:
			sql = "select %s as model,\
				(select min(cena) from kolobezky where model like %s and datum > %s and datum < %s limit 1) as min, \
				max(cena) as max, \
				(select min(cena) from kolobezky where model like %s and cas = %s) as today_min, \
				(select eshop from kolobezky where model like %s and cas = %s and cena = (select min(cena) where model like %s and cas = %s limit 1) limit 1) as today_min_eshop \
				from kolobezky where model like %s"
			cursor.execute(sql, (model ,"%"+model+"%", week_old, yesterday,"%"+model+"%", today, "%"+model+"%", today, "%"+model+"%", today, "%"+model+"%"))
			result = cursor.fetchone()
			print("Model: " + result['model'].replace("%", " ") + "\n" + \
			      "Weekly minimum: " + str(result['min']) + "\n" + \
                              "Weekly maximum: " + str(result['max']) + "\n"+ \
                              "Today's minimum: "  + str(result['today_min']) + "\n" + \
                              "E-shop: " + result['today_min_eshop'] + "\n")
			if int(result['today_min']) < int(result['min']):
				print("we have a winner!")


finally:
	connection.close()
