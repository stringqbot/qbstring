from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
hallo {}
━━━━━━━━━━━━━━━━━━━━━━━━
jika km tidak percaya bot ini
1. jgn baca pesan ini
2. blokir bot atau delete chat
━━━━━━━━━━━━━━━━━━━━━━━━
bot ini untuk membantu km 
mendapatkan string via bot..
━━━━━━━━━━━━━━━━━━━━━━━
managed by @akudnr
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton(" START GENERATING SESSION ", callback_data="generate")],
        [InlineKeyboardButton(text=" kembali ", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton(" start generating session ", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton(" START GENERATING STRING ", callback_data="generate")],
        
        [
            InlineKeyboardButton("HELP", callback_data="help"),
            InlineKeyboardButton("ABOUT", callback_data="about")
        ],
        
    ]

    # Help Message
    HELP = """
CARA PENGGUNAAN :

/about - tentang bot ini
/help - bantuan
/start - mulai bot
/generate - mulai generating session
/cancel - membatalkan process
/restart - process membatalkan
"""

    # About Message
    ABOUT = """
TENTANG BOT INI :

𝗤𝗕𝗦𝗧𝗥𝗜𝗡𝗚 dibuat untuk membantu kamu mengambil  string session yang mudah dan aman!!
channel : [join](https://t.me/mmmaself)
developer : @akudnr
    """
