from flickrapi import FlickrAPI
from urllib.request import urlretrieve
from pprint import pprint
import os,time,sys

#APIキーの情報
key = "3147ac69515f82ffcbcebdeb8dc64e53"
secret = "131abc3c798b15df"
wait_time = 1

#保存フォルダの指定
noodlename = sys.argv[1]
savedir = "./" + noodlename

flickr = FlickrAPI(key, secret, format='parsed-json')
result = flickr.photos.search(
    text = noodlename,
    per_page = 400,
    media = 'photos',
    sort = 'relevance',
    safe_search = 1,
    extras = 'url_q, licence'
)

photos = result['photos']
#pprint(photos)

for i, photo in enumerate(photos['photo']):
    url_q = photo['url_q']
    filepath = savedir + '/' + photo['id'] + '.jpg'
    if os.path.exists(filepath): continue
    urlretrieve(url_q,filepath)
    time.sleep(wait_time)
