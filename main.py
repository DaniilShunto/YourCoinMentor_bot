import telebot
from telebot import types
from telebot.types import LabeledPrice

bot = telebot.TeleBot('7552048882:AAGL1jOYpUIEKaASeZpffo1126PIqzET8JU')

PROVIDER_TOKEN = '381764678:TEST:109939'
CURRENCY = 'RUB'





@bot.message_handler(commands=['start'])
def heart(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item3 = types.KeyboardButton('Ваши вопросы и предложения')
    markup.row(item3)
    item4 = types.KeyboardButton('Поддержать проект')
    markup.row(item4)
    bot.send_message(message.chat.id, '💫', reply_markup=markup)
    start(message)



def start(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Стать автором', callback_data='Стать автором'))
    markup.add(types.InlineKeyboardButton('Каталог авторов', callback_data='Каталог авторов'))
    with open('Фото приветствия.png', 'rb') as photo:
        bot.send_photo(message.chat.id, photo, caption=f'⭐️ <b>Привет , {message.chat.first_name} {message.chat.last_name}! Рады приветствовать тебя в нашем боте!</b>\n\n' 
        
        'Наша команда разработала уникальную платформу, которая объединяет трейдеров и инвесторов. Здесь ты найдёшь всё необходимое для уверенной работы на крипторынке.\n\n' 
        
        '💼 <b>Для опытных трейдеров:</b>\n\n' 'Если ты умеешь торговать и хочешь монетизировать свои навыки, нажимай кнопку «Стать автором». Наша платформа предоставит тебе удобный способ делиться своим опытом и зарабатывать на этом.\n\n' 
        
        '📈 <b>Для новичков и инвесторов:</b>\n\n' 'Если ты только начинаешь изучать крипторынок или хочешь инвестировать с опорой на профессиональные рекомендации, кнопка «Каталог авторов» поможет найти подходящего трейдера, который соответствует твоим целям и стратегии\n\n'
        
        '⭐️ Мы создаём пространство для роста и успеха каждого участника.', parse_mode='html', 
        
        reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def handle_text(message):
    if message.text == 'Ваши вопросы и предложения':       
        bot.send_message(message.chat.id, '⭐️Мы всегда рады вашим вопросам и предложениям. \n\n'
         'Если у вас возникли какие-то идеи или проблемы, пожалуйста, свяжитесь с нами. Вы можете написать нам на почту:\n\n'
         '41015S@mail.ru\n\n' 
         'Oтправить сообщение напрямую в чат администраторов:\n\n'
         'https://t.me/+9wLwGSQswFlmYmNi\n\n'
         '⭐️Мы обязательно ответим вам в ближайшее время')
        bot.delete_message(message.chat.id, message.message_id)
    elif message.text == 'Поддержать проект':
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, '⭐️Мы ценим каждого нашего пользователя и стремимся сделать наш проект ещё лучше.🥇\n\n' '⭐️Если вам нравится то, что мы делаем, пожалуйста, поддержите нас. Это поможет нам расти и развиваться, чтобы продолжать радовать вас новыми идеями и возможностями\n\n' 'https://yoomoney.ru/fundraise/17R0PSLH1DH.250117')


@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data == 'Стать автором':
        author_start(call)
    elif call.data == 'Продолжить':
         author_path(call)
    elif call.data == 'Главное меню':
        back_to_main_menu(call)
    elif call.data == 'Каталог авторов':
        authors_menu(call)
    elif call.data == 'Назад':
        authors_menu(call) 
    elif call.data == 'Петя':
        author_Petya(call)
    elif call.data == 'Подписка Петя':
        subscribe_Petya(call)
    elif call.data == 'Вася':
        author_Vasya(call)
    elif call.data == 'Подписка Вася':
        subscribe_Vasya(call)
    elif call.data == 'Коля':
        author_Kolya(call)
    elif call.data == 'Подписка Коля':
        subscribe_Kolya(call)
    elif call.data == 'Степа':
        author_Stepa(call)
    elif call.data == 'Подписка Степа':
        subscribe_Stepa(call)
    elif call.data == 'Оплата1':
         payment_1(call)
    elif call.data == 'Оплата2':
         payment_2(call)
        
@bot.pre_checkout_query_handler(func=lambda query: True)
def pre_checkout_query_handler(pre_checkout_query):
    bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)

@bot.message_handler(content_types=['successful_payment'])
def successful_payment(message):
    payload = message.successful_payment.invoice_payload

    markup = types.InlineKeyboardMarkup()

    if payload == 'product_1':
        markup.add(types.InlineKeyboardButton(text='Перейти к чату', url='https://t.me/+Dv8JtZFAI79jMjgy'))
    
    elif payload == 'product_2':
         markup.add(types.InlineKeyboardButton(text='Перейти к чату', url='https://t.me/+j3J1ku04JvdhZTZi'))
         
    bot.send_message(message.chat.id, 'Подписка успешно оформлена!', reply_markup=markup)


def author_start(call):
        bot.delete_message(call.message.chat.id, call.message.message_id)
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Продолжить', callback_data='Продолжить'))
        markup.add(types.InlineKeyboardButton('Главное меню', callback_data='Главное меню'))
        with open('Автор1.2.png', 'rb') as photo:
            bot.send_photo(call.message.chat.id, photo, caption=
            
            '⭐️ <b>Стать автором — это круто!\n' 'Ты получаешь подписчиков и возможность монетизировать свои знания и опыт.</b>\n\n'

            '👨‍💻Что ты сможешь делать на платформе:\n\n'

            '1️⃣ Вести свой личный профиль или Telegram-канал, где ты будешь:\n\n'

            '-Публиковать аналитические обзоры.\n\n'
            '-Делиться своими предположениями и сделками с выбранными активами.\n\n'

            '2️⃣ Самостоятельно устанавливать стоимость ежемесячной подписки для своих фолловеров.\n\n'

            '3️⃣ Развивать свою медийность:\n\n'

            '-Увеличивать базу подписчиков.\n\n'
            '-Зарабатывать больше благодаря своему профессионализму и активности.', parse_mode='html',
            
            reply_markup=markup)

def author_path(call):  
        bot.delete_message(call.message.chat.id, call.message.message_id)
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Поддержка', url='https://t.me/@SHUNTO1'))
        markup.add(types.InlineKeyboardButton('Главное меню', callback_data='Главное меню'))
        with open('Автор2.1.png', 'rb') as photo:
            bot.send_photo(call.message.chat.id, photo, caption=
            
            '⭐️<b>Поздравляем, вы выбрали стать автором!</b>\n\n'  
            
            'Для подтверждения вашего статуса, пожалуйста, нажмите кнопку "Поддержка" и предоставьте следующие данные:\n\n'

            '1️⃣Ваш годовой и месячный PNL (Profit and Loss):\n'
            '📊 Подробная информация о ваших финансовых результатах.\n\n'

            '2️⃣Основная информация о вас как о трейдере:\n'
            '💼 Укажите ваш торговый стаж, достижения и ключевые моменты вашей карьеры.\n\n'

            '3️⃣Имя вашего будущего канала (профиля):\n'
            'Название, которое будет отображаться в вашем канале или профиле.', parse_mode='html', 
            
            reply_markup=markup)


def back_to_main_menu(call):
    bot.delete_message(call.message.chat.id, call.message.message_id)
    start(call.message)

def authors_menu(call):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Петя', callback_data='Петя')
    btn2 = types.InlineKeyboardButton('Вася', callback_data='Вася')
    markup.row(btn1, btn2)
    btn3 = types.InlineKeyboardButton('Пусто...', callback_data='Коля')
    btn4 = types.InlineKeyboardButton('Пусто...', callback_data='Степа')
    markup.row(btn3, btn4)
    btn5 = types.InlineKeyboardButton('Назад', callback_data='Назад')
    btn6 = types.InlineKeyboardButton('1', callback_data='1')
    btn7 = types.InlineKeyboardButton('Вперед', callback_data='Вперед')
    markup.row(btn5, btn6, btn7)
    markup.add(types.InlineKeyboardButton('Главное меню', callback_data='Главное меню'))
    with open('Фото Подписчик 1.png', 'rb') as photo:
        bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id, media=types.InputMediaPhoto(photo), reply_markup=markup)




