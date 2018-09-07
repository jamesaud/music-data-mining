import requests
from pprint import pprint
import json

API = '54262b6457447cafa4023115f5562679'
SECRET = '7f16190e426a3b83cd6ac0850c12c0d9'

ROOT = 'http://ws.audioscrobbler.com/2.0/'
CHARTS = ROOT + f'?method=chart.gettoptracks&api_key={API}&format=json'

# MAIN
charts = requests.get(CHARTS)
content = json.loads(charts.content)
pprint(content)

