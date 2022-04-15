from Script import script

PHOTO = [
    "https://telegra.ph/file/8f65af0419d2e4b92bf2a.jpg",
    "https://telegra.ph/file/099fdd8ae27a68e73c4b4.jpg",
    "https://telegra.ph/file/3e5d288f42ea557ec5325.jpg",
    "https://telegra.ph/file/3c77153a47314ac7a99f2.jpg",
    "https://telegra.ph/file/1050fc48d6402bfdcd7af.jpg",
    "https://telegra.ph/file/f45a5c0e064411027333c.jpg",
    "https://telegra.ph/file/8da62823c9508fe054d76.jpg",
    "https://telegra.ph/file/6c97af926e1f1cd54c146.jpg",
]

@Bot.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    if not await db.is_user_exist(update.from_user.id):
        await db.add_user(update.from_user.id)  
        await message.reply_photo(
            photo=f"{random.choice(PHOTO)}",
            caption=script.STRT_MSG,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("😎 About", callback_data="about")
                    ],
                    [
                        InlineKeyboardButton("➕ Add Me To Your Group ➕", url="https://t.me/proannaben_bot?startgroup=true")
                    ]
                ]
            )
        )
