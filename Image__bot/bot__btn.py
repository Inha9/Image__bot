from aiogram import types

pillow__filters = [
    "BLUR", "CONTOUR", "DETAIL", "EDGE_ENHANCE", "EDGE_ENHANCE_MORE", "EMBOSS", "FIND_EDGES", "SHARPEN", "SMOOTH", "SMOOTH_MORE"
]

async def start_menu_btn():
    btn = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=True)
    btn.add(
        types.KeyboardButton("🖼 Effects"),
        types.KeyboardButton("👱‍♂️ Admin"),
    )
    return btn

async def effects_btn():
    btn = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn.add(
        *[types.KeyboardButton(f"{item}") for item in pillow__filters],
        types.KeyboardButton("⬅️ Back")
    )
    return btn