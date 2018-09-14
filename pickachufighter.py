import pygame
import time # used sleep one
import random # random to make things

pygame.init() #without this no run

crash_sound = pygame.mixer.Sound("file-name.wav") # music file for crash sound

pygame.mixer.music.load("file-name.mp3") # music file


display_width=800 #defined width of window
display_height=500 #defined height of window

black = (0,0,0) #color code for black minimum value 0
white = (255,255,255) #Color code for white maximum 255 RGB
red = (200,0,0) # color code
green = (0,200,0) # color code
blue = (0,0,255) # color
yellow = (242,237,3) # color bright for our button
violet = (64,0,64) # color bright for our button

block_color = (53,115,225)

pause = False  # pause global variable 

pickachuWidth = 63 #define if boundry of imagre  then exit hoga

gameDisplay = pygame.display.set_mode((display_width ,display_height)) #display window and tuple 

pygame.display.set_caption("PIKACHU FIGHTER") #caption

clock=pygame.time.Clock() #clock use 

pickachuImg = pygame.image.load("file-name.png")# pickachu ki image

pickIcon = pygame.image.load("filename.png")
pygame.display.set_icon(pickIcon)



def things_dodged(count): # score 

    font = pygame.font.SysFont(None ,25) # font

    text = font.render("Score: "+str(count), True, black) 

    gameDisplay.blit(text, (0,0)) 

    


    
                            


def pickachu(x,y):
    
    gameDisplay.blit(pickachuImg,(x,y)) 


def things(thingx, thingy, thingw, thingh, color): 

    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh]) #draw rect

    


def text_objects(text, font): # text aur font ke liye func parameter as specified

    textSurface = font.render(text, True, black) #render pygame fun passed text true and color

    return textSurface , textSurface.get_rect() # to position our text


def message_display(text): 

    largeText = pygame.font.Font('freesansbold.ttf',35) # font name and size define 

    TextSurf , TextRect = text_objects(text, largeText) # rectangle box 

    TextRect.center = ((display_width/2),(display_height/2)) # center 


    gameDisplay.blit(TextSurf,TextRect) 

    pygame.display.update() # need to update the msg after start game again after 5 sec



    time.sleep(2)# msg aane ke bad 5 sec tk msg show karega uske bad game start

    game_loop() 

    

    

def crash():

    pygame.mixer.music.stop() # background music stop 

    pygame.mixer.Sound.play(crash_sound) # crash sound play 

    
    
    
    largeText = pygame.font.Font('freesansbold.ttf',115) # font name and size define 

    TextSurf , TextRect = text_objects("GAME OVER", largeText) # rectangle box parameter pass 

    TextRect.center = ((display_width/2),(display_height/2)) # center 

    gameDisplay.blit(TextSurf,TextRect) # blit fun message 


    

    while True: 
        
        

        for event in pygame.event.get():
            
            

            if event.type == pygame.QUIT:
                
                pygame.quit()
                quit()

        # gameDisplay.fill(white) not fill we can see score

        
        button("Play Again",170, 400, 200, 70, red,yellow,game_loop) # intro mai play button  play parameter

        button("QUIT",500, 400, 200, 70, green,violet,quitgame) # intro mai Quit button call parameter
        


        #pygame.draw.ellipse(gameDisplay, green, [500, 400, 200, 70], 10) # x+width y+height 
            


        pygame.display.update() # display kara

        clock.tick(15) # 15 sec 
    

    mouse = pygame.mouse.get_pos() # mouse postion wanna give click to it

    click = pygame.mouse.get_pressed() #(l_click, M_click, R_click) for e.g (0,0,1) rightclick print click u can see

    

    if x+width > mouse[0] >x and y+height > mouse[1] >y: # x+width y+height

         pygame.draw.rect(gameDisplay, a_color, (x, y, width, height)) # x+width y+height 

         if click[0] ==1 and action !=None: #click 

             action() 

##             if action == "play": # action hua then
##
##                 game_loop()
##
##             elif action == "quit":
##
##                 pygame.quit()
##
##                 quit()
             


    else:
        
        pygame.draw.rect(gameDisplay, i_color, (x, y, width, height)) # x+width y+height

        smallText = pygame.font.Font('freesansbold.ttf',20)

        textSurf, textRect = text_objects(msg, smallText)

        textRect.center = ((x+(width/2)), ((y+(height/2)))) # by 2 

        gameDisplay.blit(textSurf, textRect) #blit 



def quitgame():

    pygame.quit()

    quit()

    

def unpause():

    global pause

    pygame.mixer.music.upause()

    pause = False


