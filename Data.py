from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Halo {}
selamat datang {}
jika kamu tidak percaya bot ini, 
1. jgn baca pesan ini
2. blokir bot atau delete chat
bot ini bekerja untuk membantu kamu mendapatkan string session via bot
by @qbaeee
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton(" Start Generating Session ", callback_data="generate")],
        [InlineKeyboardButton(text=" Kembali ", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton(" Start Generating Session ", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton(" START GENERATING STRING ", callback_data="generate")],
        [InlineKeyboardButton(" maintaned by ", url="https://t.me/ngapainbg")],
        [
            InlineKeyboardButton("HELP", callback_data="help"),
            InlineKeyboardButton("ABOUT", callback_data="about")
        ],
        
    ]

    # Help Message
    HELP = """

/about - tentang bot ini
/help - bantuan
/start - mulai mot
/generate - mulai menerating session
/cancel - membatalkan process
/restart - process membatalkan
"""

    # About Message
    ABOUT = """
*tentang bot ini* 

𝗤𝗕𝗦𝗧𝗥𝗜𝗡𝗚 dibuat untuk membantu kamu mengambil  string session yang mudah dan aman!!
Group Support : [join](https://t.me/ngapainbg)
Developer : @qbaeee
    """
