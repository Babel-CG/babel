import tkinter as tk
import tkinter.font as font
import tkinter.ttk as tkk
import speech_recognition as sr
import playsound
import os
import random
from gtts import gTTS
from googletrans import Translator


root = tk.Tk(className=" Babel, Tradutor Simultâneo")
root.geometry("420x590")


def myClick():
    comboi = tkk.Combobox(frame5, values=["Português", "Inglês"])
    comboi.current(comboboxLangOri.current())
    comboboxLangOri.current(comboboxLangDest.current())
    comboboxLangDest.current(comboi.current())



fontNameApp = font.Font(family='Times', size=24)
frame1 = tk.Frame(root, height=100, pady=10, bg="black")
frame1.pack(fill=tk.X)

#colocando o icone do App
iconNameApp = tk.PhotoImage(file="languageIcon.png")
iconApp = tk.Label(frame1, image=iconNameApp, bg="black")
iconApp.pack()

#Titulo do App
lblNameApp = tk.Label(frame1, text="BABEL", fg="#0099FF", bg="black")
lblNameApp['font'] = fontNameApp
lblNameApp.pack()


lblWelcome = tk.Label(frame1, text="Bem vindo ao Babel, seu tradutor de voz simultâneo", bg="black", fg="#00CCFF")
lblWelcome.pack(fill=tk.X)

frame2 = tk.Frame(root, padx=10, pady=20, bg="black")
frame2.pack(fill=tk.X)

frame3 = tk.Frame(root, padx=10, pady=20, bg="black")
frame3.pack(fill=tk.X)

frame4 = tk.Frame(root, padx=30, pady=10, bg="#14406c")
frame4.pack(fill=tk.X)

frame5 = tk.Frame(root, padx=10, pady=30, bg="#14406c")
frame5.pack(fill=tk.X)

emptySpace2 = tk.Label(frame4, text="           ", bg="#14406c")
emptySpace2.grid(row=0, column=0)

lblInfoLang = tk.Label(frame4, text="Aqui você pode escolher quais línguas deseja traduzir", bg="#14406c", fg="#00CCFF")
lblInfoLang.grid(row=0, column=1)

lblChooseLang = tk.Label(frame5, text="Escolha sua lingua de origem", bg="#14406c", fg="#00CCFF")
lblChooseLang.grid(row=0, column=0)

comboboxLangOri = tkk.Combobox(frame5, values=["Português", "Inglês", "Coreano"], )
comboboxLangOri.grid(row=1, column=0)
comboboxLangOri.current(0)

lblExtraSpace = tk.Label(frame5, text = " ", bg="#14406c", fg="#00CCFF")
lblExtraSpace.grid(row=1,column=1)

lblChooseLangDest = tk.Label(frame5, text="Escolha sua língua de Destino", bg="#14406c", fg="#00CCFF")
lblChooseLangDest.grid(row=0, column=4)

comboboxLangDest= tkk.Combobox(frame5, values=["Português", "Inglês", "Coreano"])
comboboxLangDest.grid(row=1, column=4)
comboboxLangDest.current(1)

def retornaLinguaOrigem():
    linguaOrigem = ""
    print(comboboxLangOri.current())
    if comboboxLangOri.current() == 0:
         linguaOrigem = "pt"
    elif comboboxLangOri.current() == 2:
         linguaOrigem = "ko"
    else:
         linguaOrigem = "en"
    return linguaOrigem


def retornaLinguaDestino():
    linguaDestino = ""
    if comboboxLangDest.current() == 0:
        linguaDestino = "pt"
    elif comboboxLangDest.current() == 2:
        linguaDestino = "ko"
    else:
        linguaDestino = "en"
    return linguaDestino

imageUpdate = tk.PhotoImage(file="switch.png")
imageUpdateIcon = tk.Label(image=imageUpdate)

updateButton = tk.Button(frame5, imageUpdateIcon, padx=30, pady=10, command=myClick, bg="#14406c")
updateButton.grid(row=1, column=2)


emptySpace = tk.Label(frame2, text="                     ", bg="black")
emptySpace.grid(row=1, column=2)

lblGravaAudio = tk.Label(frame2, text="Clique no microfone para gravar seu áudio", bg="black", fg="#CC00CC")
lblGravaAudio.grid(row=0, column=5)

microfoneIcon = tk.PhotoImage(file="miku.png")
imageMicrofoneIcon = tk.Label(frame2, image=microfoneIcon, bg="black", pady=30)
imageMicrofoneIcon.grid(row=2, column=5)

lblOuvirAudio = tk.Label(frame3, text="Você pode ouvir a tradução do que você disse, clicando no botão Play", bg="black", fg="#CC00CC")
lblOuvirAudio.pack()

playaudioIcon = tk.PhotoImage(file="playaudio.png")
imagePlayaudio = tk.Label(frame3, image=playaudioIcon, bg="black")


microfone = sr.Recognizer()
def ouvir_microfone():
   with sr.Microphone() as source:
      microfone.adjust_for_ambient_noise(source)
      audio = microfone.listen(source)
      frase = ""
      try:
        linguaOrigem = retornaLinguaOrigem()
        linguaDestino = retornaLinguaDestino()
        frase = microfone.recognize_google(audio, language=linguaOrigem)
        print(frase)
        tradutor = Translator()
        traducao = tradutor.translate(frase, dest=linguaDestino)
        print("Você disse: " + traducao.text)
        global audio_desc
        audio_desc = traducao.text
      except Exception as e:
        print("Não entendi o que você falou")
        print(e)
      return audio_desc


def cria_audio():
   #audio = ouvir_microfone()
   tts = gTTS(text=audio_desc,lang=retornaLinguaDestino())
   r = random.randint(1, 100000)
   audioFile = 'audio' + str(r) + '.mp3'
   tts.save(audioFile)
   print("Estou traduzindo o que você disse...")
   playsound.playsound(audioFile)
   print(audioFile)
   os.remove(audioFile)


btnMicrofone = tk.Button(frame2, imageMicrofoneIcon, padx=40, pady=10, command=ouvir_microfone)
btnMicrofone.grid(row=2, column=5)

btnListen = tk.Button(frame3, imagePlayaudio, padx=40, command=cria_audio)
btnListen.pack()

audio_desc = ""

root.mainloop()