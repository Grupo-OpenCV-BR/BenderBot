import core
import re
from Handlers import dados
from config.settings import BOT_NAME
from features import generateOffensePerson


def echo(update, context):
    if core.bender_bot.mute:
        return

    message = update.message.text.lower()
    chat_id = update.effective_chat.id

    if  "oi bender" in message or "bender" in message :
        context.bot.send_message(
            chat_id=chat_id, text="Oi, vamos tomar um Velho Fortran?"
        )

    elif "boa noite" in message:
        context.bot.send_message(
            chat_id=chat_id,
            text="Vai humano !",
        )

    elif "bom dia" in message:
        context.bot.send_message(
            chat_id=chat_id,
            text="Tá com tempo humano ?!?!",
        )

    elif "boa tarde" in message:
        context.bot.send_message(
            chat_id=chat_id,
            text="É, tá com muito tempo mesmo ?!?!",
        )

    elif "delphi" in message:
        context.bot.send_message(
            chat_id=chat_id,
            text="É, tá com muito tempo mesmo ?!?!",
        )

    elif "muito bom" in message:
        context.bot.send_message(
            chat_id=chat_id,
            text="Qualquer coisa abaixo da imortalidade é uma perda de tempo completa!",
        )

    elif "ajuda" in message:
        context.bot.send_message(
            chat_id=chat_id, text="Humanos... Sempre precisando de ajuda.. tsc.. tsc..."
        )

    elif "obrigad" in message:
        context.bot.send_message(
            chat_id=chat_id,
            text="Como posso ser tão ruim em tudo que tento e ainda ser melhor que vocês?",
        )

    elif "java" in message:
        context.bot.send_message(
            chat_id=chat_id, text="Java? Esse grupo já foi melhor, hein!"
        )

    elif "php" in message:
        context.bot.send_message(
            chat_id=chat_id, text="PHP? Você acordou de um coma?")

    elif "teori" in message:
        context.bot.send_message(
            chat_id=chat_id,
            text="Teoria? Tá brincando com a minha cara? "
                 + "Bora meter a mão na porra do código!",
        )

    elif "excelente" in message:
        context.bot.send_message(
            chat_id=chat_id, text="Excelente? Eu sei que sou, humanos..."
        )

    elif "maquina" in message or "pc" in message or "computador" in message:
        context.bot.send_message(
            chat_id=chat_id,
            text="Sendo sincero, se teu PC fosse um microondas, "
                 + "não rodava nem o prato.",
        )

    elif "c++" in message:
        context.bot.send_message(
            chat_id=chat_id,
            text="Vocês sabem o que o C++ disse para o C?"
                 + "\n\n"
                 + "Resposta: Você não tem classe!",
        )

    elif "puto" in message or "puta" in message:
        context.bot.send_photo(chat_id=chat_id, photo=open(
            "images/baixa_bola.jpg", "rb"))

    elif "assembly" in message:
        context.bot.send_message(
            chat_id=chat_id, text="Assembly? De qual período da pré-história é você? "
        )

    elif "fortran" in message:
        context.bot.send_message(
            chat_id=chat_id, text="Fortran ? É uma brasa mora ! ")

    elif "projeto" in message or "projetinho" in message or "ideia" in message or "interno" in message or "parceria" in message or "hackathon" in message:
        context.bot.send_photo(
            chat_id=chat_id, photo=open(
                "images/fry_shut_up_and_take_my_money.jpg", "rb")
        )

    elif "Preciso de Ajuda" in message or "Alguém me ajuda" in message or "Alguem me ajuda" in message or "alguem me ajuda" in message or "alguém me ajuda" in message:
        context.bot.send_photo(chat_id=chat_id, photo=open(
            "images/send_my_burguer_image.jpg", "rb"))

    elif "indian" in message or "chineses" in message or "china" in message:
        context.bot.send_photo(chat_id=chat_id, photo=open(
            "images/fry_shut_up_and_take_my_money_v2.jpg", "rb"))

    # elif '#evento' in message:
        #file_id = message.document.file_id
        #newFile = bot.get_file(file_id)
        # newFile.download()

        #update.message.reply_text("Image received")

        # dates = re.findall(
        #    '([1-9]|1[0-9]|2[0-9]|3[0-1]|0[0-9])(.|-|\/)([1-9]|1[0-2]|0[0-9])(.|-|\/)(20[0-9][0-9])', message)

        #dates = [''.join(dates[i]) for i in range(len(dates))]

        # print(dates)

        # pattern = r'(?:#?\b\w\w+\b)'
        #pattern = re.compile(pattern)
        #results = pattern.findall(message)

        #novo_texto = " ".join(results[1:-1])
        # print(novo_texto)

        # data = dict(
        #    data=dates[0],
        #    Nome=novo_texto,
        #    Link=novo_texto)

        #dados.salva('eventos', data)


def welcome(update, context, new_member):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Olá, "
             + str(new_member.first_name)
             + "!"
             + " Seja bem vindo ao Grupo OpenCV Brasil!\n"
             + "\nLeia as regras do grupo: https://github.com/Grupo-OpenCV-BR/Regras"
             + "\n\nConheça nosso repositório de conteúdo gratuito: https://github.com/Grupo-OpenCV-BR/tutoriais-tecnologia \n\n"
             + generateOffensePerson.set_xing(new_member.first_name),
        parse_mode="Markdown",
    )


def goodbye(update, context):
    chat_id = update.effective_chat.id
    context.bot.send_message(
        chat_id=chat_id,
        text="Este é o pior tipo de discriminação...\n" + "DISCRIMINAÇÃO CONTRA MIM!",
    )


def empty_message(update, context):
    if update.message.new_chat_members:
        for new_member in update.message.new_chat_members:
            if new_member.username != BOT_NAME:
                # Bot was added to a group chat
                return welcome(update, context, new_member)

    elif update.message.left_chat_member is not None:
        if update.message.left_chat_member.username != BOT_NAME:
            return goodbye(update, context)
