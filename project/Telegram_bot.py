import telebot
import requests
import json

bot=telebot.TeleBot('8121469774:AAGtWUWxzmp9p5T8BJAZCwAbf8q2xPElPNw')
API='820df6dccd8a86cd83805a33477dff09'


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,'Здравствуй. Напиши только название города, чтобы узнать погоду.')


@bot.message_handler(content_types=['text']) #отслеживает только текст
def get_weather(message):
    city=message.text.strip().lower()
    res=requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:
        data= json.loads(res.text)
        bot.reply_to(message, f'🌤 Погода на данный момент:\n 🌡Температура: {data["main"]["temp"]}°C\n🌡Ощущается как: {data["main"]["feels_like"]}°C\n 💧Влажность: {data['main']['humidity']}%\n 🌬 Ветер: {data['wind']['speed']} м/с\n ☁️ Облачность: {data['clouds']['all']}%')
    else:
        bot.reply_to(message,'Так нельзя')

bot.polling(none_stop=True)
