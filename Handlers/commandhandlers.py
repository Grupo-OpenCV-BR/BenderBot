from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from telegram.utils import helpers

import core
from features import generateOffense
from features import timeHelper

SO_COOL = "so-cool"


def callback_minute(context):
    if timeHelper.get_actual_time() >= 0 and timeHelper.get_actual_time() <= 7:
        return
    if not core.bender_bot.mute:
        chat_id = context.job.context
        context.bot.send_message(chat_id=chat_id,
                                 text=generateOffense.generateOffense())


def start(update, context):
    if not core.bender_bot.offenseOn and not (0 <= timeHelper.get_actual_time() <= 7):
        core.bender_bot.offenseOn = True
        context.job_queue.run_repeating(callback_minute, interval=3600, first=1,
                                        context=update.message.chat_id)
    else:
        if not (timeHelper.get_actual_time() >= 0 and timeHelper.get_actual_time() <= 7):
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text="Seu degenerado! Alguém já deu start em mim! " +
                                          "Se você quer tanto assim que eu te humilhe, espere a sua vez!")


def eventos(update, context):
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open("images/420947.jpg", "rb"))
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=f"@{update.effective_chat.username} o(s) próximo(s) evento(s)\n\n" +
                                    "Tem evento Humanos \n\n" +
                                    "E ai rapaziada, O Matheus falará sobre visão computacional e ele tem muito conhecimento na área, vale super a pena ver. \n\n" +
                                    "Live sobre Visão computacional com  Matheus Barcelos Especialista em Visão Computacional e Engenheiro de Inteligência Artificial \n\n" +
                                    "Horário: 20h30 \n\n" +
                                    "Data: 16/06/2022 \n\n" +
                                    "Canal: https://www.youtube.com/watch?v=ydlpV7gf_lQ \n\n" +
                                    "# E vão estudar bando de baderneiros !!")

def repo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Nossos repositórios\n\n" +
                                  "Grupo-OpenCV-BR -> https://github.com/Grupo-OpenCV-BR \n\n" +
                                  "Tutoriais e Dicas -> https://grupo-opencv-br.github.io/tutoriais-tecnologia/ \n\n" +
                                  "Desafios -> https://github.com/Grupo-OpenCV-BR/desafios \n\n" +
                                  "Imagens Médicas -> https://grupo-opencv-br.github.io/imagens-medicas/ \n\n" +
                                  "Prova e testes -> https://github.com/Grupo-OpenCV-BR/provas-testes \n\n" +
                                  "CookBook -> https://grupo-opencv-br.github.io/ \n\n" +
                                  "Claro , o repositório mais importante -> https://github.com/Grupo-OpenCV-BR/BenderBot \n\n" +
                                  "A contribuição é aberta, só mandar a PR que a @natalia_py e o @andreemidio1 aprovam\n\n " +
                                  "Se eu apresentar mal funcionamento, fale com os idiotas que cuidam da minha manutenção:\n" +
                                  "@ natalia_py, @andreemidio1 , @ TioPerneta e @ hugueds \n\n\n\n" +
                                  "# E vão estudar bando de baderneiros !!")


    
def facematch(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Facematch\n\n" +
                                  "Basicamente é comparar uma face com seu banco de dados de face e assim validar aquela pessoa \n\n" +
                                  "Essas referências são boas para segurança (Validação da face ), onde você pode usar \n\n" + 
                                  "Referências teóricas \n\n" +
                                  "OpenFace  ->https://cmusatyalab.github.io/openface/ \n\n" +
                                  "What is Face Detection? – The Ultimate Guide for 2022  -> https://learnopencv.com/what-is-face-detection-the-ultimate-guide/ \n\n" +
                                  "Lib Python \n\n" +
                                  "deepface -> https://github.com/serengil/deepface \n\n" )

   
def medicas(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Imagens Médicas \n\n" +                              
                                  "Uma referência sobre processamento de imagens médicas \n\n" + 
                                  "Imagens Médicas  ->https://grupo-opencv-br.github.io/imagens-medicas/ \n\n"
                            )
def tutoriais(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Tutoriais e Dicas \n\n" +                              
                                  "Uma referência sobre Visão Computacional \n\n" + 
                                  "Tutoriais e Tecnologia -> https://grupo-opencv-br.github.io/tutoriais-tecnologia/ \n\n"
                            )
 

    
def vagas(update, context):
    bot = context.bot
    url = helpers.create_deep_linked_url(bot.username, SO_COOL)

    keyboard = InlineKeyboardMarkup.from_button(
        InlineKeyboardButton("Só me chame se nunca falou comigo rs", url=url)
    )

    context.bot.send_message(chat_id=update.effective_chat.id, text="Humano para receber vagas me chame no privado.",
                             reply_markup=keyboard)

    context.bot.send_message(chat_id=update.effective_user.id,
                             text="Vagas de Visão Computacional \n\n" +
                                  "Visão Computacional -> https://www.linkedin.com/jobs/search/?geoId=106057199&keywords=%22Vis%C3%A3o%20computacional%22%20%22OpenCV%22&location=Brasil" +
                                  "A Até conseguirmos criar uma plataforma de visualização dessas vagas aqui no grupo, iremos usar o link acima.\n\n " +
                                  "Se eu apresentar mal funcionamento, fale com os idiotas que cuidam da minha manutenção:\n" +
                                  "@ natalia_py, @andreemidio1 , @ TioPerneta e @ hugueds \n\n" +
                                  "Parem de vacilação e corram atrás, se você não for, você é um bundão !! \n\n")


def mute_(update, context):
    # blackListManager.free_members()
    # member_in_blacklist = blackListManager.is_member_in_blacklist(update.message.from_user.first_name, "mute")

    # if member_in_blacklist:
    #     return
    # else:
    #     blackListManager.add_member(update.message.from_user.first_name, "mute")
    
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
    # blackListManager.free_members()
    # member_in_blacklist = blackListManager.is_member_in_blacklist(update.message.from_user.first_name, "help")
    #
    # if member_in_blacklist:
    #     return
    # else:
    #     blackListManager.add_member(update.message.from_user.first_name, "help")
    #
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="LISTA DE COMANDOS:\n" +
                                  "/start -> Comando para que eu envie xingamentos a cada 1h\n" +
                                  "/tutoriais -> Comando para acessar Tutoriais e Tecnologia" + 
                                  "/eventos -> Comando para que eu mostre eventos.\n" +
                                  "/repo -> Comando para acessar nossos repositórios\n" +
                                  "/facematch -> Informações sobre facematch\n" +
                                  "/medicas -> Informações sobre Imagens Médicas\n" +
                                  "/vagas -> Comando para mostrar vagas de CV \n" +
                                  "/mute_ -> Comando para eu calar a minha boca\n" +
                                  "/unmute -> Comando para que eu volte a xingar vocês\n" +
                                  "/help -> Comando que exibe esta lista de comandos\n\n" +
                                  "ATENÇÃO\n" +
                                  "Se eu ficar xingando de madrugada, basta usar o comando /mute_\n" +
                                  "Se eu apresentar mal funcionamento, fale com os idiotas que cuidam da minha manutenção:\n" +
                                  "@ natalia_py, @andreemidio1, @ TioPerneta e @ hugueds \n\n" +
                                  "E tenho dito! Truuuuucccoooooooooooo Marreco !")
