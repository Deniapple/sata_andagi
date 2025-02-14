import random
import time
import pgzrun
import pygame
import sys#öğrenilmedi
from pgzero.clock import clock#öğrenilmedi

WIDTH = 1024
HEIGHT = 512

clock_py = pygame.time.Clock()#öğrenilmedi

TITLE = "sata andagi"
FPS = 60


arkaplan = Actor("arkaplan")
osaka = Actor("osaka")
osaka_picture = Actor("osakabig", (200,310))
osaka_picture2 = Actor("osakabig", (900,310))

rb_button = Actor("rebirth", (120, 470))
play = Actor("play", (512, 256))
pause = Actor("pause", (90, 380))
settings = Actor("settings", (512, 390))
go_back = Actor("go_back", (100, 430))
close_button = Actor("close", (970, 50))
up = Actor("up",(900, 400))
down = Actor("down",(900, 460))
left = Actor("left",(860, 430))
right = Actor("right",(940, 430))

toggle_bgm = Actor("on", (100, 200))
toggle_sound = Actor("on", (300, 200))
toggle_tm = Actor("off", (500, 200))
toggle_fps = Actor("60", (700, 200))

points = 0
rebirths = 0
mode = "menu"
music.play("neko_atsume_bgm.mp3")#öğrenilmedi
sounds.sata_andagi.play()#öğrenilmedi
sata_andagi_play = True

touch_mode = False
moving_left = False
moving_right = False
moving_up = False
moving_down = False

sata_andagiler = []
sayi = random.randint(15, 25)
for i in range(sayi):
    x = random.randint(20, 890)
    y = random.randint(20, 890)
    sata_andagi = Actor("sata_andagi", (x, y))
    sata_andagiler.append(sata_andagi)

def draw():
    if mode == "menu":
        arkaplan.draw()
        screen.draw.text("sata andagi", center = (512, 150), color = "#00ffff", fontsize = 53)
        play.draw()
        settings.draw()
        close_button.draw()
        osaka_picture.draw()
    if mode == "settings":
        arkaplan.draw()
        osaka_picture2.draw()
        screen.draw.text("BGM", center = (100, 100), color = "#00ffff", fontsize = 50)
        toggle_bgm.draw()
        screen.draw.text("Sounds", center = (300, 100), color = "#00ffff", fontsize = 50)
        toggle_sound.draw()
        screen.draw.text("Touch Mode", center = (500, 100), color = "#00ffff", fontsize = 50)
        toggle_tm.draw()
        screen.draw.text("FPS", center = (700, 100), color = "#00ffff", fontsize = 50)
        toggle_fps.draw()
        screen.draw.text("BGM from Neko Atsume, Game by Deniapple", center = (550, 480), color = "#00ffff", fontsize = 40)
        go_back.draw()
    if mode == "game":
        arkaplan.draw()
        screen.draw.text(str(points), center = (990, 30), color = "#00ffff", fontsize = 53)
        screen.draw.text(str(rebirths), center = (990, 490), color = "#00ffff", fontsize = 53)
        rb_button.draw()
        pause.draw()
        osaka.draw()
        for i in range(len(sata_andagiler)):
            sata_andagiler[i].draw()
        if touch_mode == True:
            touch_buttons()
        if points >= 1000:
            screen.draw.text("you are unemployed", center = (512, 260), color = "#00ffff", fontsize = 53)
    
def yeni_sata_andagi():
    x = random.randint(0, 970)
    y = random.randint(0, 470)  
    sata_andagi = Actor("sata_andagi", (x, y))
    sata_andagiler.append(sata_andagi)     

def touch_buttons():
    up.draw()
    down.draw()
    left.draw()
    right.draw()

def update(dt):
    global points, menu, FPS, moving_left, moving_right, moving_up, moving_down
    if toggle_fps.image == "30":
        FPS = 30
    else:
        FPS = 60
    clock_py.tick(FPS) #öğrenilmedi

    if keyboard.left or moving_left:
        osaka.x -= 5
    if keyboard.right or moving_right:
        osaka.x += 5
    if keyboard.up or moving_up:
        osaka.y -= 5
    if keyboard.down or moving_down:
        osaka.y += 5
    
    sayi = osaka.collidelist(sata_andagiler)
    if sayi != -1:
        sata_andagiler.pop(sayi)
        if sata_andagi_play == True:
            sounds.sata_andagi.play()#öğrenilmedi
        clock.schedule(yeni_sata_andagi, 0.7)
        points += 1 + rebirths
        if points == 50 or points == 100 or points == 150 or points >= 200:
            osaka_pic = random.randint(1,3)
            if osaka_pic == 1:
                osaka.image = "osaka"
            elif osaka_pic == 2:
                osaka.image = "osaka2"
            elif osaka_pic == 3:
                osaka.image = "osaka3"

