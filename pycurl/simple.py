import pycurl
from io import BytesIO
c = pycurl.Curl()
c.setopt(c.URL,'http://www.baidu.com')
header = BytesIO()
data = BytesIO()
c.setopt(c.WRITEHEADER, header)
c.setopt(c.WRITEDATA, data)
c.perform()
print(header.getvalue())
print(data.getvalue())
c.close()

