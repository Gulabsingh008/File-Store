from pyrogram import Client 
from bot import Bot
from config import *
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from database.database import add_user, del_user, full_userbase, present_user

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "help":
        await query.message.edit_text(
            text=HELP_TXT.format(first=query.from_user.first_name),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton('ʜᴏᴍᴇ', callback_data='start'),
                        InlineKeyboardButton("ᴄʟᴏꜱᴇ", callback_data='close')
                    ]
                ]
            )
        )
    elif data == "about":
        await query.message.edit_text(
            text=ABOUT_TXT.format(first=query.from_user.first_name),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [ [ InlineKeyboardButton("ᴍᴏᴠɪᴇ ᴄʜᴀɴɴᴇʟ", callback_data ="https://t.me/Ra_yan_2024_movie"),
                  InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ" , callback_data = "https://t.me/+OiKmB79YlMJmNTJl")],
                 [InlineKeyboardButton("sᴇᴀʀᴄʜ ᴀɴʏ ᴍᴏᴠɪᴇ", url = "https://t.me/rezii_auto_filter")],
                    [
                        InlineKeyboardButton("ʜᴏᴍᴇ", callback_data = "start"),
                        InlineKeyboardButton(" ᴄʟᴏsᴇ ", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "start":
        await query.message.edit_text(
            text=START_MSG.format(first=query.from_user.first_name),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [ InlineKeyboardButton(text="🏖️", callback_data="about"),
                    InlineKeyboardButton(text="🍂", callback_data="about"),
                    InlineKeyboardButton(text="⚠️", callback_data="me"),
                    InlineKeyboardButton(text="💸", callback_data="about"),
                    InlineKeyboardButton(text="🎭", callback_data="about"),
                ],[ InlineKeyboardButton( "ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ", callback_data = "main" ),
                    InlineKeyboardButton("ᴍᴏᴠɪᴇ ᴄʜᴀɴɴᴇʟ ", callback_data = "main")
                ], [ InlineKeyboardButton("sᴇᴀʀᴄʜ ᴀɴʏ ᴍᴏᴠɪᴇ", url = "http://t.me/rezii_auto_filter_bot") ],
                [
                    InlineKeyboardButton("ʜᴇʟᴘ", callback_data = "help"),
                    InlineKeyboardButton("ᴀʙᴏᴜᴛ", callback_data = "about")
                ]
            ]
            )
        )
    
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
      
    elif data == "main":
        await query.message.edit_text(
            text=f"<blockquote>ʜᴇʟʟᴏ ᴍʏ ᴜsᴇʀs ᴍʏ ᴜᴘᴅᴀᴛᴇ & ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ ɪs ɢɪᴠᴇɴ ʙᴇʟᴏᴡ.</blockquote>",
            disable_web_page_preview=True,
            reply_markup = InlineKeyboardMarkup(
                [   
                    [
                        InlineKeyboardButton("ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ", url="https://t.me/Ra_yan_2024_movie"),
                        InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ",url = "https://t.me/+OiKmB79YlMJmNTJl")
                    ],
                    [   InlineKeyboardButton("ʜᴏᴍᴇ ", callback_data = "start"), 
                        InlineKeyboardButton("ᴄʟᴏsᴇ ", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "me":
            await query.message.edit(
                text=f"<b>ᴛʜɪs sᴇᴄᴛɪᴏɴ ɪs ᴀᴠᴀɪʟᴀʙʟᴇ ᴏɴʟʏ ғᴏʀ ᴀᴅᴍɪɴs & ᴅᴇᴠᴇʟᴏᴘᴇʀ</b>",
                disable_web_page_preview=True,
                reply_markup = InlineKeyboardMarkup(
                    [
                        [  InlineKeyboardButton("ᴅᴇᴠʟᴏᴘᴇʀ",url= "t.me/af_mhakal"),
                         InlineKeyboardButton("ᴀᴅᴍɪɴ",url = "t.me/af_mhakal")],
                        [ InlineKeyboardButton("ʜᴏᴍᴇ", callback_data = "start"),
                         InlineKeyboardButton( "ᴄʟᴏsᴇ", callback_data = "close")]
                    ]
                )
        )
    elif data == "source":
        await query.message.edit_text(
            text=f"<b><blockquote>ᴄᴏɴᴛᴀᴄᴛ ᴍʏ ᴅᴇᴠʟᴏᴘᴇʀ\n ᴀғ ᴍʜᴀᴋᴀʟ ❤️ \n★ <a herf='t.me/af_mhakal'>ᴀғ ᴍʜᴀᴋᴀʟ ❤️</a> \n★ <a herf='https://t.me/+OiKmB79YlMJmNTJl'> ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ </a></blockquote></b>",
            disable_web_page_preview=True,
            reply_markup = InlineKeyboardMarkup(
                [   
                    [
                        InlineKeyboardButton("ᴀғ ᴍʜᴀᴋᴀʟ ❤️ ", url="t.me/af_mhakal"),
                        InlineKeyboardButton(" ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ",url="https://t.me/+OiKmB79YlMJmNTJl")
                    ],
                    [   InlineKeyboardButton("ʜᴏᴍᴇ" , callback_data = "start"),
                        InlineKeyboardButton(" ᴄʟᴏsᴇ", callback_data = "close")
                    ]
                ]
            )
        )
