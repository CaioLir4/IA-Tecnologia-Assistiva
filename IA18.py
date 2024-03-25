from tkinter import *
import tkinter as tk
from tkinter import Button
import speech_recognition as sr
import pyttsx4
import webbrowser
import re
import datetime

reconhecimento = sr.Recognizer()

# cores -----------------------------
co0 = "#f0f3f5"  # Preta / black
co1 = "#feffff"  # branca / white
co2 = "#3fb5a3"  # verde / green
co3 = "#38576b"  # valor / value
co4 = "#403d3d"  # letra / letters
co5 = "#2c3e50"  # Cinza / grey


def printResultado(nome_arquivo):
    arquivo = nome_arquivo
    webbrowser.open(arquivo)


recognizer = sr.Recognizer()
maquina = pyttsx4.init()
voices = maquina.getProperty('voices')
maquina.setProperty('voice', voices[1].id)


def calcular_pergunta(pergunta):
    # Usando expressão regular para extrair números e operador da pergunta
    pergunta = pergunta + "?"
    if 'quanto' in pergunta:
        pergunta = pergunta.replace('quanto', 'Quanto')
    match = re.match(r'Quanto é (\d+) (\S+) (\d+)\?', pergunta)

    if match:
        # Extrair valores e operador
        valor1 = int(match.group(1))
        operador = match.group(2)
        valor2 = int(match.group(3))

        # Realizar cálculo
        if operador == '+':
            resultado = valor1 + valor2
        elif operador == '-':
            resultado = valor1 - valor2
        elif operador == '*':
            resultado = valor1 * valor2
        elif operador == 'x':
            resultado = valor1 * valor2
        elif operador == '/':
            resultado = valor1 / valor2
        else:
            return "Operador inválido"

        # Exibir resultado
        return f"O resultado de {valor1} {operador} {valor2} é {resultado}"
    else:
        return "Formato de pergunta inválido"


def ouvir_microfone():
    reconhecimento = sr.Recognizer()

    with sr.Microphone() as source:
        print("Aguardando palavra-chave...")

        reconhecimento.adjust_for_ambient_noise(source)  # Ajusta para o ruído ambiente
        audio = reconhecimento.listen(source)

    return audio


'''def executar_acao():
    print("Palavra-chave detectada! Executando ação.")
    # Adicione aqui a ação que você deseja realizar quando a palavra-chave for detectada.
    # Pode ser qualquer código ou chamada de função.'''


