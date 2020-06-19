'''
ESTE PROGRAMA FAZ A TRADUÇÃO DE UM CONTEÚDO EM INGLÊS PARA PORTUGUÊS E REPRODUZ O ÁUDIO
O PROGRAMA ESCOLHE UM ARQUIVO PDF, FAZ A EXTRAÇÃO DO CONTEÚDO, TRADUZ E MONTA UMA FAIXA DE AUDIO
QUE É REPRODUZIDO AUTOMATICAMENTE
'''


'''
IMPLEMENTAÇÕES: 
1. CONTROLE DA QUALIDADE DO SOM, PARA EVITAR A VOZ MECANIZADA 
2. UTILIZAR OUTRAS APIS PARA MELHOR O CONTEÚDO DA TRADUÇÃO
'''

from gtts import gTTS #Biblioteca de reprodução de áudio
from googletrans import Translator #Biblioteca de tradução
import PyPDF2 #Biblioteca para manipular PDFs
import pygame #Biblioteca para reproduzir sons
import os

'''EXTRAÇÃO DO CONTEÚDO DO PDF'''
pdfFileObj = open('C:/Users/danye/Downloads/teste.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pages = int(pdfReader.numPages)
i = 0
texto = ''

for i in range(0, pages):
    '''EXTRAÇÃO DE CONTEÚDO'''
    pageObj = pdfReader.getPage(i) #i REPRESENTA O NÚMERO DA PÁGINA
    fonte = pageObj.extractText()

    '''TRADUÇÃO'''
    tradutor = Translator()
    traducao = tradutor.translate("olá boa noite", dest='pt')
    texto = texto + traducao.text
    i = i+1 #INTERAÇÃO DO NÚMERO DE PÁGINAS

    '''ESCREVER NO TXT'''
    backup = open('artigo.txt','w')
    backup.write(texto)

    '''LEITURA EM ÁUDIO'''
    tts = gTTS(texto, 'pt')
    tts.save('texto.mp3')

    '''REPRODUZIR A MÚSICA'''
    pygame.init()
    pygame.mixer_music.load('texto.mp3')
    pygame.mixer_music.play()
    pygame.event.wait()
