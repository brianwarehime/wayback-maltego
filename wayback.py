from MaltegoTransform import *
import requests
import json

me = MaltegoTransform()
me.parseArguments(sys.argv)
url = sys.argv[1]

base = 'http://archive.org/wayback/available?url='

r = requests.get(base+url, verify=False)
j = json.loads(r.text)

if j['archived_snapshots'] == {}:
	pass
else:
	ent = me.addEntity("maltego.Website",j['archived_snapshots']['closest']['url'])

me.returnOutput()
