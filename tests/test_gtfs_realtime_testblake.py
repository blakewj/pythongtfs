from google.transit import gtfs_realtime_pb2
import os.path
import requests
url = 'https://api.transport.nsw.gov.au/v1/gtfs/vehiclepos/sydneytrains?key=kyKR5nC5rihOjiI3MGdHPUYz99HzyL1LVUvN'

headers = {'content-type': 'application/x-google-protobuf', 'Accept-Charset': 'UTF-8', 'Authorization': 'apikey kyKR5nC5rihOjiI3MGdHPUYz99HzyL1LVUvN'}

response = requests.get(url, data=url, headers=headers)





feed = gtfs_realtime_pb2.FeedMessage()
print(feed.ParseFromString(response.content))


for entity in feed.entity:
  if entity.HasField('vehicle'):
    print (entity.vehicle)
    
'''
example feed trip

trip {
  trip_id: "NonTimetabled.T289"
  schedule_relationship: SCHEDULED
}
position {
  latitude: -33.914825439453125
  longitude: 151.15785217285156
}
timestamp: 1533793320
congestion_level: UNKNOWN_CONGESTION_LEVEL
stop_id: "Sydenham.CR713 Entry LOC"
vehicle {
  id: "CR713 Entry LOC"


'''
