import serial
import time
import re
from IA17 import processar_fala
from IA18 import processar_fala2
def gerar_palavras(frase_ia):
    lista_palavras = frase_ia.split()
    for palavra in lista_palavras:
        yield palavra
def remover_acentos(texto):
    texto_sem_acentos = texto

    texto_sem_acentos = re.sub(r'[áàãâä]', 'a', texto_sem_acentos)
    texto_sem_acentos = re.sub(r'[éèêë]', 'e', texto_sem_acentos)
    texto_sem_acentos = re.sub(r'[íìîï]', 'i', texto_sem_acentos)
    texto_sem_acentos = re.sub(r'[óòõôö]', 'o', texto_sem_acentos)
    texto_sem_acentos = re.sub(r'[úùûü]', 'u', texto_sem_acentos)

    numeros_para_string = {
        0: "zero",
        1: "um",
        2: "dois",
        3: "três",
        4: "quatro",
        5: "cinco",
        6: "seis",
        7: "sete",
        8: "oito",
        9: "nove"
    }

    if texto_sem_acentos.isdigit():
        numero = int(texto_sem_acentos)
        if numero >= 0 and numero <= 9:
            texto_sem_acentos = numeros_para_string[numero]

    return texto_sem_acentos



try:
    conexao = serial.Serial("COM3", 9600, timeout=1)
    print("Conexao teve sucesso: ", conexao.port)

    while True:

        Comando = int(input("\nOque deseja fazer?\n"
                        "Calculos (1) / Tradução de Audio (2) / Encerrar Programa (3): "))

        if Comando == 1:
            frase_ia = processar_fala2()
            gerador = gerar_palavras(remover_acentos(frase_ia))

            for palavra in gerador:

                palavra_bytes = palavra.encode('utf-8')


                conexao.write(palavra_bytes)
                print("Palavra enviada com sucesso:", frase_ia)

                time.sleep(0.6)

            start_time = time.time()
            while True:
                linha = conexao.readline().decode()
                print(linha)

                if linha in gerador:
                    break
                if time.time() - start_time >= len(frase_ia) + 7:
                    print("Fim do Calculo.")
                    break


        elif Comando == 2:
            frase_ia = processar_fala()
            gerador = gerar_palavras(remover_acentos(frase_ia))

            for palavra in gerador:
                palavra_bytes = palavra.encode('utf-8')

                conexao.write(palavra_bytes)
                print("Palavra enviada com sucesso:", frase_ia)

                time.sleep(0.6)

            start_time = time.time()
            while True:
                linha = conexao.readline().decode()
                print(linha)

                if linha in gerador:
                    break
                if time.time() - start_time >= len(frase_ia)+7:
                    print("Fim do texto.")
                    break


        elif Comando == 3:
            print("Programa finalizado! ")
            break



except serial.SerialException:
    print("Error ", serial.SerialException)
    pass

