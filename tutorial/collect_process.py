#!/usr/bin/env python
# -*- coding: utf-8 -*-r

import json
import datetime
import mysql.connector as mariadb
import unidecode

user = 'root'
password = 'Free4lamas'
database = 'scrapy'

today = datetime.datetime.today().strftime('%Y-%m-%d')
path = "data/" + today + ".json"

with open(path) as json_data:
	data = json.load(json_data)
	mariadb_connection = mariadb.connect(user=user, password=password, database=database, port=1433)
	cursor = mariadb_connection.cursor()
	for item in data:
		model = unidecode.unidecode(item[u'name']).replace("Kolobezka ", "")  
		cursor.execute("INSERT INTO kolobezky (cas, eshop, model, cena) VALUES (%s,%s,%s,%s)", (item[u'date'], item[u'eshop'], model, item[u'price']))
	mariadb_connection.commit()
	mariadb_connection.close()		
