import random

def set_xing(nome):
    classificador = [
        'pessoa',
        'criatura',
        'criatura']

    xingneutro = [
        'imbecil',
        'idiota',
        'palerma',
        'pateta',
        'boçal',
        'ignorante',
        'besta',
        'torpe',
        'canalha',
        'vigarista',
        'mau-caráter',
        'indecente',
        'imoral',
        'sem-vergonha',
        'parasita',
        'patife',
        'desprezível',
        'infame',
        'execrável',
        'repugnante',
        'imprestável',
        'abominável']
        
    exagero = [
        'que eu já vi',
        'do mundo',
        'da face da Terra',
        'de todos os tempos',
        'que este país já viu',
        'que eu tive o desprazer de conhecer',
        'que já existiu']
        

    conclusao = [
        'Não presta.',
        'Nunca fez nada que preste.',
        'Não me engana.',
        'Não engana ninguém.',
        'Nunca me enganou.',
        'Todo mundo sabe disso.',
        'Eu sempre disse isso.',
        'Isso não é segredo pra ninguém.',
        'Alguém tinha que falar isso.',
        'Com toda a certeza.',
        'Envergonha o povo dele.',
        'Cara de pau.',
        'Precisa pegar uma cana.']

    return (f'{str(nome)} é a {random.choice(classificador)} mais {random.choice(xingneutro)} {random.choice(exagero)}. {random.choice(conclusao)}')