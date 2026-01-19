from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = 8326959748:AAGG4rqkj136IjGqE8rlPCSrJquWeL1sgyI
ADMIN_ID = 5712230245

jogadores = []
vagas = 48
sala = {"aberta": False, "codigo": "", "senha": ""}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔥 BOT DE SALAS FREE FIRE 🔥\nUse /entrar para participar."
    )

async def entrar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user.first_name
    if user in jogadores:
        await update.message.reply_text("Você já entrou.")
        return
    if len(jogadores) >= vagas:
        await update.message.reply_text("Sala cheia.")
        return
    jogadores.append(user)
    await update.message.reply_text("Inscrição confirmada.")

async def abrirsala(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        return
    if len(context.args) != 2:
        await update.message.reply_text("Use /abrirsala CODIGO SENHA")
        return
    sala["aberta"] = True
    sala["codigo"], sala["senha"] = context.args
    await update.message.reply_text(
        f"SALA ABERTA\nCódigo: {sala['codigo']}\nSenha: {sala['senha']}"
    )

async def sala_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not sala["aberta"]:
        await update.message.reply_text("Sala ainda não aberta.")
        return
    await update.message.reply_text(
        f"Código: {sala['codigo']}\nSenha: {sala['senha']}"
    )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("entrar", entrar))
app.add_handler(CommandHandler("abrirsala", abrirsala))
app.add_handler(CommandHandler("sala", sala_cmd))
app.run_polling()