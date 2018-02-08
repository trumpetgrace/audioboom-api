import requests
import json
import sys
import csv


username = 'radio-x'
per_page = 100
page = 1
count = 0
asking = True

def get_booms(p, asking):
    global count
    r = requests.get("http://api.audioboom.com/users/185399/audio_clips.json")
    response = r.text
    parsed_json = r.json()
    body = parsed_json['body']
    totals = body['totals']
    if p == 1:
        print ('user: '+ username + ' -total: ' + str(totals['count']))
        print ('')
    for clip in body['audio_clips']:
        print ('-----------------------------------------------')
        mp3_url = clip['urls']['high_mp3']
        print ('TITLE   : ' + clip['title'])
        print ('mp3 url : ' + mp3_url)
        naming = mp3_url.split('/')
        mp3_name = naming[-1]
        name = mp3_name.split('mp3')
        json_name = name[0] + '.json'
        print ('mp3 name: ' + mp3_name)
        count = count + 1
    if count < totals['count']:
        get_booms(p + 1, asking)
    while asking:
        choice = raw_input("Please choose the podcast you would like to keep: ")
        for clip in body['audio_clips']:
            if choice == clip['title']:
                print ('-----------------------------------------------')
                mp3_url = clip['urls']['high_mp3']
                print ('TITLE   : ' + clip['title'])
                print ('mp3 url : ' + mp3_url)
                naming = mp3_url.split('/')
                mp3_name = naming[-1]
                name = mp3_name.split('mp3')
                json_name = name[0] + '.json'
                print ('mp3 name: ' + mp3_name)
                with open(json_name, 'w') as outfile:
                    json.dump(clip, outfile)
                    print('writing JSON file: ' + json_name)
                asking = False


print('===== ArchiveBoom =============================')
get_booms(page, asking)
print('ALL DONE!')
print('')
