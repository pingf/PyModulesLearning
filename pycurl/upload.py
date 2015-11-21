import pycurl

c = pycurl.Curl()
c.setopt(c.URL, 'http://127.0.0.1:5000/')
c.setopt(c.HTTPPOST, [
    ('fileupload', (
        # upload the contents of this file
        c.FORM_FILE, 'a.txt',
        # # specify a different file name for the upload
        c.FORM_FILENAME, 'b.txt',
        # # specify a different content type
        c.FORM_CONTENTTYPE, 'text/html',
    )),
])

c.perform()
c.close()
