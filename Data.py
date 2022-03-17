from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
halo {}
━━━━━━━━━━━━━━━━━━━━━━━━
jika m tidak percaya bot ini
1. jgn baca pesan ini
2. blokir bot atau delete chat
━━━━━━━━━━━━━━━━━━━━━━━━
bot ini untuk membantu km 
mendapatkan string via bot..
━━━━━━━━━━━━━━━━━━━━━━━
managed by @qbaeee
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
        [InlineKeyboardButton(" maintaned by ", url="https://t.me/qbaeee")],
        [
            InlineKeyboardButton("HELP", callback_data="help"),
            InlineKeyboardButton("ABOUT", callback_data="about")
        ],
        
    ]

    # Help Message
    HELP = """

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
group : [join](https://t.me/ngapainbg)
developer : @qbaeee
    """
