from telegram.ext import Updater
from telegram.ext import CommandHandler

from features import generateOffense
from features import generateOffensePerson
from features import timeHelper, blackListManager

import core

def callback_minute(context):
        if timeHelper.get_actual_time() >=0 and timeHelper.get_actual_time() <=7:
            return
        if not core.bender_bot.mute:
            chat_id=context.job.context
            context.bot.send_message(chat_id=chat_id, 
                                    text=generateOffense.generateOffense())


def start(update, context):
    #context.bot.send_message(chat_id=update.message.chat_id,
                        #text="")

    if not core.bender_bot.offenseOn and not (timeHelper.get_actual_time() >=0 and timeHelper.get_actual_time() <=7):
        core.bender_bot.offenseOn = True
        context.job_queue.run_repeating(callback_minute, interval=3600, first=1,
                                            context=update.message.chat_id)
    else:
        if not (timeHelper.get_actual_time() >=0 and timeHelper.get_actual_time() <=7):
            context.bot.send_message(chat_id=update.effective_chat.id, 
                                    text="Seu degenerado! Alguém já deu start em mim! " +
                                        "Se você quer tanto assim que eu te humilhe, espere a sua vez!")

def mute_(update, context):
    blackListManager.free_members()
    member_in_blacklist = blackListManager.is_member_in_blacklist(update.message.from_user.first_name, "mute")
    
    if member_in_blacklist:
        return
    else:
        blackListManager.add_member(update.message.from_user.first_name, "mute")
    
    if core.bender_bot.mute:
        pass
    else:
        core.bender_bot.mute = True
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                            text= "Ok... Ok... Estou calando a boca!")
    
def unmute(update, context):
    if not core.bender_bot.mute:
        pass
    else:       
        core.bender_bot.mute = False
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                    text= "I'm back, bitches! Mordam a minha bunda de metal!")
    
def help(update, context):
    blackListManager.free_members()
    member_in_blacklist = blackListManager.is_member_in_blacklist(update.message.from_user.first_name, "help")
    
    if member_in_blacklist:
        return
    else:
        blackListManager.add_member(update.message.from_user.first_name, "help")
    
    context.bot.send_message(chat_id=update.effective_chat.id, 
                                        text= "LISTA DE COMANDOS:\n" +
                                        "/start -> Comando para que eu envie xingamentos a cada 1h\n"+
                                        "/mute_ -> Comando para eu calar a minha boca\n" +
                                        "/unmute -> Comando para que eu volte a xingar vocês\n" +
                                        "/help -> Comando que exibe esta lista de comandos\n\n" +
                                        "ATENÇÃO\n"+
                                        "Se eu ficar xingando de madrugada, basta usar o comando /mute_\n"+
                                        "Se eu apresentar mal funcionamento, fale com os idiotas que cuidam da minha manutenção:\n"+
                                        "Natalia, André e Felipe\n\n"+
                                        "E tenho dito!")