def on_mouse_down(button, pos):
    global points, rebirths, mode, sata_andagi_play, touch_mode, FPS, moving_left, moving_right, moving_up, moving_down
    if mode == "menu" and play.collidepoint(pos) and button == mouse.LEFT:
        mode = "game"
        sounds.click_wii.play()
    if mode == "game" and pause.collidepoint(pos) and button == mouse.LEFT:
        mode = "menu"
        sounds.click_wii.play()
    if mode == "menu" and close_button.collidepoint(pos) and button == mouse.LEFT:
        sounds.click_wii.play()
        sys.exit()#öğrenilmedi
    
    if mode == "menu" and settings.collidepoint(pos) and button == mouse.LEFT:
        mode = "settings"
        sounds.click_wii.play()
    if mode == "settings" and toggle_bgm.collidepoint(pos) and button == mouse.LEFT and toggle_bgm.image == "on":
        toggle_bgm.image = "off"
        sounds.click_wii.play()
        music.stop()#öğrenilmedi
    elif mode == "settings" and toggle_bgm.collidepoint(pos) and button == mouse.LEFT and toggle_bgm.image == "off":
        toggle_bgm.image = "on"
        sounds.click_wii.play()
        music.play("neko_atsume_bgm.mp3")#öğrenilmedi

    if mode == "settings" and toggle_sound.collidepoint(pos) and button == mouse.LEFT and toggle_sound.image == "on":
        toggle_sound.image = "off"
        sounds.click_wii.play()
        sata_andagi_play = False
    elif mode == "settings" and toggle_sound.collidepoint(pos) and button == mouse.LEFT and toggle_sound.image == "off":
        toggle_sound.image = "on"
        sounds.click_wii.play()
        sata_andagi_play = True
    
    if mode == "settings" and toggle_tm.collidepoint(pos) and button == mouse.LEFT and toggle_tm.image == "off":
        toggle_tm.image = "on"
        sounds.click_wii.play()
        touch_mode = True
    elif mode == "settings" and toggle_tm.collidepoint(pos) and button == mouse.LEFT and toggle_tm.image == "on":
        toggle_tm.image = "off"
        sounds.click_wii.play()
        touch_mode = False
    
    if mode == "settings" and toggle_fps.collidepoint(pos) and button == mouse.LEFT and toggle_fps.image == "60":
        toggle_fps.image = "30"
        sounds.click_wii.play()
    elif mode == "settings" and toggle_fps.collidepoint(pos) and button == mouse.LEFT and toggle_fps.image == "30":
        toggle_fps.image = "60"
        sounds.click_wii.play()
    if mode == "settings" and go_back.collidepoint(pos) and button == mouse.LEFT:
        mode = "menu"
        sounds.click_wii.play()
    if rb_button.collidepoint(pos) and button == mouse.LEFT and points >= 300:
        rebirths += 1
        sounds.click_wii.play()
        points -= 300
    elif points <= 300 and mode == "game" and rb_button.collidepoint(pos):
        sounds.not_allowed.play()
    
    if mode == "game" and touch_mode:
        moving_left = moving_right = moving_up = moving_down = False
        if left.collidepoint(pos) and button == mouse.LEFT:
            moving_left = True
        if right.collidepoint(pos) and button == mouse.LEFT:
            moving_right = True
        if up.collidepoint(pos) and button == mouse.LEFT:
            moving_up = True
        if down.collidepoint(pos) and button == mouse.LEFT:
            moving_down = True

def on_mouse_up(button, pos):
    global moving_left, moving_right, moving_up, moving_down

    if mode == "game" and touch_mode:
        if left.collidepoint(pos) or right.collidepoint(pos) or up.collidepoint(pos) or down.collidepoint(pos):
            moving_left = moving_right = moving_up = moving_down = False



pgzrun.go()
