#!/usr/bin/env python
# -*- coding: utf-8 -*-


# ----------------------------------------------
# khan_academy_video.py 
# ----------------------------------------------


import requests
import json
import csv
import pandas as pd 


# ----------------------------------------------
# need khan.csv to start iterating 
# on the column called "id"
# id is basically like "child" node of a DAG 
# in this case, Khan Academy used DAG to 
# organize their data
# so math => arithmetic => arith-review-add-subtract
# => basic-addition => videos 
# ----------------------------------------------


if __name__ == "__main__":

	khan_academy_csv = pd.read_csv('/Users/michaelchon/Documents/Github/Personal_Github/Khan_Academy/khan.csv')
	data_frame = khan_academy_csv[['title', 'id_number']]

	with open('khan_academy_video.csv', 'a') as f:
		f.write('title' + ',' + 'id_number' + ',' + 'relative_url' + ',' + 'mp4-low' + ',' + 'mp4' + ','
			+ 'mp4-low-ios' + ',' + 'youtube_url' + ',' + 'translated_description' + '\n')

# ----------------------------------------------
# looping thru the data_frame 
# ----------------------------------------------

		for i in range(len(data_frame)):

			id_number = data_frame['id_number'][i]
			title = data_frame['title'][i]
			url_base = "https://www.khanacademy.org/api/v1/topic/"
			url = "https://www.khanacademy.org/api/v1/topic/" + id_number

# ----------------------------------------------
# moving the children node of "id_number"
# loading the json of the url above
# ----------------------------------------------

			response = requests.get(url).content.decode()
			data = json.loads(response)

			data_children = data['children']

# ----------------------------------------------
# parsing the "children" key of the json 
# ----------------------------------------------

			node_list = []
			for i in range(len(data['children'])):
				node_list.append(data_children[i]['node_slug'])

# ----------------------------------------------
# finding the node_slugs of the "children" 
# ----------------------------------------------

			for i in range(len(node_list)):
				url_again = url_base + node_list[i]
				response_again = requests.get(url_again).content.decode()
				data_again = json.loads(response_again)
				data_children_again = data_again['children']

				video_list = []
				for i in range(len(data_children_again)):
					if data_children_again[i]['kind'] == "Video":
						video_list.append(data_children_again[i]['id'])

# ----------------------------------------------
# finally, reached at the leaves that contain
# video urls of "id_number" we started 
# ----------------------------------------------

				url_video = "https://www.khanacademy.org/api/v1/videos/"
				for i in range(len(video_list)):
					url_video_again = url_video + video_list[i]
					video_response = requests.get(url_video_again).content.decode()
					data_video = json.loads(video_response)

# ----------------------------------------------
# prasing the very last json by appropriate
# keys to obtain video urls
# ----------------------------------------------

					relative_url = data_video['relative_url']

					try: 
						mp4_low = data_video['download_urls']['mp4-low']
					except:
						mp4_low = ' '
					
					mp4 = data_video['download_urls']['mp4']
					
					try:
						mp4_low_ios = data_video['download_urls']['mp4-low-ios']
					except:
						mp4_low_ios = ' '

					youtube_url = data_video['url']
					
					try:
						description = data_video['translated_description']
						description = description.strip().replace(',', ' ')
						description = description.strip().replace('&nbsp', ' ')
						description = description.strip().replace('÷', '/')
						description = description.strip().replace('\n', ',')
					except:
						description = ' '

					f.write(title + ',' + id_number + ',' + relative_url + ',' + mp4_low + ',' + mp4 + ','
						+ mp4_low_ios + ',' + youtube_url + ',' + description + '\n')







