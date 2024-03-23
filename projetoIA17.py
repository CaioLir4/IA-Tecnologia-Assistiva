
'''
Instalar as bibliotecas
pip install SpeechRecognition Pillow
pip install reportlab
pip install PyMuPDF
pip install PyPDF2
pip install PyAudio

'''

import speech_recognition as sr
'''from PIL import Image, ImageDraw, ImageFont
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase import ttfonts
from reportlab.platypus import SimpleDocTemplate, Image
from reportlab.lib.utils import ImageReader'''
import pyttsx4
import webbrowser

def printResultado():
        webbrowser.open("relatorio.txt")
        webbrowser.open('relatorio.html')

# Inicializa o reconhecimento de fala
recognizer = sr.Recognizer()
maquina = pyttsx4.init()
voices = maquina.getProperty('voices')
maquina.setProperty('voice', voices[0].id)

# Função para converter texto em Braille
def convert_to_braille(text):
    
    braille_dict = {
        'a':'\u2801', 'á':'\u2821', 'à':'\u2812', 'â':'\u281a', 'ã':'\u2816',
        'b':'\u2803', 'c':'\u2809', 'd':'\u280d', 'e':'\u2815', 'é':'\u2825',
        'ê':'\u281d', 'f':'\u281d', 'g':'\u280b', 'h':'\u281b', 'i':'\u2810',
        'í':'\u2822', 'j':'\u281e', 'k':'\u2805', 'l':'\u2807', 'm':'\u280d',
        'n':'\u2813', 'o':'\u281f', 'ó':'\u2827', 'ô':'\u281b', 'õ':'\u2817',
        'p':'\u2817', 'q':'\u281b', 'r':'\u2813', 's':'\u280f', 't':'\u2811',
        'u':'\u280f', 'v':'\u2811', 'w':'\u2823', 'x':'\u2819', 'y':'\u281b',
        'z':'\u281d', '0':'\u281f', '1':'\u280b', '2':'\u281b', '3':'\u280d',
        '4':'\u280a', '5':'\u280e', '6':'\u280d', '7':'\u2809', '8':'\u281b',
        '9':'\u2809', '+':'\u280a', '-':'\u2802', '×':'\u2818', '÷':'\u2826',
        '=':'\u2812', '<':'\u2802 \u2825', '>':'\u2802 \u281e', '(':'\u2803 \u2817',
        ')':'\u280f \u2807', '[':'\u2803 \u2827', ']':'\u280f \u281b',
        '{':'\u2803 \u2829', '}':'\u280f \u282d', '.':'\u2833', ',':'\u2836',
        ':':'\u2812 \u2806', ';':'\u2812 \u2826', '"':'\u2837', '\'':'\u2827',
        '@':'\u2802 \u2839', '#':'\u2823 \u2833', '$':'\u2803 \u2823',
        '%':'\u2805 \u280f', '&':'\u281d \u2807', '_':'\u282d', '/':'\u2816',
        '\\':'\u280b', ' ':'\u2800'
    }

    braille_text = ""
    for char in text:
        if char.lower() in braille_dict:
            braille_text += braille_dict[char.lower()] + ' '

    return braille_text

# Função para reconhecer a fala e processar
def processar_fala():
    with sr.Microphone(device_index=1) as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Fale alguma coisa...")
        audio = recognizer.listen(source)

        try:
            '''pdf = canvas.Canvas("1-Braille.pdf")
            im = ImageReader('faci.png')
            x = 150
            y = 750
            reg = 1
            pdf.setFont("Helvetica-Bold", 12)
            pdf.drawString(200, 790, 'Projeto de iniciação científica')
            pdf.drawImage(im, 520,770,width=50,height=50)
            pdf.rect(20, 770, 550, 50, fill=False, stroke=True)
            pdf.setFont("Helvetica-Bold", 12)
            pdf.drawString(50, y, 'Professor: Paulo Tássio')
            y -= 20
            pdf.drawString(50, y, f'Alunos: CAIO GOMES LIRA : 202202887064')
            y -= 20'''

            # Reconhece a fala e converte em texto
            text = recognizer.recognize_google(audio, language="pt-BR")
            print("Texto reconhecido:", text)

            '''pdf.drawString(50, y, f'Texto reconhecido: {text}')
            y -= 20'''
            
            # Converte o texto em Braille
            braille_text = convert_to_braille(text)
            
            print("Texto em Braille:", braille_text)
            '''pdf.drawString(50, y, f'Texto em Braille: {braille_text}')
            y -= 20
            pdf.save()'''

            #Se descomentar abre as abas
            '''printResultado()'''
            

            # Salva o relatório de texto
            with open('relatorio.txt', 'w', encoding='utf-8') as relatorio:
                relatorio.write('Projeto de iniciação científica \n')
                relatorio.write('Título: Inteligência Artificial:Conversão de audio em Braili. Contribuindo com Educação de Pessoas com Deficiência Visual \n\n')
                relatorio.write('Curso: Ciência da Computação \n')
                relatorio.write('Aluno: CAIO GOMES LIRA : 202202887064\n')
                relatorio.write('Professor: Paulo Tássio \n')
                relatorio.write('=================================================================== \n\n')
                relatorio.write('Texto reconhecido: \n')
                relatorio.write(text + '\n\n')
                relatorio.write('Texto em Braille: \n')
                relatorio.write(braille_text)
            
            with open('relatorio.html', 'w', encoding='utf-8') as relatorio:
                relatorio.write('<html>')
                relatorio.write('<head>')
                relatorio.write('<title>Projeto de iniciação científica</title>')
                relatorio.write('<style>\n')
                relatorio.write('.imagem-lado { float: left; margin-right: 20px; }\n')
                relatorio.write('</style>\n')
                relatorio.write('</head>')
                relatorio.write('<body>')
                relatorio.write('<img src="faci.png" alt="Faci Wyden" style="width:200px; height:200px;" class="imagem-lado"><h2>Faculdade Faci Wyden</h2>')
                relatorio.write('<h3>Curso: Ciência da Computação</h3>')
                relatorio.write('<h3>Aluno: CAIO GOMES LIRA : 202202887064</h3>')
                relatorio.write('<h3>Professor: Paulo Tássio</h3>')
                relatorio.write('<h3>Coordenador: Iranildo Encarnação</h2>')
                relatorio.write('<h2>Título: Inteligência Artificial:Conversão de audio em Braili. Contribuindo com Educação de Pessoas com Deficiência Visual</h2>\n')
                relatorio.write('<hr>')
                relatorio.write(f'<h3>Texto reconecido: {text}</h3>')
                relatorio.write(f'<h3>Texto em Braille: {braille_text}</h3>')
                relatorio.write('</body>\n')
                relatorio.write('</html>\n')
    
            maquina.say(text)
            maquina.runAndWait()

            return text
        except sr.UnknownValueError:
            print("Não foi possível reconhecer a fala.")
        except sr.RequestError as e:
            print("Erro na solicitação: {0}".format(e))

if __name__ == "__main__":
    processar_fala()

