import random

import core
from config.settings import BOT_NAME
from features import generateOffensePerson


def echo(update, context):

    if core.bender_bot.mute:
        return
    if (
            update.message.text == "Bender, tu é?" or
            update.message.text == "bender tu é?" or
            update.message.text == "Bender tu e" or
            update.message.text == "Bender, tu e ?" or
            update.message.text == "Bender, tu e ?"

    ):
        text = ["Não sou você Humano !",
                "Para com essas ideias",
                "Não sou seu reflexo "
                ]

        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=random.choice(text))



    elif (
            update.message.text == "bender" or
            update.message.text == "Bender" or
            update.message.text == "Bneder" or
            update.message.text == "bneder"

    ):
        text = ["Que foi humano ?",
                "Fala humano",
                "Oi ?!"
                ]

        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=random.choice(text))

    elif (
            update.message.text == "bender" or
            update.message.text == "Bender" or
            update.message.text == "Bneder"

    ):
        text = ["Que foi humano ?",
                "Fala humano",
                "Oi ?!"
                ]

        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=random.choice(text))

    elif (
            update.message.text == "Boa noite bender" or
            update.message.text == "Bender boa noite " or
            update.message.text == "bender boa noite" or
            update.message.text == "boa noite Bender" or
            update.message.text == "Boa Noite Bender"
    ):

        text = ["Vai humano !"]

        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=random.choice(text))

    elif (
            update.message.text == "Bender você é desprezível" or
            update.message.text == "bender, você é desprezível" or
            update.message.text == "bender você e desprezível" or
            update.message.text == "bender você é desprezível" or
            update.message.text == "Bender, você é desprezível"
    ):
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Ei não sou espelho, olhe para você humano desprezível")

    elif (
            update.message.text == "Oi Bender" or
            update.message.text == "oi bender" or
            update.message.text == "Oi bender" or
            update.message.text == "oi Bender"
    ):
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Oi, vamos tomar um Velho Fortran?")

    elif (
            "Muito Bom" in update.message.text or
            "muito bom" in update.message.text or
            "Muito bom" in update.message.text or
            "muito Bom" in update.message.text
    ):
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Qualquer coisa abaixo da imortalidade é uma perda de tempo completa!")

    elif (
            "ajuda" in update.message.text or
            "Ajuda" in update.message.text or
            "ajudar" in update.message.text or
            "Ajudar" in update.message.text
    ):
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Humanos... Sempre precisando de ajuda.. tsc.. tsc...")

    elif (
            "obrigado" in update.message.text or
            "Obrigado" in update.message.text or
            "obrigada" in update.message.text or
            "Obrigada" in update.message.text
    ):

        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Como posso ser tão ruim em tudo que tento e ainda ser melhor que vocês?")

    elif (
            "GO" in update.message.text or
            "go" in update.message.text or
            "Go" in update.message.text

    ):

        text = ["Go go go Power Ranger !",
                "Go para onde Humano ?",
                "Go Pher Gof Gof "
                ]

        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=random.choice(text))

    elif (
            "Julia" in update.message.text or
            "julia" in update.message.text

    ):

        text = ["Quem é Julia ?!"]

        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=random.choice(text))


    elif (
            "Fuck you Bender Bot Rodrigues" in update.message.text or
            "fuck you bender bot rodrigues" in update.message.text or
            "fuck you" in update.message.text or
            "fuck you bender" in update.message.text or
            "Fuck you bender bot" in update.message.text or
            "Fuck You" in update.message.text

    ):

        text = ["Fuck you? Fuck tu, fuck eu, fuck todo mundo  !!"]

        context.bot.send_message(chat_id=update.effective_chat.id,

                                 text=random.choice(text))


    elif (
            "MATLAB" in update.message.text or
            "matlab" in update.message.text

    ):

        text = ["Ai você está de sacanagem Humano !!",
                "Mat o quê ? Matemática"
                ]

        context.bot.send_message(chat_id=update.effective_chat.id,

                                 text=random.choice(text))

    elif (
            "Python" in update.message.text or
            "python" in update.message.text or
            "py" in update.message.text

    ):

        text = ["O pytaon !!"]

        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=random.choice(text))

    elif (
            "java" in update.message.text or
            "Java" in update.message.text
    ):
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Java? Esse grupo já foi melhor, hein!")

    elif (
            "PHP" in update.message.text or
            "php" in update.message.text
    ):
        context.bot.send_message(chat_id=update.effective_chat.id,
                             text="PHP? Você acordou de um coma?")

    elif (
            "Teoria" in update.message.text or
            "teoria" in update.message.text or
            "Teórico" in update.message.text or
            "teórico" in update.message.text
    ):
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Teoria? Tá brincando com a minha cara? " +
                                      "Bora meter a mão na porra do código!")

    elif ("Excelente" in update.message.text or "excelente" in update.message.text):
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Excelente? Eu sei que sou, humanos...")

    elif (
            "Máquina" in update.message.text or
            "máquina" in update.message.text or
            "Maquina" in update.message.text or
            "maquina" in update.message.text or
            "PC" in update.message.text or
            "pc" in update.message.text or
            "Computador" in update.message.text or
            "computador" in update.message.text
    ):
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Sendo sincero, se teu PC fosse um microondas, " +
                                      "não rodava nem o prato.")

    elif (
            "C++" in update.message.text or
            "c++" in update.message.text
    ):
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Vocês sabem o que o C++ disse para o C?" + "\n\n" +
                                      "Resposta: Você não tem classe!")


    if message == "oi bender":
        context.bot.send_message(
            chat_id=chat_id, text="Oi, vamos tomar um Velho Fortran?"
        )

    elif message == "muito bom":
        context.bot.send_message(
            chat_id=chat_id,
            text="Qualquer coisa abaixo da imortalidade é uma perda de tempo completa!",
        )

    elif message in ["ajuda", "ajudar"]:
        context.bot.send_message(
            chat_id=chat_id, text="Humanos... Sempre precisando de ajuda.. tsc.. tsc..."
        )

    elif message in ["obrigado", "obrigada"]:
        context.bot.send_message(
            chat_id=chat_id,
            text="Como posso ser tão ruim em tudo que tento e ainda ser melhor que vocês?",
        )

    elif message == "java":
        context.bot.send_message(
            chat_id=chat_id, text="Java? Esse grupo já foi melhor, hein!"
        )

    elif message == "php":
        context.bot.send_message(chat_id=chat_id, text="PHP? Você acordou de um coma?")

    elif message in ["teoria", "teórico", "teorico"]:
        context.bot.send_message(
            chat_id=chat_id,
            text="Teoria? Tá brincando com a minha cara? "
            + "Bora meter a mão na porra do código!",
        )

    elif message == "excelente":
        context.bot.send_message(
            chat_id=chat_id, text="Excelente? Eu sei que sou, humanos..."
        )

    elif message in ["maquina", "pc", "computador"]:
        context.bot.send_message(
            chat_id=chat_id,
            text="Sendo sincero, se teu PC fosse um microondas, "
            + "não rodava nem o prato.",
        )

    elif message == "c++":
        context.bot.send_message(
            chat_id=chat_id,
            text="Vocês sabem o que o C++ disse para o C?"
            + "\n\n"
            + "Resposta: Você não tem classe!",
        )

    elif message in ["puto", "puta"]:
        context.bot.send_photo(chat_id=chat_id, photo=open("images/baixa_bola.jpg", "rb"))

    elif message == "assembly":
        context.bot.send_message(
            chat_id=chat_id, text="Assembly? De qual período da pré-história é você? "
        )

    elif message == "fortran":
        context.bot.send_message(chat_id=chat_id, text="Fortran ? É uma brasa mora ! ")

    elif message in [
        "projeto",
        "projetinho",
        "ideia",
        "interno",
        "parceria",
        "hackathon",
    ]:
        context.bot.send_photo(
            chat_id=chat_id, photo=open("images/fry_shut_up_and_take_my_money.jpg", "rb")
        )
    
    elif message in [
        "Preciso de Ajuda",
        "Alguém me ajuda",
        "Alguém me ajuda",
        "E tô precisando de ajuda",
        "Eu tô precisando de ajuda",
        
    ]:
        context.bot.send_photo(
            chat_id=chat_id, photo=open("images/send_my_burguer_image.jpg", "rb")
        )


    elif message in ["indiano", "indianos", "chineses", "china"]:
        context.bot.send_photo(chat_id=chat_id, photo=open("images/fry_shut_up_and_take_my_money_v2.jpg", "rb"))

def welcome(update, context, new_member):
    context.bot.send_message(
        chat_id=chat_id,
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
