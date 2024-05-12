from telegram.ext import Updater, CommandHandler
from telegram.error import BadRequest, TelegramError
import time

TOKEN = '7062585200:AAFMZQIKse16z4KfCIrg2xHxr-KrvFyPuPE'

# Store the members already invited
invited_members = set()

def invite_members(update, context):
    global invited_members
    chat_id = (-1002062094979)
    with open('members.txt', 'r') as file:
        members_list = file.read().splitlines()

    # Filter out already invited members
    new_members = [member for member in members_list if member not in invited_members]

    # Send invitation messages to each member
    for member in new_members:
        invitation_message = f"Hey @{member}, join our group chat to participate in discussions!"
        context.bot.send_message(chat_id, invitation_message)
        invited_members.add(member)

    update.message.reply_text("Invitation messages sent successfully.")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('invite_members', invite_members))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
    
