from datetime import datetime


class journalEntry(object):

    """Model of a single journal entry

    title: title of journal entry,
    body:  body of journal entry
   

    """

    def __init__(self, data):
        self.title = data['title']
        self.body = data['body']
        

    def getDict(self):
        return self.__dict__
