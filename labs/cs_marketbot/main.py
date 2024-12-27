import telebot
import sqlite3
from telebot import types
import config


bot = telebot.TeleBot('1869072250:AAEYDMmKbX2O55VcsJ094xOF2wC0GK-27ts')


conn = sqlite3.connect('skins_market.db', check_same_thread=False)
cursor = conn.cursor()


cursor.execute('''CREATE TABLE IF NOT EXISTS users
                (user_id INTEGER PRIMARY KEY,
                 username TEXT,
                 language TEXT DEFAULT 'en')''')

cursor.execute('''CREATE TABLE IF NOT EXISTS skins
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 seller_id INTEGER,
                 skin_name TEXT,
                 wear TEXT,
                 price REAL,
                 status TEXT DEFAULT 'available')''')

conn.commit()


MESSAGES = {
    'en': {
        'welcome': 'Welcome to CS:GO Skins Market Bot!\nChoose your language:',
        'menu': 'Main Menu:\n1. Sell Skin\n2. Buy Skins\n3. My Listings\n4. Change Language',
        'enter_skin_name': 'Enter skin name:',
        'enter_wear': 'Enter skin wear (Factory New/Minimal Wear/Field-Tested/Well-Worn/Battle-Scarred):',
        'enter_price': 'Enter price in USD:',
        'listing_created': 'Your listing has been created!',
        'available_skins': 'Available skins:',
        'no_skins': 'No skins available',
        'contact_seller': 'Contact seller: @{}',
    },
    'ru': {
        'welcome': 'Добро пожаловать в бот CS:GO Skins Market!\nВыберите язык:',
        'menu': 'Главное меню:\n1. Продать скин\n2. Купить скины\n3. Мои объявления\n4. Изменить язык',
        'enter_skin_name': 'Введите название скина:',
        'enter_wear': 'Введите состояние (Factory New/Minimal Wear/Field-Tested/Well-Worn/Battle-Scarred):',
        'enter_price': 'Введите цену в USD:',
        'listing_created': 'Ваше объявление создано!',
        'available_skins': 'Доступные скины:',
        'no_skins': 'Нет доступных скинов',
        'contact_seller': 'Связаться с продавцом: @{}',
    }
}



class UserState:
    def __init__(self):
        self.waiting_for_skin_name = False
        self.waiting_for_wear = False
        self.waiting_for_price = False
        self.temp_skin_data = {}


user_states = {}



def get_user_language(user_id):
    cursor.execute('SELECT language FROM users WHERE user_id = ?', (user_id,))
    result = cursor.fetchone()
    return result[0] if result else 'en'



@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    username = message.from_user.username

    cursor.execute('INSERT OR IGNORE INTO users (user_id, username) VALUES (?, ?)',
                   (user_id, username))
    conn.commit()

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('English 🇬🇧', 'Русский 🇷🇺')

    bot.send_message(user_id, MESSAGES['en']['welcome'], reply_markup=markup)



@bot.message_handler(func=lambda message: message.text in ['English 🇬🇧', 'Русский 🇷🇺'])
def set_language(message):
    user_id = message.from_user.id
    language = 'en' if message.text == 'English 🇬🇧' else 'ru'

    cursor.execute('UPDATE users SET language = ? WHERE user_id = ?',
                   (language, user_id))
    conn.commit()

    show_menu(message)



def show_menu(message):
    user_id = message.from_user.id
    language = get_user_language(user_id)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if language == 'en':
        markup.add('Sell Skin', 'Buy Skins')
        markup.add('My Listings', 'Change Language')
    else:
        markup.add('Продать скин', 'Купить скины')
        markup.add('Мои объявления', 'Изменить язык')

    bot.send_message(user_id, MESSAGES[language]['menu'], reply_markup=markup)


@bot.message_handler(func=lambda message: message.text in ['Sell Skin', 'Продать скин'])
def start_sell(message):
    user_id = message.from_user.id
    language = get_user_language(user_id)

    user_states[user_id] = UserState()
    user_states[user_id].waiting_for_skin_name = True

    bot.send_message(user_id, MESSAGES[language]['enter_skin_name'])



@bot.message_handler(func=lambda message: True)
def handle_messages(message):
    user_id = message.from_user.id
    language = get_user_language(user_id)

    if user_id in user_states:
        state = user_states[user_id]

        if state.waiting_for_skin_name:
            state.temp_skin_data['name'] = message.text
            state.waiting_for_skin_name = False
            state.waiting_for_wear = True
            bot.send_message(user_id, MESSAGES[language]['enter_wear'])

        elif state.waiting_for_wear:
            state.temp_skin_data['wear'] = message.text
            state.waiting_for_wear = False
            state.waiting_for_price = True
            bot.send_message(user_id, MESSAGES[language]['enter_price'])

        elif state.waiting_for_price:
            try:
                price = float(message.text)
                state.temp_skin_data['price'] = price


                cursor.execute('''INSERT INTO skins (seller_id, skin_name, wear, price)
                                VALUES (?, ?, ?, ?)''',
                               (user_id, state.temp_skin_data['name'],
                                state.temp_skin_data['wear'],
                                state.temp_skin_data['price']))
                conn.commit()

                bot.send_message(user_id, MESSAGES[language]['listing_created'])
                del user_states[user_id]
                show_menu(message)

            except ValueError:
                bot.send_message(user_id, MESSAGES[language]['enter_price'])

    elif message.text in ['Buy Skins', 'Купить скины']:

        cursor.execute('''SELECT skin_name, wear, price, username 
                         FROM skins JOIN users ON seller_id = user_id 
                         WHERE status = 'available' ''')
        skins = cursor.fetchall()

        if skins:
            response = MESSAGES[language]['available_skins'] + '\n\n'
            for skin in skins:
                response += f"{skin[0]} | {skin[1]} | ${skin[2]}\n"
                response += MESSAGES[language]['contact_seller'].format(skin[3]) + '\n\n'
            bot.send_message(user_id, response)
        else:
            bot.send_message(user_id, MESSAGES[language]['no_skins'])

    elif message.text in ['Change Language', 'Изменить язык']:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add('English 🇬🇧', 'Русский 🇷🇺')
        bot.send_message(user_id, MESSAGES['en']['welcome'], reply_markup=markup)



bot.polling(none_stop=True)
