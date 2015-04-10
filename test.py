import urllib2  
response = urllib2.urlopen('http://tar2.telenav.com/repository/telenav/Autobahn/Autobahn/1.0.280/')  
html = response.read()  
print html