def paused(): # menu  pause

    pygame.mixer.music.pause() # pause music when it plays pause function now to upause unpause function

    largeText = pygame.font.Font('freesansbold.ttf',115)
	
    TextSurf , TextRect = text_objects("Paused", largeText) # rectangle box

    TextRect.center = ((display_width/2),(display_height/2)) # center 

    gameDisplay.blit(TextSurf,TextRect) # blit 


    # intro start hua

    while pause: 
        

        for event in pygame.event.get():
            
            

            if event.type == pygame.QUIT:
                
                pygame.quit()
                quit()

        # gameDisplay.fill(white) not fill we can see score

        
        button("Continue",170, 400, 200, 70, red,yellow,unpause) 

        button("QUIT",500, 400, 200, 70, green,violet,quitgame) 
        


        #pygame.draw.ellipse(gameDisplay, green, [500, 400, 200, 70], 10) # x+width y+height 
            


        pygame.display.update() # display

        clock.tick(15) # 15 

    

    



def game_intro(): # menu  

    intro = True # intro start hua

    while intro: 
        
        

        for event in pygame.event.get():
            
            

            if event.type == pygame.QUIT:
                
                pygame.quit()
                quit()

        gameDisplay.fill(white)

        largeText = pygame.font.Font('freesansbold.ttf',35) # font name and size define 

        TextSurf , TextRect = text_objects('PIKACHU FIGHTER', largeText) # rectangle box 

        TextRect.center = ((display_width/2),(display_height/2)) # center 

        gameDisplay.blit(TextSurf,TextRect) # blit 

        button("GO!",170, 400, 200, 70, red,yellow,game_loop) 

        button("QUIT",500, 400, 200, 70, green,violet,quitgame) # intro
        


        #pygame.draw.ellipse(gameDisplay, green, [500, 400, 200, 70], 10) # x+width y+height 
            


        pygame.display.update() # display kara

        clock.tick(15) # 15 sec ke liye screen pr rahega

    

    


def game_loop(): 


    global pause

    pygame.mixer.music.play(-1) # it will play in loop music will continue to play
    
    x = (display_width*0.40)
    y = (display_height*0.8)

    x_change = 0 # if key pressed then to store location of the image

    thing_startx = random.randrange(0, display_width) 

    thing_starty =  -600 # thing first upar mai -600 par banega

    thing_speed = 4

    thing_width = 100

    thing_height = 100

    thingCount=1

    dodged = 0 # initially no of dodged thing is 0
    


        




    #game loop start and it break iff it got crashed or close all  event in pygame hoga

    gameExit = False 



    while not gameExit: #loop starts event handling loop

        for event in pygame.event.get(): #list of event per sec if clicked or shoot or any thing
            

            if event.type == pygame.QUIT:    #user can be asked to quit the game if he wants pygame.Quit() quit then close
                pygame.quit() #exit button will work
                quit() # quit the program

            if event.type == pygame.KEYDOWN: #key press hua then kya hoga

                if event.key == pygame.K_LEFT: # left arrow key press  then location change

                    x_change = -5  # left key press pr -5 left  postion change in x

                if event.key == pygame.K_RIGHT: 

                    x_change = 5   # right key press  x  position change by 5

                if event.key == pygame.K_SPACE:

                    pause = True #global variable pause ko true kara

                    paused() # paused function call 

                    

            if event.type == pygame.KEYUP: 

                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:

                    x_change = 0 


        x +=x_change 

                

            

            

                    
                

        gameDisplay.fill(white)


        # things(thingx, thingy, thingw, thingh, color)
        things(thing_startx, thing_starty, thing_width, thing_height, block_color)

        thing_starty += thing_speed
            
        pickachu(x,y) #function call for making pickachu

        things_dodged(dodged) # func ke andar count ke jagah dodged pass kara

        if x >display_width - pickachuWidth or x < 0: 

            crash()

        if thing_starty > display_height: 

            thing_starty = 0 - thing_height 

            thing_startx = random.randrange(0, display_width) 

            dodged += 1 # score badhate jana hai

            if dodged % 5 == 0: # score % 5 == 0 then increase difficulty

                thing_speed += 1 # increase the speed

                thing_width += (dodged*1.5) #increase the width

            



        if y < thing_starty + thing_height: 

            print('Y crossover') 

            if x > thing_startx and x < thing_startx + thing_width or x+pickachuWidth > thing_startx and x+pickachuWidth < thing_startx+thing_width:

                print('x Crossover')

                crash() # crash  called  to crash 

                
                

            

            #gameExit = True 



        pygame.display.flip()  

        clock.tick(60) #frame rate defined  how fast it move


game_intro()

game_loop() 

pygame.quit()

quit()

