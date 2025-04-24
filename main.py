from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove, Update,
                      InlineKeyboardButton, InlineKeyboardMarkup)
from telegram.ext import (Application, CallbackQueryHandler, CommandHandler,
                          ContextTypes, ConversationHandler, MessageHandler, filters, ApplicationBuilder)

ESTADO1, ESTADO2 = range(2)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Starts the conversation and asks the user about their preferred car type."""

    await update.message.reply_text(
        '<b>Welcome to the Car Sales Listing Bot!\n'
        'Let\'s get some details about the car you\'re selling.\n'
        'What is your car type?</b>',
        parse_mode='HTML'
    )

    return ESTADO1

async def teste(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data['car_type'] = update.message.text
    cars = {"Sedan": "🚗", "SUV": "🚙", "Sports": "🏎️", "Electric": "⚡"}
    await update.message.reply_text(
        f'<b>You selected {update.message.text}.\n'
        f'What color your car is?</b>',
        parse_mode='HTML',
    )

    await update.message.reply_text('<b>Please choose:</b>', parse_mode='HTML')

    return ESTADO2

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text('Bye! Hope to talk to you again soon.')
    return ConversationHandler.END

def main() -> None:
    app = ApplicationBuilder().token("7873152918:AAEVpEom1LF0BixCufzBLB2vi3mPKCH9iUg").build()
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            ESTADO1: [MessageHandler(filters.TEXT & ~filters.COMMAND, teste)]
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    app.add_handler(conv_handler)
    app.run_polling()

if __name__ == "__main__":
    main()