import urllib.parse
import urllib.request
import json

URL_BASE = 'https://commons.wikimedia.org/w/api.php?'

def get_flag_image_url(country_dict):
    parameters = (('action', 'query'), ('titles', 'File:' + country_dict['国旗画像']), ('prop', 'imageinfo'), ('iiprop', 'url'), ('format', 'json'))
    url = URL_BASE + urllib.parse.urlencode(parameters)
    json_object = json.loads(urllib.request.urlopen(url).read().decode('utf-8'))
    pages = json_object['query']['pages']
    return pages[list(pages.keys())[0]]['imageinfo'][0]['url']
