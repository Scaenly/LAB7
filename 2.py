import pygame
pygame.init()
screen = pygame.display.set_mode((225, 225))

background = pygame.image.load("spotify.png")

songs = ["J_Cole_-_No_Role_Modelz_61157578.mp3",
         "Santiz_-_O_moejj_lyubvi_77115454.mp3",
         "Macklemore_-_Cant_Hold_Us_48376720.mp3"]
current_song = 0

pygame.mixer.music.load(songs[current_song])
pygame.mixer.music.play()

music_playing = True

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if music_playing:
                    pygame.mixer.music.pause()
                    music_playing = False
                else:
                    pygame.mixer.music.unpause()
                    music_playing = True
            elif event.key == pygame.K_RIGHT:
                current_song += 1
                if current_song >= len(songs):
                    current_song = 0
                pygame.mixer.music.load(songs[current_song])
                pygame.mixer.music.play()
            elif event.key == pygame.K_LEFT:
                current_song -= 1
                if current_song < 0:
                    current_song = len(songs) - 1
                pygame.mixer.music.load(songs[current_song])
                pygame.mixer.music.play()

    screen.blit(background, (0, 0))
    pygame.display.flip() 