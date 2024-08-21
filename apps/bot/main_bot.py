import asyncio
from telebot.async_telebot import AsyncTeleBot
from django.conf import settings

bot = AsyncTeleBot(token=settings.TOKEN_BOT, parse_mode="HTML")


# Handle '/start' and '/help'
@bot.message_handler(commands=["help", "start"])
async def send_welcome(message):
    text = "Привет! Добро пожаловать!\nКакой у вас вопрос?"
    await bot.send_message(message.chat.id, text)


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
async def echo_message(message):
    await bot.reply_to(message, message.text)


asyncio.run(bot.polling())