
from urllib2   import urlopen
from datetime  import datetime
from os.path   import join, expanduser, exists
import SOAPpy, getpass

USER_CONFIG = join(expanduser('~'), '.git-jira-tools')

class JiraAttachement(object):
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
        handle = urlopen(self.url + "/rpc/soap/jirasoapservice-v2?wsdl")
        self.client = SOAPpy.WSDL.Proxy(handle)
        self.token = self.client.login(self.user, self.passwd)
        
    def get_attachments(self, issue):
        resultset = []
        for a in self.client.getAttachmentsFromIssue(self.token, issue.upper()):
            resultset.append(JiraAttachement(a))
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

def get_user_config():
    """Parse a user settings file, return a dict result."""
    user_config = {}

    if exists(USER_CONFIG):
        try:
            f = open(USER_CONFIG, 'r')
            for ln in f.readlines():
                tokens = ln.split('=')
                if len(tokens) == 2:
                    user_config[tokens[0].strip()] = tokens[1].strip()
            f.close()
        except Exception, error:
            from sys import stderr
            print >>stderr, "Warning: unable to parse user config:", error
    
    return user_config

def get_username(user_config=None):
    if isinstance(user_config, dict) and user_config.has_key("username"):
        return user_config["username"]
    return getpass.getuser()

def get_password(user_config=None):
    if isinstance(user_config, dict) and user_config.has_key("password"):
        return user_config["password"]
    return getpass.getpass()
 
# vi:ai sw=4 ts=4 tw=0 et: