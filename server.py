import cherrypy
import os.path
import time
import subprocess
from os import listdir
from jinja2 import Template
import sys


def load_template(path):
    with open(path, 'r') as f:
        return Template(f.read())

def display_photos(path):
	photos = [os.path.join(path, f) for f in listdir(path) if os.path.isfile(os.path.join(path, f))]
	return subprocess.Popen(['feh','-D','3','-F','--zoom','max'] + photos)


# Terminates the process responsible for displaying photos
def terminate_photos(popen):
	popen.terminate()

def test():
	pass

class PhotoFrame:
        album_photos = None

        @cherrypy.expose
        def index(self, album=None):
            username = "Ben"
            output = load_template("./templates/index.html")
            
            if album != None:
                album_display = os.path.join(album_path, album)
                print(album_display)
                
                if self.album_photos != None:
                        # Kill the running album
                        terminate_photos(self.album_photos)
                        print("test")
                        self.album_photos = display_photos(album_display)
                else:
                        self.album_photos = display_photos(album_display)


            album_list = listdir(album_path)
            print(album_list)

            return output.render(username=username, album_list=album_list) 




if __name__ == '__main__':
	if len(sys.argv) == 1:
		print("You must supply the album location.")
		sys.exit()
	else:
		album_path = sys.argv[1]

	cherrypy.server.socket_host = 'localhost'
	configfile = os.path.join(os.path.dirname(__file__),'server.conf')
	cherrypy.quickstart(PhotoFrame(),config=configfile)
