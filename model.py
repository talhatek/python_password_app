class Password(object):
    def __init__(self, site_name=None, user_name=None, password=None):
        self.site_name = site_name
        self.user_name = user_name
        self.password = password
    def __str__(self):
        return self.site_name+"\n"+self.user_name+"\n"+self.password   

