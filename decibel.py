import urllib2,urllib,time,datetime
timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d %H:%M:%S')
headers = {'DecibelAppID': 'a644dcab',
           'DecibelAppKey': 'a6ada2663a63a6c3e2f29054408ac59d',
           'DecibelTimestamp': timestamp,
           'Accept': 'application/xml'}
#url = 'https://rest.decibel.net/v3/Albums/?artists=Pink%20Floyd&depth=Recordings'
#url = 'https://rest.decibel.net/v3/Artists/?name=Pink%20Floyd'
url = 'https://rest.decibel.net/v3/Albums/?title=Blood%20on%20the%20tracks&depth=ArtistDetails'
req = urllib2.Request(url, None, headers)
resp = urllib2.urlopen(req).read()
