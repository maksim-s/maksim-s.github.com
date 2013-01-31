import os, shutil
import Image
import requests
import json

INSTAGRAM_ACCESS_TOKEN = '11136145.1fb234f.5f7f4ffc3f03469eac5f5c5e4b2957da'
DROPBOX_PATH = '/Users/maksimus16/Dropbox/Public/photos'
DROPBOX_PUBLIC_LINK = 'https://dl.dropbox.com/u/4515918/photos'
JSON_FILE_PATH = (
    '/Users/maksimus16/Documents/sites/maksim-s.github.com/js/photoMosaic/files/data/photoMosaic.data.js')


def populate_json(json_file):
  """
  Get photos and thumbnails from dropbox and instagram.
  Populate the json file for photoMosaic:
  { 
    src: "https://dl.dropbox.com/u/4515918/photos/p6.jpg",
    thumb: "https://dl.dropbox.com/u/4515918/photos/thumbnails/p6.jpg",
    width: "640",
    height: "279"
  }
  """
  output = get_dropbox_photos(DROPBOX_PATH, DROPBOX_PUBLIC_LINK)
  output += get_instagram_photos(INSTAGRAM_ACCESS_TOKEN)
  f = open(json_file, 'w')
  f.write('var PMalbum = %s' % json.dumps(output))
  f.close()



def get_dropbox_photos(dropbox_path, public_link):
  """
  Returns a JSON of dropbox photos.
  """
  photos = os.listdir(dropbox_path)
  output = []
  if 'thumbnails' in photos:
    shutil.rmtree('%s/%s' % (dropbox_path, 'thumbnails'))
    photos.remove('thumbnails')
  os.mkdir('%s/%s/' % (dropbox_path, 'thumbnails'))
  for p in photos:
    if not p.endswith('.jpg') and not p.endswith('.jpeg'):
      continue
    img = Image.open('%s/%s' % (dropbox_path, p))
    width, height = img.size
    thumbnail_size = (width/2, height/2)
    img.thumbnail(thumbnail_size, Image.ANTIALIAS)
    img.save('%s/%s/%s' % (dropbox_path, 'thumbnails', p), 'JPEG')
    photo = { 
        'src'    : '%s/%s' % (public_link, p),
        'thumb'  : '%s/thumbnails/%s' % (public_link, p),
        'width'  : width / 2,
        'height' : height / 2,
        }
    output.append(photo)
  return output



def get_instagram_photos(access_token):
  """
  Returns a JSON of instagram photos
  """
  output = []
  my_media = (
      'https://api.instagram.com/v1/users/11136145/media/recent?access_token=%s&count=100' % access_token)
  r = requests.get(my_media)
  if r.status_code != 200:
    return output
  if 'data' not in r.json:
    return output
  data = r.json['data']
  for d in data:
    i = d['images']
    photo = {
        'src' : i['standard_resolution']['url'],
        'thumb' : i['low_resolution']['url'],
        'width' : i['low_resolution']['width'],
        'height' : i['low_resolution']['height']
        }
    output.append(photo)
  return output

populate_json(JSON_FILE_PATH)
  

