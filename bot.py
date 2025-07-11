
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackContext, CallbackQueryHandler

TOKEN = os.getenv("TOKEN")  # Получаем токен из переменной окружения

# Кнопки главного меню
def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("🎁 Получить бесплатный урок", callback_data='free_lesson')],
        [InlineKeyboardButton("📅 Записаться на консультацию", callback_data='consult')],
        [InlineKeyboardButton("👩‍🍳 Клуб тарелочниц", callback_data='club')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    text = (
        "Привет! 👋\n\n"
        "Чем могу быть полезна:\n"
        "— Бесплатный урок «Как снизить вес здорОво раз и навсегда»\n"
        "— Консультация\n"
        "— Индивидуальное сопровождение\n"
        "— Секретный «Клуб тарелочниц» 🍽️\n\n"
        "Выбери, что тебя интересует:"
    )

    update.message.reply_text(text, reply_markup=reply_markup)

# Обработка нажатий кнопок
def button_handler(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    if query.data == 'free_lesson':
        query.message.reply_text("📨 Отправляю бесплатный урок...\n[Ссылка на урок](https://example.com)", parse_mode='Markdown')

    elif query.data == 'consult':
        query.message.reply_text(
            "📋 Запишись на консультацию:\nЗаполни форму, и я с тобой свяжусь 💬\n\n"
            "[Форма записи](https://forms.gle/example)", parse_mode='Markdown')

    elif query.data == 'club':
        query.message.reply_text(
            "👩‍🍳 «Клуб тарелочниц» — это:\n"
            "• Еженедельные созвоны\n"
            "• Поддержка единомышленниц\n"
            "• Доступ к закрытым материалам\n\n"
            "💳 Инструкция по оплате:\nПереведи 1990₽ на [СБП/счёт/карта], и пришли скрин в ответ.\nПосле оплаты — я дам доступ в клуб."
        )

# Запуск бота
def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("Бот запущен...")
    app.run_polling()

if __name__ == "__main__":
    main()
