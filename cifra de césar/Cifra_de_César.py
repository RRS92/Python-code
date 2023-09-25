arq = open('arquivo','a')
texto = input('Digite um texto para o arquivo:')
arq.write(texto)
arq.close()

Encriptar = 1
Decifrar = 0

def cesar(dado, chave, modo):
    alfabeto = 'abcdefghijklmnopqrstuvwyzàáãâéêóôõíúçABCDEFGHIJKLMNOPQRSTUVWYZÀÁÃÉÊÓÕÍÚÇ'
    novo_dado = ' '
    for i in dado:
        indice = alfabeto.find(i)
        if indice == -1:
            novo_dado += i
        else:
            novo_indice = indice + chave if modo == Encriptar else indice - chave
            novo_indice = novo_indice % len(alfabeto)
            novo_dado += alfabeto[novo_indice:novo_indice+1]
    return novo_dado

def ler_arq1(arquivo):
    ler = open(arquivo,'r')
    conteudo = ler.readlines()
    for linha in conteudo:
        chave = int(input('diga um valor inteiro para a chave:'))
        cifra = cesar(linha,chave,Encriptar)
        escrita = open('texto encriptado','a')
        escrita.write(cifra)
        escrita.close()

    ler.close()

ler_arq1('arquivo')

def ler_arq2(arquivo):
    ler = open(arquivo,'r')
    conteudo = ler.readlines()
    for linha in conteudo:
        chave = int(input('diga um valor inteiro para a chave:'))
        decifrar = cesar(linha,chave,Decifrar)
        print('Texto decifrado',decifrar)

        pergunta = input('A mensagem foi decifrada de maneira satisfatoria: Sim(S) ou Não(N):')
        while pergunta != 'S' and pergunta != 'N':
          pergunta = input('Valor invalido!! responda S ou N:')

        while pergunta == 'N':
            ler = open(arquivo,'r')
            conteudo = ler.readlines()
            for linha in conteudo:
                chave = int(input('diga um valor inteiro para a chave:'))
                decifrar = cesar(linha,chave,Decifrar)
                print('Texto decifrado',decifrar)
                pergunta = input('A mensagem foi decifrada de maneira satisfatoria: Sim(S) ou Não(N):')
                while pergunta != 'S' and pergunta != 'N':
                  pergunta = input('Valor invalido!! responda S ou N:')

        if pergunta == 'S':
          print('Você conseguiu decifrar o texto!! PARABÉNS!!')
    ler.close()

ler_arq2('texto encriptado')

