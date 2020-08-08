from telegram.ext import Updater
from conf.settings import TELEGRAM_TOKEN, BOT_NAME
from features import generateOffense
from features import generateOffensePerson
from threading import Timer

updater = Updater(token=TELEGRAM_TOKEN, use_context=True)

dispatcher = updater.dispatcher


def callback_minute(context):
    chat_id=context.job.context
    context.bot.send_message(chat_id=chat_id, 
                             text=generateOffense.generateOffense())


def start(update, context):
    #context.bot.send_message(chat_id=update.message.chat_id,
                     #text="")

    context.job_queue.run_repeating(callback_minute, interval=3600, first=1,
                                    context=update.message.chat_id)


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
    
    elif "PHP" in update.message.text or "php" in update.message.text:
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                     text= "PHP? Você acordou de um coma?")


def welcome(update, context, new_member):
    context.bot.send_message(chat_id=update.effective_chat.id, 
                                     text= "Olá, " + new_member.first_name + "!" +
                                     " Seja bem vindo ao Grupo OpenCV Brasil!\n" +
                                     "Leia as regras na mensagem fixada! " +
                                     "Lá também tem alguns links úteis!\n\n" +
                                     generateOffensePerson.set_xing(new_member.first_name))


def goodbye(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, 
                                     text= "Este é o pior tipo de discriminação...\n"+
                                            "DISCRIMINAÇÃO CONTRA MIM!")

def empty_message(update, context):
    if update.message.new_chat_members:
        for new_member in update.message.new_chat_members:
            if new_member.username != BOT_NAME:
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

