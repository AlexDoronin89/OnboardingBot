# -*- coding: cp1251 -*-
import time

import telebot
from telebot import types

bot = telebot.TeleBot('5943394315:AAEHraI-8AwFmhAfH-GL0yfNu-3_3SWuPsk')

@bot.message_handler(commands=['start'])
def start(message):
    try:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('1')
        btn2 = types.KeyboardButton('2')
        btn3 = types.KeyboardButton('3')
        markup.add(btn1, btn2, btn3)
        helo = f'Приветcвуем, <b>{message.from_user.first_name}</b>! Что вас интересует? Выберете: \n1 - если вы хотите узнать о нашем офисе \n2 - если вы хотите узнать про нашe корпорацию\n3 - если у вас появились проблемы'
        bot.send_message(message.chat.id, helo, parse_mode='html', reply_markup=markup)
        bot.register_next_step_handler(message, select)
    except:
        bot.send_message(message.chat.id, '<b>Не понял!</b>', parse_mode='html')

def select(message):
    try:
        if (message.text == '1'):
            aboutus(message)
        elif (message.text == '3'):
            learning(message)
        elif (message.text == '2'):
            productcs(message)
    except:
        bot.send_message(message.chat.id, '<b>Не понял!</b>', parse_mode='html')

@bot.message_handler(commands=['about'])
def aboutus(message):
    try:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Карта офиса')
        btn2 = types.KeyboardButton('Тех-лидеры')
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, 'Что вы хотите узнать о офисе?', reply_markup=markup)
        bot.register_next_step_handler(message, office)

    except:
        bot.send_message(message.chat.id, '<b>Не понял!</b>', parse_mode='html')

def office(message):
    try:
        if (message.text == 'Карта офиса'):
            bot.send_photo(message.chat.id, 'https://cdn.discordapp.com/attachments/1093571641088413706/1095608257395032157/image.png')
            time.sleep(2)
            start(message)
        elif (message.text == 'Тех-лидеры'):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            emp1 = types.KeyboardButton('Бэкэнд')
            emp2 = types.KeyboardButton('Фронтэнд')
            emp3 = types.KeyboardButton('Дизайнер')
            emp4 = types.KeyboardButton('Проджект-менеджер')
            markup.add(emp1, emp2, emp3, emp4)
            bot.send_message(message.chat.id, 'О сотруднике какого типа разработки вы хотите узнать?', reply_markup=markup)
            bot.register_next_step_handler(message, staff)
    except:
        bot.send_message(message.chat.id, '<b>Не понял!</b>', parse_mode='html')

