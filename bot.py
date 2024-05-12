from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram.error import BadRequest
import time

TOKEN = ''

# Store the members already added
added_members = set()

def add_members(update, context):
    global added_members
    chat_id = ()
    with open('members.txt', 'r') as file:
        members_list = file.read().splitlines()
    
    # Filter out already added members
    new_members = [member for member in members_list if member not in added_members]
    
    # Add 13 members at a time
    for i in range(0, len(new_members), 13):
        chunk = new_members[i:i+13]
        for member in chunk:
            try:
                context.bot.add_chat_member(chat_id, member)
                added_members.add(member)
            except BadRequest:
                pass
        # Wait for 1 hour before adding the next chunk
        time.sleep(3600)

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('add_members', add_members))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