def convert_to_braille(text):
    braille_dict2 = {
        'a': '\u2801', 'á': '\u2821', 'à': '\u2812', 'â': '\u281a', 'ã': '\u2816',
        'b': '\u2803', 'c': '\u2809', 'd': '\u280d', 'e': '\u2815', 'é': '\u2825',
        'ê': '\u281d', 'f': '\u281d', 'g': '\u280b', 'h': '\u281b', 'i': '\u2810',
        'í': '\u2822', 'j': '\u281e', 'k': '\u2805', 'l': '\u2807', 'm': '\u280d',
        'n': '\u2813', 'o': '\u281f', 'ó': '\u2827', 'ô': '\u281b', 'õ': '\u2817',
        'p': '\u2817', 'q': '\u281b', 'r': '\u2813', 's': '\u280f', 't': '\u2811',
        'u': '\u280f', 'v': '\u2811', 'w': '\u2823', 'x': '\u2819', 'y': '\u281b',
        'z': '\u281d', '0': '\u281f', '1': '\u280b', '2': '\u281b', '3': '\u280d',
        '4': '\u280a', '5': '\u280e', '6': '\u280d', '7': '\u2809', '8': '\u281b',
        '9': '\u2809', '+': '\u280a', '-': '\u2802', '×': '\u2818', '÷': '\u2826',
        '=': '\u2812', '<': '\u2802 \u2825', '>': '\u2802 \u281e', '(': '\u2803 \u2817',
        ')': '\u280f \u2807', '[': '\u2803 \u2827', ']': '\u280f \u281b',
        '{': '\u2803 \u2829', '}': '\u280f \u282d', '.': '\u2833', ',': '\u2836',
        ':': '\u2812 \u2806', ';': '\u2812 \u2826', '"': '\u2837', '\'': '\u2827',
        '@': '\u2802 \u2839', '#': '\u2823 \u2833', '$': '\u2803 \u2823',
        '%': '\u2805 \u280f', '&': '\u281d \u2807', '_': '\u282d', '/': '\u2816',
        '\\': '\u280b', ' ': '\u2800'
    }

    braille_dict = {
        'a': '\u2801', 'á': '\u2821', 'à': '\u2822', 'â': '\u2809', 'ã': '\u281d',
        'b': '\u2803', 'c': '\u2809', 'd': '\u2819', 'e': '\u2811', 'é': '\u2827',
        'ê': '\u2811\u2809', 'f': '\u280b', 'g': '\u281b', 'h': '\u2813', 'i': '\u280a',
        'í': '\u280a\u2822', 'j': '\u281a', 'k': '\u2805', 'l': '\u2807', 'm': '\u280d',
        'n': '\u281d', 'o': '\u2805', 'ó': '\u2805\u2827', 'ô': '\u2805\u2811\u2809',
        'õ': '\u2805\u281d\u2809', 'p': '\u280f', 'q': '\u281f', 'r': '\u2817',
        's': '\u280e', 't': '\u2821', 'u': '\u2825', 'ú': '\u2825\u2827', 'v': '\u2827',
        'w': '\u282a', 'x': '\u282d', 'y': '\u282f', 'z': '\u2835', '1': '\u283c\u2802',
        '2': '\u283c\u2806', '3': '\u283c\u280a', '4': '\u283c\u2802', '5': '\u283c\u2802',
        '6': '\u283c\u2806', '7': '\u283c\u280e', '8': '\u283c\u280a', '9': '\u283c\u2804',
        '0': '\u283c\u2800', '.': '\u2802', ',': '\u2802', ';': '\u2806', ':': '\u280a',
        '!': '\u280e', '?': '\u2826', '-': '\u2824', '_': '\u2824', '(': '\u2800\u2813',
        ')': '\u2800\u280c', '[': '\u2800\u2820', ']': '\u2800\u280a', '{': '\u2800\u2806',
        '}': '\u2800\u2834', '+': '\u2824', '*': '\u2826', '/': '\u2834', '=': '\u2800\u2826',
        '<': '\u2800\u2822', '>': '\u2800\u2824', '&': '\u282f', '%': '\u2828\u2834', '$': '\u281a',
        '#': '\u283c\u2802\u2824', '@': '\u2808\u2811', ' ': '\u2800'
    }

    braille_text = ""
    for char in text:
        if char.lower() in braille_dict:
            braille_text += braille_dict[char.lower()] + ' '

    return braille_text


def processar_fala2():
    with sr.Microphone(device_index=1) as source:
        recognizer.adjust_for_ambient_noise(source)

        print("Fale alguma coisa...")
        maquina.say("Olá, Pergunte-me sobre o cálculo simples desejado!")
        maquina.runAndWait()

        print("Pergunte: Quanto é .......")
        audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio, language="pt-BR")
            print("Texto reconhecido:", text)

            pergunta = text
            resultado = calcular_pergunta(pergunta)
            braille_text = convert_to_braille(text)
            braille_resultado = convert_to_braille(resultado)
            text_falado = ''
            resultado_falado = ''
            if ('dividido por' in text) or ('dividido por' in resultado):
                text = text.replace('/', 'dividido por')
                resultado = resultado.replace('dividido por', '/')

            print("Texto em Braille:", braille_text)

            # Obter a data e hora atual
            agora = datetime.datetime.now()

            # Formatar a data e hora no formato desejado
            data_hora_formatada = agora.strftime("%d-%m-%Y_%H-%M")

            # Concatenar o nome base com a data e hora formatada
            nome_arquivo = f"Braille_{data_hora_formatada}.html"

            '''with open(nome_arquivo, 'w', encoding='utf-8') as relatorio:
                relatorio.write('<html>')
                relatorio.write('<head>')
                relatorio.write('<title>Projeto de iniciação científica</title>')
                relatorio.write('<style>\n')
                relatorio.write('.imagem-lado { float: left; margin-right: 20px; }\n')
                relatorio.write('</style>\n')
                relatorio.write('</head>')
                relatorio.write('<body>')
                relatorio.write(
                    '<img src="faci.png" alt="Faci Wyden" style="width:200px; height:200px;" class="imagem-lado"><h2>Faculdade Faci Wyden</h2>')
                relatorio.write('<h3>Curso: Ciência da Computação</h3>')
                relatorio.write('<h3>Aluno: José Roberto Vasconcellos Lopes - 20203071971</h3>')
                relatorio.write('<h3>Professor: Paulo Tássio</h3>')
                relatorio.write('<h3>Coordenador: Iranildo Encarnação</h2>')
                relatorio.write(
                    '<h2>Título: Inteligência Artificial:Transformando a Oralização de Palavras em Braille e Matemática - Uma Ferramenta para Inclusão e Operações Matemáticas na Educação de Pessoas com Deficiência Visual</h2>\n')
                relatorio.write('<hr>')
                relatorio.write(f'<h3>Texto reconecido: {text}</h3>')
                relatorio.write(f'<h3>Texto em Braille: {braille_text}</h3>')
                relatorio.write(f'<h3>{resultado}</h3>')
                relatorio.write(f'<h3>{braille_resultado}</h3>')

                relatorio.write('</body>\n')
                relatorio.write('</html>\n')

            printResultado(nome_arquivo)'''

            if ('/' in text) or ('/' in resultado):
                text_falado = text.replace('/', 'dividido por')
                resultado_falado = resultado.replace('/', 'dividido por')

            if ('-' in text) or ('-' in resultado):
                text_falado = text.replace('-', 'menos')
                resultado_falado = resultado.replace('-', 'menos')

            if ('+' in text) or ('+' in resultado):
                text_falado = text.replace('+', 'mais')
                resultado_falado = resultado.replace('+', 'mais')

            if ('x' in text) or ('x' in resultado):
                text_falado = text.replace('x', 'vezes')
                resultado_falado = resultado.replace('x', 'vezes')

            if ('inválido' in resultado):
                maquina.say(resultado)
                maquina.runAndWait()
            else:
                maquina.say(text_falado)
                maquina.say(resultado_falado)
                maquina.runAndWait()

            return text

        except sr.UnknownValueError:
            print("Não foi possível reconhecer a fala.")

        except sr.RequestError as e:
            print("Erro na solicitação: {0}".format(e))


