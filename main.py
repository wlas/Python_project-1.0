from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


app = ApplicationBuilder().token("5775290558:AAEB5lWXsO8LBqnai2JqmxzwTRNdgNX6GEo").build()

app.add_handler(CommandHandler("hello", hello))
print('server start')
app.run_polling()