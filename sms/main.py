import requests
from threading import Thread


class SMS(Thread):

    def __init__(self, credentials, to_, message_):

        Thread.__init__(self)

        self.USERNAME = credentials['USERNAME']
        self.PASSWORD = credentials['PASSWORD']

        self.API_KEY = credentials['API_KEY']

        self.url = "https://smsapi.engineeringtgr.com/send/"

        self.to = to_
        self.message = message_

    def run(self):

        parms = dict(
            Mobile = self.USERNAME,
            Password = self.PASSWORD,
            Key = self.API_KEY,
            Message = self.message,
            To = self.to
        )

        req = requests.get(self.url, params = parms)

        print(req.text)

        #will implement error handle later



