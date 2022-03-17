from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Halo {}
Selamat datang {}
Jika kamu tidak percaya bot ini, 
1. jgn baca pesan ini
2. blokir bot atau delete chat
Bot ini Bekerja Untuk Membantu Kamu Mendapatkan String Session Via Bot
By @qbaeee
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
            InlineKeyboardButton("HELP&COMMANDS", callback_data="help"),
            InlineKeyboardButton(" ABOUT ", callback_data="about")
        ],
        
    ]

    # Help Message
    HELP = """
✨ cara penggunaan ✨
/about - Tentang Bot ini
/help - bantuan
/start - Mulai Bot
/generate - Mulai Generating Session
/cancel - Membatalkan process
/restart - process membatalkan
"""

    # About Message
    ABOUT = """
*tentang bot ini* 
𝗤𝗕𝗦𝗧𝗥𝗜𝗡𝗚 dibuat untuk membantu kamu mengambil  string session yang mudah dan aman!!
Group Support : [Gabung](https://t.me/ngapainbg)
Developer : @qbaeee
    """
