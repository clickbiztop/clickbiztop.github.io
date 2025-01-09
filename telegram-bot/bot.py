import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Включение логирования
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Замени 'YOUR_TOKEN' на токен, полученный от BotFather
TOKEN = '7793616855:AAGThuwR6t7T4CzVsVAisH0JDbe50MnQ8tE'

def start(update: Update, context: CallbackContext) -> None:
    """Отправляет приветственное сообщение при команде /start."""
    update.message.reply_text('Привет! Нажми /play, чтобы начать игру.')

def play(update: Update, context: CallbackContext) -> None:
    """Отправляет ссылку на игру при команде /play."""
    update.message.reply_text('Начинаем игру! Перейди по ссылке: [Игра](https://st4l1f3top3run.github.io/merge-3/)', parse_mode='Markdown')

def main() -> None:
    """Запускает бота."""
    # Создание объекта Updater и передача ему токена
    updater = Updater(TOKEN)

    # Получаем диспетчер для регистрации обработчиков
    dispatcher = updater.dispatcher

    # Регистрация обработчиков команд
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("play", play))

    # Запуск бота
    updater.start_polling()

    # Ожидание завершения работы
    updater.idle()

if __name__ == '__main__':
    main()
