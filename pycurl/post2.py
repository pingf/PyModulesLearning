import pycurl
from io import BytesIO
header = BytesIO()
data = BytesIO()

try:
    # python 3
    from urllib.parse import urlencode
except ImportError:
    # python 2
    from urllib import urlencode

c = pycurl.Curl()
c.setopt(c.URL, 'http://127.0.0.1:5000/post_test')

c.setopt(pycurl.HTTPPOST, [('username', 'jesse')])
c.setopt(c.WRITEHEADER, header)
c.setopt(c.WRITEDATA, data)
c.setopt(c.FOLLOWLOCATION, True)
c.perform()
c.close()
print(header.getvalue())
print(data.getvalue())


