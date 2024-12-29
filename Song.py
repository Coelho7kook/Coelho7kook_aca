import pygame
import random
import time
from pytube import YouTube
import os
import requests
from io import BytesIO

# Inicializa o mixer do pygame para áudio
pygame.mixer.init()

# Lista de links do YouTube para as músicas
musicas_links = [
    "https://www.youtube.com/watch?v=s7RRgF5Ve_E",  # Música 1
    "https://www.youtube.com/watch?v=InkKkTcw9_A",  # Música 2
    "https://www.youtube.com/watch?v=v9l52KilyLU",  # Música 3
    "https://www.youtube.com/watch?v=8FuRsZ7U4BU",  # Música 4
    "https://www.youtube.com/watch?v=AvaLLgG8yaE",  # Música 5
]

# Função para baixar a música do YouTube
def baixar_musica(link):
    yt = YouTube(link)
    stream = yt.streams.filter(only_audio=True).first()  # Filtra a melhor stream de áudio
    audio_file = stream.download(filename='temp_audio.mp4')  # Baixa o áudio como arquivo temporário
    return audio_file

# Função para tocar música aleatória
def tocar_musica_aleatoria():
    musica_escolhida = random.choice(musicas_links)  # Escolhe uma música aleatoriamente
    arquivo_audio = baixar_musica(musica_escolhida)  # Baixa o arquivo de áudio
    pygame.mixer.music.load(arquivo_audio)  # Carrega o arquivo de música
    pygame.mixer.music.play()  # Reproduz a música

# Função para tocar a música automaticamente ao iniciar o programa
def iniciar():
    print("Iniciando a música aleatória...")
    tocar_musica_aleatoria()

# Função principal
if __name__ == "__main__":
    iniciar()

    # Mantém o programa rodando enquanto a música está tocando
    while pygame.mixer.music.get_busy():
        time.sleep(1)  # Aguarda 1 segundo entre as verificações

    # Exclui o arquivo temporário após a reprodução
    if os.path.exists('temp_audio.mp4'):
        os.remove('temp_audio.mp4')
