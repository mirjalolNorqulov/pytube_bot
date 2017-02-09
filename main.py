import telebot

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from pytube import YouTube
bot = telebot.TeleBot('344796659:AAGXf_gJkUxGhmJp7pihg6DjJFTd5-GX3pw')


@bot.message_handler(commands = ['start'])
def start(message):
	text = "Salom, {first_name}\nYoutube bot sizga youtube.com saytidan videoni yuklab olishingizda yordam beradi\nVideoni olish uchun menga video havola(url)sini yuboring.".format(first_name = message.from_user.first_name)
	bot.send_message(message.chat.id, text = text)

@bot.message_handler(commands = ['help'])
def start(message):
	text = "<b>Buyruqlar</b>\n<b>start<b> - ishga tushirish\n<b>help</b> - yordam\nYouTube video url sini yuboring va yuklab oling"
	bot.send_message(message.chat.id, text = text, parse_mode = "HTML")




def check_url(message):
	urls = [
		"https://youtube.com",
		"https://www.youtube.com"
	]
	return message.text.startswith(urls[0]) or message.text.startswith(urls[1])

@bot.message_handler(func = check_url)
def download(message):
	bot.send_chat_action(message.chat.id, 'typing')
	
	try:
		youtube = YouTube(message.text)
	except:
		bot.send_message(message.chat.id, text = "URL manzil noto'g'ri, iltimos qayta urinib ko'ring.")
		return
	
	youtube.get_videos()
	keyboard = InlineKeyboardMarkup(row_width = 2)
	buttons = []

	for video in youtube.videos:
		button = InlineKeyboardButton(text = video.extension + " " + video.resolution, url = video.url)
		buttons.append(button)

	keyboard.add(*buttons)

	bot.send_message(message.chat.id, text = youtube.filename, reply_markup = keyboard)
	
