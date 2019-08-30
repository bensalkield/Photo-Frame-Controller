import time
import subprocess
from os import listdir
from os.path import isfile, join

# Displays all photos in path on the screen
# Returns Popen for the image viewer
def display_photos(path):
    photos = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    return subprocess.Popen(['feh','-D','3','-F','--zoom','max'] + photos)


# Terminates the process responsible for displaying photos
def terminate_photos(popen):
    popen.terminate()





mypath = "/home/benjaminsalkield/programming/Photo frame"
album_photos = display_photos(mypath)
time.sleep(10)
terminate_photos(album_photos)



