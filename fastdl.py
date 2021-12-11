from os.path import *
import socketserver
import http.server
import requests
import os
import bz2
import sys

print('Setting up fastdl directory')

try:
    if not isdir('../fastdl') or not isdir('../fastdl/maps'):
        if not isdir('../fastdl'):
            os.mkdir('../fastdl')
        if not isdir('../fastdl/maps'):
            os.mkdir('../fastdl/maps')
except Exception as ex:
    print(f'Failed to setup fastdl directories, this is critical:\n{ex}')
    print(f'Press ENTER to close this window.')
    sys.stdin.readline()
    exit(0)

print('Finished setting up fastdl directory')

print('Running map compression')

try:
    for file in [file for file in os.listdir(os.getcwd()) if isfile(join(os.getcwd(), file))]:
        # check if this is an actual map and if it hasn't been compressed before in order to save time
        if not file.endswith('.bsp'):
            continue
        if isfile(f'../fastdl/maps/{file}.bz2'):
            continue

        compressed = bz2.compress(open(file, 'rb').read(), 2)

        with open(f'../fastdl/maps/{file}.bz2', 'wb') as file:
            file.write(compressed)
            file.close()
except Exception as ex:
    print(f'Failed to setup fastdl directories, server will run regardless:\n{ex}')

print('Finished map compression')

IP = requests.get('https://v4.ident.me/').text
PORT = 8080
DIRECTORY = '../fastdl'

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

with socketserver.TCPServer(('', PORT), Handler) as http_server:
    print(f'Server live on {IP}:{PORT}')
    http_server.serve_forever()