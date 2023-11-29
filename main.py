import telebot

bot = telebot.TeleBot('6546962069:AAGT3pwdOtEWDAqdcK88rxYaeq_A0IAGqEo')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Привет! Мы рады видеть тебя в чате нашего бота! \nЭтот бот сделает твой день чуть-чуть счастливее, а так же предложит варианты времяпрепровождения. \nДля этого введите команды: /get, /getmore, /way или /hangout')

@bot.message_handler(commands=['get'])
def main(message):
    bot.send_message(message.chat.id, 'Ты- солнышко! У тебя всё получиться! Главное- идти к своей цели!')

@bot.message_handler(commands=['getmore'])
def main(message):
    bot.send_message(message.chat.id, 'Перейди по [ссылке](https://t.me/etoznakmag)', parse_mode='Markdown')

@bot.message_handler(commands=['way'])
def main(message):
    bot.send_message(message.chat.id, 'Этот день ты можешь провести замечательно! Сделай то, что давно хотел! Начни новое хобби, посмотри новый фмльм, сходи в то самое место!')

@bot.message_handler(commands=['hangout'])
def main(message):
    bot.send_message(message.chat.id, 'Также, ты можешь встретиться с друзьями, сходить в кафе, музей, театр или кино! \nВот кстати ссылка на тг-канал одного кинотеатра, где ты можешь найти информацию о фильмах в прокате(https://t.me/moricinema)', parse_mode='Markdown')

bot.infinity_polling()
