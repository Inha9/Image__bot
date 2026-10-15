from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [

            KeyboardButton(text="Ichimlikar"),
            KeyboardButton(text="Lavashlar")
        ],
        [
            KeyboardButton(text="Pitsalar"),
            KeyboardButton(text="Burgerlar"),
        ],
        [
            KeyboardButton(text="Shirinliklar"),
            KeyboardButton(text="Orqaga"),
        ]
    ],
    resize_keyboard=True
)

drinks_menu_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="CocaCola"),

            KeyboardButton(text="Pepsi"),
            KeyboardButton(text="Fanta"),
            KeyboardButton(text="Sprite"),
        ],
        [
            KeyboardButton(text="Orqaga"),
        ]
    ],
    resize_keyboard=True
)

dessert_menu_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Cake"),

            KeyboardButton(text="Pencake"),
            KeyboardButton(text="sweets"),
            KeyboardButton(text="donuts"),
        ],
        [
            KeyboardButton(text="Orqaga"),
        ]
    ],
    resize_keyboard=True
)