import os
import requests
import json

baseUrl = 'http://data.re-publica.de/api/'
speaker_nodes = []
speaker_edges = []
if 'MORPH_EVENTID' in os.environ: 
  eventId = os.environ['MORPH_EVENTID']
else:
  print 'Please add the ID of the event you want to analyze with the name "MORPH_EVENTIF" to the morph.io settings of this scraper'
  print 'See http://data.re-publica.de/doc/ to find supported events'
  
#make nodes
print 'nodedef>name VARCHAR,label VARCHAR'
response = requests.get(baseUrl+eventId+'/speakers').content
speakers = json.loads(response)
for speaker in speakers['data']:
  print speaker['id']+','+speaker['name'].encode('ascii', 'replace')

#make edges
print 'edgedef>node1 VARCHAR,node2 VARCHAR,label VARCHAR'
response = requests.get(baseUrl+eventId+'/sessions').content
sessions = json.loads(response)
for session in sessions['data']:
  if len(session['speakers']) > 1:
    for i, speaker in enumerate(session['speakers']):
      for y in range (i, len(session['speakers'])-1):
        print session['speakers'][i]['id']+','+session['speakers'][y+1]['id']+','+session['title'].encode('ascii', 'replace')

quit()
