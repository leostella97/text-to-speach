import pyttsx3
import tkinter as tk

def text_to_speech():
    texto = entry.get()
    engine = pyttsx3.init()
    engine.say(texto)
    engine.runAndWait()

# Cria a janela
window = tk.Tk()
window.title("Texto para Fala")

# Cria a label e o campo de texto
label = tk.Label(window, text="Digite a frase que deseja transformar em fala:")
label.pack()
entry = tk.Entry(window)
entry.pack()

# Cria o botão
button = tk.Button(window, text="Falar", command=text_to_speech)
button.pack()

# Inicia o loop da janela
window.mainloop()
