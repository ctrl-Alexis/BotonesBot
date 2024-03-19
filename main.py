
import telebot
##esto es un comentario
from telebot import types
from telebot.types import ForceReply
from telebot.types import ReplyKeyboardMarkup
import telebot
from telebot import types

# CONEXION CON EL BOT
TOKEN = '7105004298:AAFPHV1rURHtGGvw-fsabi0nTz0kmQhyqyc'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help', 'ayuda'])
def cmd_start(message):
    bot.send_message(message.chat.id, "Usa el comando /alta para introducir datos")

@bot.message_handler(commands=['alta'])
def cmd_alta(message):
    markup = types.ForceReply()
    bot.send_message(message.chat.id, "¿Cómo te llamas?", reply_markup=markup)
    bot.register_next_step_handler(message, preguntar_sexo)

def preguntar_sexo(message):
    if not message.text.isdigit():
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add("/start", "/help","Hombre")
        msg = bot.send_message(message.chat.id, '¿Cuál es tu sexo?', reply_markup=markup)
        bot.register_next_step_handler(msg, procesar_sexo)
    else:
        bot.send_message(message.chat.id, 'Error: Debes indicar un género válido (Hombre o Mujer).')
        bot.register_next_step_handler(message, preguntar_sexo)

def procesar_sexo(message):
    sexo = message.text
    # Aquí puedes realizar cualquier acción necesaria con el género proporcionado
    bot.send_message(message.chat.id, f'Tu género es: {sexo}')

if __name__ == "__main__":
    bot.polling(none_stop=True)




