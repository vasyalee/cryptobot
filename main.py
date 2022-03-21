import logging
from telegram import Update
import yaml
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext,
)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                                level=logging.INFO)
logger = logging.getLogger(__name__)

def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, 
                                text="Ну привет, криптан!")


with open('config.yml') as f: 
    data = yaml.load(f, Loader=yaml.FullLoader)
    

updater = Updater(token=data['TOKEN'], use_context=True)
dispatcher = updater.dispatcher

def main():
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)


    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