def main():
    def on_button_click():
        code()

    # Função para atualizar o label
    def atualizar_label(var_label):
        var_label.set("Fale alguma coisa...")

    root = tk.Tk()
    root.title("Reconhecimento de Fala")
    root.geometry('500x510')
    root.config(bg=co5)
    #favicon = PhotoImage(file="faci.png")
    #root.iconphoto(False, favicon)
    root.resizable(width=FALSE, height=FALSE)
    # Dividindo a janela ----------------------
    frame_cima = Frame(root, width=510, height=150, bg=co5, relief='flat')
    frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

    frame_baixo = Frame(root, width=510, height=350, bg=co5, relief='flat')
    frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

    # Variável de controle para a mensagem
    mensagem_var1 = tk.StringVar()
    mensagem_var1.set("Fale alguma coisa.....")

    mensagem_var2 = tk.StringVar()
    mensagem_var2.set("Comando: Quanto é....?")

    titulo = Label(frame_cima, text='Sistema Braille', anchor=NE, font='Ivy 25', bg=co5, fg=co1)
    titulo.place(x=5, y=5)
    msg1 = Label(frame_baixo, text='Click no botão para iniciar o sistema.', anchor=NW, font='Ivy 10', bg=co5, fg=co1)
    msg1.place(x=10, y=12)
    msg2 = Label(frame_baixo, textvariable=mensagem_var1, anchor=NW, font='Ivy 10', bg=co5, fg=co1)
    msg2.place(x=10, y=52)
    msg3 = Label(frame_baixo, textvariable=mensagem_var2, anchor=NW, font='Ivy 10', bg=co5, fg=co1)
    msg3.place(x=10, y=92)

    login_button = Button(frame_baixo, text="Ativar o J.A.R.V.I.S", width=29, height=2, bg=co2, fg=co1, font=('Ivy 10'),
                          relief='raised', overrelief='ridge', command=on_button_click)
    login_button.place(x=25, y=160)

    def code():
        motor_texto = pyttsx4.init()
        Fim = "Sim"
        while Fim == "Sim":
            try:
                audio = ouvir_microfone()
                texto = reconhecimento.recognize_google(audio, language="pt-BR").lower()

                if "jarvis" in texto:
                    processar_fala2()
                elif "fim" in texto:
                    print("False")
                    Fim = "False"
                    root.destroy()

            except sr.UnknownValueError:
                print("Não foi possível entender a fala. Tente novamente.")
                # mensagem_var.set("Não foi possível entender a fala. Tente novamente.")
            except sr.RequestError as e:
                print(f"Erro ao acessar o serviço de reconhecimento de fala; {e}")
                # mensagem_var.set("Erro ao acessar o serviço de reconhecimento de fala; {e}")

    root.mainloop()


if __name__ == "__main__":
    main()
