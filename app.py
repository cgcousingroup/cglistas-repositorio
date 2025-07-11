from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = '7208398050:AAEUpN7mK6UStxlfGyizedW-i2amVcaQTmE'
SUPORTE_USERNAME = '@supvipoficial'
LINK_PAGAMENTO = 'https://app.pushinpay.com.br/service/pay/9f4851ac-8054-4e0e-be14-19455a348fe1'  # Substitua pelo seu link real

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mensagem = (
        f"🔥 Para se tornar VIP, faça o pagamento pelo link abaixo:\n\n"
        f"{LINK_PAGAMENTO}\n\n"
        f"✅ Após o pagamento, envie o comprovante para: {SUPORTE_USERNAME}"
    )
    await update.message.reply_text(mensagem)

async def receber_comprovante(update: Update, context: ContextTypes.DEFAULT_TYPE):
    suporte_chat = await context.bot.get_chat(SUPORTE_USERNAME)
    for photo in update.message.photo:
        await context.bot.forward_message(chat_id=supporte_chat.id,
                                          from_chat_id=update.message.chat_id,
                                          message_id=update.message.message_id)
        break
    await update.message.reply_text("📩 Comprovante enviado ao suporte. Obrigado!")

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.PHOTO & (~filters.COMMAND), receber_comprovante))

    print("Bot rodando...")
    app.run_polling()

if __name__ == "__main__":
    main()
