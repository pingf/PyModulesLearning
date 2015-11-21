import pycurl
from io import BytesIO


try:
    # python 3
    from urllib.parse import urlencode
except ImportError:
    # python 2
    from urllib import urlencode

c = pycurl.Curl()
c.setopt(c.URL, 'http://127.0.0.1:5000/get_test' + '?' + urlencode({'user': 1}))
header = BytesIO()
data = BytesIO()
c.setopt(c.WRITEHEADER, header)
c.setopt(c.WRITEDATA, data)
c.perform()
print(header.getvalue())
print(data.getvalue())
c.close()
