from telegram.ext   import Updater, CommandHandler, MessageHandler, Filters
from check_thread   import ControlThread
from read_pages     import check_url
from stop_aux       import stop_aux
from stop_aux       import threads
from telegram       import Bot

def start(update, context):
    print("start")
    update.send_message(context.message.chat_id, "Hi!")
    update.send_message(context.message.chat_id, "Send a link to control")


def help(update, context):
    print("help")
    update.send_message(context.message.chat_id, "No one can help you")


def url(update, context):
    print("url")

    url = context.message.text

    if not ("http://" in url or "https://" in url):
        url = "http://"+url

    if not check_url(url):
        update.send_message(context.message.chat_id, "URL not valid")
        return

    ct = ControlThread(context.message.chat_id, update, url, 1)
    
    try:
        threads[context.message.chat_id].append(ct)
    except:
        print("except")
        threads[context.message.chat_id] = [ct]

    ct.start()
    

def stop(update, context):
    print(context.message.text)

    url = context.message.text.split(" ")[1]

    if url == "":
        update.send_message(context.message.chat_id, "Tell me what thread to stop")

    stop_aux(url, context.message.chat_id, update)

def delete_all(update, context):
    ths = None
    try:
        ths = threads[context.message.chat_id]
    except:
        update.send_message(context.message.chat_id, "You have not started any thread")
        return

    for i in range(0, len(ths)):
        ths[i].stop()
    update.send_message(context.message.chat_id, "deleted {} threads".format(len(ths)))
    del threads[context.message.chat_id]


def list_all(update, context):
    ths = None
    try:
        ths = threads[context.message.chat_id]
    except:
        update.send_message(context.message.chat_id, "You have not started any thread")
        return
    print(len(ths))
    for i in range(0, len(ths)):
        update.send_message(context.message.chat_id, ths[i].get_url())



def error(update, context):
    pass

updater = Updater("YOUR_TOKEN")

def main():

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("stop", stop))
    dp.add_handler(CommandHandler("delete_all", delete_all))
    dp.add_handler(CommandHandler("list", list_all))


    dp.add_handler(MessageHandler(Filters.text, url))

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main() 
