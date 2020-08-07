from telegram.ext import Updater
from conf.settings import TELEGRAM_TOKEN, BOT_NAME

updater = Updater(token=TELEGRAM_TOKEN, use_context=True)

dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, 
    text="Minha história é como a de vocês, só que mais interessante, pois envolve robôs...")

from telegram.ext import CommandHandler
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()

def echo(update, context):
    if (update.message.text == "Oi Bender" or update.message.text == "oi bender" or
        update.message.text == "Oi bender" or update.message.text == "oi Bender"):
        context.bot.send_message(chat_id=update.effective_chat.id, 
        text= "Oi, vamos tomar um Velho Fortran?")
    
    elif ("Muito Bom" in update.message.text or "muito bom" in update.message.text or
          "Muito bom" in update.message.text or "muito Bom" in update.message.text):
            context.bot.send_message(chat_id=update.effective_chat.id, 
                                     text= "Qualquer coisa abaixo da imortalidade é uma perda de tempo completa!")
    
    elif ("ajuda" in update.message.text or "Ajuda" in update.message.text or
          "ajudar" in update.message.text or "Ajudar" in update.message.text):
          context.bot.send_message(chat_id=update.effective_chat.id, 
                                     text= "Humanos... Sempre precisando de ajuda.. tsc.. tsc...")
    
    elif ("obrigado" in update.message.text or "Obrigado" in update.message.text or
          "obrigada" in update.message.text or "Obrigada" in update.message.text):
          
          context.bot.send_message(chat_id=update.effective_chat.id, 
                                     text= "Como posso ser tão ruim em tudo que tento e ainda ser melhor que vocês?")
    
    elif "java" in update.message.text or "Java" in update.message.text:
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                     text= "Java? Esse grupo já foi melhor, hein!")
    
    else:
        print(update.message.text)


def welcome(update, context, new_member):
    context.bot.send_message(chat_id=update.effective_chat.id, 
                                     text= "Olá, " + new_member.first_name + "!" +
                                     " Seja bem vindo ao Grupo OpenCV Brasil!\n" +
                                     "Leia as regras na mensagem fixada! " +
                                     "Lá também tem alguns links úteis!\n\n" +
                                     "E não se esqueça: Eu vim aqui com um sonho simples ... Um sonho de matar todos os humanos!")


def goodbye(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, 
                                     text= "Este é o pior tipo de discriminação...\n"+
                                            "DISCRIMINAÇÃO CONTRA MIM!")

def empty_message(update, context):
    if update.message.new_chat_members:
        for new_member in update.message.new_chat_members:
            if update.message.left_chat_member.username != BOT_NAME:
            # Bot was added to a group chat
                return welcome(update, context, new_member)
    
    elif update.message.left_chat_member is not None:
        if update.message.left_chat_member.username != BOT_NAME:
            return goodbye(update, context)


from telegram.ext import MessageHandler, Filters
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)
sys_handler = MessageHandler(Filters.status_update, empty_message)
dispatcher.add_handler(sys_handler)

