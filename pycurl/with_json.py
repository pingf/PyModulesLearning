import pycurl
from io import BytesIO
import json

# this example is tested with elasticsearch
c = pycurl.Curl()
c.setopt(c.URL, 'http://localhost:9200/customer/external/1')
header = BytesIO()
data = BytesIO()
c.setopt(c.WRITEHEADER, header)
c.setopt(c.WRITEDATA, data)
c.perform()
print(header.getvalue())
response = data.getvalue().decode('utf-8')
c.close()
result = json.loads(response)
print(json.dumps(result, indent=4))
