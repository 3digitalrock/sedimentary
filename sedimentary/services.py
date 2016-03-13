import config
import requests
import rethinkdb as r
from rethinkdb.errors import RqlRuntimeError, RqlDriverError


def get_channels():
    url = config.API_BASE+'channels'
    r = requests.get(url)
    channels = r.json()
    channels_list = channels['items']
    return channels_list

def get_channelvideos(channel):
    url = config.API_BASE+'channels/'+channel+'/videos?limit=10&fields=uid,title,slug,thumbnails'
    r = requests.get(url)
    videos = r.json()
    videos_list = videos['items']
    return videos_list

def get_trailers(playlist):
    rdb_conn = r.connect(host=config.DB_HOST, port=config.DB_PORT, db=config.ENV+"_web")
    cursor = r.table("featured").filter(r.row["playlists"].contains(playlist)).order_by('order').eq_join('uid', r.db('production_api').table('trailers')).zip().pluck('uid','title','files','thumbnails').run(rdb_conn)
    
    trailers = []
    for trailer in cursor:
        trailers.append(trailer)
        
    return trailers