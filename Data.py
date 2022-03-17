from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Halo {}
Selamat datang {}
Jika kamu tidak percaya bot ini, 
1. gausa baca pesan ini
2. blokir bot atau delete chat
Bot ini Bekerja Untuk Membantu Kamu Mendapatkan String Session Via Bot. Rekomendasi Jika Ingin Mengambil String session
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
        [InlineKeyboardButton(" Start Generating Session ", callback_data="generate")],
        [InlineKeyboardButton("✨ Maintaned By ✨", url="https://t.me/ngapainbg")],
        [
            InlineKeyboardButton("Cara Menggunakan Saya ❔", callback_data="help"),
            InlineKeyboardButton(" About ", callback_data="about")
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
𝗤𝗕𝗦𝗧𝗥𝗜𝗡𝗚 dibuat untuk membantu mengambil  string session yang mudah dan aman!!
Group Support : [Gabung](https://t.me/ngapainbg)
Framework : [Pyrogram](docs.pyrogram.org)
Language : [Python](www.python.org)
Developer : @qbaeee
    """