def author_Petya(call):
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Настройка подписки на 1м |250 руб|', callback_data='Подписка Петя'))
        markup.add(types.InlineKeyboardButton('Каталог авторов', callback_data='Каталог авторов'))
        with open('Фото Автора 1.png', 'rb') as photo:
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id, media=types.InputMediaPhoto(photo, caption="Это Петя. Торгуемые валюты -****, PNL:****\n Петя в рынке уже столько лет\n Риск профиль пети - рисковый\n oсновная стратегия - смарт мани\n Петя: расскзывает о себе привет бродяги и тд"), reply_markup=markup)

def subscribe_Petya(call):
        bot.delete_message(call.message.chat.id, call.message.message_id)
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('ЮKassa', callback_data='Оплата1'))
        markup.add(types.InlineKeyboardButton('Каталог авторов', callback_data='Каталог авторов'))
        bot.send_message(call.message.chat.id, 'Выберите способ оплаты:', reply_markup=markup)


def payment_1(call):
     description = 'Подписка на Петю'
     prices = [LabeledPrice(label='Подписка на канал автора "Петя" на 1 месяц.\n' 'Вы получаете доступ к контенту, который предоставляет Петя в совем канале\n\n'
                             'Стоимость: 250 рублей', amount=250 * 100)]
     bot.send_invoice(call.message.chat.id, 
                      title='Покупка подписки',
                      description=description,
                      invoice_payload='product_1',
                      provider_token=PROVIDER_TOKEN,
                      currency=CURRENCY,
                      start_parameter='Test',
                      prices=prices
                      )
    

    

    



