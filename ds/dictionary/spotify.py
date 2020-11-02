import time

playlist = []

playlist.append({
    'songName': 'kho Gaye Hum kahan',
    'singerName': 'Jasleen Royal',
    'duration': time.time(),
    'isSingerFemale': True,

})

playlist.append({
    'songName': 'Sang Rahiyo',
    'singerName': ['Jasleen Royal', 'Ranveer Allahbadia'],
    'duration': time.time(),
    'isSingerFemale': None,

})

my_playlist = {
    'title': 'Romantic Mood and Soothing',
    'author': 'Tejas Sabunkar',
    'playlist': playlist
}

print(my_playlist)

# Iterate over the object/dictionary
print('_____')
for item_key, item_value in my_playlist.items():
    print(item_key, '::', item_value)

# Iterate over the Array/list
print('_____')
for item in my_playlist['playlist']:
    print(item['singerName'])