def staff(message):
    try:
        if (message.text == 'Фронтэнд'):
            bot.send_message(message.chat.id,
                             'Макаров Клим Олегович - опытный frontend разработчик, который работает в сфере IT уже 11 лет. Он специализируется на frontend разработке, с фокусом на создании телеграмм ботов, сайтов и программ. Его знания и опыт в этой области являются ключевыми факторами успеха в его карьере. Макаров Клим Олегович обладает глубокими знаниями языков программирования, таких как Python, C++, Kotlin. Он также имеет богатый опыт в различных фреймворках и библиотеках для frontend разработки. Он может быстро адаптироваться к новым технологиям и инструментам, что позволяет ему создавать высококачественные и инновационные проекты. Кроме того, Макаров Клим Олегович является экспертом в дизайне и пользовательском опыте. Он уделяет особое внимание деталям и дизайну интерфейсов, что помогает создавать лучшие пользовательские интерфейсы. Макаров Клим Олегович является частью команды разработчиков, и его коммуникационные навыки и умение работать в коллективе являются ключевыми для успешного завершения проектов. Он также готов делиться своими знаниями и опытом с другими членами команды, чтобы обеспечить лучший результат для проекта. В целом, Макаров Клим Олегович - это опытный и талантливый frontend разработчик, который обладает всеми необходимыми навыками и знаниями для создания высококачественных, эффективных и инновационных frontend решений для своих клиентов и команды.')
            time.sleep(2)
            start(message)
        elif (message.text == 'Проджект-менеджер'):
            bot.send_message(message.chat.id,
                             'Колегов Алексей Михайлович - опытный project менеджер, который работает в сфере менеджемента уже 13 лет. Он специализируется на работе с людьми и имеет развитые лидерские качества, которые помогают ему эффективно управлять командами и достигать поставленных целей. Колегов Алексей Михайлович также обладает глубокими знаниями в области программирования, что позволяет ему лучше понимать работу команды и принимать более эффективные управленческие решения. Он может связываться с разработчиками, чтобы понимать, какие технологии используются и какие решения лучше всего подходят для конкретного проекта. Однако, ключевой навык Колегова Алексея Михайловича - это его способность работать с людьми. Он хорошо разбирается в психологии, что помогает ему понимать потребности и мотивации каждого члена команды. Он умеет находить общий язык с людьми и строить эффективные коммуникационные стратегии, что позволяет ему убедительно объяснять цели и задачи проекта. Колегов Алексей Михайлович имеет опыт работы на различных проектах и в различных индустриях, что позволяет ему принимать быстрые решения и эффективно управлять рисками. Он уделяет особое внимание контролю за бюджетом и сроками, чтобы проект был выполнен вовремя и в рамках бюджета. В целом, Колегов Алексей Михайлович - это опытный и талантливый project менеджер, который обладает всеми необходимыми навыками и знаниями для эффективного управления проектами. Его коммуникационные и лидерские качества позволяют ему эффективно работать с командой и достигать поставленных целей.')
            time.sleep(2)
            start(message)
        elif (message.text == 'Дизайнер'):
            bot.send_message(message.chat.id,
                             'Ершов Арсений Александрович - известный дизайнер в сфере графического дизайна, который уже более 15 лет работает в этой области. Его уникальный стиль и профессионализм сделали его одним из самых востребованных дизайнеров в России. Ершов Арсений специализируется на создании дизайна офисов, чат-ботов сайтов и других объектов, связанных с графическим дизайном. Он проявляет большую креативность и глубокое понимание технологий, которые используются в современном дизайне. Его работы отличаются высоким качеством и инновационными решениями, которые помогают клиентам достичь их бизнес-целей. Ершов Арсений также известен своей способностью слушать клиента и понимать их потребности, чтобы создавать дизайн, который наилучшим образом отвечает их требованиям. Он постоянно отслеживает последние тенденции и новые технологии в индустрии, чтобы обеспечивать своих клиентов самыми передовыми решениями в графическом дизайне. Кроме того, Ершов Арсений является активным участником сообщества дизайнеров, участвует в многих мероприятиях и конференциях по дизайну, что помогает ему быть в курсе последних тенденций и лучших практик. В целом, Ершов Арсений Александрович - это опытный и талантливый дизайнер, который обладает всеми необходимыми навыками, чтобы создавать впечатляющие и эффективные дизайны для своих клиентов.')
            time.sleep(2)
            start(message)
        elif (message.text == 'Бэкэнд'):
            bot.send_message(message.chat.id,
                             'Алексей Доронин Владимирович - опытный backend разработчик, который работает в сфере IT уже много лет. Он специализируется на backend разработке, и его опыт и знания в этой области являются ключевыми факторами успеха в его карьере. Алексей Доронин является экспертом в использовании языков программирования, таких как C#, CSS, JavaScript, TypeScript. Он также обладает глубокими знаниями в области баз данных и взаимодействия между компонентами backend и frontend веб-приложений. Он проявляет большую креативность и инновационный подход в своей работе. Он всегда ищет новые и более эффективные способы решения задач, связанных с backend разработкой. Его решения отличаются высоким качеством и производительностью. Алексей Доронин является частью команды разработчиков, и его коммуникационные навыки и умение работать в коллективе являются ключевыми для успешного завершения проектов. Он также готов делиться своими знаниями и опытом с другими членами команды, чтобы обеспечить лучший результат для проекта. В целом, Алексей Доронин Владимирович - это опытный и талантливый backend разработчик, который обладает всеми необходимыми навыками и знаниями для создания высококачественных, эффективных и инновационных backend решений для своих клиентов и команды.')
            time.sleep(2)
            start(message)
    except:
        bot.send_message(message.chat.id, '<b>Не понял!</b>', parse_mode='html')

