import pycurl

c = pycurl.Curl()
c.setopt(pycurl.URL, "http://localhost:8000")
c.setopt(pycurl.HTTPPOST, [('foo', 'bar')])
c.setopt(pycurl.CUSTOMREQUEST, "PUT")
c.perform()
c.close()