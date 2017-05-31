# ----------------------------------------------
# khan_academy.py 
# ----------------------------------------------


import requests
import json
from bs4 import BeautifulSoup
import csv


if __name__ == "__main__":

# ----------------------------------------------
# loading json file using curl --user 
# ----------------------------------------------

	d = open('khan.json', 'r')
	data = json.load(d)
	d.close()

# ----------------------------------------------
# writing header and other attributes 
# ----------------------------------------------

	with open('khan.csv', 'a') as f:

		writer = csv.DictWriter(f, fieldnames = ['title', 'subject', 'interal_id', 'url', 'id_number', 'description'])
		writer.writeheader()
		
		for i in range(len(data['children'])):
			title = data['children'][i]['title']
			title = title.strip().replace(':', '')
			title = title.strip().replace(',', '')
			subject = data['translated_title']
			internal_id = data['children'][i]['internal_id']
			internal_id = internal_id.strip().replace(',', ' ')
			id_number = data['children'][i]['node_slug']
			url = data['children'][i]['url']
			description = data['children'][i]['description']
			description = description.strip().replace(',', ' ')
			description = description.strip().replace('\n', ' ')	

			f.write(title + ',' + subject + ',' + internal_id + ',' + 
			url + ',' + id_number + ',' + description + '\n')


