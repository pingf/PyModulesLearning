import pycurl
from asyncio import coroutine
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
c.setopt(c.URL, 'https://posttestserver.com/post.php')

post_data = {'field': 'value'}
# Form data must be provided already urlencoded.
postfields = urlencode(post_data)
# Sets request method to POST,
# Content-Type header to application/x-www-form-urlencoded
# and data to send in request body.
c.setopt(c.POSTFIELDS, postfields)
c.setopt(c.WRITEHEADER, header)
c.setopt(c.WRITEDATA, data)
c.perform()
c.close()
print(header.getvalue())
print(data.getvalue())


