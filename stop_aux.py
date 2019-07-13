threads = {}

def stop_aux(url, chat_id, update):
    ths = None

    try:
        ths = threads[chat_id]
    except:
        update.send_message(chat_id, "You have not started any thread")
        return
    
    for i in range(0,len(ths)):
        pass
        if ths[i].get_url() == url:
            ths[i].stop()
            del ths[i]
            update.send_message(chat_id, "removed")    
            if(len(ths) == 0):
                threads.pop(chat_id, None)

            return
    update.send_message(chat_id, "The url you inserted was not controlled")
    update.send_message(chat_id, "If you whant to control a thread send a message with the ulr")
