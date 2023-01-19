import telebot
from config import keys, TOKEN
from extensions import CriptoConverter, APIException
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Чтобы начать работу введите команду боту в следующем формате:\n<имя валюты> <в какую валюту перевести> <количество переводимой валюты>\nДля получения списка валют введите /values'
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты'
    for key in keys.keys():
        text = '\n'.join((text, key))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')
        if len(values) != 3:
            raise APIException('Неверное количество параметров')
        quote, base, amount = values
        CriptoConverter.check_param(quote, base, amount)
        price_base, sum_total = CriptoConverter.get_price(quote, base, amount)
    except APIException as e:
        bot.reply_to(message, f'Ошибка пользователя\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        text = f'Цена одного {quote} в {base} - {price_base}\nСтоимость  {amount}шт. {quote} в {base}(aх) - {sum_total}'
        bot.send_message(message.chat.id, text)

bot.polling()


