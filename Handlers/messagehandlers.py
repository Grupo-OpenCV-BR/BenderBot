from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters
from conf.settings import TELEGRAM_TOKEN, BOT_NAME

from features import generateOffensePerson

import core

def echo(update, context):
    if core.bender_bot.mute:
        return
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
        
    elif ("Teoria" in update.message.text or "teoria" in update.message.text or
            "Teórico" in update.message.text or "teórico" in update.message.text):
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                        text= "Teoria? Tá brincando com a minha cara? "+
                                                "Bora meter a mão na porra do código!")
    
    elif ("Excelente" in update.message.text or "excelente" in update.message.text):
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                        text= "Excelente? Eu sei que sou, humanos...")

    elif ("Máquina" in update.message.text or "máquina" in update.message.text or
          "Maquina" in update.message.text or "maquina" in update.message.text or
          "PC" in update.message.text or "pc" in update.message.text or
          "Computador" in update.message.text or "computador" in update.message.text):
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                        text= "Sendo sincero, se teu PC fosse um microondas, " +
                                        "não rodava nem o prato.")

    elif ("C++" in update.message.text or "c++" in update.message.text):
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                        text= "Vocês sabem o que o C++ disse para o C?" + "\n\n" +
                                                "Resposta: Você não tem classe!")


def welcome(update, context, new_member):
    #user_id = new_member.id
    #user_name = new_member.username
    #mention = "["+user_name+"](tg://user?id="+str(user_id)+")"
    #print(bool(user_id))
    context.bot.send_message(chat_id=update.effective_chat.id, 
                                        text= "Olá, " + str(new_member.first_name) + "!" +
                                        " Seja bem vindo ao Grupo OpenCV Brasil!\n" +
                                        "\nLeia as regras do grupo: https://github.com/Grupo-OpenCV-BR/Regras" +
                                        "\n\nConheça nosso repositório de conteúdo gratuito: https://github.com/Grupo-OpenCV-BR/tutoriais-tecnologia \n\n" +
                                        generateOffensePerson.set_xing(new_member.first_name), parse_mode="Markdown")


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