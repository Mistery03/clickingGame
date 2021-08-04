import pygame
import sys
import json
import os

pygame.init();
WIDTH, HEIGHT = 600,400;
screen = pygame.display.set_mode((WIDTH,HEIGHT));
clock = pygame.time.Clock();
gameFont = pygame.font.SysFont("Arial",32);

#Audio
clickSound = pygame.mixer.Sound(os.path.join("audio","click.wav"));

#Background music
pygame.mixer.music.load(os.path.join("audio","music.wav"));
pygame.mixer.music.play(-1);
pygame.mixer.music.set_volume(0.5);

#Rectangles
redSurf = pygame.Surface([200,200]);
redSurf.fill((240,80,54));
redRect = redSurf.get_rect(center =(150,180));

blueSurf = pygame.Surface([200,200]);
blueSurf.fill((0,123,194));
blueRect = blueSurf.get_rect(center =(450,180));

#Data
data = {
    "red":0,
    "blue":0
    }

try:
    with open('clickerScore.txt') as scoreFile:
        data = json.load(scoreFile);
except:
    print("New save file created");

#text
redScoreSurf = gameFont.render(f"Clicks:{data['red']}",True,"Black");
redScoreRect = redScoreSurf.get_rect(center=(150,320));

blueScoreSurf = gameFont.render(f"Clicks:{data['blue']}",True,"Black");
blueScoreRect = blueScoreSurf.get_rect(center=(450,320));

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            with open('clickerScore.txt','w') as scoreFile:
                json.dump(data,scoreFile);
                
            pygame.quit();
            exit();
        if event.type == pygame.MOUSEBUTTONDOWN:
            if redRect.collidepoint(event.pos):
                clickSound.play();
                data['red'] += 1;
                redScoreSurf = gameFont.render(f"Clicks:{data['red']}",True,"Black");
                redScoreRect = redScoreSurf.get_rect(center=(150,320));
                
            elif blueRect.collidepoint(event.pos):
                clickSound.play();
                data['blue'] += 1;
                blueScoreSurf = gameFont.render(f"Clicks:{data['blue']}",True,"Black");
                blueScoreRect = blueScoreSurf.get_rect(center=(450,320));
                
    screen.fill((245,255,252));
    screen.blit(redSurf,redRect);
    screen.blit(blueSurf,blueRect)

    screen.blit(redScoreSurf,redScoreRect);
    screen.blit(blueScoreSurf,blueScoreRect);

    pygame.display.update();
    clock.tick(60);


