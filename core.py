from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from functools import partial
from conf.settings import TELEGRAM_TOKEN, BOT_NAME
import os

from features import generateOffense
from features import generateOffensePerson
from features import timeHelper

class Bot:

    def __init__(self, offenseOn, muteOn):
        self.offenseOn = offenseOn
        self.mute = muteOn


    def callback_minute(self, context):
        if timeHelper.get_actual_time() >=0 and timeHelper.get_actual_time() <=7:
            return
        if not self.mute:
            chat_id=context.job.context
            context.bot.send_message(chat_id=chat_id, 
                                    text=generateOffense.generateOffense())


    def start(self, update, context):
        #context.bot.send_message(chat_id=update.message.chat_id,
                        #text="")

        if not self.offenseOn and not (timeHelper.get_actual_time() >=0 and timeHelper.get_actual_time() <=7):
            self.offenseOn = True
            context.job_queue.run_repeating(self.callback_minute, interval=3600, first=1,
                                            context=update.message.chat_id)
        else:
            if not (timeHelper.get_actual_time() >=0 and timeHelper.get_actual_time() <=7):
                context.bot.send_message(chat_id=update.effective_chat.id, 
                                    text="Seu degenerado! Alguém já deu start em mim! " +
                                        "Se você quer tanto assim que eu te humilhe, espere a sua vez!")


    def echo(self, update, context):
        if self.mute:
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


    def welcome(self, update, context, new_member):
        user_id = new_member.id
        user_name = new_member.username
        mention = "["+user_name+"](tg://user?id="+str(user_id)+")"
        
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                        text= "Olá, " + mention + "!" +
                                        " Seja bem vindo ao Grupo OpenCV Brasil!\n" +
                                        "Leia as regras na mensagem fixada! " +
                                        "Lá também tem alguns links úteis!\n\n" +
                                        generateOffensePerson.set_xing(new_member.first_name), parse_mode="Markdown")


    def goodbye(self, update, context):
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                        text= "Este é o pior tipo de discriminação...\n"+
                                                "DISCRIMINAÇÃO CONTRA MIM!")

    def empty_message(self, update, context):
        if update.message.new_chat_members:
            for new_member in update.message.new_chat_members:
                if new_member.username != BOT_NAME:
                # Bot was added to a group chat
                    return self.welcome(update, context, new_member)
        
        elif update.message.left_chat_member is not None:
            if update.message.left_chat_member.username != BOT_NAME:
                return self.goodbye(update, context)
    
    def mute_(self, update, context):
        if self.mute:
            pass
        else:
            self.mute = True
            context.bot.send_message(chat_id=update.effective_chat.id, 
                                            text= "Ok... Ok... Estou calando a boca!")
    
    def unmute(self, update, context):
        if not self.mute:
            pass
        else:       
            self.mute = False
            context.bot.send_message(chat_id=update.effective_chat.id, 
                                    text= "I'm back, bitches! Mordam a minha bunda de metal!")
    
    def help(self, update, context):
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

def main():

    PORT = int(os.environ.get('PORT', 5000))
    bender_bot = Bot(False, False)
    updater = Updater(token=TELEGRAM_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', bender_bot.start)
    mute_handler = CommandHandler('mute_', bender_bot.mute_)
    unmute_handler = CommandHandler('unmute', bender_bot.unmute)
    help_handler = CommandHandler('help', bender_bot.help)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(mute_handler)
    dispatcher.add_handler(unmute_handler)
    dispatcher.add_handler(help_handler)
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TELEGRAM_TOKEN)
    updater.bot.setWebhook('https://opencv-bender.herokuapp.com/' + TELEGRAM_TOKEN)
    echo_handler = MessageHandler(Filters.text & (~Filters.command), bender_bot.echo)
    dispatcher.add_handler(echo_handler)
    sys_handler = MessageHandler(Filters.status_update, bender_bot.empty_message)
    dispatcher.add_handler(sys_handler)


if __name__ == "__main__":
    main()