def author_Vasya(call):
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Настройка подписки на 1м |300 руб|', callback_data='Подписка Вася'))
        markup.add(types.InlineKeyboardButton('Каталог авторов', callback_data='Каталог авторов'))
        with open('Фото Автора 1.png', 'rb') as photo:
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id, media=types.InputMediaPhoto(photo, caption="Это Вася. Торгуемые валюты -****, PNL:****"), reply_markup=markup)

def subscribe_Vasya(call):
        bot.delete_message(call.message.chat.id, call.message.message_id)
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('ЮKassa', callback_data='Оплата2'))
        markup.add(types.InlineKeyboardButton('Каталог авторов', callback_data='Каталог авторов'))
        bot.send_message(call.message.chat.id, 'Выберите способ оплаты:', reply_markup=markup)

def payment_2(call):
    description = 'Подписка на Васю'
    prices = [LabeledPrice(label='Подписка на васю', amount=300 * 100)]
    bot.send_invoice(call.message.chat.id, 
                      title='Покупка подписки',
                      description=description,
                      invoice_payload='product_2',
                      provider_token=PROVIDER_TOKEN,
                      currency=CURRENCY,
                      start_parameter='test',
                      prices=prices
                      )

def author_Kolya(call):
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Каталог авторов', callback_data='Каталог авторов'))
        with open('Фото Автора 1.png', 'rb') as photo:
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id, media=types.InputMediaPhoto(photo, caption="Здесь пока ничего нет. Место автора свободно."), reply_markup=markup)


def subscribe_Kolya(call):
        bot.delete_message(call.message.chat.id, call.message.message_id)
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('ROBOKASSA', callback_data='Оплата'))
        markup.add(types.InlineKeyboardButton('Каталог авторов', callback_data='Каталог авторов'))
        bot.send_message(call.message.chat.id, 'Выберите способ оплаты:', reply_markup=markup)

def author_Stepa(call):
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Каталог авторов', callback_data='Каталог авторов'))
        with open('Фото Автора 1.png', 'rb') as photo:
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id, media=types.InputMediaPhoto(photo, caption="Здесь пока ничего нет. Место автора свободно."), reply_markup=markup)

def subscribe_Stepa(call):
        bot.delete_message(call.message.chat.id, call.message.message_id)
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('ROBOKASSA', callback_data='Оплата'))
        markup.add(types.InlineKeyboardButton('Каталог авторов', callback_data='Каталог авторов'))
        bot.send_message(call.message.chat.id, 'Выберите способ оплаты:', reply_markup=markup)
       




     
   
 
bot.polling(none_stop=True)
        

