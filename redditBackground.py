import urllib.request
import json
import random
import os
import sys
import ctypes

subreddits = ['/r/EarthPorn/top.json?limit=5', "/r/CityPorn/top.json?limit=5", "/r/wallpapers/top.json?limit=5", "/r/cats/top.json?limit=5"]
#Must change store_images path to one on PC
store_images = ['/home/joey/redditImages/redditWallpaper']
image_urls = []

def getImage( post ):
    return post[ 'data' ][ 'url' ]

def checkValidity( image_url ):
    if image_url.endswith( 'jpg' ):
            return True
    return False

print( "Now Finding Wallpapers. . .")
try:
    for s in subreddits:
        f = urllib.request.urlopen( "https://www.reddit.com" + s )
        data = f.read()
        r = data.decode( encoding = "utf-8" )
        readable = json.loads( r )
        posts = readable['data']['children']

        image_urls += list(filter( checkValidity, list( map( getImage, posts) ) ) )
except:
    num = len( image_urls )
    if num != 0:
        print( "Reddit is mad about all the requests so we have to stop looking, it's okay though we still have " + str(num) + " wallpapers to choose from!" )
    else:
        print( "Reddit got mad about all the requests and kicked us out, try again in one second, sorry about that :(")
        sys.exit()


    
print( "Now Deciding on the Wallpaper. . ." )
rand_urls = random.sample( image_urls, len(store_images) )
for rand_url, store_image in zip( rand_urls, store_images ):
    urllib.request.urlretrieve( rand_url, store_image+".jpg" )
print( "Setting Wallpaper. . . " )
#Must change ending path to one on your pc
if( os.name == "nt" ):
    print("here")
    ctypes.windll.user32.SystemParametersInfoW(20, 0, "C:/home/joey/redditImages/redditWallpaper.jpg", 3)
else:   
    os.system("/usr/bin/gsettings set org.gnome.desktop.background picture-uri /home/joey/redditImages/redditWallpaper.jpg" )
    
print( "Complete!" )
