import core
from conf.settings import BOT_NAME
from features import generateOffensePerson


def echo(update, context):

    if core.bender_bot.mute:
        return

    message = update.message.text.lower()
    chat_id = update.effective_chat.id

    if message == "oi bender":
        context.bot.send_message(chat_id=chat_id, text="Oi, vamos tomar um Velho Fortran?")

    elif message == "muito bom":
        context.bot.send_message(chat_id=chat_id,
                                 text="Qualquer coisa abaixo da imortalidade é uma perda de tempo completa!")

    elif message in ["ajuda", "ajudar"]:
        context.bot.send_message(chat_id=chat_id,
                                 text="Humanos... Sempre precisando de ajuda.. tsc.. tsc...")

    elif message in ["obrigado", "obrigada"]:
        context.bot.send_message(chat_id=chat_id,
                                 text="Como posso ser tão ruim em tudo que tento e ainda ser melhor que vocês?")

    elif message == "java":
        context.bot.send_message(chat_id=chat_id,
                                 text="Java? Esse grupo já foi melhor, hein!")

    elif message == "php":
        context.bot.send_message(chat_id=chat_id, text="PHP? Você acordou de um coma?")

    elif message in ["teoria", "teórico", "teorico"]:
        context.bot.send_message(chat_id=chat_id,
                                 text="Teoria? Tá brincando com a minha cara? " +
                                      "Bora meter a mão na porra do código!")

    elif message == "excelente":
        context.bot.send_message(chat_id=chat_id,
                                 text="Excelente? Eu sei que sou, humanos...")

    elif message in ["maquina", "pc", "computador"]:
        context.bot.send_message(chat_id=chat_id,
                                 text="Sendo sincero, se teu PC fosse um microondas, " +
                                      "não rodava nem o prato.")

    elif message == "c++":
        context.bot.send_message(chat_id=chat_id,
                                 text="Vocês sabem o que o C++ disse para o C?" + "\n\n" +
                                      "Resposta: Você não tem classe!")

    elif message in ["puto", "puta"]:
        context.bot.send_photo(chat_id=chat_id, photo=open('baixa_bola.jpg', 'rb'))

    elif message == "assembly":
        context.bot.send_message(chat_id=chat_id,
                                 text="Assembly? De qual período da pré-história é você? ")

    elif message == "fortran":
        context.bot.send_message(chat_id=chat_id, text="Fortran ? É uma brasa mora ! ")

    elif message in ["projeto", "projetinho", "ideia", "interno", "parceria", "hackathon"]:    
        context.bot.send_photo(chat_id=chat_id,photo=open('fry_shut_up_and_take_my_money.jpg', 'rb'))

    elif message in ["indiano","indianos","chineses","china":    
        context.bot.send_photo(chat_id=chat_id, photo=open('JLClvEy.jpeg', 'rb'))


def welcome(update, context, new_member):
    context.bot.send_message(chat_id=chat_id,
                             text="Olá, " + str(new_member.first_name) + "!" +
                                  " Seja bem vindo ao Grupo OpenCV Brasil!\n" +
                                  "\nLeia as regras do grupo: https://github.com/Grupo-OpenCV-BR/Regras" +
                                  "\n\nConheça nosso repositório de conteúdo gratuito: https://github.com/Grupo-OpenCV-BR/tutoriais-tecnologia \n\n" +
                                  generateOffensePerson.set_xing(new_member.first_name), parse_mode="Markdown")

def goodbye(update, context):
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id=chat_id,
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
