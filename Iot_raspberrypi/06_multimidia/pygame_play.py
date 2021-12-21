import pygame

pygame.init()

pygame.mixer.music.load("sample.mp3")

while True:
    cmd = input("play : p  pause : pa  unpause : up  stop : s  quit : other >")
    if cmd == 'p':
        pygame.mixer.music.play()
    elif cmd == 'pa':
        pygame.mixer.music.pause()
    elif cmd == 'up':
        pygame.mixer.music.unpause()
    elif cmd == 's':
        pygame.mixer.music.stop()
    else:
        break

print("quit")