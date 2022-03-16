from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
    

 
hallo {}
selamat datang 

jika km tida percaya bot ini, 
1. gausa baca pesan ini
2. blokir bot atau delete chat

bot ini bekerja untuk membantu kamu mendapatkan string session via bot, mks anjing😺
by @qbaeee
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴇssɪᴏɴ​", callback_data="generate")],
        [InlineKeyboardButton(text="ʙᴀᴄᴋ​", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴇssɪᴏɴ", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴇssɪᴏɴ", callback_data="generate")],
        [InlineKeyboardButton("ᴍᴀɪɴᴛᴀɴᴇᴅ ʙʏ​", url="https://t.me/qbaeee")],
        [
            InlineKeyboardButton("ʜᴏᴡ ᴛᴏ ᴜsᴇ ᴍᴇ​​", callback_data="help"),
            InlineKeyboardButton("ᴀʙᴏᴜᴛ​", callback_data="about")
        ],
        [InlineKeyboardButton("ɪɴꜰᴏ ʙᴏᴛ ʟᴀɪɴɴʏᴀ​", url="https://t.me/mmmaself")],
    ]

    # Help Message
    HELP = """
✨cara penggunaan ✨

/about - tentang bot ini
/help - bantuan
/start - mulai bot
/generate - mulai generating session
/cancel - membatalkan process
/restart - process membatalkan
"""

    # About Message
    ABOUT = """
**About This Bot** 

Sebuah telegram bot untuk mengambil pyrogram dan telethon string session by @stringqbot



Developer : @qbaeee
    """
