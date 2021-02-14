import core
from conf.settings import BOT_NAME
from features import generateOffensePerson


def echo(update, context):
    if core.bender_bot.mute:
        return

    if (
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


    elif (
            "Puto" in update.message.text or
            "PUTO" in update.message.text or
            "PUTA" in update.message.text or
            "Puta" in update.message.text or
            "puto" in update.message.text or
            "puta" in update.message.text
    ):

        context.bot.send_photo(
            chat_id=update.effective_chat.id,
            photo=open('baixa_bola.jpg', 'rb')
        )



    elif (
            "Assembly" in update.message.text or
            "assembly" in update.message.text
    ):
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Assembly? De qual período da pré-história é você? ")

    elif (
            "Fortran" in update.message.text or
            "fortran" in update.message.text
    ) :
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Fortran ? É uma brasa mora ! ")

    elif (
            "Projeto" in update.message.text or
            "projeto" in update.message.text or
            "projetinho" in update.message.text or
            "ideia" in update.message.text or
            "interno" in update.message.text or
            "parceria" in update.message.text or
            "hackthon" in update.message.text
    ):
        context.bot.send_photo(
            chat_id=update.effective_chat.id,
            photo=open('fry_shut_up_and_take_my_money.jpg', 'rb')
        )

    elif (
            'Indiano' in update.message.text or
            'indiano' in update.message.text or
            'Indianos' in update.message.text or
            'indianos' in update.message.text or
            'chineses' in update.message.text or
            'china' in update.message.text
    ):
        context.bot.send_photo(
            chat_id=update.effective_chat.id,
            photo=open('JLClvEy.jpeg', 'rb')
        )


def welcome(update, context, new_member):
    # user_id = new_member.id
    # user_name = new_member.username
    # mention = "["+user_name+"](tg://user?id="+str(user_id)+")"
    # print(bool(user_id))
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Olá, " + str(new_member.first_name) + "!" +
                                  " Seja bem vindo ao Grupo OpenCV Brasil!\n" +
                                  "\nLeia as regras do grupo: https://github.com/Grupo-OpenCV-BR/Regras" +
                                  "\n\nConheça nosso repositório de conteúdo gratuito: https://github.com/Grupo-OpenCV-BR/tutoriais-tecnologia \n\n" +
                                  generateOffensePerson.set_xing(new_member.first_name), parse_mode="Markdown")


def goodbye(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Este é o pior tipo de discriminação...\n" +
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
