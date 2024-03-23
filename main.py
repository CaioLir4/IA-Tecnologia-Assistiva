import serial
import time
from projetoIA17 import processar_fala

def gerar_palavras(frase):
    lista_palavras = frase.split()
    for palavra in lista_palavras:
        yield palavra


try:
    conexao = serial.Serial("COM3", 9600, timeout=1)
    print("Conexao teve sucesso: ", conexao.port)

    while True:

        frase_ia = processar_fala()
        gerador = gerar_palavras(frase_ia)

        for palavra in gerador:

            palavra_bytes = palavra.encode('utf-8')

            conexao.write(palavra_bytes)
            print("Palavra enviada com sucesso:", palavra)

            time.sleep(0.2)

except serial.SerialException:
    print("Error ", serial.SerialException)
    pass