@bot.message_handler(commands=['learning'])
def learning(message):
    try:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Изучение программирования')
        btn2 = types.KeyboardButton('Изучение работы с клиентами')
        btn3 = types.KeyboardButton('Изучение проектной деятельности')
        markup.add(btn1, btn2, btn3)
        helo = f'<b>Приветcвуем, {message.from_user.first_name}! С чем вы хотите познакомится?</b>'
        bot.send_message(message.chat.id, helo, parse_mode='html', reply_markup=markup)
        bot.register_next_step_handler(message, select1)
    except:
        bot.send_message(message.chat.id, '<b>Не понял!</b>', parse_mode='html')

def select1(message):
    try:
        if (message.text == 'Изучение работы с клиентами'):
            markup = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton("Учебник", url='https://vc.ru/marketing/282775-kak-obshchatsya-s-klientami/')
            markup.add(btn1)
            bot.send_message(message.chat.id, "Вот учебник:", reply_markup=markup)
            time.sleep(2)
            start(message)
        elif (message.text == 'Изучение проектной деятельности'):
            markup = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton("Учебник", url='https://www.atlassian.com/ru/work-management/project-collaboration/')
            markup.add(btn1)
            bot.send_message(message.chat.id, "Вот учебник:", reply_markup=markup)
            time.sleep(2)
            start(message)
        elif (message.text == 'Изучение программирования'):
            markup = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton("Учебник", url='https://pythontutor.ru/')
            markup.add(btn1)
            bot.send_message(message.chat.id, "Вот учебник:", reply_markup=markup)
            time.sleep(2)
            start(message)
    except:
        bot.send_message(message.chat.id, '<b>Не понял!</b>', parse_mode='html')

def productcs(message):
    try:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Продукт компании')
        btn2 = types.KeyboardButton('Услуги компании')
        btn3 = types.KeyboardButton('Информация о компании')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, f'Выбери что ты хочешь', reply_markup=markup)
        bot.register_next_step_handler(message, info)
    except:
        bot.send_message(message.chat.id, 'Не понял!', parse_mode='html')

def info(message):
    try:
        if (message.text == 'Продукт компании'):
            bot.send_message(message.chat.id, 'Telegram боты для компаний для проведения onboarding сотрудников')
            time.sleep(2)
            start(message)
        elif (message.text == 'Услуги компании'):
            bot.send_message(message.chat.id, 'Разработка Telegram ботов')
            time.sleep(2)
            start(message)
        elif (message.text == 'Информация о компании'):
            bot.send_message(message.chat.id, 'BracerIncorporation - это ведущая IT-компания, специализирующаяся на разработке заказных приложений, сайтов, ботов и других IT-решений для различных компаний. Компания имеет высококвалифицированных сотрудников, включая главных backend и frontend разработчиков, а также опытного project менеджера. Команда разработчиков BracerIncorporation, во главе с главным backend разработчиком Алексеем Дорониным Владимировичем, обладает широким спектром знаний и опыта в различных языках программирования, таких как C#, CSS, JavaScript, TypeScript. Они разрабатывают высококачественные и инновационные IT-решения, соответствующие требованиям и ожиданиям клиентов. Главный frontend разработчик Макаров Клим Олегович в команде BracerIncorporation отвечает за разработку фронтенд-части проектов, таких как телеграмм боты, сайты и программы. Его опыт в различных языках программирования, таких как Python, C++ и Kotlin, позволяет ему создавать инновационные и пользовательски дружественные интерфейсы, соответствующие требованиям клиентов и современным технологическим стандартам.')
            time.sleep(2)
            start(message)
    except:
        bot.send_message(message.chat.id, '<b>Не понял!</b>', parse_mode='html')

bot.polling(none_stop=True)