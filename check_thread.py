from threading      import Thread
from read_pages     import read
from read_pages     import check_url
from stop_aux       import stop_aux

import time


#thread class that controls urls
class ControlThread(Thread):

    def __init__(self,chat_id,bot,url,mins):
        Thread.__init__(self)
        self._url       = url 
        self._bot       = bot
        self._mins      = mins
        self._flag      = True                     #if True the Thread has not been stopped
        self._chat_id   = chat_id


    def run(self):  
        text = read(self._url)
        condition = True
        while(condition):
            condition = text == read(self._url)
            if (not condition):
                break
            time.sleep(self._mins*60)
            if(not self._flag):
                return

        
        self.send_message()
            
    def stop(self):
        self._flag = False
        
    def send_message(self):
        self._bot.send_message(self._chat_id, "{} has changed".format(self._url))
        stop_aux(self._url, self._chat_id, self._bot)

    def get_url(self):
        return self._url

    def get_chat_id(self):
        return self._chat_id