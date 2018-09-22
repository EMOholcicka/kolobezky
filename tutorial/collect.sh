#!/bin/bash

IFS=$'\n'
date=$(date +%Y-%m-%d)

cd /scrapy/tutorial

###run spiders###
for spider in AlzaCZ KolobkyCZ SvetkolobezekCZ; do
	rm data/$date.json 2>/dev/null
	/usr/local/bin/scrapy crawl $spider -o ./data/$date.json && sed -i "s/,-//g" ./data/$date.json &&./collect_process.py
done


