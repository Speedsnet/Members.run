from telegram.ext import Updater, CommandHandler
from telegram.error import BadRequest, TelegramError
import time

TOKEN = '7062585200:AAFMZQIKse16z4KfCIrg2xHxr-KrvFyPuPE'

# Store the members already added
added_members = set()

def add_members(update, context):
    global added_members
    chat_id = (-1002062094979)
    with open('members.txt', 'r') as file:
        members_list = file.read().splitlines()

    # Filter out already added members
    new_members = [member for member in members_list if member not in added_members]

    # Add 13 members at a time
    for i in range(0, len(new_members), 13):
        chunk = new_members[i:i+13]
        members_to_add = []
        for member in chunk:
            try:
                chat_member = context.bot.get_chat_member(chat_id, member)
                if chat_member.status == 'left':
                    members_to_add.append(member)
            except TelegramError:
                pass
        if members_to_add:
            try:
                context.bot.add_chat_members(chat_id, members_to_add)
                added_members.update(members_to_add)
                update.message.reply_text("Members added successfully.")
            except BadRequest as e:
                update.message.reply_text(f"Failed to add members: {e.message}")
        # Wait for 1 hour before adding the next chunk
        time.sleep(36)

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('add_members', add_members))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
    
