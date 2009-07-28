from urllib2   import urlopen
from datetime  import datetime
from suds.client import Client

class JiraAttachment(object):
    fields = ('filename', 'filesize', 'mimetype', 'author', 'created', 'id')
    default_base_url = 'http://issues.apache.org/jira/secure/attachment/'
    
    def __init__(self, attachment, base_url=default_base_url):
        for k in self.fields:
            setattr(self, k, attachment[k])
        self.base_url = base_url
        
        # Convert 'created' tuple to a proper datetime object
        if isinstance(self.created, tuple):
            self.created = datetime(*[int(i) for i in self.created])
            
    def get_download_url(self):
        return "%s/%s/%s" % (self.base_url.rstrip('/'), self.id, self.filename)
    
    def get_attached_file(self):
        return urlopen(self.get_download_url())

class JiraClient(object):
    default_base_url = 'https://issues.apache.org/jira'
    
    def __init__(self, user, passwd, url=default_base_url):
        self.user = user
        self.passwd = passwd
        self.url = url.rstrip("/")
        self.token, self.client = None, None
        self.__connect()
    
    def __connect(self):
        url = self.url + "/rpc/soap/jirasoapservice-v2?wsdl"
        self.client = Client(url)
        self.token = self.client.service.login(self.user, self.passwd)
        
    def get_attachments(self, issue):
        resultset = []
        for a in self.client.service.getAttachmentsFromIssue(self.token, issue.upper())[0]:
            resultset.append(JiraAttachment(a))
        return resultset

def formatted_attachment_list(attachments):
    """
    Given a list of JiraAttachment instances, formats and prints the 
    attachment metadata to stdout.
    """
    counter = 1
    for a in attachments:
        print "-" * 80
        print "%-10s: %d" % ("ID No.", counter)
        print "%-10s: %s (%s)" % ('Filename', a.filename, a.mimetype)
        print "%-10s: %s" % ('Author', a.author)
        print "%-10s: %s" % ('Created', a.created)
        print "%-10s: %s bytes" % ('Size', a.filesize)
        counter += 1
    print "-" * 80

def parse_patch_ids(ids):
    # This is a little naive but OK for now
    return ids.replace(',', ' ').split()
 
# vi:ai sw=4 ts=4 tw=0 et:
