from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def greet_user(bot, update):
    #print(update)
    mytext = """Привет {}!

Понимаю только команду {} 
    """.format(update.message.chat.first_name, '/start')

    logging.info('User {} pressed /start'.format(update.message.chat.username))

    update.message.reply_text(mytext)

    print("Вызван")

def chat(bot, update):
    text = update.message.text
    logging.info(text)
    update.message.reply_text(text)

def main():
    updater = Updater(settings.TELEGRAM_API_KEY)
 
    updater.dispatcher.add_handler(CommandHandler("start", greet_user))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, chat))

    updater.start_polling()
    updater.idle()

if __name__=="__main__":
    logging.info('Started')
    main()