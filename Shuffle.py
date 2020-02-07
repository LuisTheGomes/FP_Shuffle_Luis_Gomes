import pygame
import pygame.freetype
import random

def main():

    pygame.init()

    menu()

# A função menu() desenha o menu e apresenta as várias opções de jogo

def menu():
    
    my_font = pygame.freetype.Font("NotoSans-Regular.ttf", 24)

    logo = pygame.image.load("shuffle.png")

    res = (1280,720)

    screen = pygame.display.set_mode(res)

    screen.fill((0,0,20))

    my_font.render_to(screen, (575, 307), "4x3", (255, 255, 0))

    my_font.render_to(screen, (575, 347), "4x4", (255, 255, 0))

    my_font.render_to(screen, (575, 387), "5x4", (255, 255, 0))

    my_font.render_to(screen, (575, 427), "6x4", (255, 255, 0))

    my_font.render_to(screen, (575, 467), "6x5", (255, 255, 0))

    my_font.render_to(screen, (575, 507), "6x6", (255, 255, 0))

    my_font.render_to(screen, (575, 567), "Exit", (255, 255, 0))

    dim4x3 = pygame.draw.rect(screen, (255, 255, 0), (540,300,120,30),3)

    dim4x4 = pygame.draw.rect(screen, (255, 255, 0), (540,340,120,30),3)

    dim5x4 = pygame.draw.rect(screen, (255, 255, 0), (540,380,120,30),3)

    dim6x4 = pygame.draw.rect(screen, (255, 255, 0), (540,420,120,30),3)

    dim6x5 = pygame.draw.rect(screen, (255, 255, 0), (540,460,120,30),3)

    dim6x6 = pygame.draw.rect(screen, (255, 255, 0), (540,500,120,30),3)

    sair = pygame.draw.rect(screen, (255, 255, 0), (540,560,120,30),3)

    screen.blit(logo, (220,40))

    pygame.display.flip()

    while(True):

        for event in pygame.event.get():

            if (event.type == pygame.QUIT):

                exit()
            
            #Se o jogador efetuar um click com o botão esquerdo do rato

            if event.type == pygame.MOUSEBUTTONDOWN and event.button== 1:

                #Se a posição do rato ao efetuar um click colidir com alguma das surfaces
                pos = pygame.mouse.get_pos()

                if sair.collidepoint(pos):

                    exit()
                
                if dim4x3.collidepoint(pos):

                    game4x3()

                if dim4x4.collidepoint(pos):

                    game4x4()
                
                if dim5x4.collidepoint(pos):

                    game5x4()
                
                if dim6x4.collidepoint(pos):

                    game6x4()
                
                if dim6x5.collidepoint(pos):

                    game6x5()
                
                if dim6x6.collidepoint(pos):

                    game6x6()

#Dividi o jogo em 6 funções, cada uma com um número específico de cartas.
#Não existe grande diferença entre elas visto que o ciclo do jogo é igual.

def game4x3():

    shapes = shapes_pos(6)

    my_font = pygame.freetype.Font("NotoSans-Regular.ttf", 24)

    res = (1280,720)

    screen = pygame.display.set_mode(res)

    screen.fill((0,0,20))

    #Cada uma destas surfaces corresponde a uma carta
    #O primeiro no nome da variável número indica a sua posição horizontal e o segundo a sua posição vertical

    card1x1 = pygame.draw.rect(screen,(124,252,0), (350, 50, 130, 200),0)

    card2x1 = pygame.draw.rect(screen,(124,252,0), (490, 50, 130, 200),0)

    card3x1 = pygame.draw.rect(screen,(124,252,0), (630, 50, 130, 200),0)

    card4x1 = pygame.draw.rect(screen,(124,252,0), (770, 50, 130, 200),0)

    card1x2 = pygame.draw.rect(screen,(124,252,0), (350, 260, 130, 200),0)

    card2x2 = pygame.draw.rect(screen,(124,252,0), (490, 260, 130, 200),0)

    card3x2 = pygame.draw.rect(screen,(124,252,0), (630, 260, 130, 200),0)

    card4x2 = pygame.draw.rect(screen,(124,252,0), (770, 260, 130, 200),0)

    card1x3 = pygame.draw.rect(screen,(124,252,0), (350, 470, 130, 200),0)

    card2x3 = pygame.draw.rect(screen,(124,252,0), (490, 470, 130, 200),0)

    card3x3 = pygame.draw.rect(screen,(124,252,0), (630, 470, 130, 200),0)

    card4x3 = pygame.draw.rect(screen,(124,252,0), (770, 470, 130, 200),0)

    sair = pygame.draw.rect(screen, (255, 255, 0), (30,600,120,30),3)

    my_font.render_to(screen, (65, 607), "Exit", (255, 255, 0))

    pygame.display.flip()

    turned_card=[]
    card_ver=[] 
    removed_card=[] #Se um par for encontrado, o número associado á carta é adicionado a esta lista
    win=0
    score=0

    #Cada uma destas variáveis,associadas a uma carta cada, representa a penalização do jogador ao virar uma carta

    penalty1x1=-20
    penalty2x1=-20
    penalty3x1=-20
    penalty4x1=-20
    penalty1x2=-20
    penalty2x2=-20
    penalty3x2=-20
    penalty4x2=-20
    penalty1x3=-20
    penalty2x3=-20
    penalty3x3=-20
    penalty4x3=-20

    score_display = my_font.render_to(screen, (10, 10), "Score: " + str(score), (255, 255, 0))

    #Ciclo de jogo

    while(True):

        pygame.display.flip()

        for event in pygame.event.get():

            if (event.type == pygame.QUIT):

                exit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button== 1:

                pos = pygame.mouse.get_pos()

                if sair.collidepoint(pos):

                    menu()
                
                #Se o jogador clickar numa carta que não foi virada ou removida, esta é virada
                
                if card1x1.collidepoint(pos) and 1 not in turned_card and 1 not in removed_card:

                    turned_card.append(1)

                    screen.fill((0,0,20),card1x1)

                    card1x1= pygame.draw.rect(screen,(200,0,0),(350, 50, 130, 200),1)

                    #A carta é preenchida com a cor do background e depois o seu outline é desenhado

                    draw = shapes[0]

                    #A lista shapes contém a forma associada á posição da carta, com cada forma associada a um número

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(415,150,30,30))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(415,150,30,30))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(415,150),15)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(415,150),15)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(415,150,30,30))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(415,150),15)

                    pygame.display.flip()


                if card2x1.collidepoint(pos) and 2 not in turned_card and 2 not in removed_card:

                    turned_card.append(2)

                    screen.fill((0,0,20),card2x1)

                    card2x1 = pygame.draw.rect(screen,(200,0,0), (490, 50, 130, 200),1)

                    draw = shapes[1]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(555,150,30,30))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(555,150,30,30))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(555,150),15)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(555,150),15)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(555,150,30,30))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(555,150),15)

                    pygame.display.flip()


                if card3x1.collidepoint(pos) and 3 not in turned_card and 3 not in removed_card:

                    turned_card.append(3)

                    screen.fill((0,0,20),card3x1)

                    card3x1 = pygame.draw.rect(screen,(200,0,0), (630, 50, 130, 200),1)

                    draw = shapes[2]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(695,150,30,30))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(695,150,30,30))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(695,150),15)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(695,150),15)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(695,150,30,30))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(695,150),15)

                    pygame.display.flip()

                if card4x1.collidepoint(pos) and 4 not in turned_card and 4 not in removed_card:

                    turned_card.append(4)

                    screen.fill((0,0,20),card4x1)
                    
                    card4x1 = pygame.draw.rect(screen,(200,0,0), (770, 50, 130, 200),1)

                    draw = shapes[3]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(835,150,30,30))
         
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(835,150,30,30))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(835,150),15)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(835,150),15)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(835,150,30,30))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(835,150),15)

                    pygame.display.flip()

                if card1x2.collidepoint(pos) and 5 not in turned_card and 5 not in removed_card:

                    turned_card.append(5)

                    screen.fill((0,0,20),card1x2)

                    card1x2 = pygame.draw.rect(screen,(200,0,0), (350, 260, 130, 200),1)

                    draw = shapes[4]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(415,360,30,30))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(415,360,30,30))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(415,360),15)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(415,360),15)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(415,360,30,30))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(415,360),15)

                    pygame.display.flip()

                if card2x2.collidepoint(pos) and 6 not in turned_card and 6 not in removed_card:

                    turned_card.append(6)

                    screen.fill((0,0,20),card2x2)

                    card2x2 = pygame.draw.rect(screen,(124,252,0), (490, 260, 130, 200),1)

                    draw = shapes[5]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(555,360,30,30))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(555,360,30,30))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(555,360),15)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(555,360),15)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(555,360,30,30))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(555,360),15)

                    pygame.display.flip()

                if card3x2.collidepoint(pos) and 7 not in turned_card and 7 not in removed_card:

                    turned_card.append(7)

                    screen.fill((0,0,20),card3x2)

                    card3x2 = pygame.draw.rect(screen,(124,252,0), (630, 260, 130, 200),1)

                    draw = shapes[6]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(695,360,30,30))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(695,360,30,30))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(695,360),15)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(695,360),15)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(695,360,30,30))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(695,360),15)

                    pygame.display.flip()

                if card4x2.collidepoint(pos) and 8 not in turned_card and 8 not in removed_card:

                    turned_card.append(8)

                    screen.fill((0,0,20),card4x2)

                    card4x2 = pygame.draw.rect(screen,(124,252,0), (770, 260, 130, 200),1)

                    draw = shapes[7]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(835,360,30,30))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(835,360,30,30))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(835,360),15)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(835,360),15)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(835,360,30,30))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(835,360),15)

                    pygame.display.flip()

                if card1x3.collidepoint(pos) and 9 not in turned_card and 9 not in removed_card:

                    turned_card.append(9)

                    screen.fill((0,0,20),card1x3)

                    card1x3 = pygame.draw.rect(screen,(124,252,0), (350, 470, 130, 200),1)

                    draw = shapes[8]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(415,570,30,30))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(415,570,30,30))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(415,570),15)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(415,570),15)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(415,570,30,30))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(415,570),15)

                    pygame.display.flip()

                if card2x3.collidepoint(pos) and 10 not in turned_card and 10 not in removed_card:

                    turned_card.append(10)

                    screen.fill((0,0,20),card2x3)

                    card2x3 = pygame.draw.rect(screen,(124,252,0), (490, 470, 130, 200),1)

                    draw = shapes[9]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(555,570,30,30))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(555,570,30,30))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(555,570),15)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(555,570),15)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(555,570,30,30))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(555,570),15)

                    pygame.display.flip()

                if card3x3.collidepoint(pos) and 11 not in turned_card and 11 not in removed_card:

                    turned_card.append(11)

                    screen.fill((0,0,20),card3x3)

                    card3x3 = pygame.draw.rect(screen,(124,252,0), (630, 470, 130, 200),1)

                    draw = shapes[10]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(695,570,30,30))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(695,570,30,30))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(695,570),15)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(695,570),15)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(695,570,30,30))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(695,570),15)

                    pygame.display.flip()

                if card4x3.collidepoint(pos) and 12 not in turned_card and 12 not in removed_card:

                    turned_card.append(12)

                    screen.fill((0,0,20),card4x3)

                    card4x3 = pygame.draw.rect(screen,(124,252,0), (770, 470, 130, 200),1)

                    draw = shapes[11]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(835,570,30,30))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(835,570,30,30))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(835,570),15)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(835,570),15)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(835,570,30,30))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(835,570),15)

                    pygame.display.flip()

                #Se foram viradas 2 cartas, é verificado se as formas coincidem
                
                if len(turned_card)==2:

                    pygame.time.wait(1000)

                    if card_ver[0]==card_ver[1]:

                        score+=100

                        pygame.draw.rect(screen,(0,0,20),(0,0,100,100))
                        
                        score_display = my_font.render_to(screen, (10, 10), "Score: " + str(score), (255, 255, 0))

                        pygame.display.flip()

                        #As cartas são removidas ao serem preenchidas pela cor do background

                        removed_card.append(turned_card[0])
                        removed_card.append(turned_card[1])

                        win+=2 
                    
                        for i in turned_card:

                            if i==1:
                                
                                screen.fill((0,0,20),card1x1)

                            if i==2:

                                screen.fill((0,0,20),card2x1)


                            if i==3:
                                
                                screen.fill((0,0,20),card3x1)

                            if i==4:

                                screen.fill((0,0,20),card4x1)
                                
                            if i==5:

                                screen.fill((0,0,20),card1x2)
                                
                            if i==6:

                                screen.fill((0,0,20),card2x2)

                            if i==7:

                                screen.fill((0,0,20),card3x2)

                            if i==8:

                                screen.fill((0,0,20),card4x2)
                                
                            if i==9:

                                screen.fill((0,0,20),card1x3)
                                
                            if i==10:

                                screen.fill((0,0,20),card2x3)
                                
                            if i==11:

                                screen.fill((0,0,20),card3x3)
                                
                            if i==12:

                                screen.fill((0,0,20),card4x3)

                    else:

                        #Se as formas não forem iguais a carta é virada novamente e a penaçlização associada a cada carta é incrementada

                        for i in turned_card:

                            if i==1:

                                penalty1x1+=20

                                score=score-penalty1x1
                                
                                card1x1 = pygame.draw.rect(screen,(124,252,0), (350, 50, 130, 200),0)

                            if i==2:

                                penalty2x1+=20

                                score=score-penalty2x1

                                card2x1 = pygame.draw.rect(screen,(124,252,0), (490, 50, 130, 200),0)


                            if i==3:

                                penalty3x1+=20

                                score=score-penalty3x1
                                
                                card3x1 = pygame.draw.rect(screen,(124,252,0), (630, 50, 130, 200),0)

                            if i==4:

                                penalty4x1+=20

                                score=score-penalty4x1

                                card4x1 = pygame.draw.rect(screen,(124,252,0), (770, 50, 130, 200),0)
                                
                            if i==5:

                                penalty1x2+=20

                                score=score-penalty1x2

                                card1x2 = pygame.draw.rect(screen,(124,252,0), (350, 260, 130, 200),0)
                                
                            if i==6:

                                penalty2x2+=20

                                score=score-penalty2x2

                                card2x2 = pygame.draw.rect(screen,(124,252,0), (490, 260, 130, 200),0)

                            if i==7:

                                penalty3x2+=20

                                score=score-penalty3x2

                                card3x2 = pygame.draw.rect(screen,(124,252,0), (630, 260, 130, 200),0)

                            if i==8:

                                penalty4x2+=20

                                score=score-penalty4x2

                                card4x2 = pygame.draw.rect(screen,(124,252,0), (770, 260, 130, 200),0)
                                
                            if i==9:

                                penalty1x3+=20

                                score=score-penalty1x3

                                card1x3 = pygame.draw.rect(screen,(124,252,0), (350, 470, 130, 200),0)
                                
                            if i==10:

                                penalty2x3+=20

                                score=score-penalty2x3

                                card2x3 = pygame.draw.rect(screen,(124,252,0), (490, 470, 130, 200),0)
                                
                            if i==11:

                                penalty3x3+=20

                                score=score-penalty3x3

                                card3x3 = pygame.draw.rect(screen,(124,252,0), (630, 470, 130, 200),0)
                                
                            if i==12:

                                penalty4x3+=20

                                score=score-penalty4x3

                                card4x3 = pygame.draw.rect(screen,(124,252,0), (770, 470, 130, 200),0)

                    turned_card=[]

                    card_ver=[]

                    pygame.draw.rect(screen,(0,0,20),(0,0,200,200))

                    if score<0:

                        score = 0
                        
                    score_display = my_font.render_to(screen, (10, 10), "Score: " + str(score), (255, 255, 0))

                
                    pygame.display.flip()

                    if win==12:
                        
                        my_font.render_to(screen, (540, 360), "CONGRATULATIONS, YOU WON!", (255, 255, 0))

                        pygame.display.flip()

def game4x4():

    my_font = pygame.freetype.Font("NotoSans-Regular.ttf", 24)

    res = (1280,720)

    screen = pygame.display.set_mode(res)

    screen.fill((0,0,20))

    card1x1 = pygame.draw.rect(screen,(124,252,0), (350, 50, 90, 150),0)

    card2x1 = pygame.draw.rect(screen,(124,252,0), (450, 50, 90, 150),0)

    card3x1 = pygame.draw.rect(screen,(124,252,0), (550, 50, 90, 150),0)

    card4x1 = pygame.draw.rect(screen,(124,252,0), (650, 50, 90, 150),0)

    card1x2 = pygame.draw.rect(screen,(124,252,0), (350, 210, 90, 150),0)

    card2x2 = pygame.draw.rect(screen,(124,252,0), (450, 210, 90, 150),0)

    card3x2 = pygame.draw.rect(screen,(124,252,0), (550, 210, 90, 150),0)

    card4x2 = pygame.draw.rect(screen,(124,252,0), (650, 210, 90, 150),0)

    card1x3 = pygame.draw.rect(screen,(124,252,0), (350, 370, 90, 150),0)

    card2x3 = pygame.draw.rect(screen,(124,252,0), (450, 370, 90, 150),0)

    card3x3 = pygame.draw.rect(screen,(124,252,0), (550, 370, 90, 150),0)

    card4x3 = pygame.draw.rect(screen,(124,252,0), (650, 370, 90, 150),0)

    card1x4 = pygame.draw.rect(screen,(124,252,0), (350, 530, 90, 150),0)

    card2x4 = pygame.draw.rect(screen,(124,252,0), (450, 530, 90, 150),0)

    card3x4 = pygame.draw.rect(screen,(124,252,0), (550, 530, 90, 150),0)

    card4x4 = pygame.draw.rect(screen,(124,252,0), (650, 530, 90, 150),0)

    sair = pygame.draw.rect(screen, (255, 255, 0), (30,600,120,30),3)

    shapes = shapes_pos(8)

    my_font.render_to(screen, (65, 607), "Exit", (255, 255, 0))

    pygame.display.flip()

    turned_card=[]
    card_ver=[]
    removed_card=[]
    win=0
    score=0
    penalty1x1=-20
    penalty2x1=-20
    penalty3x1=-20
    penalty4x1=-20
    penalty1x2=-20
    penalty2x2=-20
    penalty3x2=-20
    penalty4x2=-20
    penalty1x3=-20
    penalty2x3=-20
    penalty3x3=-20
    penalty4x3=-20
    penalty1x4=-20
    penalty2x4=-20
    penalty3x4=-20
    penalty4x4=-20
    

    score_display = my_font.render_to(screen, (10, 10), "Score: " + str(score), (255, 255, 0))


    while(True):

        pygame.display.flip()

        for event in pygame.event.get():

            if (event.type == pygame.QUIT):

                exit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button== 1:

                pos = pygame.mouse.get_pos()

                if sair.collidepoint(pos):

                    menu()
                
                if card1x1.collidepoint(pos) and 1 not in turned_card and 1 not in removed_card:

                    turned_card.append(1)

                    screen.fill((0,0,20),card1x1)

                    card1x1 = pygame.draw.rect(screen,(0,200,0), (350, 50, 90, 150),1)

                    draw = shapes[0]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(395,120,30,30))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(395,120,30,30))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(395,120),15)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(395,120),15)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(395,120,30,30))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(395,120),15)

                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(395,120),15)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(395,120,30,30))
                        

                    pygame.display.flip()


                if card2x1.collidepoint(pos) and 2 not in turned_card and 2 not in removed_card:

                    turned_card.append(2)

                    screen.fill((0,0,20),card2x1)

                    card2x1 = pygame.draw.rect(screen,(124,252,0), (450, 50, 90, 150),1)

                    draw = shapes[1]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(495,120,30,30))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(495,120,30,30))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(495,120),15)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(495,120),15)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(495,120,30,30))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(495,120),15)

                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(495,120),15)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(495,120,30,30))

                    

                    pygame.display.flip()


                if card3x1.collidepoint(pos) and 3 not in turned_card and 3 not in removed_card:

                    turned_card.append(3)

                    screen.fill((0,0,20),card3x1)

                    card3x1 = pygame.draw.rect(screen,(124,252,0), (550, 50, 90, 150),1)

                    draw = shapes[2]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(595,120,30,30))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(595,120,30,30))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(595,120),15)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(595,120),15)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(595,120,30,30))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(595,120),15)

                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(595,120),15)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(595,120,30,30))

                    pygame.display.flip()

                if card4x1.collidepoint(pos) and 4 not in turned_card and 4 not in removed_card:

                    turned_card.append(4)

                    screen.fill((0,0,20),card4x1)
                    
                    card4x1 = pygame.draw.rect(screen,(124,252,0), (650, 50, 90, 150),1)

                    draw = shapes[3]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(695,120,30,30))
         
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(695,120,30,30))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(695,120),15)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(695,120),15)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(695,120,30,30))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(695,120),15)
                    
                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(695,120),15)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(695,120,30,30))

                    pygame.display.flip()

                if card1x2.collidepoint(pos) and 5 not in turned_card and 5 not in removed_card:

                    turned_card.append(5)

                    screen.fill((0,0,20),card1x2)

                    card1x2 = pygame.draw.rect(screen,(124,252,0), (350, 210, 90, 150),1)

                    draw = shapes[4]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(395,280,30,30))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(395,280,30,30))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(395,280),15)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(395,280),15)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(395,280,30,30))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(395,280),15)

                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(395,280),15)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(395,280,30,30))

                    pygame.display.flip()

                if card2x2.collidepoint(pos) and 6 not in turned_card and 6 not in removed_card:

                    turned_card.append(6)

                    screen.fill((0,0,20),card2x2)

                    card2x2 = pygame.draw.rect(screen,(124,252,0), (450, 210, 90, 150),1)

                    draw = shapes[5]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(495,280,30,30))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(495,280,30,30))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(495,280),15)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(495,280),15)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(495,280,30,30))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(495,280),15)
                    
                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(495,280),15)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(495,280,30,30))

                    pygame.display.flip()

                if card3x2.collidepoint(pos) and 7 not in turned_card and 7 not in removed_card:

                    turned_card.append(7)

                    screen.fill((0,0,20),card3x2)

                    card3x2 = pygame.draw.rect(screen,(124,252,0), (550, 210, 90, 150),1)

                    draw = shapes[6]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(595,280,30,30))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(595,280,30,30))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(595,280),15)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(595,280),15)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(595,280,30,30))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(595,280),15)
                    
                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(595,280),15)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(595,280,30,30))

                    pygame.display.flip()

                if card4x2.collidepoint(pos) and 8 not in turned_card and 8 not in removed_card:

                    turned_card.append(8)

                    screen.fill((0,0,20),card4x2)

                    card4x2 = pygame.draw.rect(screen,(124,252,0), (650, 210, 90, 150),1)

                    draw = shapes[7]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(695,280,30,30))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(695,280,30,30))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(695,280),15)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(695,280),15)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(695,280,30,30))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(695,280),15)

                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(695,280),15)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(695,280,30,30))

                    pygame.display.flip()

                if card1x3.collidepoint(pos) and 9 not in turned_card and 9 not in removed_card:

                    turned_card.append(9)

                    screen.fill((0,0,20),card1x3)

                    card1x3 = pygame.draw.rect(screen,(124,252,0), (350, 370, 90, 150),1)

                    draw = shapes[8]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(395,440,30,30))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(395,440,30,30))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(395,440),15)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(395,440),15)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(395,440,30,30))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(395,440),15)

                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(395,440),15)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(395,440,30,30))

                    pygame.display.flip()

                if card2x3.collidepoint(pos) and 10 not in turned_card and 10 not in removed_card:

                    turned_card.append(10)

                    screen.fill((0,0,20),card2x3)

                    card2x3 = pygame.draw.rect(screen,(124,252,0), (450, 370, 90, 150),1)

                    draw = shapes[9]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(495,440,30,30))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(495,440,30,30))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(495,440),15)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(495,440),15)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(495,440,30,30))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(495,440),15)

                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(495,440),15)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(495,440,30,30))

                    pygame.display.flip()

                if card3x3.collidepoint(pos) and 11 not in turned_card and 11 not in removed_card:

                    turned_card.append(11)

                    screen.fill((0,0,20),card3x3)

                    card3x3 = pygame.draw.rect(screen,(124,252,0), (550, 370, 90, 150),1)

                    draw = shapes[10]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(595,440,30,30))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(595,440,30,30))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(595,440),15)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(595,440),15)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(595,440,30,30))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(595,440),15)

                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(595,440),15)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(595,440,30,30))

                    pygame.display.flip()

                if card4x3.collidepoint(pos) and 12 not in turned_card and 12 not in removed_card:

                    turned_card.append(12)

                    screen.fill((0,0,20),card4x3)

                    card4x3 = pygame.draw.rect(screen,(124,252,0), (650, 370, 90, 150),1)

                    draw = shapes[11]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(695,440,30,30))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(695,440,30,30))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(695,440),15)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(695,440),15)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(695,440,30,30))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(695,440),15)
                    
                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(695,440),15)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(695,440,30,30))

                    pygame.display.flip()

                if card1x4.collidepoint(pos) and 13 not in turned_card and 13 not in removed_card:

                    turned_card.append(13)

                    screen.fill((0,0,20),card1x4)

                    card1x4 = pygame.draw.rect(screen,(124,252,0), (350, 530, 90, 150),1)

                    draw = shapes[12]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(395,600,30,30))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(395,600,30,30))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(395,600),15)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(395,600),15)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(395,600,30,30))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(395,600),15)
                    
                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(395,600),15)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(395,600,30,30))

                    pygame.display.flip()

                if card2x4.collidepoint(pos) and 14 not in turned_card and 14 not in removed_card:

                    turned_card.append(14)

                    screen.fill((0,0,20),card2x4)

                    card2x4 = pygame.draw.rect(screen,(124,252,0), (450, 530, 90, 150),1)

                    draw = shapes[13]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(495,600,30,30))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(495,600,30,30))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(495,600),15)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(495,600),15)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(495,600,30,30))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(495,600),15)
                    
                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(495,600),15)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(495,600,30,30))

                    pygame.display.flip()

                if card3x4.collidepoint(pos) and 15 not in turned_card and 15 not in removed_card:

                    turned_card.append(15)

                    screen.fill((0,0,20),card3x4)

                    card3x4 = pygame.draw.rect(screen,(124,252,0), (550, 530, 90, 150),1)

                    draw = shapes[14]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(595,600,30,30))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(595,600,30,30))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(595,600),15)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(595,600),15)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(595,600,30,30))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(595,600),15)
                    
                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(595,600),15)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(595,600,30,30))

                    pygame.display.flip()

                if card4x4.collidepoint(pos) and 16 not in turned_card and 16 not in removed_card:

                    turned_card.append(16)

                    screen.fill((0,0,20),card4x4)

                    card4x4 = pygame.draw.rect(screen,(124,252,0), (650, 530, 90, 150),1)

                    draw = shapes[15]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(695,600,30,30))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(695,600,30,30))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(695,600),15)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(695,600),15)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(695,600,30,30))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(695,600),15)
                    
                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(695,600),15)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(695,600,30,30))

                    pygame.display.flip()
                
                if len(turned_card)==2:

                    pygame.time.wait(1000)

                    if card_ver[0]==card_ver[1]:

                        score+=100

                        pygame.draw.rect(screen,(0,0,20),(0,0,100,100))
                        
                        score_display = my_font.render_to(screen, (10, 10), "Score: " + str(score), (255, 255, 0))

                        pygame.display.flip()

                        removed_card.append(turned_card[0])
                        removed_card.append(turned_card[1])

                        win+=2 
                    
                        for i in turned_card:

                            if i==1:
                                
                                screen.fill((0,0,20),card1x1)

                            if i==2:

                                screen.fill((0,0,20),card2x1)


                            if i==3:
                                
                                screen.fill((0,0,20),card3x1)

                            if i==4:

                                screen.fill((0,0,20),card4x1)
                                
                            if i==5:

                                screen.fill((0,0,20),card1x2)
                                
                            if i==6:

                                screen.fill((0,0,20),card2x2)

                            if i==7:

                                screen.fill((0,0,20),card3x2)

                            if i==8:

                                screen.fill((0,0,20),card4x2)
                                
                            if i==9:

                                screen.fill((0,0,20),card1x3)
                                
                            if i==10:

                                screen.fill((0,0,20),card2x3)
                                
                            if i==11:

                                screen.fill((0,0,20),card3x3)
                                
                            if i==12:

                                screen.fill((0,0,20),card4x3)
                            
                            if i==13:

                                screen.fill((0,0,20),card1x4)
                                
                            if i==14:

                                screen.fill((0,0,20),card2x4)
                                
                            if i==15:

                                screen.fill((0,0,20),card3x4)
                                
                            if i==16:

                                screen.fill((0,0,20),card4x4)

                    else:

                        for i in turned_card:

                            if i==1:

                                penalty1x1+=20

                                score=score-penalty1x1
                                
                                card1x1 = pygame.draw.rect(screen,(124,252,0), (350, 50, 90, 150),0)

                            if i==2:

                                penalty2x1+=20

                                score=score-penalty2x1
                                
                                card2x1 = pygame.draw.rect(screen,(124,252,0), (450, 50, 90, 150),0)


                            if i==3:

                                penalty3x1+=20

                                score=score-penalty3x1
                                
                                card3x1 = pygame.draw.rect(screen,(124,252,0), (550, 50, 90, 150),0)

                            if i==4:

                                penalty4x1+=20

                                score=score-penalty4x1

                                card4x1 = pygame.draw.rect(screen,(124,252,0), (650, 50, 90, 150),0)
                                
                            if i==5:

                                penalty1x2+=20

                                score=score-penalty1x2

                                card1x2 = pygame.draw.rect(screen,(124,252,0), (350, 210, 90, 150),0)
                                
                            if i==6:

                                penalty2x2+=20

                                score=score-penalty2x2

                                card2x2 = pygame.draw.rect(screen,(124,252,0), (450, 210, 90, 150),0)

                            if i==7:

                                penalty3x2+=20

                                score=score-penalty3x2

                                card3x2 = pygame.draw.rect(screen,(124,252,0), (550, 210, 90, 150),0)

                            if i==8:

                                penalty4x2+=20

                                score=score-penalty4x2

                                card4x2 = pygame.draw.rect(screen,(124,252,0), (650, 210, 90, 150),0)
                                
                            if i==9:

                                penalty1x3+=20

                                score=score-penalty1x3

                                card1x3 = pygame.draw.rect(screen,(124,252,0), (350, 370, 90, 150),0)
                                
                            if i==10:

                                penalty2x3+=20

                                score=score-penalty2x3

                                card2x3 = pygame.draw.rect(screen,(124,252,0), (450, 370, 90, 150),0)
                                
                            if i==11:

                                penalty3x3+=20

                                score=score-penalty3x3

                                card3x3 = pygame.draw.rect(screen,(124,252,0), (550, 370, 90, 150),0)
                                
                            if i==12:

                                penalty4x3+=20

                                score=score-penalty4x3

                                card4x3 = pygame.draw.rect(screen,(124,252,0), (650, 370, 90, 150),0)
                            
                            if i==13:

                                penalty1x4+=20

                                score=score-penalty1x4

                                card1x4 = pygame.draw.rect(screen,(124,252,0), (350, 530, 90, 150),0)

                                
                                
                            if i==14:

                                penalty2x4+=20

                                score=score-penalty2x4

                                card2x4 = pygame.draw.rect(screen,(124,252,0), (450, 530, 90, 150),0)
                                
                            if i==15:

                                penalty3x4+=20

                                score=score-penalty3x4

                                card3x4 = pygame.draw.rect(screen,(124,252,0), (550, 530, 90, 150),0)
                                
                            if i==16:

                                penalty4x4+=20

                                score=score-penalty4x4

                                card4x4 = pygame.draw.rect(screen,(124,252,0), (650, 530, 90, 150),0)

                                

                    turned_card=[]

                    card_ver=[]

                    pygame.draw.rect(screen,(0,0,20),(0,0,200,200))

                    if score<0:

                        score = 0
                        
                    score_display = my_font.render_to(screen, (10, 10), "Score: " + str(score), (255, 255, 0))

                
                    pygame.display.flip()

                    if win==16:
                        
                        my_font.render_to(screen, (540, 360), "CONGRATULATIONS, YOU WON!", (255, 255, 0))

                        pygame.display.flip()

def game5x4():

    my_font = pygame.freetype.Font("NotoSans-Regular.ttf", 24)

    res = (1280,720)

    screen = pygame.display.set_mode(res)

    screen.fill((0,0,20))

    card1x1 = pygame.draw.rect(screen,(124,252,0), (350, 50, 90, 150),0)

    card2x1 = pygame.draw.rect(screen,(124,252,0), (450, 50, 90, 150),0)

    card3x1 = pygame.draw.rect(screen,(124,252,0), (550, 50, 90, 150),0)

    card4x1 = pygame.draw.rect(screen,(124,252,0), (650, 50, 90, 150),0)

    card5x1 = pygame.draw.rect(screen,(124,252,0), (750, 50, 90, 150),0)

    card1x2 = pygame.draw.rect(screen,(124,252,0), (350, 210, 90, 150),0)

    card2x2 = pygame.draw.rect(screen,(124,252,0), (450, 210, 90, 150),0)

    card3x2 = pygame.draw.rect(screen,(124,252,0), (550, 210, 90, 150),0)

    card4x2 = pygame.draw.rect(screen,(124,252,0), (650, 210, 90, 150),0)

    card5x2 = pygame.draw.rect(screen,(124,252,0), (750, 210, 90, 150),0)

    card1x3 = pygame.draw.rect(screen,(124,252,0), (350, 370, 90, 150),0)

    card2x3 = pygame.draw.rect(screen,(124,252,0), (450, 370, 90, 150),0)

    card3x3 = pygame.draw.rect(screen,(124,252,0), (550, 370, 90, 150),0)

    card4x3 = pygame.draw.rect(screen,(124,252,0), (650, 370, 90, 150),0)

    card5x3 = pygame.draw.rect(screen,(124,252,0), (750, 370, 90, 150),0)

    card1x4 = pygame.draw.rect(screen,(124,252,0), (350, 530, 90, 150),0)

    card2x4 = pygame.draw.rect(screen,(124,252,0), (450, 530, 90, 150),0)

    card3x4 = pygame.draw.rect(screen,(124,252,0), (550, 530, 90, 150),0)

    card4x4 = pygame.draw.rect(screen,(124,252,0), (650, 530, 90, 150),0)

    card5x4 = pygame.draw.rect(screen,(124,252,0), (750, 530, 90, 150),0)

    sair = pygame.draw.rect(screen, (255, 255, 0), (30,600,120,30),3)

    my_font.render_to(screen, (65, 607), "Exit", (255, 255, 0))

    shapes = shapes_pos(10)

    turned_card=[]
    card_ver=[]
    removed_card=[]
    win=0
    score=0
    penalty1x1=-20
    penalty2x1=-20
    penalty3x1=-20
    penalty4x1=-20
    penalty5x1=-20
    penalty1x2=-20
    penalty2x2=-20
    penalty3x2=-20
    penalty4x2=-20
    penalty5x2=-20
    penalty1x3=-20
    penalty2x3=-20
    penalty3x3=-20
    penalty4x3=-20
    penalty5x3=-20
    penalty1x4=-20
    penalty2x4=-20
    penalty3x4=-20
    penalty4x4=-20
    penalty5x4=-20

    pygame.display.flip()

    score_display = my_font.render_to(screen, (10, 10), "Score: " + str(score), (255, 255, 0))


    while(True):

        pygame.display.flip()

        for event in pygame.event.get():

            if (event.type == pygame.QUIT):

                exit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button== 1:

                pos = pygame.mouse.get_pos()

                if sair.collidepoint(pos):

                    menu()
                
                if card1x1.collidepoint(pos) and 1 not in turned_card and 1 not in removed_card:

                    turned_card.append(1)

                    screen.fill((0,0,20),card1x1)

                    card1x1 = pygame.draw.rect(screen,(0,200,0), (350, 50, 90, 150),1)

                    draw = shapes[0]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(395,120,30,30))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(395,120,30,30))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(395,120),15)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(395,120),15)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(395,120,30,30))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(395,120),15)

                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(395,120),15)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(395,120,30,30))

                    elif draw==9:

                        card_ver.append(9)

                        pygame.draw.circle(screen,(200,200,200),(395,120),15)

                    elif draw==10:

                        card_ver.append(10)

                        pygame.draw.rect(screen,(200,200,200),(395,120,30,30))
                        

                    pygame.display.flip()

                if card2x1.collidepoint(pos) and 2 not in turned_card and 2 not in removed_card:

                    turned_card.append(2)

                    screen.fill((0,0,20),card2x1)

                    card2x1 = pygame.draw.rect(screen,(124,252,0), (450, 50, 90, 150),1)

                    draw = shapes[1]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(495,120,30,30))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(495,120,30,30))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(495,120),15)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(495,120),15)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(495,120,30,30))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(495,120),15)

                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(495,120),15)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(495,120,30,30))

                    elif draw==9:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(200,200,200),(495,120),15)

                    elif draw==10:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(200,200,200),(495,120,30,30))

                    

                    pygame.display.flip()

                if card3x1.collidepoint(pos) and 3 not in turned_card and 3 not in removed_card:

                    turned_card.append(3)

                    screen.fill((0,0,20),card3x1)

                    card3x1 = pygame.draw.rect(screen,(124,252,0), (550, 50, 90, 150),1)

                    draw = shapes[2]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(595,120,30,30))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(595,120,30,30))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(595,120),15)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(595,120),15)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(595,120,30,30))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(595,120),15)

                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(595,120),15)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(595,120,30,30))

                    elif draw==9:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,200,200),(595,120),15)

                    elif draw==10:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,200,200),(595,120,30,30))

                    pygame.display.flip()

                if card4x1.collidepoint(pos) and 4 not in turned_card and 4 not in removed_card:

                    turned_card.append(4)

                    screen.fill((0,0,20),card4x1)
                    
                    card4x1 = pygame.draw.rect(screen,(124,252,0), (650, 50, 90, 150),1)

                    draw = shapes[3]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(695,120,30,30))
         
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(695,120,30,30))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(695,120),15)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(695,120),15)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(695,120,30,30))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(695,120),15)
                    
                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(695,120),15)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(695,120,30,30))

                    elif draw==9:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,200,200),(695,120),15)

                    elif draw==10:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,200,200),(695,120,30,30))

                    pygame.display.flip()
                
                if card5x1.collidepoint(pos) and 5 not in turned_card and 5 not in removed_card:

                    turned_card.append(5)

                    screen.fill((0,0,20),card5x1)
                    
                    card5x1 = pygame.draw.rect(screen,(124,252,0), (750, 50, 90, 150),1)

                    draw = shapes[4]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(795,120,30,30))
         
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(795,120,30,30))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(795,120),15)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(795,120),15)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(795,120,30,30))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(795,120),15)
                    
                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(795,120),15)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(795,120,30,30))

                    elif draw==9:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,200,200),(795,120),15)

                    elif draw==10:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,200,200),(795,120,30,30))

                    pygame.display.flip()

                if card1x2.collidepoint(pos) and 6 not in turned_card and 6 not in removed_card:

                    turned_card.append(6)

                    screen.fill((0,0,20),card1x2)

                    card1x2 = pygame.draw.rect(screen,(124,252,0), (350, 210, 90, 150),1)

                    draw = shapes[5]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(395,280,30,30))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(395,280,30,30))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(395,280),15)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(395,280),15)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(395,280,30,30))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(395,280),15)

                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(395,280),15)

                    elif draw==8:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(0,200,200),(395,280,30,30))

                    elif draw==9:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,200,200),(395,280),15)

                    elif draw==10:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,200,200),(395,280,30,30))

                    pygame.display.flip()

                if card2x2.collidepoint(pos) and 7 not in turned_card and 7 not in removed_card:

                    turned_card.append(7)

                    screen.fill((0,0,20),card2x2)

                    card2x2 = pygame.draw.rect(screen,(124,252,0), (450, 210, 90, 150),1)

                    draw = shapes[6]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(495,280,30,30))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(495,280,30,30))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(495,280),15)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(495,280),15)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(495,280,30,30))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(495,280),15)
                    
                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(495,280),15)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(495,280,30,30))

                    elif draw==9:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,200,200),(495,280),15)

                    elif draw==10:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,200,200),(495,280,30,30))

                    pygame.display.flip()

                if card3x2.collidepoint(pos) and 8 not in turned_card and 8 not in removed_card:

                    turned_card.append(8)

                    screen.fill((0,0,20),card3x2)

                    card3x2 = pygame.draw.rect(screen,(124,252,0), (550, 210, 90, 150),1)

                    draw = shapes[7]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(595,280,30,30))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(595,280,30,30))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(595,280),15)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(595,280),15)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(595,280,30,30))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(595,280),15)
                    
                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(595,280),15)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(595,280,30,30))

                    elif draw==9:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,200,200),(595,280),15)

                    elif draw==10:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,200,200),(595,280,30,30))

                    pygame.display.flip()

                if card4x2.collidepoint(pos) and 9 not in turned_card and 9 not in removed_card:

                    turned_card.append(9)

                    screen.fill((0,0,20),card4x2)

                    card4x2 = pygame.draw.rect(screen,(124,252,0), (650, 210, 90, 150),1)

                    draw = shapes[8]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(695,280,30,30))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(695,280,30,30))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(695,280),15)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(695,280),15)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(695,280,30,30))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(695,280),15)

                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(695,280),15)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(695,280,30,30))

                    elif draw==9:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,200,200),(695,280),15)

                    elif draw==10:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,200,200),(695,280,30,30))

                    pygame.display.flip()

                if card5x2.collidepoint(pos) and 10 not in turned_card and 10 not in removed_card:

                    turned_card.append(10)

                    screen.fill((0,0,20),card5x2)

                    card5x2 = pygame.draw.rect(screen,(124,252,0), (750, 210, 90, 150),1)

                    draw = shapes[9]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(795,280,30,30))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(795,280,30,30))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(795,280),15)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(795,280),15)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(795,280,30,30))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(795,280),15)

                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(795,280),15)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(795,280,30,30))

                    elif draw==9:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,200,200),(795,280),15)

                    elif draw==10:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,200,200),(795,280,30,30))

                    pygame.display.flip()

                if card1x3.collidepoint(pos) and 11 not in turned_card and 11 not in removed_card:

                    turned_card.append(11)

                    screen.fill((0,0,20),card1x3)

                    card1x3 = pygame.draw.rect(screen,(124,252,0), (350, 370, 90, 150),1)

                    draw = shapes[10]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(395,440,30,30))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(395,440,30,30))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(395,440),15)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(395,440),15)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(395,440,30,30))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(395,440),15)

                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(395,440),15)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(395,440,30,30))

                    elif draw==9:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,200,200),(395,440),15)

                    elif draw==10:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,200,200),(395,440,30,30))

                    pygame.display.flip()

                if card2x3.collidepoint(pos) and 12 not in turned_card and 12 not in removed_card:

                    turned_card.append(12)

                    screen.fill((0,0,20),card2x3)

                    card2x3 = pygame.draw.rect(screen,(124,252,0), (450, 370, 90, 150),1)

                    draw = shapes[11]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(495,440,30,30))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(495,440,30,30))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(495,440),15)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(495,440),15)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(495,440,30,30))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(495,440),15)

                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(495,440),15)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(495,440,30,30))

                    elif draw==9:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,200,200),(495,440),15)

                    elif draw==10:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,200,200),(495,440,30,30))

                    pygame.display.flip()

                if card3x3.collidepoint(pos) and 13 not in turned_card and 13 not in removed_card:

                    turned_card.append(13)

                    screen.fill((0,0,20),card3x3)

                    card3x3 = pygame.draw.rect(screen,(124,252,0), (550, 370, 90, 150),1)

                    draw = shapes[12]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(595,440,30,30))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(595,440,30,30))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(595,440),15)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(595,440),15)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(595,440,30,30))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(595,440),15)

                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(595,440),15)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(595,440,30,30))

                    elif draw==9:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,200,200),(595,440),15)

                    elif draw==10:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,200,200),(595,440,30,30))

                    pygame.display.flip()

                if card4x3.collidepoint(pos) and 14 not in turned_card and 14 not in removed_card:

                    turned_card.append(14)

                    screen.fill((0,0,20),card4x3)

                    card4x3 = pygame.draw.rect(screen,(124,252,0), (650, 370, 90, 150),1)

                    draw = shapes[13]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(695,440,30,30))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(695,440,30,30))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(695,440),15)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(695,440),15)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(695,440,30,30))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(695,440),15)
                    
                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(695,440),15)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(695,440,30,30))

                    elif draw==9:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,200,200),(695,440),15)

                    elif draw==10:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,200,200),(695,440,30,30))

                    pygame.display.flip()
                
                if card5x3.collidepoint(pos) and 15 not in turned_card and 15 not in removed_card:

                    turned_card.append(15)

                    screen.fill((0,0,20),card5x3)

                    card5x3 = pygame.draw.rect(screen,(124,252,0), (750, 370, 90, 150),1)

                    draw = shapes[14]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(795,440,30,30))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(795,440,30,30))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(795,440),15)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(795,440),15)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(795,440,30,30))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(795,440),15)
                    
                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(795,440),15)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(795,440,30,30))

                    elif draw==9:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,200,200),(795,440),15)

                    elif draw==10:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,200,200),(795,440,30,30))

                    pygame.display.flip()

                if card1x4.collidepoint(pos) and 16 not in turned_card and 16 not in removed_card:

                    turned_card.append(16)

                    screen.fill((0,0,20),card1x4)

                    card1x4 = pygame.draw.rect(screen,(124,252,0), (350, 530, 90, 150),1)

                    draw = shapes[15]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(395,600,30,30))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(395,600,30,30))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(395,600),15)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(395,600),15)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(395,600,30,30))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(395,600),15)
                    
                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(395,600),15)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(395,600,30,30))

                    elif draw==9:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,200,200),(395,600),15)

                    elif draw==10:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,200,200),(395,600,30,30))

                    pygame.display.flip()

                if card2x4.collidepoint(pos) and 17 not in turned_card and 17 not in removed_card:

                    turned_card.append(17)

                    screen.fill((0,0,20),card2x4)

                    card2x4 = pygame.draw.rect(screen,(124,252,0), (450, 530, 90, 150),1)

                    draw = shapes[16]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(495,600,30,30))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(495,600,30,30))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(495,600),15)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(495,600),15)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(495,600,30,30))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(495,600),15)
                    
                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(495,600),15)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(495,600,30,30))
                    
                    elif draw==9:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,200,200),(495,600),15)

                    elif draw==10:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,200,200),(495,600,30,30))

                    pygame.display.flip()

                if card3x4.collidepoint(pos) and 18 not in turned_card and 18 not in removed_card:

                    turned_card.append(18)

                    screen.fill((0,0,20),card3x4)

                    card3x4 = pygame.draw.rect(screen,(124,252,0), (550, 530, 90, 150),1)

                    draw = shapes[17]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(595,600,30,30))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(595,600,30,30))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(595,600),15)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(595,600),15)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(595,600,30,30))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(595,600),15)
                    
                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(595,600),15)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(595,600,30,30))

                    elif draw==9:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,200,200),(595,600),15)

                    elif draw==10:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,200,200),(595,600,30,30))

                    pygame.display.flip()

                if card4x4.collidepoint(pos) and 19 not in turned_card and 19 not in removed_card:

                    turned_card.append(19)

                    screen.fill((0,0,20),card4x4)

                    card4x4 = pygame.draw.rect(screen,(124,252,0), (650, 530, 90, 150),1)

                    draw = shapes[18]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(695,600,30,30))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(695,600,30,30))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(695,600),15)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(695,600),15)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(695,600,30,30))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(695,600),15)
                    
                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(695,600),15)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(695,600,30,30))

                    elif draw==9:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,200,200),(695,600),15)

                    elif draw==10:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,200,200),(695,600,30,30))

                    pygame.display.flip()
                
                if card5x4.collidepoint(pos) and 20 not in turned_card and 20 not in removed_card:

                    turned_card.append(20)

                    screen.fill((0,0,20),card5x4)

                    card5x4 = pygame.draw.rect(screen,(124,252,0), (750, 530, 90, 150),1)

                    draw = shapes[19]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(795,600,30,30))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(795,600,30,30))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(795,600),15)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(795,600),15)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(795,600,30,30))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(795,600),15)
                    
                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(795,600),15)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(795,600,30,30))

                    elif draw==9:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,200,200),(795,600),15)

                    elif draw==10:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,200,200),(795,600,30,30))

                    pygame.display.flip()

                if len(turned_card)==2:

                    pygame.time.wait(1000)

                    if card_ver[0]==card_ver[1]:

                        score+=100

                        pygame.draw.rect(screen,(0,0,20),(0,0,100,100))
                        
                        score_display = my_font.render_to(screen, (10, 10), "Score: " + str(score), (255, 255, 0))

                        pygame.display.flip()

                        removed_card.append(turned_card[0])
                        removed_card.append(turned_card[1])

                        win+=2 
                    
                        for i in turned_card:

                            if i==1:
                                
                                screen.fill((0,0,20),card1x1)

                            if i==2:

                                screen.fill((0,0,20),card2x1)


                            if i==3:
                                
                                screen.fill((0,0,20),card3x1)

                            if i==4:

                                screen.fill((0,0,20),card4x1)

                            if i==5:
                                
                                screen.fill((0,0,20),card5x1)
                                
                            if i==6:

                                screen.fill((0,0,20),card1x2)
                                
                            if i==7:

                                screen.fill((0,0,20),card2x2)

                            if i==8:

                                screen.fill((0,0,20),card3x2)

                            if i==9:

                                screen.fill((0,0,20),card4x2)
                            
                            if i==10:
                                
                                screen.fill((0,0,20),card5x2)
                                
                            if i==11:

                                screen.fill((0,0,20),card1x3)
                                
                            if i==12:

                                screen.fill((0,0,20),card2x3)
                                
                            if i==13:

                                screen.fill((0,0,20),card3x3)
                                
                            if i==14:

                                screen.fill((0,0,20),card4x3)
                            
                            if i==15:
                                
                                screen.fill((0,0,20),card5x3)
                            
                            if i==16:

                                screen.fill((0,0,20),card1x4)
                                
                            if i==17:

                                screen.fill((0,0,20),card2x4)
                                
                            if i==18:

                                screen.fill((0,0,20),card3x4)
                                
                            if i==19:

                                screen.fill((0,0,20),card4x4)
                            
                            if i==20:
                                
                                screen.fill((0,0,20),card5x4)

                    else:

                        for i in turned_card:

                            if i==1:

                                penalty1x1+=20

                                score=score-penalty1x1
                                
                                card1x1 = pygame.draw.rect(screen,(124,252,0), (350, 50, 90, 150),0)

                            if i==2:

                                penalty2x1+=20

                                score=score-penalty2x1
                                
                                card2x1 = pygame.draw.rect(screen,(124,252,0), (450, 50, 90, 150),0)

                            if i==3:

                                penalty3x1+=20

                                score=score-penalty3x1
                                
                                card3x1 = pygame.draw.rect(screen,(124,252,0), (550, 50, 90, 150),0)

                            if i==4:

                                penalty4x1+=20

                                score=score-penalty4x1

                                card4x1 = pygame.draw.rect(screen,(124,252,0), (650, 50, 90, 150),0)
                            
                            if i==5:

                                penalty5x1+=20

                                score=score-penalty5x1

                                card5x1 = pygame.draw.rect(screen,(124,252,0), (750, 50, 90, 150),0)
                                
                            if i==6:

                                penalty1x2+=20

                                score=score-penalty1x2

                                card1x2 = pygame.draw.rect(screen,(124,252,0), (350, 210, 90, 150),0)
                                
                            if i==7:

                                penalty2x2+=20

                                score=score-penalty2x2

                                card2x2 = pygame.draw.rect(screen,(124,252,0), (450, 210, 90, 150),0)

                            if i==8:

                                penalty3x2+=20

                                score=score-penalty3x2

                                card3x2 = pygame.draw.rect(screen,(124,252,0), (550, 210, 90, 150),0)

                            if i==9:

                                penalty4x2+=20

                                score=score-penalty4x2

                                card4x2 = pygame.draw.rect(screen,(124,252,0), (650, 210, 90, 150),0)
                                
                            if i==10:

                                penalty5x2+=20

                                score=score-penalty5x2

                                card5x2 = pygame.draw.rect(screen,(124,252,0), (750, 210, 90, 150),0)

                            if i==11:

                                penalty1x3+=20

                                score=score-penalty1x3

                                card1x3 = pygame.draw.rect(screen,(124,252,0), (350, 370, 90, 150),0)
                                
                            if i==12:

                                penalty2x3+=20

                                score=score-penalty2x3

                                card2x3 = pygame.draw.rect(screen,(124,252,0), (450, 370, 90, 150),0)
                                
                            if i==13:

                                penalty3x3+=20

                                score=score-penalty3x3

                                card3x3 = pygame.draw.rect(screen,(124,252,0), (550, 370, 90, 150),0)
                                
                            if i==14:

                                penalty4x3+=20

                                score=score-penalty4x3

                                card4x3 = pygame.draw.rect(screen,(124,252,0), (650, 370, 90, 150),0)
                            
                            if i==15:

                                penalty5x3+=20

                                score=score-penalty5x3

                                card5x3 = pygame.draw.rect(screen,(124,252,0), (750, 370, 90, 150),0)

                            if i==16:

                                penalty1x4+=20

                                score=score-penalty1x4

                                card1x4 = pygame.draw.rect(screen,(124,252,0), (350, 530, 90, 150),0)
                                     
                            if i==17:

                                penalty2x4+=20

                                score=score-penalty2x4

                                card2x4 = pygame.draw.rect(screen,(124,252,0), (450, 530, 90, 150),0)
                                
                            if i==18:

                                penalty3x4+=20

                                score=score-penalty3x4

                                card3x4 = pygame.draw.rect(screen,(124,252,0), (550, 530, 90, 150),0)
                                
                            if i==19:

                                penalty4x4+=20

                                score=score-penalty4x4

                                card4x4 = pygame.draw.rect(screen,(124,252,0), (650, 530, 90, 150),0)

                            if i==20:

                                penalty5x4+=20

                                score=score-penalty5x4

                                card5x4 = pygame.draw.rect(screen,(124,252,0), (750, 530, 90, 150),0)

                                

                    turned_card=[]

                    card_ver=[]

                    pygame.draw.rect(screen,(0,0,20),(0,0,200,200))

                    if score<0:

                        score = 0
                        
                    score_display = my_font.render_to(screen, (10, 10), "Score: " + str(score), (255, 255, 0))

                
                    pygame.display.flip()

                    if win==20:
                        
                        my_font.render_to(screen, (540, 360), "CONGRATULATIONS, YOU WON!", (255, 255, 0))

                        pygame.display.flip()

def game6x4():

    my_font = pygame.freetype.Font("NotoSans-Regular.ttf", 24)

    res = (1280,720)

    screen = pygame.display.set_mode(res)

    screen.fill((0,0,20))

    card1x1 = pygame.draw.rect(screen,(124,252,0), (350, 50, 90, 150),0)

    card2x1 = pygame.draw.rect(screen,(124,252,0), (450, 50, 90, 150),0)

    card3x1 = pygame.draw.rect(screen,(124,252,0), (550, 50, 90, 150),0)

    card4x1 = pygame.draw.rect(screen,(124,252,0), (650, 50, 90, 150),0)

    card5x1 = pygame.draw.rect(screen,(124,252,0), (750, 50, 90, 150),0)

    card6x1 = pygame.draw.rect(screen,(124,252,0), (850, 50, 90, 150),0)

    card1x2 = pygame.draw.rect(screen,(124,252,0), (350, 210, 90, 150),0)

    card2x2 = pygame.draw.rect(screen,(124,252,0), (450, 210, 90, 150),0)

    card3x2 = pygame.draw.rect(screen,(124,252,0), (550, 210, 90, 150),0)

    card4x2 = pygame.draw.rect(screen,(124,252,0), (650, 210, 90, 150),0)

    card5x2 = pygame.draw.rect(screen,(124,252,0), (750, 210, 90, 150),0)

    card6x2 = pygame.draw.rect(screen,(124,252,0), (850, 210, 90, 150),0)

    card1x3 = pygame.draw.rect(screen,(124,252,0), (350, 370, 90, 150),0)

    card2x3 = pygame.draw.rect(screen,(124,252,0), (450, 370, 90, 150),0)

    card3x3 = pygame.draw.rect(screen,(124,252,0), (550, 370, 90, 150),0)

    card4x3 = pygame.draw.rect(screen,(124,252,0), (650, 370, 90, 150),0)

    card5x3 = pygame.draw.rect(screen,(124,252,0), (750, 370, 90, 150),0)

    card6x3 = pygame.draw.rect(screen,(124,252,0), (850, 370, 90, 150),0)

    card1x4 = pygame.draw.rect(screen,(124,252,0), (350, 530, 90, 150),0)

    card2x4 = pygame.draw.rect(screen,(124,252,0), (450, 530, 90, 150),0)

    card3x4 = pygame.draw.rect(screen,(124,252,0), (550, 530, 90, 150),0)

    card4x4 = pygame.draw.rect(screen,(124,252,0), (650, 530, 90, 150),0)

    card5x4 = pygame.draw.rect(screen,(124,252,0), (750, 530, 90, 150),0)

    card6x4 = pygame.draw.rect(screen,(124,252,0), (850, 530, 90, 150),0)

    sair = pygame.draw.rect(screen, (255, 255, 0), (30,600,120,30),3)

    my_font.render_to(screen, (65, 607), "Exit", (255, 255, 0))

    shapes = shapes_pos(12)

    turned_card=[]
    card_ver=[]
    removed_card=[]
    win=0
    score=0
    penalty1x1=-20
    penalty2x1=-20
    penalty3x1=-20
    penalty4x1=-20
    penalty5x1=-20
    penalty6x1=-20
    penalty1x2=-20
    penalty2x2=-20
    penalty3x2=-20
    penalty4x2=-20
    penalty5x2=-20
    penalty6x2=-20
    penalty1x3=-20
    penalty2x3=-20
    penalty3x3=-20
    penalty4x3=-20
    penalty5x3=-20
    penalty6x3=-20
    penalty1x4=-20
    penalty2x4=-20
    penalty3x4=-20
    penalty4x4=-20
    penalty5x4=-20
    penalty6x4=-20

    pygame.display.flip()

    score_display = my_font.render_to(screen, (10, 10), "Score: " + str(score), (255, 255, 0))


    while(True):

        pygame.display.flip()

        for event in pygame.event.get():

            if (event.type == pygame.QUIT):

                exit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button== 1:

                pos = pygame.mouse.get_pos()

                if sair.collidepoint(pos):

                    menu()
                
                if card1x1.collidepoint(pos) and 1 not in turned_card and 1 not in removed_card:

                    turned_card.append(1)

                    screen.fill((0,0,20),card1x1)

                    card1x1 = pygame.draw.rect(screen,(0,200,0), (350, 50, 90, 150),1)

                    draw = shapes[0]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(395,120,30,30))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(395,120,30,30))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(395,120),15)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(395,120),15)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(395,120,30,30))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(395,120),15)

                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(395,120),15)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(395,120,30,30))

                    elif draw==9:

                        card_ver.append(9)

                        pygame.draw.circle(screen,(200,200,200),(395,120),15)

                    elif draw==10:

                        card_ver.append(10)

                        pygame.draw.rect(screen,(200,200,200),(395,120,30,30))

                    elif draw==11:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(0,50,10),(395,120),15)

                    elif draw==12:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(0,50,10),(395,120,30,30))
                        

                    pygame.display.flip()

                if card2x1.collidepoint(pos) and 2 not in turned_card and 2 not in removed_card:

                    turned_card.append(2)

                    screen.fill((0,0,20),card2x1)

                    card2x1 = pygame.draw.rect(screen,(124,252,0), (450, 50, 90, 150),1)

                    draw = shapes[1]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(495,120,30,30))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(495,120,30,30))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(495,120),15)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(495,120),15)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(495,120,30,30))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(495,120),15)

                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(495,120),15)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(495,120,30,30))

                    elif draw==9:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(200,200,200),(495,120),15)

                    elif draw==10:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(200,200,200),(495,120,30,30))

                    elif draw==11:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(0,50,10),(495,120),15)

                    elif draw==12:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(0,50,10),(495,120,30,30))

                    

                    pygame.display.flip()

                if card3x1.collidepoint(pos) and 3 not in turned_card and 3 not in removed_card:

                    turned_card.append(3)

                    screen.fill((0,0,20),card3x1)

                    card3x1 = pygame.draw.rect(screen,(124,252,0), (550, 50, 90, 150),1)

                    draw = shapes[2]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(595,120,30,30))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(595,120,30,30))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(595,120),15)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(595,120),15)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(595,120,30,30))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(595,120),15)

                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(595,120),15)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(595,120,30,30))

                    elif draw==9:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,200,200),(595,120),15)

                    elif draw==10:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,200,200),(595,120,30,30))

                    elif draw==11:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(0,50,10),(595,120),15)

                    elif draw==12:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(0,50,10),(595,120,30,30))

                    pygame.display.flip()

                if card4x1.collidepoint(pos) and 4 not in turned_card and 4 not in removed_card:

                    turned_card.append(4)

                    screen.fill((0,0,20),card4x1)
                    
                    card4x1 = pygame.draw.rect(screen,(124,252,0), (650, 50, 90, 150),1)

                    draw = shapes[3]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(695,120,30,30))
         
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(695,120,30,30))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(695,120),15)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(695,120),15)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(695,120,30,30))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(695,120),15)
                    
                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(695,120),15)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(695,120,30,30))

                    elif draw==9:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,200,200),(695,120),15)

                    elif draw==10:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,200,200),(695,120,30,30))

                    elif draw==11:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(0,50,10),(695,120),15)

                    elif draw==12:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(0,50,10),(695,120,30,30))

                    pygame.display.flip()
                
                if card5x1.collidepoint(pos) and 5 not in turned_card and 5 not in removed_card:

                    turned_card.append(5)

                    screen.fill((0,0,20),card5x1)
                    
                    card5x1 = pygame.draw.rect(screen,(124,252,0), (750, 50, 90, 150),1)

                    draw = shapes[4]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(795,120,30,30))
         
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(795,120,30,30))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(795,120),15)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(795,120),15)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(795,120,30,30))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(795,120),15)
                    
                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(795,120),15)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(795,120,30,30))

                    elif draw==9:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,200,200),(795,120),15)

                    elif draw==10:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,200,200),(795,120,30,30))

                    elif draw==11:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(0,50,10),(795,120),15)

                    elif draw==12:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(0,50,10),(795,120,30,30))

                    pygame.display.flip()

                if card6x1.collidepoint(pos) and 6 not in turned_card and 6 not in removed_card:

                    turned_card.append(6)

                    screen.fill((0,0,20),card6x1)
                    
                    card6x1 = pygame.draw.rect(screen,(124,252,0), (850, 50, 90, 150),1)

                    draw = shapes[5]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(895,120,30,30))
         
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(895,120,30,30))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(895,120),15)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(895,120),15)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(895,120,30,30))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(895,120),15)
                    
                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(895,120),15)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(895,120,30,30))

                    elif draw==9:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,200,200),(895,120),15)

                    elif draw==10:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,200,200),(895,120,30,30))

                    elif draw==11:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(0,50,10),(895,120),15)

                    elif draw==12:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(0,50,10),(895,120,30,30))

                    pygame.display.flip()

                if card1x2.collidepoint(pos) and 7 not in turned_card and 7 not in removed_card:

                    turned_card.append(7)

                    screen.fill((0,0,20),card1x2)

                    card1x2 = pygame.draw.rect(screen,(124,252,0), (350, 210, 90, 150),1)

                    draw = shapes[6]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(395,280,30,30))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(395,280,30,30))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(395,280),15)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(395,280),15)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(395,280,30,30))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(395,280),15)

                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(395,280),15)

                    elif draw==8:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(0,200,200),(395,280,30,30))

                    elif draw==9:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,200,200),(395,280),15)

                    elif draw==10:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,200,200),(395,280,30,30))

                    elif draw==11:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(0,50,10),(395,280),15)

                    elif draw==12:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(0,50,10),(395,280,30,30))

                    pygame.display.flip()

                if card2x2.collidepoint(pos) and 8 not in turned_card and 8 not in removed_card:

                    turned_card.append(8)

                    screen.fill((0,0,20),card2x2)

                    card2x2 = pygame.draw.rect(screen,(124,252,0), (450, 210, 90, 150),1)

                    draw = shapes[7]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(495,280,30,30))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(495,280,30,30))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(495,280),15)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(495,280),15)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(495,280,30,30))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(495,280),15)
                    
                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(495,280),15)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(495,280,30,30))

                    elif draw==9:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,200,200),(495,280),15)

                    elif draw==10:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,200,200),(495,280,30,30))
                    
                    elif draw==11:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(0,50,10),(495,280),15)

                    elif draw==12:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(0,50,10),(495,280,30,30))

                    pygame.display.flip()

                if card3x2.collidepoint(pos) and 9 not in turned_card and 9 not in removed_card:

                    turned_card.append(9)

                    screen.fill((0,0,20),card3x2)

                    card3x2 = pygame.draw.rect(screen,(124,252,0), (550, 210, 90, 150),1)

                    draw = shapes[8]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(595,280,30,30))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(595,280,30,30))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(595,280),15)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(595,280),15)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(595,280,30,30))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(595,280),15)
                    
                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(595,280),15)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(595,280,30,30))

                    elif draw==9:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,200,200),(595,280),15)

                    elif draw==10:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,200,200),(595,280,30,30))
                    
                    elif draw==11:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,200,200),(595,280),15)

                    elif draw==12:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(0,50,10),(595,280,30,30))

                    pygame.display.flip()

                if card4x2.collidepoint(pos) and 10 not in turned_card and 10 not in removed_card:

                    turned_card.append(10)

                    screen.fill((0,0,20),card4x2)

                    card4x2 = pygame.draw.rect(screen,(124,252,0), (650, 210, 90, 150),1)

                    draw = shapes[9]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(695,280,30,30))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(695,280,30,30))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(695,280),15)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(695,280),15)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(695,280,30,30))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(695,280),15)

                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(695,280),15)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(695,280,30,30))

                    elif draw==9:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,200,200),(695,280),15)

                    elif draw==10:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,200,200),(695,280,30,30))

                    elif draw==11:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(0,50,10),(695,280),15)

                    elif draw==12:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(0,50,10),(695,280,30,30))

                    pygame.display.flip()

                if card5x2.collidepoint(pos) and 11 not in turned_card and 11 not in removed_card:

                    turned_card.append(11)

                    screen.fill((0,0,20),card5x2)

                    card5x2 = pygame.draw.rect(screen,(124,252,0), (750, 210, 90, 150),1)

                    draw = shapes[10]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(795,280,30,30))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(795,280,30,30))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(795,280),15)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(795,280),15)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(795,280,30,30))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(795,280),15)

                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(795,280),15)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(795,280,30,30))

                    elif draw==9:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,200,200),(795,280),15)

                    elif draw==10:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,200,200),(795,280,30,30))

                    elif draw==11:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(0,50,10),(795,280),15)

                    elif draw==12:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(0,50,10),(795,280,30,30))

                    pygame.display.flip()

                if card6x2.collidepoint(pos) and 12 not in turned_card and 12 not in removed_card:

                    turned_card.append(12)

                    screen.fill((0,0,20),card6x2)

                    card6x2 = pygame.draw.rect(screen,(124,252,0), (850, 210, 90, 150),1)

                    draw = shapes[11]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(895,280,30,30))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(895,280,30,30))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(895,280),15)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(895,280),15)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(895,280,30,30))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(895,280),15)

                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(895,280),15)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(895,280,30,30))

                    elif draw==9:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,200,200),(895,280),15)

                    elif draw==10:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,200,200),(895,280,30,30))

                    elif draw==11:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(0,50,10),(895,280),15)

                    elif draw==12:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(0,50,10),(895,280,30,30))

                    pygame.display.flip()

                if card1x3.collidepoint(pos) and 13 not in turned_card and 13 not in removed_card:

                    turned_card.append(13)

                    screen.fill((0,0,20),card1x3)

                    card1x3 = pygame.draw.rect(screen,(124,252,0), (350, 370, 90, 150),1)

                    draw = shapes[12]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(395,440,30,30))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(395,440,30,30))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(395,440),15)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(395,440),15)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(395,440,30,30))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(395,440),15)

                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(395,440),15)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(395,440,30,30))

                    elif draw==9:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,200,200),(395,440),15)

                    elif draw==10:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,200,200),(395,440,30,30))

                    elif draw==11:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(0,50,10),(395,440),15)

                    elif draw==12:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(0,50,10),(395,440,30,30))

                    pygame.display.flip()

                if card2x3.collidepoint(pos) and 14 not in turned_card and 14 not in removed_card:

                    turned_card.append(14)

                    screen.fill((0,0,20),card2x3)

                    card2x3 = pygame.draw.rect(screen,(124,252,0), (450, 370, 90, 150),1)

                    draw = shapes[13]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(495,440,30,30))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(495,440,30,30))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(495,440),15)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(495,440),15)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(495,440,30,30))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(495,440),15)

                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(495,440),15)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(495,440,30,30))

                    elif draw==9:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,200,200),(495,440),15)

                    elif draw==10:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,200,200),(495,440,30,30))

                    elif draw==11:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(0,50,10),(495,440),15)

                    elif draw==12:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(0,50,10),(495,440,30,30))

                    pygame.display.flip()

                if card3x3.collidepoint(pos) and 15 not in turned_card and 15 not in removed_card:

                    turned_card.append(15)

                    screen.fill((0,0,20),card3x3)

                    card3x3 = pygame.draw.rect(screen,(124,252,0), (550, 370, 90, 150),1)

                    draw = shapes[14]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(595,440,30,30))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(595,440,30,30))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(595,440),15)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(595,440),15)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(595,440,30,30))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(595,440),15)

                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(595,440),15)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(595,440,30,30))

                    elif draw==9:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,200,200),(595,440),15)

                    elif draw==10:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,200,200),(595,440,30,30))

                    elif draw==11:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(0,50,10),(595,440),15)

                    elif draw==12:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(0,50,10),(595,440,30,30))

                    pygame.display.flip()

                if card4x3.collidepoint(pos) and 16 not in turned_card and 16 not in removed_card:

                    turned_card.append(16)

                    screen.fill((0,0,20),card4x3)

                    card4x3 = pygame.draw.rect(screen,(124,252,0), (650, 370, 90, 150),1)

                    draw = shapes[15]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(695,440,30,30))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(695,440,30,30))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(695,440),15)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(695,440),15)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(695,440,30,30))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(695,440),15)
                    
                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(695,440),15)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(695,440,30,30))

                    elif draw==9:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,200,200),(695,440),15)

                    elif draw==10:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,200,200),(695,440,30,30))

                    elif draw==11:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(0,50,10),(695,440),15)

                    elif draw==12:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(0,50,10),(695,440,30,30))


                    pygame.display.flip()
                
                if card5x3.collidepoint(pos) and 17 not in turned_card and 17 not in removed_card:

                    turned_card.append(17)

                    screen.fill((0,0,20),card5x3)

                    card5x3 = pygame.draw.rect(screen,(124,252,0), (750, 370, 90, 150),1)

                    draw = shapes[16]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(795,440,30,30))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(795,440,30,30))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(795,440),15)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(795,440),15)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(795,440,30,30))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(795,440),15)
                    
                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(795,440),15)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(795,440,30,30))

                    elif draw==9:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,200,200),(795,440),15)

                    elif draw==10:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,200,200),(795,440,30,30))

                    elif draw==11:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(0,50,10),(795,440),15)

                    elif draw==12:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(0,50,10),(795,440,30,30))

                    pygame.display.flip()

                if card6x3.collidepoint(pos) and 18 not in turned_card and 18 not in removed_card:

                    turned_card.append(18)

                    screen.fill((0,0,20),card6x3)

                    card6x3 = pygame.draw.rect(screen,(124,252,0), (850, 370, 90, 150),1)

                    draw = shapes[17]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(895,440,30,30))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(895,440,30,30))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(895,440),15)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(895,440),15)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(895,440,30,30))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(895,440),15)
                    
                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(895,440),15)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(895,440,30,30))

                    elif draw==9:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,200,200),(895,440),15)

                    elif draw==10:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,200,200),(895,440,30,30))

                    elif draw==11:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(0,50,10),(895,440),15)

                    elif draw==12:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(0,50,10),(895,440,30,30))

                    pygame.display.flip()

                if card1x4.collidepoint(pos) and 19 not in turned_card and 19 not in removed_card:

                    turned_card.append(19)

                    screen.fill((0,0,20),card1x4)

                    card1x4 = pygame.draw.rect(screen,(124,252,0), (350, 530, 90, 150),1)

                    draw = shapes[18]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(395,600,30,30))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(395,600,30,30))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(395,600),15)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(395,600),15)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(395,600,30,30))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(395,600),15)
                    
                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(395,600),15)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(395,600,30,30))

                    elif draw==9:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,200,200),(395,600),15)

                    elif draw==10:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,200,200),(395,600,30,30))

                    elif draw==11:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(0,50,10),(395,600),15)

                    elif draw==12:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(0,50,10),(395,600,30,30))

                    pygame.display.flip()

                if card2x4.collidepoint(pos) and 20 not in turned_card and 20 not in removed_card:

                    turned_card.append(20)

                    screen.fill((0,0,20),card2x4)

                    card2x4 = pygame.draw.rect(screen,(124,252,0), (450, 530, 90, 150),1)

                    draw = shapes[19]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(495,600,30,30))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(495,600,30,30))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(495,600),15)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(495,600),15)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(495,600,30,30))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(495,600),15)
                    
                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(495,600),15)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(495,600,30,30))
                    
                    elif draw==9:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,200,200),(495,600),15)

                    elif draw==10:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,200,200),(495,600,30,30))

                    elif draw==11:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(0,50,10),(495,600),15)

                    elif draw==12:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(0,50,10),(495,600,30,30))

                    pygame.display.flip()

                if card3x4.collidepoint(pos) and 21 not in turned_card and 21 not in removed_card:

                    turned_card.append(21)

                    screen.fill((0,0,20),card3x4)

                    card3x4 = pygame.draw.rect(screen,(124,252,0), (550, 530, 90, 150),1)

                    draw = shapes[20]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(595,600,30,30))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(595,600,30,30))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(595,600),15)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(595,600),15)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(595,600,30,30))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(595,600),15)
                    
                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(595,600),15)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(595,600,30,30))

                    elif draw==9:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,200,200),(595,600),15)

                    elif draw==10:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,200,200),(595,600,30,30))

                    elif draw==11:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(0,50,10),(595,600),15)

                    elif draw==12:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(0,50,10),(595,600,30,30))

                    pygame.display.flip()

                if card4x4.collidepoint(pos) and 22 not in turned_card and 22 not in removed_card:

                    turned_card.append(22)

                    screen.fill((0,0,20),card4x4)

                    card4x4 = pygame.draw.rect(screen,(124,252,0), (650, 530, 90, 150),1)

                    draw = shapes[21]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(695,600,30,30))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(695,600,30,30))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(695,600),15)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(695,600),15)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(695,600,30,30))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(695,600),15)
                    
                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(695,600),15)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(695,600,30,30))

                    elif draw==9:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,200,200),(695,600),15)

                    elif draw==10:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,200,200),(695,600,30,30))

                    elif draw==11:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(0,50,10),(695,600),15)

                    elif draw==12:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(0,50,10),(695,600,30,30))

                    pygame.display.flip()
                
                if card5x4.collidepoint(pos) and 23 not in turned_card and 23 not in removed_card:

                    turned_card.append(23)

                    screen.fill((0,0,20),card5x4)

                    card5x4 = pygame.draw.rect(screen,(124,252,0), (750, 530, 90, 150),1)

                    draw = shapes[22]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(795,600,30,30))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(795,600,30,30))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(795,600),15)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(795,600),15)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(795,600,30,30))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(795,600),15)
                    
                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(795,600),15)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(795,600,30,30))

                    elif draw==9:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,200,200),(795,600),15)

                    elif draw==10:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,200,200),(795,600,30,30))

                    elif draw==11:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(0,50,10),(795,600),15)

                    elif draw==12:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(0,50,10),(795,600,30,30))

                    pygame.display.flip()

                if card6x4.collidepoint(pos) and 24 not in turned_card and 24 not in removed_card:

                    turned_card.append(24)

                    screen.fill((0,0,20),card6x4)

                    card6x4 = pygame.draw.rect(screen,(124,252,0), (850, 530, 90, 150),1)

                    draw = shapes[23]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(895,600,30,30))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(895,600,30,30))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(895,600),15)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(895,600),15)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(895,600,30,30))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(895,600),15)
                    
                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(895,600),15)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(895,600,30,30))

                    elif draw==9:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,200,200),(895,600),15)

                    elif draw==10:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,200,200),(895,600,30,30))

                    elif draw==11:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(0,50,10),(895,600),15)

                    elif draw==12:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(0,50,10),(895,600,30,30))

                    pygame.display.flip()

                if len(turned_card)==2:

                    pygame.time.wait(1000)

                    if card_ver[0]==card_ver[1]:

                        score+=100

                        pygame.draw.rect(screen,(0,0,20),(0,0,100,100))
                        
                        score_display = my_font.render_to(screen, (10, 10), "Score: " + str(score), (255, 255, 0))

                        pygame.display.flip()

                        removed_card.append(turned_card[0])
                        removed_card.append(turned_card[1])

                        win+=2 
                    
                        for i in turned_card:

                            if i==1:
                                
                                screen.fill((0,0,20),card1x1)

                            if i==2:

                                screen.fill((0,0,20),card2x1)


                            if i==3:
                                
                                screen.fill((0,0,20),card3x1)

                            if i==4:

                                screen.fill((0,0,20),card4x1)

                            if i==5:
                                
                                screen.fill((0,0,20),card5x1)

                            if i==6:
                                
                                screen.fill((0,0,20),card6x1)
                                
                            if i==7:

                                screen.fill((0,0,20),card1x2)
                                
                            if i==8:

                                screen.fill((0,0,20),card2x2)

                            if i==9:

                                screen.fill((0,0,20),card3x2)

                            if i==10:

                                screen.fill((0,0,20),card4x2)
                            
                            if i==11:
                                
                                screen.fill((0,0,20),card5x2)

                            if i==12:
                                
                                screen.fill((0,0,20),card6x2)
                                
                            if i==13:

                                screen.fill((0,0,20),card1x3)
                                
                            if i==14:

                                screen.fill((0,0,20),card2x3)
                                
                            if i==15:

                                screen.fill((0,0,20),card3x3)
                                
                            if i==16:

                                screen.fill((0,0,20),card4x3)
                            
                            if i==17:
                                
                                screen.fill((0,0,20),card5x3)

                            if i==18:
                                
                                screen.fill((0,0,20),card6x3)
                            
                            if i==19:

                                screen.fill((0,0,20),card1x4)
                                
                            if i==20:

                                screen.fill((0,0,20),card2x4)
                                
                            if i==21:

                                screen.fill((0,0,20),card3x4)
                                
                            if i==22:

                                screen.fill((0,0,20),card4x4)
                            
                            if i==23:
                                
                                screen.fill((0,0,20),card5x4)

                            if i==24:
                                
                                screen.fill((0,0,20),card6x4)

                    else:

                        for i in turned_card:

                            if i==1:

                                penalty1x1+=20

                                score=score-penalty1x1
                                
                                card1x1 = pygame.draw.rect(screen,(124,252,0), (350, 50, 90, 150),0)

                            if i==2:

                                penalty2x1+=20

                                score=score-penalty2x1
                                
                                card2x1 = pygame.draw.rect(screen,(124,252,0), (450, 50, 90, 150),0)

                            if i==3:

                                penalty3x1+=20

                                score=score-penalty3x1
                                
                                card3x1 = pygame.draw.rect(screen,(124,252,0), (550, 50, 90, 150),0)

                            if i==4:

                                penalty4x1+=20

                                score=score-penalty4x1

                                card4x1 = pygame.draw.rect(screen,(124,252,0), (650, 50, 90, 150),0)
                            
                            if i==5:

                                penalty5x1+=20

                                score=score-penalty5x1

                                card5x1 = pygame.draw.rect(screen,(124,252,0), (750, 50, 90, 150),0)

                            if i==6:

                                penalty6x1+=20

                                score=score-penalty6x1

                                card6x1 = pygame.draw.rect(screen,(124,252,0), (850, 50, 90, 150),0)
                                
                            if i==7:

                                penalty1x2+=20

                                score=score-penalty1x2

                                card1x2 = pygame.draw.rect(screen,(124,252,0), (350, 210, 90, 150),0)
                                
                            if i==8:

                                penalty2x2+=20

                                score=score-penalty2x2

                                card2x2 = pygame.draw.rect(screen,(124,252,0), (450, 210, 90, 150),0)

                            if i==9:

                                penalty3x2+=20

                                score=score-penalty3x2

                                card3x2 = pygame.draw.rect(screen,(124,252,0), (550, 210, 90, 150),0)

                            if i==10:

                                penalty4x2+=20

                                score=score-penalty4x2

                                card4x2 = pygame.draw.rect(screen,(124,252,0), (650, 210, 90, 150),0)
                                
                            if i==11:

                                penalty5x2+=20

                                score=score-penalty5x2

                                card5x2 = pygame.draw.rect(screen,(124,252,0), (750, 210, 90, 150),0)

                            if i==12:

                                penalty6x2+=20

                                score=score-penalty6x2

                                card6x2 = pygame.draw.rect(screen,(124,252,0), (850, 210, 90, 150),0)

                            if i==13:

                                penalty1x3+=20

                                score=score-penalty1x3

                                card1x3 = pygame.draw.rect(screen,(124,252,0), (350, 370, 90, 150),0)
                                
                            if i==14:

                                penalty2x3+=20

                                score=score-penalty2x3

                                card2x3 = pygame.draw.rect(screen,(124,252,0), (450, 370, 90, 150),0)
                                
                            if i==15:

                                penalty3x3+=20

                                score=score-penalty3x3

                                card3x3 = pygame.draw.rect(screen,(124,252,0), (550, 370, 90, 150),0)
                                
                            if i==16:

                                penalty4x3+=20

                                score=score-penalty4x3

                                card4x3 = pygame.draw.rect(screen,(124,252,0), (650, 370, 90, 150),0)
                            
                            if i==17:

                                penalty5x3+=20

                                score=score-penalty5x3

                                card5x3 = pygame.draw.rect(screen,(124,252,0), (750, 370, 90, 150),0)

                            if i==18:

                                penalty6x3+=20

                                score=score-penalty6x3

                                card6x3 = pygame.draw.rect(screen,(124,252,0), (850, 370, 90, 150),0)

                            if i==19:

                                penalty1x4+=20

                                score=score-penalty1x4

                                card1x4 = pygame.draw.rect(screen,(124,252,0), (350, 530, 90, 150),0)
                                     
                            if i==20:

                                penalty2x4+=20

                                score=score-penalty2x4

                                card2x4 = pygame.draw.rect(screen,(124,252,0), (450, 530, 90, 150),0)
                                
                            if i==21:

                                penalty3x4+=20

                                score=score-penalty3x4

                                card3x4 = pygame.draw.rect(screen,(124,252,0), (550, 530, 90, 150),0)
                                
                            if i==22:

                                penalty4x4+=20

                                score=score-penalty4x4

                                card4x4 = pygame.draw.rect(screen,(124,252,0), (650, 530, 90, 150),0)

                            if i==23:

                                penalty5x4+=20

                                score=score-penalty5x4

                                card5x4 = pygame.draw.rect(screen,(124,252,0), (750, 530, 90, 150),0)

                            if i==24:

                                penalty6x4+=20

                                score=score-penalty6x4

                                card6x4 = pygame.draw.rect(screen,(124,252,0), (850, 530, 90, 150),0)
                                

                    turned_card=[]

                    card_ver=[]

                    pygame.draw.rect(screen,(0,0,20),(0,0,200,200))

                    if score<0:

                        score = 0
                        
                    score_display = my_font.render_to(screen, (10, 10), "Score: " + str(score), (255, 255, 0))

                
                    pygame.display.flip()

                    if win==24:
                        
                        my_font.render_to(screen, (540, 360), "CONGRATULATIONS, YOU WON!", (255, 255, 0))

                        pygame.display.flip()

def game6x5():

    my_font = pygame.freetype.Font("NotoSans-Regular.ttf", 24)

    res = (1280,720)

    screen = pygame.display.set_mode(res)

    screen.fill((0,0,20))

    card1x1 = pygame.draw.rect(screen,(124,252,0), (350, 50, 60, 90),0)

    card2x1 = pygame.draw.rect(screen,(124,252,0), (420, 50, 60, 90),0)

    card3x1 = pygame.draw.rect(screen,(124,252,0), (490, 50, 60, 90),0)

    card4x1 = pygame.draw.rect(screen,(124,252,0), (560, 50, 60, 90),0)

    card5x1 = pygame.draw.rect(screen,(124,252,0), (630, 50, 60, 90),0)

    card6x1 = pygame.draw.rect(screen,(124,252,0), (700, 50, 60, 90),0)

    card1x2 = pygame.draw.rect(screen,(124,252,0), (350, 150, 60, 90),0)

    card2x2 = pygame.draw.rect(screen,(124,252,0), (420, 150, 60, 90),0)

    card3x2 = pygame.draw.rect(screen,(124,252,0), (490, 150, 60, 90),0)

    card4x2 = pygame.draw.rect(screen,(124,252,0), (560, 150, 60, 90),0)

    card5x2 = pygame.draw.rect(screen,(124,252,0), (630, 150, 60, 90),0)

    card6x2 = pygame.draw.rect(screen,(124,252,0), (700, 150, 60, 90),0)

    card1x3 = pygame.draw.rect(screen,(124,252,0), (350, 250, 60, 90),0)

    card2x3 = pygame.draw.rect(screen,(124,252,0), (420, 250, 60, 90),0)

    card3x3 = pygame.draw.rect(screen,(124,252,0), (490, 250, 60, 90),0)

    card4x3 = pygame.draw.rect(screen,(124,252,0), (560, 250, 60, 90),0)

    card5x3 = pygame.draw.rect(screen,(124,252,0), (630, 250, 60, 90),0)

    card6x3 = pygame.draw.rect(screen,(124,252,0), (700, 250, 60, 90),0)

    card1x4 = pygame.draw.rect(screen,(124,252,0), (350, 350, 60, 90),0)

    card2x4 = pygame.draw.rect(screen,(124,252,0), (420, 350, 60, 90),0)

    card3x4 = pygame.draw.rect(screen,(124,252,0), (490, 350, 60, 90),0)

    card4x4 = pygame.draw.rect(screen,(124,252,0), (560, 350, 60, 90),0)

    card5x4 = pygame.draw.rect(screen,(124,252,0), (630, 350, 60, 90),0)

    card6x4 = pygame.draw.rect(screen,(124,252,0), (700, 350, 60, 90),0)

    card1x5 = pygame.draw.rect(screen,(124,252,0), (350, 450, 60, 90),0)

    card2x5 = pygame.draw.rect(screen,(124,252,0), (420, 450, 60, 90),0)

    card3x5 = pygame.draw.rect(screen,(124,252,0), (490, 450, 60, 90),0)

    card4x5 = pygame.draw.rect(screen,(124,252,0), (560, 450, 60, 90),0)

    card5x5 = pygame.draw.rect(screen,(124,252,0), (630, 450, 60, 90),0)

    card6x5 = pygame.draw.rect(screen,(124,252,0), (700, 450, 60, 90),0)

    sair = pygame.draw.rect(screen, (255, 255, 0), (30,600,120,30),3)

    pygame.display.flip()

    my_font.render_to(screen, (65, 607), "Exit", (255, 255, 0))

    shapes = shapes_pos(15)

    turned_card=[]
    card_ver=[]
    removed_card=[]
    win=0
    score=0
    penalty1x1=-20
    penalty2x1=-20
    penalty3x1=-20
    penalty4x1=-20
    penalty5x1=-20
    penalty6x1=-20
    penalty1x2=-20
    penalty2x2=-20
    penalty3x2=-20
    penalty4x2=-20
    penalty5x2=-20
    penalty6x2=-20
    penalty1x3=-20
    penalty2x3=-20
    penalty3x3=-20
    penalty4x3=-20
    penalty5x3=-20
    penalty6x3=-20
    penalty1x4=-20
    penalty2x4=-20
    penalty3x4=-20
    penalty4x4=-20
    penalty5x4=-20
    penalty6x4=-20
    penalty1x5=-20
    penalty2x5=-20
    penalty3x5=-20
    penalty4x5=-20
    penalty5x5=-20
    penalty6x5=-20

    pygame.display.flip()

    score_display = my_font.render_to(screen, (10, 10), "Score: " + str(score), (255, 255, 0))

    while(True):

        pygame.display.flip()

        for event in pygame.event.get():

            if (event.type == pygame.QUIT):

                exit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button== 1:

                pos = pygame.mouse.get_pos()

                if sair.collidepoint(pos):

                    menu()
                
                if card1x1.collidepoint(pos) and 1 not in turned_card and 1 not in removed_card:

                    turned_card.append(1)

                    screen.fill((0,0,20),card1x1)

                    card1x1 = pygame.draw.rect(screen,(124,252,0), (350, 50, 60, 90),1)

                    draw = shapes[0]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(380,90,15,15))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(380,90,15,15))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(380,90),7)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(380,90),7)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(380,90,15,15))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(380,90),7)

                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(380,90),7)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(380,90,15,15))

                    elif draw==9:

                        card_ver.append(9)

                        pygame.draw.circle(screen,(200,200,200),(380,90),7)

                    elif draw==10:

                        card_ver.append(10)

                        pygame.draw.rect(screen,(200,200,200),(380,90,15,15))

                    elif draw==11:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(0,50,10),(380,90),7)

                    elif draw==12:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(0,50,10),(380,90,15,15))

                    elif draw==13:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,100,0),(380,90),7)

                    elif draw==14:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,100,0),(380,90,15,15))

                    elif draw==15:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,100,100),(380,90,15,15))
                
                if card2x1.collidepoint(pos) and 2 not in turned_card and 2 not in removed_card:

                    turned_card.append(2)

                    screen.fill((0,0,20),card2x1)

                    card2x1 = pygame.draw.rect(screen,(124,252,0), (420, 50, 60, 90),1)

                    draw = shapes[1]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(450,90,15,15))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(450,90,15,15))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(450,90),7)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(450,90),7)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(450,90,15,15))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(450,90),7)

                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(450,90),7)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(450,90,15,15))

                    elif draw==9:

                        card_ver.append(9)

                        pygame.draw.circle(screen,(200,200,200),(450,90),7)

                    elif draw==10:

                        card_ver.append(10)

                        pygame.draw.rect(screen,(200,200,200),(450,90,15,15))

                    elif draw==11:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(0,50,10),(450,90),7)

                    elif draw==12:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(0,50,10),(450,90,15,15))

                    elif draw==13:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,100,0),(450,90),7)

                    elif draw==14:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,100,0),(450,90,15,15))

                    elif draw==15:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,100,100),(450,90,15,15))
                        

                    pygame.display.flip()

                if card3x1.collidepoint(pos) and 3 not in turned_card and 3 not in removed_card:

                    turned_card.append(3)

                    screen.fill((0,0,20),card3x1)

                    card3x1 = pygame.draw.rect(screen,(124,252,0), (490, 50, 60, 90),1)

                    draw = shapes[2]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(520,90,15,15))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(520,90,15,15))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(520,90),7)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(520,90),7)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(520,90,15,15))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(520,90),7)

                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(520,90),7)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(520,90,15,15))

                    elif draw==9:

                        card_ver.append(9)

                        pygame.draw.circle(screen,(200,200,200),(520,90),7)

                    elif draw==10:

                        card_ver.append(10)

                        pygame.draw.rect(screen,(200,200,200),(520,90,15,15))

                    elif draw==11:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(0,50,10),(520,90),7)

                    elif draw==12:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(0,50,10),(520,90,15,15))

                    elif draw==13:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,100,0),(520,90),7)

                    elif draw==14:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,100,0),(520,90,15,15))

                    elif draw==15:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,100,100),(520,90,15,15))
                        

                    pygame.display.flip()

                if card4x1.collidepoint(pos) and 4 not in turned_card and 4 not in removed_card:

                    turned_card.append(4)

                    screen.fill((0,0,20),card4x1)

                    card4x1 = pygame.draw.rect(screen,(124,252,0), (560, 50, 60, 90),1)

                    draw = shapes[3]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(590,90,15,15))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(590,90,15,15))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(590,90),7)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(590,90),7)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(590,90,15,15))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(590,90),7)

                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(590,90),7)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(590,90,15,15))

                    elif draw==9:

                        card_ver.append(9)

                        pygame.draw.circle(screen,(200,200,200),(590,90),7)

                    elif draw==10:

                        card_ver.append(10)

                        pygame.draw.rect(screen,(200,200,200),(590,90,15,15))

                    elif draw==11:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(0,50,10),(590,90),7)

                    elif draw==12:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(0,50,10),(590,90,15,15))

                    elif draw==13:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,100,0),(590,90),7)

                    elif draw==14:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,100,0),(590,90,15,15))

                    elif draw==15:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,100,100),(590,90,15,15))
                        

                    pygame.display.flip()

                if card5x1.collidepoint(pos) and 5 not in turned_card and 5 not in removed_card:

                    turned_card.append(5)

                    screen.fill((0,0,20),card5x1)

                    card5x1 = pygame.draw.rect(screen,(124,252,0), (630, 50, 60, 90),1)

                    draw = shapes[4]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(660,90,15,15))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(660,90,15,15))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(660,90),7)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(660,90),7)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(660,90,15,15))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(660,90),7)

                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(660,90),7)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(660,90,15,15))

                    elif draw==9:

                        card_ver.append(9)

                        pygame.draw.circle(screen,(200,200,200),(660,90),7)

                    elif draw==10:

                        card_ver.append(10)

                        pygame.draw.rect(screen,(200,200,200),(660,90,15,15))

                    elif draw==11:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(0,50,10),(660,90),7)

                    elif draw==12:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(0,50,10),(660,90,15,15))

                    elif draw==13:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,100,0),(660,90),7)

                    elif draw==14:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,100,0),(660,90,15,15))

                    elif draw==15:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,100,100),(660,90,15,15))
                        

                    pygame.display.flip()

                if card6x1.collidepoint(pos) and 6 not in turned_card and 6 not in removed_card:

                    turned_card.append(6)

                    screen.fill((0,0,20),card6x1)

                    card6x1 = pygame.draw.rect(screen,(124,252,0), (700, 50, 60, 90),1)

                    draw = shapes[5]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(730,90,15,15))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(730,90,15,15))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(730,90),7)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(730,90),7)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(730,90,15,15))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(730,90),7)

                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(730,90),7)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(730,90,15,15))

                    elif draw==9:

                        card_ver.append(9)

                        pygame.draw.circle(screen,(200,200,200),(730,90),7)

                    elif draw==10:

                        card_ver.append(10)

                        pygame.draw.rect(screen,(200,200,200),(730,90,15,15))

                    elif draw==11:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(0,50,10),(730,90),7)

                    elif draw==12:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(0,50,10),(730,90,15,15))

                    elif draw==13:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,100,0),(730,90),7)

                    elif draw==14:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,100,0),(730,90,15,15))

                    elif draw==15:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,100,100),(730,90,15,15))
                        

                    pygame.display.flip()

                if card1x2.collidepoint(pos) and 7 not in turned_card and 7 not in removed_card:

                    turned_card.append(7)

                    screen.fill((0,0,20),card1x2)

                    card1x2 = pygame.draw.rect(screen,(124,252,0), (350, 150, 60, 90),1)

                    draw = shapes[6]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(380,195,15,15))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(380,195,15,15))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(380,195),7)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(380,195),7)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(380,195,15,15))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(380,195),7)

                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(380,195),7)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(380,195,15,15))

                    elif draw==9:

                        card_ver.append(9)

                        pygame.draw.circle(screen,(200,200,200),(380,195),7)

                    elif draw==10:

                        card_ver.append(10)

                        pygame.draw.rect(screen,(200,200,200),(380,195,15,15))

                    elif draw==11:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(0,50,10),(380,195),7)

                    elif draw==12:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(0,50,10),(380,195,15,15))

                    elif draw==13:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,100,0),(380,195),7)

                    elif draw==14:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,100,0),(380,195,15,15))

                    elif draw==15:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,100,100),(380,195,15,15))
                        

                    pygame.display.flip()

                if card2x2.collidepoint(pos) and 8 not in turned_card and 8 not in removed_card:

                    turned_card.append(8)

                    screen.fill((0,0,20),card2x2)

                    card2x2 = pygame.draw.rect(screen,(124,252,0), (420, 150, 60, 90),1)

                    draw = shapes[7]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(450,195,15,15))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(450,195,15,15))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(450,195),7)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(450,195),7)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(450,195,15,15))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(450,195),7)

                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(450,195),7)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(450,195,15,15))

                    elif draw==9:

                        card_ver.append(9)

                        pygame.draw.circle(screen,(200,200,200),(450,195),7)

                    elif draw==10:

                        card_ver.append(10)

                        pygame.draw.rect(screen,(200,200,200),(450,195,15,15))

                    elif draw==11:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(0,50,10),(450,195),7)

                    elif draw==12:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(0,50,10),(450,195,15,15))

                    elif draw==13:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,100,0),(450,195),7)

                    elif draw==14:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,100,0),(450,195,15,15))

                    elif draw==15:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,100,100),(450,195,15,15))
                        

                    pygame.display.flip()

                if card3x2.collidepoint(pos) and 9 not in turned_card and 9 not in removed_card:

                    turned_card.append(9)

                    screen.fill((0,0,20),card3x2)

                    card3x2 = pygame.draw.rect(screen,(124,252,0), (490, 150, 60, 90),1)

                    draw = shapes[8]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(520,195,15,15))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(520,195,15,15))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(520,195),7)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(520,195),7)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(520,195,15,15))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(520,195),7)

                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(520,195),7)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(520,195,15,15))

                    elif draw==9:

                        card_ver.append(9)

                        pygame.draw.circle(screen,(200,200,200),(520,195),7)

                    elif draw==10:

                        card_ver.append(10)

                        pygame.draw.rect(screen,(200,200,200),(520,195,15,15))

                    elif draw==11:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(0,50,10),(520,195),7)

                    elif draw==12:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(0,50,10),(520,195,15,15))

                    elif draw==13:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,100,0),(520,195),7)

                    elif draw==14:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,100,0),(520,195,15,15))

                    elif draw==15:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,100,100),(520,195,15,15))
                        

                    pygame.display.flip()

                if card4x2.collidepoint(pos) and 10 not in turned_card and 10 not in removed_card:

                    turned_card.append(10)

                    screen.fill((0,0,20),card4x2)

                    card4x2 = pygame.draw.rect(screen,(124,252,0), (560, 150, 60, 90),1)

                    draw = shapes[9]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(590,195,15,15))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(590,195,15,15))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(590,195),7)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(590,195),7)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(590,195,15,15))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(590,195),7)

                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(590,195),7)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(590,195,15,15))

                    elif draw==9:

                        card_ver.append(9)

                        pygame.draw.circle(screen,(200,200,200),(590,195),7)

                    elif draw==10:

                        card_ver.append(10)

                        pygame.draw.rect(screen,(200,200,200),(590,195,15,15))

                    elif draw==11:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(0,50,10),(590,195),7)

                    elif draw==12:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(0,50,10),(590,195,15,15))

                    elif draw==13:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,100,0),(590,195),7)

                    elif draw==14:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,100,0),(590,195,15,15))

                    elif draw==15:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,100,100),(590,195,15,15))
                        

                    pygame.display.flip()

                if card5x2.collidepoint(pos) and 11 not in turned_card and 11 not in removed_card:

                    turned_card.append(11)

                    screen.fill((0,0,20),card5x2)

                    card5x2 = pygame.draw.rect(screen,(124,252,0), (630, 150, 60, 90),1)

                    draw = shapes[10]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(660,195,15,15))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(660,195,15,15))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(660,195),7)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(660,195),7)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(660,195,15,15))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(660,195),7)

                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(660,195),7)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(660,195,15,15))

                    elif draw==9:

                        card_ver.append(9)

                        pygame.draw.circle(screen,(200,200,200),(660,195),7)

                    elif draw==10:

                        card_ver.append(10)

                        pygame.draw.rect(screen,(200,200,200),(660,195,15,15))

                    elif draw==11:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(0,50,10),(660,195),7)

                    elif draw==12:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(0,50,10),(660,195,15,15))

                    elif draw==13:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,100,0),(660,195),7)

                    elif draw==14:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,100,0),(660,195,15,15))

                    elif draw==15:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,100,100),(660,195,15,15))
                        

                    pygame.display.flip()

                if card6x2.collidepoint(pos) and 12 not in turned_card and 12 not in removed_card:

                    turned_card.append(12)

                    screen.fill((0,0,20),card6x2)

                    card6x2 = pygame.draw.rect(screen,(124,252,0), (700, 150, 60, 90),1)

                    draw = shapes[11]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(730,195,15,15))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(730,195,15,15))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(730,195),7)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(730,195),7)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(730,195,15,15))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(730,195),7)

                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(730,195),7)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(730,195,15,15))

                    elif draw==9:

                        card_ver.append(9)

                        pygame.draw.circle(screen,(200,200,200),(730,195),7)

                    elif draw==10:

                        card_ver.append(10)

                        pygame.draw.rect(screen,(200,200,200),(730,195,15,15))

                    elif draw==11:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(0,50,10),(730,195),7)

                    elif draw==12:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(0,50,10),(730,195,15,15))

                    elif draw==13:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,100,0),(730,195),7)

                    elif draw==14:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,100,0),(730,195,15,15))

                    elif draw==15:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,100,100),(730,195,15,15))
                        

                    pygame.display.flip()

                if card1x3.collidepoint(pos) and 13 not in turned_card and 13 not in removed_card:

                    turned_card.append(13)

                    screen.fill((0,0,20),card1x3)

                    card1x3 = pygame.draw.rect(screen,(124,252,0), (350, 250, 60, 90),1)

                    draw = shapes[12]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(380,295,15,15))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(380,295,15,15))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(380,295),7)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(380,295),7)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(380,295,15,15))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(380,295),7)

                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(380,295),7)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(380,295,15,15))

                    elif draw==9:

                        card_ver.append(9)

                        pygame.draw.circle(screen,(200,200,200),(380,295),7)

                    elif draw==10:

                        card_ver.append(10)

                        pygame.draw.rect(screen,(200,200,200),(380,295,15,15))

                    elif draw==11:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(0,50,10),(380,295),7)

                    elif draw==12:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(0,50,10),(380,295,15,15))

                    elif draw==13:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,100,0),(380,295),7)

                    elif draw==14:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,100,0),(380,295,15,15))

                    elif draw==15:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,100,100),(380,295,15,15))
                        

                    pygame.display.flip()

                if card2x3.collidepoint(pos) and 14 not in turned_card and 14 not in removed_card:

                    turned_card.append(14)

                    screen.fill((0,0,20),card2x3)

                    card2x3 = pygame.draw.rect(screen,(124,252,0), (420, 250, 60, 90),1)

                    draw = shapes[13]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(450,295,15,15))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(450,295,15,15))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(450,295),7)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(450,295),7)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(450,295,15,15))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(450,295),7)

                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(450,295),7)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(450,295,15,15))

                    elif draw==9:

                        card_ver.append(9)

                        pygame.draw.circle(screen,(200,200,200),(450,295),7)

                    elif draw==10:

                        card_ver.append(10)

                        pygame.draw.rect(screen,(200,200,200),(450,295,15,15))

                    elif draw==11:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(0,50,10),(450,295),7)

                    elif draw==12:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(0,50,10),(450,295,15,15))

                    elif draw==13:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,100,0),(450,295),7)

                    elif draw==14:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,100,0),(450,295,15,15))

                    elif draw==15:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,100,100),(450,295,15,15))
                        

                    pygame.display.flip()

                if card3x3.collidepoint(pos) and 15 not in turned_card and 15 not in removed_card:

                    turned_card.append(15)

                    screen.fill((0,0,20),card3x3)

                    card3x3 = pygame.draw.rect(screen,(124,252,0), (490, 250, 60, 90),1)

                    draw = shapes[14]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(520,295,15,15))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(520,295,15,15))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(520,295),7)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(520,295),7)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(520,295,15,15))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(520,295),7)

                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(520,295),7)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(520,295,15,15))

                    elif draw==9:

                        card_ver.append(9)

                        pygame.draw.circle(screen,(200,200,200),(520,295),7)

                    elif draw==10:

                        card_ver.append(10)

                        pygame.draw.rect(screen,(200,200,200),(520,295,15,15))

                    elif draw==11:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(0,50,10),(520,295),7)

                    elif draw==12:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(0,50,10),(520,295,15,15))

                    elif draw==13:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,100,0),(520,295),7)

                    elif draw==14:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,100,0),(520,295,15,15))

                    elif draw==15:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,100,100),(520,295,15,15))
                        

                    pygame.display.flip()

                if card4x3.collidepoint(pos) and 16 not in turned_card and 16 not in removed_card:

                    turned_card.append(16)

                    screen.fill((0,0,20),card4x3)

                    card4x3 = pygame.draw.rect(screen,(124,252,0), (560, 250, 60, 90),1)

                    draw = shapes[15]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(590,295,15,15))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(590,295,15,15))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(590,295),7)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(590,295),7)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(590,295,15,15))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(590,295),7)

                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(590,295),7)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(590,295,15,15))

                    elif draw==9:

                        card_ver.append(9)

                        pygame.draw.circle(screen,(200,200,200),(590,295),7)

                    elif draw==10:

                        card_ver.append(10)

                        pygame.draw.rect(screen,(200,200,200),(590,295,15,15))

                    elif draw==11:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(0,50,10),(590,295),7)

                    elif draw==12:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(0,50,10),(590,295,15,15))

                    elif draw==13:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,100,0),(590,295),7)

                    elif draw==14:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,100,0),(590,295,15,15))

                    elif draw==15:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,100,0),(590,295,15,15))
                        

                    pygame.display.flip()

                if card5x3.collidepoint(pos) and 17 not in turned_card and 17 not in removed_card:

                    turned_card.append(17)

                    screen.fill((0,0,20),card5x3)

                    card5x3 = pygame.draw.rect(screen,(124,252,0), (630, 250, 60, 90),1)

                    draw = shapes[16]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(660,295,15,15))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(660,295,15,15))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(660,295),7)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(660,295),7)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(660,295,15,15))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(660,295),7)

                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(660,295),7)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(660,295,15,15))

                    elif draw==9:

                        card_ver.append(9)

                        pygame.draw.circle(screen,(200,200,200),(660,295),7)

                    elif draw==10:

                        card_ver.append(10)

                        pygame.draw.rect(screen,(200,200,200),(660,295,15,15))

                    elif draw==11:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(0,50,10),(660,295),7)

                    elif draw==12:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(0,50,10),(660,295,15,15))

                    elif draw==13:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,100,0),(660,295),7)

                    elif draw==14:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,100,0),(660,295,15,15))

                    elif draw==15:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,100,100),(660,295,15,15))
                        

                    pygame.display.flip()

                if card6x3.collidepoint(pos) and 18 not in turned_card and 18 not in removed_card:

                    turned_card.append(18)

                    screen.fill((0,0,20),card6x3)

                    card6x3 = pygame.draw.rect(screen,(124,252,0), (700, 250, 60, 90),1)

                    draw = shapes[17]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(730,295,15,15))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(730,295,15,15))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(730,295),7)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(730,295),7)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(730,295,15,15))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(730,295),7)

                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(730,295),7)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(730,295,15,15))

                    elif draw==9:

                        card_ver.append(9)

                        pygame.draw.circle(screen,(200,200,200),(730,295),7)

                    elif draw==10:

                        card_ver.append(10)

                        pygame.draw.rect(screen,(200,200,200),(730,295,15,15))

                    elif draw==11:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(0,50,10),(730,295),7)

                    elif draw==12:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(0,50,10),(730,295,15,15))

                    elif draw==13:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,100,0),(730,295),7)

                    elif draw==14:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,100,0),(730,295,15,15))

                    elif draw==15:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,100,100),(730,295,15,15))
                        

                    pygame.display.flip()

                if card1x4.collidepoint(pos) and 19 not in turned_card and 19 not in removed_card:

                    turned_card.append(19)

                    screen.fill((0,0,20),card1x4)

                    card1x4 = pygame.draw.rect(screen,(124,252,0), (350, 350, 60, 90),1)

                    draw = shapes[18]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(380,395,15,15))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(380,395,15,15))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(380,395),7)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(380,395),7)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(380,395,15,15))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(380,395),7)

                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(380,395),7)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(380,395,15,15))

                    elif draw==9:

                        card_ver.append(9)

                        pygame.draw.circle(screen,(200,200,200),(380,395),7)

                    elif draw==10:

                        card_ver.append(10)

                        pygame.draw.rect(screen,(200,200,200),(380,395,15,15))

                    elif draw==11:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(0,50,10),(380,395),7)

                    elif draw==12:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(0,50,10),(380,395,15,15))

                    elif draw==13:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,100,0),(380,395),7)

                    elif draw==14:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,100,0),(380,395,15,15))

                    elif draw==15:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,100,100),(380,395,15,15))
                        

                    pygame.display.flip()

                if card2x4.collidepoint(pos) and 20 not in turned_card and 20 not in removed_card:

                    turned_card.append(20)

                    screen.fill((0,0,20),card2x4)

                    card2x4 = pygame.draw.rect(screen,(124,252,0), (420, 350, 60, 90),1)

                    draw = shapes[19]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(450,395,15,15))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(450,395,15,15))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(450,395),7)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(450,395),7)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(450,395,15,15))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(450,395),7)

                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(450,395),7)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(450,395,15,15))

                    elif draw==9:

                        card_ver.append(9)

                        pygame.draw.circle(screen,(200,200,200),(450,395),7)

                    elif draw==10:

                        card_ver.append(10)

                        pygame.draw.rect(screen,(200,200,200),(450,395,15,15))

                    elif draw==11:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(0,50,10),(450,395),7)

                    elif draw==12:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(0,50,10),(450,395,15,15))

                    elif draw==13:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,100,0),(450,395),7)

                    elif draw==14:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,100,0),(450,395,15,15))

                    elif draw==15:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,100,100),(450,395,15,15))
                        

                    pygame.display.flip()

                if card3x4.collidepoint(pos) and 21 not in turned_card and 21 not in removed_card:

                    turned_card.append(21)

                    screen.fill((0,0,20),card3x4)

                    card3x4 = pygame.draw.rect(screen,(124,252,0), (490, 350, 60, 90),1)

                    draw = shapes[20]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(520,395,15,15))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(520,395,15,15))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(520,395),7)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(520,395),7)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(520,395,15,15))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(520,395),7)

                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(520,395),7)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(520,395,15,15))

                    elif draw==9:

                        card_ver.append(9)

                        pygame.draw.circle(screen,(200,200,200),(520,395),7)

                    elif draw==10:

                        card_ver.append(10)

                        pygame.draw.rect(screen,(200,200,200),(520,395,15,15))

                    elif draw==11:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(0,50,10),(520,395),7)

                    elif draw==12:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(0,50,10),(520,395,15,15))

                    elif draw==13:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,100,0),(520,395),7)

                    elif draw==14:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,100,0),(520,395,15,15))

                    elif draw==15:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,100,100),(520,395,15,15))
                        

                    pygame.display.flip()

                if card4x4.collidepoint(pos) and 22 not in turned_card and 22 not in removed_card:

                    turned_card.append(22)

                    screen.fill((0,0,20),card4x4)

                    card4x4 = pygame.draw.rect(screen,(124,252,0), (560, 350, 60, 90),1)

                    draw = shapes[21]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(590,395,15,15))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(590,395,15,15))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(590,395),7)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(590,395),7)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(590,395,15,15))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(590,395),7)

                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(590,395),7)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(590,395,15,15))

                    elif draw==9:

                        card_ver.append(9)

                        pygame.draw.circle(screen,(200,200,200),(590,395),7)

                    elif draw==10:

                        card_ver.append(10)

                        pygame.draw.rect(screen,(200,200,200),(590,395,15,15))

                    elif draw==11:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(0,50,10),(590,395),7)

                    elif draw==12:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(0,50,10),(590,395,15,15))

                    elif draw==13:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,100,0),(590,395),7)

                    elif draw==14:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,100,0),(590,395,15,15))
                        
                    elif draw==15:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,100,100),(590,395,15,15))
                        

                    pygame.display.flip()

                if card5x4.collidepoint(pos) and 23 not in turned_card and 23 not in removed_card:

                    turned_card.append(23)

                    screen.fill((0,0,20),card5x4)

                    card5x4 = pygame.draw.rect(screen,(124,252,0), (630, 350, 60, 90),1)

                    draw = shapes[22]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(660,395,15,15))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(660,395,15,15))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(660,395),7)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(660,395),7)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(660,395,15,15))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(660,395),7)

                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(660,395),7)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(660,395,15,15))

                    elif draw==9:

                        card_ver.append(9)

                        pygame.draw.circle(screen,(200,200,200),(660,395),7)

                    elif draw==10:

                        card_ver.append(10)

                        pygame.draw.rect(screen,(200,200,200),(660,395,15,15))

                    elif draw==11:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(0,50,10),(660,395),7)

                    elif draw==12:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(0,50,10),(660,395,15,15))

                    elif draw==13:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,100,0),(660,395),7)

                    elif draw==14:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,100,0),(660,395,15,15))

                    elif draw==15:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,100,100),(660,395,15,15))
                        

                    pygame.display.flip()

                if card6x4.collidepoint(pos) and 24 not in turned_card and 24 not in removed_card:

                    turned_card.append(24)

                    screen.fill((0,0,20),card6x4)

                    card6x4 = pygame.draw.rect(screen,(124,252,0), (700, 350, 60, 90),1)

                    draw = shapes[23]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(730,395,15,15))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(730,395,15,15))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(730,395),7)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(730,395),7)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(730,395,15,15))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(730,395),7)

                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(730,395),7)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(730,395,15,15))

                    elif draw==9:

                        card_ver.append(9)

                        pygame.draw.circle(screen,(200,200,200),(730,395),7)

                    elif draw==10:

                        card_ver.append(10)

                        pygame.draw.rect(screen,(200,200,200),(730,395,15,15))

                    elif draw==11:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(0,50,10),(730,395),7)

                    elif draw==12:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(0,50,10),(730,395,15,15))

                    elif draw==13:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,100,0),(730,395),7)

                    elif draw==14:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,100,0),(730,395,15,15))

                    elif draw==15:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,100,100),(730,395,15,15))
                        

                    pygame.display.flip()

                if card1x5.collidepoint(pos) and 25 not in turned_card and 25 not in removed_card:

                    turned_card.append(25)

                    screen.fill((0,0,20),card1x5)

                    card1x5 = pygame.draw.rect(screen,(124,252,0), (350, 450, 60, 90),1)

                    draw = shapes[24]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(380,495,15,15))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(380,495,15,15))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(380,495),7)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(380,495),7)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(380,495,15,15))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(380,495),7)

                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(380,495),7)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(380,495,15,15))

                    elif draw==9:

                        card_ver.append(9)

                        pygame.draw.circle(screen,(200,200,200),(380,495),7)

                    elif draw==10:

                        card_ver.append(10)

                        pygame.draw.rect(screen,(200,200,200),(380,495,15,15))

                    elif draw==11:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(0,50,10),(380,495),7)

                    elif draw==12:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(0,50,10),(380,495,15,15))

                    elif draw==13:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,100,0),(380,495),7)

                    elif draw==14:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,100,0),(380,495,15,15))

                    elif draw==15:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,100,100),(380,495,15,15))
                        

                    pygame.display.flip()

                if card2x5.collidepoint(pos) and 26 not in turned_card and 26 not in removed_card:

                    turned_card.append(26)

                    screen.fill((0,0,20),card2x5)

                    card2x5 = pygame.draw.rect(screen,(124,252,0), (420, 450, 60, 90),1)

                    draw = shapes[25]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(450,495,15,15))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(450,495,15,15))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(450,495),7)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(450,495),7)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(450,495,15,15))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(450,495),7)

                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(450,495),7)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(450,495,15,15))

                    elif draw==9:

                        card_ver.append(9)

                        pygame.draw.circle(screen,(200,200,200),(450,495),7)

                    elif draw==10:

                        card_ver.append(10)

                        pygame.draw.rect(screen,(200,200,200),(450,495,15,15))

                    elif draw==11:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(0,50,10),(450,495),7)

                    elif draw==12:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(0,50,10),(450,495,15,15))

                    elif draw==13:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,100,0),(450,495),7)

                    elif draw==14:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,100,0),(450,495,15,15))

                    elif draw==15:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,100,100),(450,495,15,15))
                        

                    pygame.display.flip()

                if card3x5.collidepoint(pos) and 27 not in turned_card and 27 not in removed_card:

                    turned_card.append(27)

                    screen.fill((0,0,20),card3x5)

                    card3x5 = pygame.draw.rect(screen,(124,252,0), (490, 450, 60, 90),1)

                    draw = shapes[26]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(520,495,15,15))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(520,495,15,15))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(520,495),7)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(520,495),7)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(520,495,15,15))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(520,495),7)

                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(520,495),7)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(520,495,15,15))

                    elif draw==9:

                        card_ver.append(9)

                        pygame.draw.circle(screen,(200,200,200),(520,495),7)

                    elif draw==10:

                        card_ver.append(10)

                        pygame.draw.rect(screen,(200,200,200),(520,495,15,15))

                    elif draw==11:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(0,50,10),(520,495),7)

                    elif draw==12:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(0,50,10),(520,495,15,15))

                    elif draw==13:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,100,0),(520,495),7)

                    elif draw==14:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,100,0),(520,495,15,15))

                    elif draw==15:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,100,100),(520,495,15,15))
                        

                    pygame.display.flip()

                if card4x5.collidepoint(pos) and 28 not in turned_card and 28 not in removed_card:

                    turned_card.append(28)

                    screen.fill((0,0,20),card4x5)

                    card4x5 = pygame.draw.rect(screen,(124,252,0), (560, 450, 60, 90),1)

                    draw = shapes[27]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(590,495,15,15))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(590,495,15,15))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(590,495),7)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(590,495),7)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(590,495,15,15))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(590,495),7)

                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(590,495),7)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(590,495,15,15))

                    elif draw==9:

                        card_ver.append(9)

                        pygame.draw.circle(screen,(200,200,200),(590,495),7)

                    elif draw==10:

                        card_ver.append(10)

                        pygame.draw.rect(screen,(200,200,200),(590,495,15,15))

                    elif draw==11:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(0,50,10),(590,495),7)

                    elif draw==12:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(0,50,10),(590,495,15,15))

                    elif draw==13:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,100,0),(590,495),7)

                    elif draw==14:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,100,0),(590,495,15,15))

                    elif draw==15:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,100,100),(590,495,15,15))
                        

                    pygame.display.flip()

                if card5x5.collidepoint(pos) and 29 not in turned_card and 29 not in removed_card:

                    turned_card.append(29)

                    screen.fill((0,0,20),card5x5)

                    card5x5 = pygame.draw.rect(screen,(124,252,0), (630, 450, 60, 90),1)

                    draw = shapes[28]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(660,495,15,15))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(660,495,15,15))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(660,495),7)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(660,495),7)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(660,495,15,15))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(660,495),7)

                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(660,495),7)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(660,495,15,15))

                    elif draw==9:

                        card_ver.append(9)

                        pygame.draw.circle(screen,(200,200,200),(660,495),7)

                    elif draw==10:

                        card_ver.append(10)

                        pygame.draw.rect(screen,(200,200,200),(660,495,15,15))

                    elif draw==11:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(0,50,10),(660,495),7)

                    elif draw==12:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(0,50,10),(660,495,15,15))

                    elif draw==13:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,100,0),(660,495),7)

                    elif draw==14:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,100,0),(660,495,15,15))

                    elif draw==15:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,100,100),(660,495,15,15))
                        

                    pygame.display.flip()

                if card6x5.collidepoint(pos) and 30 not in turned_card and 30 not in removed_card:

                    turned_card.append(30)

                    screen.fill((0,0,20),card6x5)

                    card6x5 = pygame.draw.rect(screen,(124,252,0), (700, 450, 60, 90),1)

                    draw = shapes[29]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(730,495,15,15))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(730,495,15,15))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(730,495),7)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(730,495),7)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(730,495,15,15))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(730,495),7)

                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(730,495),7)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(730,495,15,15))

                    elif draw==9:

                        card_ver.append(9)

                        pygame.draw.circle(screen,(200,200,200),(730,495),7)

                    elif draw==10:

                        card_ver.append(10)

                        pygame.draw.rect(screen,(200,200,200),(730,495,15,15))

                    elif draw==11:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(0,50,10),(730,495),7)

                    elif draw==12:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(0,50,10),(730,495,15,15))

                    elif draw==13:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,100,0),(730,495),7)

                    elif draw==14:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,100,0),(730,495,15,15))

                    elif draw==15:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,100,100),(730,495,15,15))
                        

                    pygame.display.flip()

                if len(turned_card)==2:

                    pygame.time.wait(1000)

                    if card_ver[0]==card_ver[1]:

                        score+=100

                        pygame.draw.rect(screen,(0,0,20),(0,0,100,100))
                        
                        score_display = my_font.render_to(screen, (10, 10), "Score: " + str(score), (255, 255, 0))

                        pygame.display.flip()

                        removed_card.append(turned_card[0])
                        removed_card.append(turned_card[1])

                        win+=2 
                    
                        for i in turned_card:

                            if i==1:
                                
                                screen.fill((0,0,20),card1x1)

                            if i==2:

                                screen.fill((0,0,20),card2x1)


                            if i==3:
                                
                                screen.fill((0,0,20),card3x1)

                            if i==4:

                                screen.fill((0,0,20),card4x1)

                            if i==5:
                                
                                screen.fill((0,0,20),card5x1)

                            if i==6:
                                
                                screen.fill((0,0,20),card6x1)
                                
                            if i==7:

                                screen.fill((0,0,20),card1x2)
                                
                            if i==8:

                                screen.fill((0,0,20),card2x2)

                            if i==9:

                                screen.fill((0,0,20),card3x2)

                            if i==10:

                                screen.fill((0,0,20),card4x2)
                            
                            if i==11:
                                
                                screen.fill((0,0,20),card5x2)

                            if i==12:
                                
                                screen.fill((0,0,20),card6x2)
                                
                            if i==13:

                                screen.fill((0,0,20),card1x3)
                                
                            if i==14:

                                screen.fill((0,0,20),card2x3)
                                
                            if i==15:

                                screen.fill((0,0,20),card3x3)
                                
                            if i==16:

                                screen.fill((0,0,20),card4x3)
                            
                            if i==17:
                                
                                screen.fill((0,0,20),card5x3)

                            if i==18:
                                
                                screen.fill((0,0,20),card6x3)
                            
                            if i==19:

                                screen.fill((0,0,20),card1x4)
                                
                            if i==20:

                                screen.fill((0,0,20),card2x4)
                                
                            if i==21:

                                screen.fill((0,0,20),card3x4)
                                
                            if i==22:

                                screen.fill((0,0,20),card4x4)
                            
                            if i==23:
                                
                                screen.fill((0,0,20),card5x4)

                            if i==24:
                                
                                screen.fill((0,0,20),card6x4)
                            
                            if i==25:

                                screen.fill((0,0,20),card1x5)
                                
                            if i==26:

                                screen.fill((0,0,20),card2x5)
                                
                            if i==27:

                                screen.fill((0,0,20),card3x5)
                                
                            if i==28:

                                screen.fill((0,0,20),card4x5)
                            
                            if i==29:
                                
                                screen.fill((0,0,20),card5x5)

                            if i==30:
                                
                                screen.fill((0,0,20),card6x5)

                    else:

                        for i in turned_card:

                            if i==1:

                                penalty1x1+=20

                                score=score-penalty1x1
                                
                                card1x1 = pygame.draw.rect(screen,(124,252,0), (350, 50, 60, 90),0)

                            if i==2:

                                penalty2x1+=20

                                score=score-penalty2x1
                                
                                card2x1 = pygame.draw.rect(screen,(124,252,0), (420, 50, 60, 90),0)

                            if i==3:

                                penalty3x1+=20

                                score=score-penalty3x1
                                
                                card3x1 = pygame.draw.rect(screen,(124,252,0), (490, 50, 60, 90),0)

                            if i==4:

                                penalty4x1+=20

                                score=score-penalty4x1

                                card4x1 = pygame.draw.rect(screen,(124,252,0), (560, 50, 60, 90),0)

                            
                            if i==5:

                                penalty5x1+=20

                                score=score-penalty5x1

                                card5x1 = pygame.draw.rect(screen,(124,252,0), (630, 50, 60, 90),0)

                            if i==6:

                                penalty6x1+=20

                                score=score-penalty6x1

                                card6x1 = pygame.draw.rect(screen,(124,252,0), (700, 50, 60, 90),0)
                                
                            if i==7:

                                penalty1x2+=20

                                score=score-penalty1x2

                                card1x2 = pygame.draw.rect(screen,(124,252,0), (350, 150, 60, 90),0)
                                
                            if i==8:

                                penalty2x2+=20

                                score=score-penalty2x2

                                card2x2 = pygame.draw.rect(screen,(124,252,0), (420, 150, 60, 90),0)

                            if i==9:

                                penalty3x2+=20

                                score=score-penalty3x2

                                card3x2 = pygame.draw.rect(screen,(124,252,0), (490, 150, 60, 90),0)

                            if i==10:

                                penalty4x2+=20

                                score=score-penalty4x2

                                card4x2 = pygame.draw.rect(screen,(124,252,0), (560, 150, 60, 90),0)
                                
                            if i==11:

                                penalty5x2+=20

                                score=score-penalty5x2

                                card5x2 = pygame.draw.rect(screen,(124,252,0), (630, 150, 60, 90),0)

                            if i==12:

                                penalty6x2+=20

                                score=score-penalty6x2

                                card6x2 = pygame.draw.rect(screen,(124,252,0), (700, 150, 60, 90),0)

                            if i==13:

                                penalty1x3+=20

                                score=score-penalty1x3

                                card1x3 = pygame.draw.rect(screen,(124,252,0), (350, 250, 60, 90),0)
                                
                            if i==14:

                                penalty2x3+=20

                                score=score-penalty2x3

                                card2x3 = pygame.draw.rect(screen,(124,252,0), (420, 250, 60, 90),0)
                                
                            if i==15:

                                penalty3x3+=20

                                score=score-penalty3x3

                                card3x3 = pygame.draw.rect(screen,(124,252,0), (490, 250, 60, 90),0)

                                
                            if i==16:

                                penalty4x3+=20

                                score=score-penalty4x3

                                card4x3 = pygame.draw.rect(screen,(124,252,0), (560, 250, 60, 90),0)
                            
                            if i==17:

                                penalty5x3+=20

                                score=score-penalty5x3

                                card5x3 = pygame.draw.rect(screen,(124,252,0), (630, 250, 60, 90),0)

                            if i==18:

                                penalty6x3+=20

                                score=score-penalty6x3

                                card6x3 = pygame.draw.rect(screen,(124,252,0), (700, 250, 60, 90),0)

                            if i==19:

                                penalty1x4+=20

                                score=score-penalty1x4

                                card1x4 = pygame.draw.rect(screen,(124,252,0), (350, 350, 60, 90),0)
                                     
                            if i==20:

                                penalty2x4+=20

                                score=score-penalty2x4

                                card2x4 = pygame.draw.rect(screen,(124,252,0), (420, 350, 60, 90),0)
                                
                            if i==21:

                                penalty3x4+=20

                                score=score-penalty3x4

                                card3x4 = pygame.draw.rect(screen,(124,252,0), (490, 350, 60, 90),0)
                                
                            if i==22:

                                penalty4x4+=20

                                score=score-penalty4x4

                                card4x4 = pygame.draw.rect(screen,(124,252,0), (560, 350, 60, 90),0)

                            if i==23:

                                penalty5x4+=20

                                score=score-penalty5x4

                                card5x4 = pygame.draw.rect(screen,(124,252,0), (630, 350, 60, 90),0)

                            if i==24:

                                penalty6x4+=20

                                score=score-penalty6x4

                                card6x4 = pygame.draw.rect(screen,(124,252,0), (700, 350, 60, 90),0)

                            if i==25:

                                penalty1x5+=20

                                score=score-penalty1x5

                                card1x5 = pygame.draw.rect(screen,(124,252,0), (350, 450, 60, 90),0)
                                     
                            if i==26:

                                penalty2x5+=20

                                score=score-penalty2x5

                                card2x5 = pygame.draw.rect(screen,(124,252,0), (420, 450, 60, 90),0)
                                
                            if i==27:

                                penalty3x5+=20

                                score=score-penalty3x5

                                card3x5 = pygame.draw.rect(screen,(124,252,0), (490, 450, 60, 90),0)
                                
                            if i==28:

                                penalty4x5+=20

                                score=score-penalty4x5

                                card4x5 = pygame.draw.rect(screen,(124,252,0), (560, 450, 60, 90),0)

                            if i==29:

                                penalty5x5+=20

                                score=score-penalty5x5

                                card5x5 = pygame.draw.rect(screen,(124,252,0), (630, 450, 60, 90),0)
                                
                            if i==30:

                                penalty6x5+=20

                                score=score-penalty6x5

                                card6x5 = pygame.draw.rect(screen,(124,252,0), (700, 450, 60, 90),0)
                                

                    turned_card=[]

                    card_ver=[]

                    pygame.draw.rect(screen,(0,0,20),(0,0,200,200))

                    if score<0:

                        score = 0
                        
                    score_display = my_font.render_to(screen, (10, 10), "Score: " + str(score), (255, 255, 0))

                
                    pygame.display.flip()

                    if win==30:
                        
                        my_font.render_to(screen, (540, 360), "CONGRATULATIONS, YOU WON!", (255, 255, 0))

                        pygame.display.flip()

def game6x6():

    my_font = pygame.freetype.Font("NotoSans-Regular.ttf", 24)

    res = (1280,720)

    screen = pygame.display.set_mode(res)

    screen.fill((0,0,20))

    card1x1 = pygame.draw.rect(screen,(124,252,0), (350, 50, 60, 90),0)

    card2x1 = pygame.draw.rect(screen,(124,252,0), (420, 50, 60, 90),0)

    card3x1 = pygame.draw.rect(screen,(124,252,0), (490, 50, 60, 90),0)

    card4x1 = pygame.draw.rect(screen,(124,252,0), (560, 50, 60, 90),0)

    card5x1 = pygame.draw.rect(screen,(124,252,0), (630, 50, 60, 90),0)

    card6x1 = pygame.draw.rect(screen,(124,252,0), (700, 50, 60, 90),0)

    card1x2 = pygame.draw.rect(screen,(124,252,0), (350, 150, 60, 90),0)

    card2x2 = pygame.draw.rect(screen,(124,252,0), (420, 150, 60, 90),0)

    card3x2 = pygame.draw.rect(screen,(124,252,0), (490, 150, 60, 90),0)

    card4x2 = pygame.draw.rect(screen,(124,252,0), (560, 150, 60, 90),0)

    card5x2 = pygame.draw.rect(screen,(124,252,0), (630, 150, 60, 90),0)

    card6x2 = pygame.draw.rect(screen,(124,252,0), (700, 150, 60, 90),0)

    card1x3 = pygame.draw.rect(screen,(124,252,0), (350, 250, 60, 90),0)

    card2x3 = pygame.draw.rect(screen,(124,252,0), (420, 250, 60, 90),0)

    card3x3 = pygame.draw.rect(screen,(124,252,0), (490, 250, 60, 90),0)

    card4x3 = pygame.draw.rect(screen,(124,252,0), (560, 250, 60, 90),0)

    card5x3 = pygame.draw.rect(screen,(124,252,0), (630, 250, 60, 90),0)

    card6x3 = pygame.draw.rect(screen,(124,252,0), (700, 250, 60, 90),0)

    card1x4 = pygame.draw.rect(screen,(124,252,0), (350, 350, 60, 90),0)

    card2x4 = pygame.draw.rect(screen,(124,252,0), (420, 350, 60, 90),0)

    card3x4 = pygame.draw.rect(screen,(124,252,0), (490, 350, 60, 90),0)

    card4x4 = pygame.draw.rect(screen,(124,252,0), (560, 350, 60, 90),0)

    card5x4 = pygame.draw.rect(screen,(124,252,0), (630, 350, 60, 90),0)

    card6x4 = pygame.draw.rect(screen,(124,252,0), (700, 350, 60, 90),0)

    card1x5 = pygame.draw.rect(screen,(124,252,0), (350, 450, 60, 90),0)

    card2x5 = pygame.draw.rect(screen,(124,252,0), (420, 450, 60, 90),0)

    card3x5 = pygame.draw.rect(screen,(124,252,0), (490, 450, 60, 90),0)

    card4x5 = pygame.draw.rect(screen,(124,252,0), (560, 450, 60, 90),0)

    card5x5 = pygame.draw.rect(screen,(124,252,0), (630, 450, 60, 90),0)

    card6x5 = pygame.draw.rect(screen,(124,252,0), (700, 450, 60, 90),0)

    card1x6 = pygame.draw.rect(screen,(124,252,0), (350, 550, 60, 90),0)

    card2x6 = pygame.draw.rect(screen,(124,252,0), (420, 550, 60, 90),0)

    card3x6 = pygame.draw.rect(screen,(124,252,0), (490, 550, 60, 90),0)

    card4x6 = pygame.draw.rect(screen,(124,252,0), (560, 550, 60, 90),0)

    card5x6 = pygame.draw.rect(screen,(124,252,0), (630, 550, 60, 90),0)

    card6x6 = pygame.draw.rect(screen,(124,252,0), (700, 550, 60, 90),0)

    sair = pygame.draw.rect(screen, (255, 255, 0), (30,600,120,30),3)

    pygame.display.flip()

    my_font.render_to(screen, (65, 607), "Exit", (255, 255, 0))

    shapes = shapes_pos(18)

    turned_card=[]
    card_ver=[]
    removed_card=[]
    win=0
    score=0
    penalty1x1=-20
    penalty2x1=-20
    penalty3x1=-20
    penalty4x1=-20
    penalty5x1=-20
    penalty6x1=-20
    penalty1x2=-20
    penalty2x2=-20
    penalty3x2=-20
    penalty4x2=-20
    penalty5x2=-20
    penalty6x2=-20
    penalty1x3=-20
    penalty2x3=-20
    penalty3x3=-20
    penalty4x3=-20
    penalty5x3=-20
    penalty6x3=-20
    penalty1x4=-20
    penalty2x4=-20
    penalty3x4=-20
    penalty4x4=-20
    penalty5x4=-20
    penalty6x4=-20
    penalty1x5=-20
    penalty2x5=-20
    penalty3x5=-20
    penalty4x5=-20
    penalty5x5=-20
    penalty6x5=-20
    penalty1x6=-20
    penalty2x6=-20
    penalty3x6=-20
    penalty4x6=-20
    penalty5x6=-20
    penalty6x6=-20

    pygame.display.flip()

    score_display = my_font.render_to(screen, (10, 10), "Score: " + str(score), (255, 255, 0))

    while(True):

        pygame.display.flip()

        for event in pygame.event.get():

            if (event.type == pygame.QUIT):

                exit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button== 1:

                pos = pygame.mouse.get_pos()

                if sair.collidepoint(pos):

                    menu()
                
                if card1x1.collidepoint(pos) and 1 not in turned_card and 1 not in removed_card:

                    turned_card.append(1)

                    screen.fill((0,0,20),card1x1)

                    card1x1 = pygame.draw.rect(screen,(124,252,0), (350, 50, 60, 90),1)

                    draw = shapes[0]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(380,90,15,15))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(380,90,15,15))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(380,90),7)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(380,90),7)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(380,90,15,15))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(380,90),7)

                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(380,90),7)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(380,90,15,15))

                    elif draw==9:

                        card_ver.append(9)

                        pygame.draw.circle(screen,(200,200,200),(380,90),7)

                    elif draw==10:

                        card_ver.append(10)

                        pygame.draw.rect(screen,(200,200,200),(380,90,15,15))

                    elif draw==11:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(0,50,10),(380,90),7)

                    elif draw==12:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(0,50,10),(380,90,15,15))

                    elif draw==13:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,100,0),(380,90),7)

                    elif draw==14:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,100,0),(380,90,15,15))

                    elif draw==15:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,100,100),(380,90,15,15))
                    
                    elif draw==16:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(100,100,100),(380,90),7)

                    elif draw==17:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,20,200),(380,90,15,15))

                    elif draw==18:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(100,20,200),(380,90),7)
                
                if card2x1.collidepoint(pos) and 2 not in turned_card and 2 not in removed_card:

                    turned_card.append(2)

                    screen.fill((0,0,20),card2x1)

                    card2x1 = pygame.draw.rect(screen,(124,252,0), (420, 50, 60, 90),1)

                    draw = shapes[1]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(450,90,15,15))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(450,90,15,15))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(450,90),7)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(450,90),7)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(450,90,15,15))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(450,90),7)

                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(450,90),7)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(450,90,15,15))

                    elif draw==9:

                        card_ver.append(9)

                        pygame.draw.circle(screen,(200,200,200),(450,90),7)

                    elif draw==10:

                        card_ver.append(10)

                        pygame.draw.rect(screen,(200,200,200),(450,90,15,15))

                    elif draw==11:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(0,50,10),(450,90),7)

                    elif draw==12:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(0,50,10),(450,90,15,15))

                    elif draw==13:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,100,0),(450,90),7)

                    elif draw==14:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,100,0),(450,90,15,15))

                    elif draw==15:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,100,100),(450,90,15,15))

                    elif draw==16:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(100,100,100),(450,90),7)

                    elif draw==17:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,20,200),(450,90,15,15))

                    elif draw==18:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(100,20,200),(450,90),7)
                        

                    pygame.display.flip()

                if card3x1.collidepoint(pos) and 3 not in turned_card and 3 not in removed_card:

                    turned_card.append(3)

                    screen.fill((0,0,20),card3x1)

                    card3x1 = pygame.draw.rect(screen,(124,252,0), (490, 50, 60, 90),1)

                    draw = shapes[2]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(520,90,15,15))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(520,90,15,15))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(520,90),7)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(520,90),7)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(520,90,15,15))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(520,90),7)

                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(520,90),7)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(520,90,15,15))

                    elif draw==9:

                        card_ver.append(9)

                        pygame.draw.circle(screen,(200,200,200),(520,90),7)

                    elif draw==10:

                        card_ver.append(10)

                        pygame.draw.rect(screen,(200,200,200),(520,90,15,15))

                    elif draw==11:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(0,50,10),(520,90),7)

                    elif draw==12:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(0,50,10),(520,90,15,15))

                    elif draw==13:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,100,0),(520,90),7)

                    elif draw==14:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,100,0),(520,90,15,15))

                    elif draw==15:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,100,100),(520,90,15,15))

                    elif draw==16:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(100,100,100),(520,90),7)

                    elif draw==17:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,20,200),(520,90,15,15))

                    elif draw==18:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(100,20,200),(520,90),7)
                        

                    pygame.display.flip()

                if card4x1.collidepoint(pos) and 4 not in turned_card and 4 not in removed_card:

                    turned_card.append(4)

                    screen.fill((0,0,20),card4x1)

                    card4x1 = pygame.draw.rect(screen,(124,252,0), (560, 50, 60, 90),1)

                    draw = shapes[3]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(590,90,15,15))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(590,90,15,15))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(590,90),7)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(590,90),7)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(590,90,15,15))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(590,90),7)

                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(590,90),7)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(590,90,15,15))

                    elif draw==9:

                        card_ver.append(9)

                        pygame.draw.circle(screen,(200,200,200),(590,90),7)

                    elif draw==10:

                        card_ver.append(10)

                        pygame.draw.rect(screen,(200,200,200),(590,90,15,15))

                    elif draw==11:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(0,50,10),(590,90),7)

                    elif draw==12:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(0,50,10),(590,90,15,15))

                    elif draw==13:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,100,0),(590,90),7)

                    elif draw==14:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,100,0),(590,90,15,15))

                    elif draw==15:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,100,100),(590,90,15,15))

                    elif draw==16:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(100,100,100),(590,90),7)

                    elif draw==17:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,20,200),(590,90,15,15))

                    elif draw==18:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(100,20,200),(590,90),7)
                        

                    pygame.display.flip()

                if card5x1.collidepoint(pos) and 5 not in turned_card and 5 not in removed_card:

                    turned_card.append(5)

                    screen.fill((0,0,20),card5x1)

                    card5x1 = pygame.draw.rect(screen,(124,252,0), (630, 50, 60, 90),1)

                    draw = shapes[4]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(660,90,15,15))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(660,90,15,15))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(660,90),7)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(660,90),7)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(660,90,15,15))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(660,90),7)

                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(660,90),7)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(660,90,15,15))

                    elif draw==9:

                        card_ver.append(9)

                        pygame.draw.circle(screen,(200,200,200),(660,90),7)

                    elif draw==10:

                        card_ver.append(10)

                        pygame.draw.rect(screen,(200,200,200),(660,90,15,15))

                    elif draw==11:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(0,50,10),(660,90),7)

                    elif draw==12:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(0,50,10),(660,90,15,15))

                    elif draw==13:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,100,0),(660,90),7)

                    elif draw==14:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,100,0),(660,90,15,15))

                    elif draw==15:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,100,100),(660,90,15,15))

                    elif draw==16:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(100,100,100),(660,90),7)

                    elif draw==17:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,20,200),(660,90,15,15))

                    elif draw==18:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(100,20,200),(660,90),7)
                        

                    pygame.display.flip()

                if card6x1.collidepoint(pos) and 6 not in turned_card and 6 not in removed_card:

                    turned_card.append(6)

                    screen.fill((0,0,20),card6x1)

                    card6x1 = pygame.draw.rect(screen,(124,252,0), (700, 50, 60, 90),1)

                    draw = shapes[5]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(730,90,15,15))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(730,90,15,15))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(730,90),7)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(730,90),7)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(730,90,15,15))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(730,90),7)

                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(730,90),7)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(730,90,15,15))

                    elif draw==9:

                        card_ver.append(9)

                        pygame.draw.circle(screen,(200,200,200),(730,90),7)

                    elif draw==10:

                        card_ver.append(10)

                        pygame.draw.rect(screen,(200,200,200),(730,90,15,15))

                    elif draw==11:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(0,50,10),(730,90),7)

                    elif draw==12:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(0,50,10),(730,90,15,15))

                    elif draw==13:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,100,0),(730,90),7)

                    elif draw==14:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,100,0),(730,90,15,15))

                    elif draw==15:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,100,100),(730,90,15,15))

                    elif draw==16:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(100,100,100),(730,90),7)

                    elif draw==17:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,20,200),(730,90,15,15))

                    elif draw==18:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(100,20,200),(730,90),7)
                        

                    pygame.display.flip()

                if card1x2.collidepoint(pos) and 7 not in turned_card and 7 not in removed_card:

                    turned_card.append(7)

                    screen.fill((0,0,20),card1x2)

                    card1x2 = pygame.draw.rect(screen,(124,252,0), (350, 150, 60, 90),1)

                    draw = shapes[6]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(380,195,15,15))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(380,195,15,15))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(380,195),7)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(380,195),7)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(380,195,15,15))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(380,195),7)

                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(380,195),7)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(380,195,15,15))

                    elif draw==9:

                        card_ver.append(9)

                        pygame.draw.circle(screen,(200,200,200),(380,195),7)

                    elif draw==10:

                        card_ver.append(10)

                        pygame.draw.rect(screen,(200,200,200),(380,195,15,15))

                    elif draw==11:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(0,50,10),(380,195),7)

                    elif draw==12:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(0,50,10),(380,195,15,15))

                    elif draw==13:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,100,0),(380,195),7)

                    elif draw==14:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,100,0),(380,195,15,15))

                    elif draw==15:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,100,100),(380,195,15,15))
                    
                    elif draw==16:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(100,100,100),(380,195),7)

                    elif draw==17:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,20,200),(380,195,15,15))

                    elif draw==18:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(100,20,200),(380,195),7)

                    pygame.display.flip()

                if card2x2.collidepoint(pos) and 8 not in turned_card and 8 not in removed_card:

                    turned_card.append(8)

                    screen.fill((0,0,20),card2x2)

                    card2x2 = pygame.draw.rect(screen,(124,252,0), (420, 150, 60, 90),1)

                    draw = shapes[7]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(450,195,15,15))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(450,195,15,15))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(450,195),7)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(450,195),7)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(450,195,15,15))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(450,195),7)

                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(450,195),7)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(450,195,15,15))

                    elif draw==9:

                        card_ver.append(9)

                        pygame.draw.circle(screen,(200,200,200),(450,195),7)

                    elif draw==10:

                        card_ver.append(10)

                        pygame.draw.rect(screen,(200,200,200),(450,195,15,15))

                    elif draw==11:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(0,50,10),(450,195),7)

                    elif draw==12:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(0,50,10),(450,195,15,15))

                    elif draw==13:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,100,0),(450,195),7)

                    elif draw==14:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,100,0),(450,195,15,15))

                    elif draw==15:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,100,100),(450,195,15,15))

                    elif draw==16:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(100,100,100),(450,195),7)

                    elif draw==17:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,20,200),(450,195,15,15))

                    elif draw==18:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(100,20,200),(450,195),7)
                        

                    pygame.display.flip()

                if card3x2.collidepoint(pos) and 9 not in turned_card and 9 not in removed_card:

                    turned_card.append(9)

                    screen.fill((0,0,20),card3x2)

                    card3x2 = pygame.draw.rect(screen,(124,252,0), (490, 150, 60, 90),1)

                    draw = shapes[8]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(520,195,15,15))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(520,195,15,15))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(520,195),7)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(520,195),7)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(520,195,15,15))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(520,195),7)

                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(520,195),7)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(520,195,15,15))

                    elif draw==9:

                        card_ver.append(9)

                        pygame.draw.circle(screen,(200,200,200),(520,195),7)

                    elif draw==10:

                        card_ver.append(10)

                        pygame.draw.rect(screen,(200,200,200),(520,195,15,15))

                    elif draw==11:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(0,50,10),(520,195),7)

                    elif draw==12:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(0,50,10),(520,195,15,15))

                    elif draw==13:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,100,0),(520,195),7)

                    elif draw==14:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,100,0),(520,195,15,15))

                    elif draw==15:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,100,100),(520,195,15,15))

                    elif draw==16:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(100,100,100),(520,195),7)

                    elif draw==17:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,20,200),(520,195,15,15))

                    elif draw==18:

                        card_ver.append(draw)
                        
                        pygame.draw.circle(screen,(100,20,200),(520,195),7)

                    pygame.display.flip()

                if card4x2.collidepoint(pos) and 10 not in turned_card and 10 not in removed_card:

                    turned_card.append(10)

                    screen.fill((0,0,20),card4x2)

                    card4x2 = pygame.draw.rect(screen,(124,252,0), (560, 150, 60, 90),1)

                    draw = shapes[9]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(590,195,15,15))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(590,195,15,15))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(590,195),7)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(590,195),7)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(590,195,15,15))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(590,195),7)

                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(590,195),7)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(590,195,15,15))

                    elif draw==9:

                        card_ver.append(9)

                        pygame.draw.circle(screen,(200,200,200),(590,195),7)

                    elif draw==10:

                        card_ver.append(10)

                        pygame.draw.rect(screen,(200,200,200),(590,195,15,15))

                    elif draw==11:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(0,50,10),(590,195),7)

                    elif draw==12:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(0,50,10),(590,195,15,15))

                    elif draw==13:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,100,0),(590,195),7)

                    elif draw==14:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,100,0),(590,195,15,15))

                    elif draw==15:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,100,100),(590,195,15,15))
                    
                    elif draw==16:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(100,100,100),(590,195),7)

                    elif draw==17:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,20,200),(590,195,15,15))

                    elif draw==18:

                        card_ver.append(draw)
                        
                        pygame.draw.circle(screen,(100,20,200),(590,195),7)

                    pygame.display.flip()

                if card5x2.collidepoint(pos) and 11 not in turned_card and 11 not in removed_card:

                    turned_card.append(11)

                    screen.fill((0,0,20),card5x2)

                    card5x2 = pygame.draw.rect(screen,(124,252,0), (630, 150, 60, 90),1)

                    draw = shapes[10]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(660,195,15,15))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(660,195,15,15))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(660,195),7)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(660,195),7)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(660,195,15,15))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(660,195),7)

                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(660,195),7)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(660,195,15,15))

                    elif draw==9:

                        card_ver.append(9)

                        pygame.draw.circle(screen,(200,200,200),(660,195),7)

                    elif draw==10:

                        card_ver.append(10)

                        pygame.draw.rect(screen,(200,200,200),(660,195,15,15))

                    elif draw==11:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(0,50,10),(660,195),7)

                    elif draw==12:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(0,50,10),(660,195,15,15))

                    elif draw==13:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,100,0),(660,195),7)

                    elif draw==14:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,100,0),(660,195,15,15))

                    elif draw==15:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,100,100),(660,195,15,15))

                    elif draw==16:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(100,100,100),(660,195),7)

                    elif draw==17:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,20,200),(660,195,15,15))

                    elif draw==18:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(100,20,200),(660,195),7)
                        

                    pygame.display.flip()

                if card6x2.collidepoint(pos) and 12 not in turned_card and 12 not in removed_card:

                    turned_card.append(12)

                    screen.fill((0,0,20),card6x2)

                    card6x2 = pygame.draw.rect(screen,(124,252,0), (700, 150, 60, 90),1)

                    draw = shapes[11]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(730,195,15,15))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(730,195,15,15))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(730,195),7)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(730,195),7)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(730,195,15,15))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(730,195),7)

                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(730,195),7)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(730,195,15,15))

                    elif draw==9:

                        card_ver.append(9)

                        pygame.draw.circle(screen,(200,200,200),(730,195),7)

                    elif draw==10:

                        card_ver.append(10)

                        pygame.draw.rect(screen,(200,200,200),(730,195,15,15))

                    elif draw==11:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(0,50,10),(730,195),7)

                    elif draw==12:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(0,50,10),(730,195,15,15))

                    elif draw==13:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,100,0),(730,195),7)

                    elif draw==14:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,100,0),(730,195,15,15))

                    elif draw==15:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,100,100),(730,195,15,15))

                    elif draw==16:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(100,100,100),(730,195),7)

                    elif draw==17:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,20,200),(730,195,15,15))

                    elif draw==18:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(100,20,200),(730,195),7)
                        

                    pygame.display.flip()

                if card1x3.collidepoint(pos) and 13 not in turned_card and 13 not in removed_card:

                    turned_card.append(13)

                    screen.fill((0,0,20),card1x3)

                    card1x3 = pygame.draw.rect(screen,(124,252,0), (350, 250, 60, 90),1)

                    draw = shapes[12]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(380,295,15,15))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(380,295,15,15))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(380,295),7)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(380,295),7)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(380,295,15,15))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(380,295),7)

                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(380,295),7)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(380,295,15,15))

                    elif draw==9:

                        card_ver.append(9)

                        pygame.draw.circle(screen,(200,200,200),(380,295),7)

                    elif draw==10:

                        card_ver.append(10)

                        pygame.draw.rect(screen,(200,200,200),(380,295,15,15))

                    elif draw==11:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(0,50,10),(380,295),7)

                    elif draw==12:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(0,50,10),(380,295,15,15))

                    elif draw==13:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,100,0),(380,295),7)

                    elif draw==14:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,100,0),(380,295,15,15))

                    elif draw==15:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,100,100),(380,295,15,15))

                    elif draw==16:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(100,100,100),(380,295),7)

                    elif draw==17:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,20,200),(380,295,15,15))

                    elif draw==18:

                        card_ver.append(draw)
                        
                        pygame.draw.circle(screen,(100,20,200),(380,295),7)

                    pygame.display.flip()

                if card2x3.collidepoint(pos) and 14 not in turned_card and 14 not in removed_card:

                    turned_card.append(14)

                    screen.fill((0,0,20),card2x3)

                    card2x3 = pygame.draw.rect(screen,(124,252,0), (420, 250, 60, 90),1)

                    draw = shapes[13]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(450,295,15,15))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(450,295,15,15))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(450,295),7)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(450,295),7)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(450,295,15,15))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(450,295),7)

                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(450,295),7)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(450,295,15,15))

                    elif draw==9:

                        card_ver.append(9)

                        pygame.draw.circle(screen,(200,200,200),(450,295),7)

                    elif draw==10:

                        card_ver.append(10)

                        pygame.draw.rect(screen,(200,200,200),(450,295,15,15))

                    elif draw==11:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(0,50,10),(450,295),7)

                    elif draw==12:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(0,50,10),(450,295,15,15))

                    elif draw==13:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,100,0),(450,295),7)

                    elif draw==14:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,100,0),(450,295,15,15))

                    elif draw==15:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,100,100),(450,295,15,15))

                    elif draw==16:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(100,100,100),(450,295),7)

                    elif draw==17:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,20,200),(450,295,15,15))

                    elif draw==18:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(100,20,200),(450,295),7)
                        

                    pygame.display.flip()

                if card3x3.collidepoint(pos) and 15 not in turned_card and 15 not in removed_card:

                    turned_card.append(15)

                    screen.fill((0,0,20),card3x3)

                    card3x3 = pygame.draw.rect(screen,(124,252,0), (490, 250, 60, 90),1)

                    draw = shapes[14]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(520,295,15,15))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(520,295,15,15))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(520,295),7)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(520,295),7)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(520,295,15,15))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(520,295),7)

                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(520,295),7)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(520,295,15,15))

                    elif draw==9:

                        card_ver.append(9)

                        pygame.draw.circle(screen,(200,200,200),(520,295),7)

                    elif draw==10:

                        card_ver.append(10)

                        pygame.draw.rect(screen,(200,200,200),(520,295,15,15))

                    elif draw==11:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(0,50,10),(520,295),7)

                    elif draw==12:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(0,50,10),(520,295,15,15))

                    elif draw==13:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,100,0),(520,295),7)

                    elif draw==14:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,100,0),(520,295,15,15))

                    elif draw==15:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,100,100),(520,295,15,15))

                    elif draw==16:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(100,100,100),(520,295),7)

                    elif draw==17:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,20,200),(520,295,15,15))

                    elif draw==18:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(100,20,200),(520,295),7)
                        

                    pygame.display.flip()

                if card4x3.collidepoint(pos) and 16 not in turned_card and 16 not in removed_card:

                    turned_card.append(16)

                    screen.fill((0,0,20),card4x3)

                    card4x3 = pygame.draw.rect(screen,(124,252,0), (560, 250, 60, 90),1)

                    draw = shapes[15]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(590,295,15,15))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(590,295,15,15))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(590,295),7)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(590,295),7)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(590,295,15,15))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(590,295),7)

                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(590,295),7)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(590,295,15,15))

                    elif draw==9:

                        card_ver.append(9)

                        pygame.draw.circle(screen,(200,200,200),(590,295),7)

                    elif draw==10:

                        card_ver.append(10)

                        pygame.draw.rect(screen,(200,200,200),(590,295,15,15))

                    elif draw==11:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(0,50,10),(590,295),7)

                    elif draw==12:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(0,50,10),(590,295,15,15))

                    elif draw==13:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,100,0),(590,295),7)

                    elif draw==14:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,100,0),(590,295,15,15))

                    elif draw==15:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,100,0),(590,295,15,15))

                    elif draw==16:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(100,100,100),(590,295),7)

                    elif draw==17:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,20,200),(590,295,15,15))

                    elif draw==18:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(100,20,200),(590,295),7)
                        

                    pygame.display.flip()

                if card5x3.collidepoint(pos) and 17 not in turned_card and 17 not in removed_card:

                    turned_card.append(17)

                    screen.fill((0,0,20),card5x3)

                    card5x3 = pygame.draw.rect(screen,(124,252,0), (630, 250, 60, 90),1)

                    draw = shapes[16]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(660,295,15,15))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(660,295,15,15))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(660,295),7)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(660,295),7)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(660,295,15,15))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(660,295),7)

                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(660,295),7)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(660,295,15,15))

                    elif draw==9:

                        card_ver.append(9)

                        pygame.draw.circle(screen,(200,200,200),(660,295),7)

                    elif draw==10:

                        card_ver.append(10)

                        pygame.draw.rect(screen,(200,200,200),(660,295,15,15))

                    elif draw==11:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(0,50,10),(660,295),7)

                    elif draw==12:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(0,50,10),(660,295,15,15))

                    elif draw==13:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,100,0),(660,295),7)

                    elif draw==14:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,100,0),(660,295,15,15))

                    elif draw==15:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,100,100),(660,295,15,15))

                    elif draw==16:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(100,100,100),(660,295),7)

                    elif draw==17:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,20,200),(660,295,15,15))

                    elif draw==18:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(100,20,200),(660,295),7)
                        

                    pygame.display.flip()

                if card6x3.collidepoint(pos) and 18 not in turned_card and 18 not in removed_card:

                    turned_card.append(18)

                    screen.fill((0,0,20),card6x3)

                    card6x3 = pygame.draw.rect(screen,(124,252,0), (700, 250, 60, 90),1)

                    draw = shapes[17]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(730,295,15,15))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(730,295,15,15))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(730,295),7)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(730,295),7)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(730,295,15,15))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(730,295),7)

                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(730,295),7)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(730,295,15,15))

                    elif draw==9:

                        card_ver.append(9)

                        pygame.draw.circle(screen,(200,200,200),(730,295),7)

                    elif draw==10:

                        card_ver.append(10)

                        pygame.draw.rect(screen,(200,200,200),(730,295,15,15))

                    elif draw==11:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(0,50,10),(730,295),7)

                    elif draw==12:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(0,50,10),(730,295,15,15))

                    elif draw==13:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,100,0),(730,295),7)

                    elif draw==14:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,100,0),(730,295,15,15))

                    elif draw==15:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,100,100),(730,295,15,15))

                    elif draw==16:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(100,100,100),(730,295),7)

                    elif draw==17:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,20,200),(730,295,15,15))

                    elif draw==18:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(100,20,200),(730,295),7)
                        

                    pygame.display.flip()

                if card1x4.collidepoint(pos) and 19 not in turned_card and 19 not in removed_card:

                    turned_card.append(19)

                    screen.fill((0,0,20),card1x4)

                    card1x4 = pygame.draw.rect(screen,(124,252,0), (350, 350, 60, 90),1)

                    draw = shapes[18]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(380,395,15,15))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(380,395,15,15))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(380,395),7)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(380,395),7)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(380,395,15,15))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(380,395),7)

                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(380,395),7)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(380,395,15,15))

                    elif draw==9:

                        card_ver.append(9)

                        pygame.draw.circle(screen,(200,200,200),(380,395),7)

                    elif draw==10:

                        card_ver.append(10)

                        pygame.draw.rect(screen,(200,200,200),(380,395,15,15))

                    elif draw==11:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(0,50,10),(380,395),7)

                    elif draw==12:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(0,50,10),(380,395,15,15))

                    elif draw==13:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,100,0),(380,395),7)

                    elif draw==14:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,100,0),(380,395,15,15))

                    elif draw==15:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,100,100),(380,395,15,15))

                    elif draw==16:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(100,100,100),(380,395),7)

                    elif draw==17:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,20,200),(380,395,15,15))

                    elif draw==18:

                        card_ver.append(draw)
                        
                        pygame.draw.circle(screen,(100,20,200),(380,395),7)

                    pygame.display.flip()

                if card2x4.collidepoint(pos) and 20 not in turned_card and 20 not in removed_card:

                    turned_card.append(20)

                    screen.fill((0,0,20),card2x4)

                    card2x4 = pygame.draw.rect(screen,(124,252,0), (420, 350, 60, 90),1)

                    draw = shapes[19]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(450,395,15,15))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(450,395,15,15))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(450,395),7)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(450,395),7)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(450,395,15,15))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(450,395),7)

                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(450,395),7)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(450,395,15,15))

                    elif draw==9:

                        card_ver.append(9)

                        pygame.draw.circle(screen,(200,200,200),(450,395),7)

                    elif draw==10:

                        card_ver.append(10)

                        pygame.draw.rect(screen,(200,200,200),(450,395,15,15))

                    elif draw==11:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(0,50,10),(450,395),7)

                    elif draw==12:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(0,50,10),(450,395,15,15))

                    elif draw==13:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,100,0),(450,395),7)

                    elif draw==14:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,100,0),(450,395,15,15))

                    elif draw==15:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,100,100),(450,395,15,15))

                    elif draw==16:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(100,100,100),(450,395),7)

                    elif draw==17:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,20,200),(450,395,15,15))

                    elif draw==18:

                        card_ver.append(draw)
                        
                        pygame.draw.circle(screen,(100,20,200),(450,395),7)

                    pygame.display.flip()

                if card3x4.collidepoint(pos) and 21 not in turned_card and 21 not in removed_card:

                    turned_card.append(21)

                    screen.fill((0,0,20),card3x4)

                    card3x4 = pygame.draw.rect(screen,(124,252,0), (490, 350, 60, 90),1)

                    draw = shapes[20]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(520,395,15,15))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(520,395,15,15))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(520,395),7)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(520,395),7)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(520,395,15,15))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(520,395),7)

                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(520,395),7)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(520,395,15,15))

                    elif draw==9:

                        card_ver.append(9)

                        pygame.draw.circle(screen,(200,200,200),(520,395),7)

                    elif draw==10:

                        card_ver.append(10)

                        pygame.draw.rect(screen,(200,200,200),(520,395,15,15))

                    elif draw==11:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(0,50,10),(520,395),7)

                    elif draw==12:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(0,50,10),(520,395,15,15))

                    elif draw==13:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,100,0),(520,395),7)

                    elif draw==14:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,100,0),(520,395,15,15))

                    elif draw==15:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,100,100),(520,395,15,15))

                    elif draw==16:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(100,100,100),(520,395),7)

                    elif draw==17:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,20,200),(520,395,15,15))

                    elif draw==18:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(100,20,200),(520,395),7)
                        

                    pygame.display.flip()

                if card4x4.collidepoint(pos) and 22 not in turned_card and 22 not in removed_card:

                    turned_card.append(22)

                    screen.fill((0,0,20),card4x4)

                    card4x4 = pygame.draw.rect(screen,(124,252,0), (560, 350, 60, 90),1)

                    draw = shapes[21]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(590,395,15,15))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(590,395,15,15))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(590,395),7)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(590,395),7)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(590,395,15,15))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(590,395),7)

                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(590,395),7)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(590,395,15,15))

                    elif draw==9:

                        card_ver.append(9)

                        pygame.draw.circle(screen,(200,200,200),(590,395),7)

                    elif draw==10:

                        card_ver.append(10)

                        pygame.draw.rect(screen,(200,200,200),(590,395,15,15))

                    elif draw==11:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(0,50,10),(590,395),7)

                    elif draw==12:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(0,50,10),(590,395,15,15))

                    elif draw==13:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,100,0),(590,395),7)

                    elif draw==14:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,100,0),(590,395,15,15))
                        
                    elif draw==15:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,100,100),(590,395,15,15))

                    elif draw==16:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(100,100,100),(590,395),7)

                    elif draw==17:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,20,200),(590,395,15,15))
                        
                    elif draw==18:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(100,20,200),(590,395),7)
                        

                    pygame.display.flip()

                if card5x4.collidepoint(pos) and 23 not in turned_card and 23 not in removed_card:

                    turned_card.append(23)

                    screen.fill((0,0,20),card5x4)

                    card5x4 = pygame.draw.rect(screen,(124,252,0), (630, 350, 60, 90),1)

                    draw = shapes[22]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(660,395,15,15))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(660,395,15,15))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(660,395),7)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(660,395),7)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(660,395,15,15))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(660,395),7)

                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(660,395),7)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(660,395,15,15))

                    elif draw==9:

                        card_ver.append(9)

                        pygame.draw.circle(screen,(200,200,200),(660,395),7)

                    elif draw==10:

                        card_ver.append(10)

                        pygame.draw.rect(screen,(200,200,200),(660,395,15,15))

                    elif draw==11:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(0,50,10),(660,395),7)

                    elif draw==12:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(0,50,10),(660,395,15,15))

                    elif draw==13:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,100,0),(660,395),7)

                    elif draw==14:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,100,0),(660,395,15,15))

                    elif draw==15:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,100,100),(660,395,15,15))

                    elif draw==16:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(100,100,100),(660,395),7)

                    elif draw==17:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,20,200),(660,395,15,15))

                    elif draw==18:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(100,20,200),(660,395),7)
                        

                    pygame.display.flip()

                if card6x4.collidepoint(pos) and 24 not in turned_card and 24 not in removed_card:

                    turned_card.append(24)

                    screen.fill((0,0,20),card6x4)

                    card6x4 = pygame.draw.rect(screen,(124,252,0), (700, 350, 60, 90),1)

                    draw = shapes[23]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(730,395,15,15))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(730,395,15,15))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(730,395),7)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(730,395),7)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(730,395,15,15))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(730,395),7)

                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(730,395),7)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(730,395,15,15))

                    elif draw==9:

                        card_ver.append(9)

                        pygame.draw.circle(screen,(200,200,200),(730,395),7)

                    elif draw==10:

                        card_ver.append(10)

                        pygame.draw.rect(screen,(200,200,200),(730,395,15,15))

                    elif draw==11:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(0,50,10),(730,395),7)

                    elif draw==12:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(0,50,10),(730,395,15,15))

                    elif draw==13:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,100,0),(730,395),7)

                    elif draw==14:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,100,0),(730,395,15,15))

                    elif draw==15:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,100,100),(730,395,15,15))

                    elif draw==16:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(100,100,100),(730,395),7)

                    elif draw==17:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,20,200),(730,395,15,15))

                    elif draw==18:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(100,20,200),(730,395),7)
                        

                    pygame.display.flip()

                if card1x5.collidepoint(pos) and 25 not in turned_card and 25 not in removed_card:

                    turned_card.append(25)

                    screen.fill((0,0,20),card1x5)

                    card1x5 = pygame.draw.rect(screen,(124,252,0), (350, 450, 60, 90),1)

                    draw = shapes[24]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(380,495,15,15))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(380,495,15,15))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(380,495),7)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(380,495),7)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(380,495,15,15))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(380,495),7)

                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(380,495),7)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(380,495,15,15))

                    elif draw==9:

                        card_ver.append(9)

                        pygame.draw.circle(screen,(200,200,200),(380,495),7)

                    elif draw==10:

                        card_ver.append(10)

                        pygame.draw.rect(screen,(200,200,200),(380,495,15,15))

                    elif draw==11:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(0,50,10),(380,495),7)

                    elif draw==12:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(0,50,10),(380,495,15,15))

                    elif draw==13:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,100,0),(380,495),7)

                    elif draw==14:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,100,0),(380,495,15,15))

                    elif draw==15:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,100,100),(380,495,15,15))

                    elif draw==16:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(100,100,100),(380,495),7)

                    elif draw==17:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,20,200),(380,495,15,15))

                    elif draw==18:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(100,20,200),(380,495),7)
                        

                    pygame.display.flip()

                if card2x5.collidepoint(pos) and 26 not in turned_card and 26 not in removed_card:

                    turned_card.append(26)

                    screen.fill((0,0,20),card2x5)

                    card2x5 = pygame.draw.rect(screen,(124,252,0), (420, 450, 60, 90),1)

                    draw = shapes[25]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(450,495,15,15))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(450,495,15,15))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(450,495),7)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(450,495),7)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(450,495,15,15))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(450,495),7)

                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(450,495),7)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(450,495,15,15))

                    elif draw==9:

                        card_ver.append(9)

                        pygame.draw.circle(screen,(200,200,200),(450,495),7)

                    elif draw==10:

                        card_ver.append(10)

                        pygame.draw.rect(screen,(200,200,200),(450,495,15,15))

                    elif draw==11:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(0,50,10),(450,495),7)

                    elif draw==12:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(0,50,10),(450,495,15,15))

                    elif draw==13:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,100,0),(450,495),7)

                    elif draw==14:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,100,0),(450,495,15,15))

                    elif draw==15:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,100,100),(450,495,15,15))

                    elif draw==13:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(100,100,100),(450,495),7)

                    elif draw==14:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,20,200),(450,495,15,15))

                    elif draw==15:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(100,20,200),(450,495),7)
                        

                    pygame.display.flip()

                if card3x5.collidepoint(pos) and 27 not in turned_card and 27 not in removed_card:

                    turned_card.append(27)

                    screen.fill((0,0,20),card3x5)

                    card3x5 = pygame.draw.rect(screen,(124,252,0), (490, 450, 60, 90),1)

                    draw = shapes[26]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(520,495,15,15))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(520,495,15,15))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(520,495),7)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(520,495),7)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(520,495,15,15))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(520,495),7)

                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(520,495),7)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(520,495,15,15))

                    elif draw==9:

                        card_ver.append(9)

                        pygame.draw.circle(screen,(200,200,200),(520,495),7)

                    elif draw==10:

                        card_ver.append(10)

                        pygame.draw.rect(screen,(200,200,200),(520,495,15,15))

                    elif draw==11:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(0,50,10),(520,495),7)

                    elif draw==12:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(0,50,10),(520,495,15,15))

                    elif draw==13:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,100,0),(520,495),7)

                    elif draw==14:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,100,0),(520,495,15,15))

                    elif draw==15:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,100,100),(520,495,15,15))

                    elif draw==16:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(100,100,100),(520,495),7)

                    elif draw==17:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,20,200),(520,495,15,15))

                    elif draw==18:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(100,20,200),(520,495),7)
                        

                    pygame.display.flip()

                if card4x5.collidepoint(pos) and 28 not in turned_card and 28 not in removed_card:

                    turned_card.append(28)

                    screen.fill((0,0,20),card4x5)

                    card4x5 = pygame.draw.rect(screen,(124,252,0), (560, 450, 60, 90),1)

                    draw = shapes[27]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(590,495,15,15))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(590,495,15,15))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(590,495),7)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(590,495),7)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(590,495,15,15))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(590,495),7)

                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(590,495),7)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(590,495,15,15))

                    elif draw==9:

                        card_ver.append(9)

                        pygame.draw.circle(screen,(200,200,200),(590,495),7)

                    elif draw==10:

                        card_ver.append(10)

                        pygame.draw.rect(screen,(200,200,200),(590,495,15,15))

                    elif draw==11:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(0,50,10),(590,495),7)

                    elif draw==12:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(0,50,10),(590,495,15,15))

                    elif draw==13:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,100,0),(590,495),7)

                    elif draw==14:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,100,0),(590,495,15,15))

                    elif draw==15:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,100,100),(590,495,15,15))

                    elif draw==13:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(100,100,100),(590,495),7)

                    elif draw==14:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,20,200),(590,495,15,15))

                    elif draw==15:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(100,20,200),(590,495),7)
                        

                    pygame.display.flip()

                if card5x5.collidepoint(pos) and 29 not in turned_card and 29 not in removed_card:

                    turned_card.append(29)

                    screen.fill((0,0,20),card5x5)

                    card5x5 = pygame.draw.rect(screen,(124,252,0), (630, 450, 60, 90),1)

                    draw = shapes[28]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(660,495,15,15))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(660,495,15,15))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(660,495),7)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(660,495),7)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(660,495,15,15))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(660,495),7)

                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(660,495),7)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(660,495,15,15))

                    elif draw==9:

                        card_ver.append(9)

                        pygame.draw.circle(screen,(200,200,200),(660,495),7)

                    elif draw==10:

                        card_ver.append(10)

                        pygame.draw.rect(screen,(200,200,200),(660,495,15,15))

                    elif draw==11:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(0,50,10),(660,495),7)

                    elif draw==12:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(0,50,10),(660,495,15,15))

                    elif draw==13:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,100,0),(660,495),7)

                    elif draw==14:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,100,0),(660,495,15,15))

                    elif draw==15:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,100,100),(660,495,15,15))

                    elif draw==16:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(100,100,100),(660,495),7)

                    elif draw==17:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,20,200),(660,495,15,15))

                    elif draw==18:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(100,20,200),(660,495),7)
                        

                    pygame.display.flip()

                if card6x5.collidepoint(pos) and 30 not in turned_card and 30 not in removed_card:

                    turned_card.append(30)

                    screen.fill((0,0,20),card6x5)

                    card6x5 = pygame.draw.rect(screen,(124,252,0), (700, 450, 60, 90),1)

                    draw = shapes[29]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(730,495,15,15))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(730,495,15,15))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(730,495),7)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(730,495),7)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(730,495,15,15))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(730,495),7)

                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(730,495),7)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(730,495,15,15))

                    elif draw==9:

                        card_ver.append(9)

                        pygame.draw.circle(screen,(200,200,200),(730,495),7)

                    elif draw==10:

                        card_ver.append(10)

                        pygame.draw.rect(screen,(200,200,200),(730,495,15,15))

                    elif draw==11:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(0,50,10),(730,495),7)

                    elif draw==12:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(0,50,10),(730,495,15,15))

                    elif draw==13:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,100,0),(730,495),7)

                    elif draw==14:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,100,0),(730,495,15,15))

                    elif draw==15:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,100,100),(730,495,15,15))

                    elif draw==16:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(100,100,100),(730,495),7)

                    elif draw==17:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,20,200),(730,495,15,15))

                    elif draw==18:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(100,20,200),(730,495),7)
                        

                    pygame.display.flip()
                
                if card1x6.collidepoint(pos) and 31 not in turned_card and 31 not in removed_card:

                    turned_card.append(31)

                    screen.fill((0,0,20),card1x6)

                    card1x6 = pygame.draw.rect(screen,(124,252,0), (350, 550, 60, 90),1)

                    draw = shapes[30]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(380,595,15,15))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(380,595,15,15))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(380,595),7)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(380,595),7)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(380,595,15,15))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(380,595),7)

                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(380,595),7)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(380,595,15,15))

                    elif draw==9:

                        card_ver.append(9)

                        pygame.draw.circle(screen,(200,200,200),(380,595),7)

                    elif draw==10:

                        card_ver.append(10)

                        pygame.draw.rect(screen,(200,200,200),(380,595,15,15))

                    elif draw==11:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(0,50,10),(380,595),7)

                    elif draw==12:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(0,50,10),(380,595,15,15))

                    elif draw==13:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,100,0),(380,595),7)

                    elif draw==14:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,100,0),(380,595,15,15))

                    elif draw==15:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,100,100),(380,595,15,15))

                    elif draw==16:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(100,100,100),(380,595),7)

                    elif draw==17:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,20,200),(380,595,15,15))

                    elif draw==18:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(100,20,200),(380,595),7)
                        

                    pygame.display.flip()

                if card2x6.collidepoint(pos) and 32 not in turned_card and 32 not in removed_card:

                    turned_card.append(32)

                    screen.fill((0,0,20),card2x6)

                    card2x6 = pygame.draw.rect(screen,(124,252,0), (420, 550, 60, 90),1)

                    draw = shapes[31]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(450,595,15,15))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(450,595,15,15))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(450,595),7)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(450,595),7)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(450,595,15,15))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(450,595),7)

                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(450,595),7)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(450,595,15,15))

                    elif draw==9:

                        card_ver.append(9)

                        pygame.draw.circle(screen,(200,200,200),(450,595),7)

                    elif draw==10:

                        card_ver.append(10)

                        pygame.draw.rect(screen,(200,200,200),(450,595,15,15))

                    elif draw==11:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(0,50,10),(450,595),7)

                    elif draw==12:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(0,50,10),(450,595,15,15))

                    elif draw==13:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,100,0),(450,595),7)

                    elif draw==14:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,100,0),(450,595,15,15))

                    elif draw==15:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,100,100),(450,595,15,15))

                    elif draw==16:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(100,100,100),(450,595),7)

                    elif draw==17:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,20,200),(450,595,15,15))

                    elif draw==18:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(100,20,200),(450,595),7)
                        

                    pygame.display.flip()

                if card3x6.collidepoint(pos) and 33 not in turned_card and 33 not in removed_card:

                    turned_card.append(33)

                    screen.fill((0,0,20),card3x6)

                    card3x6 = pygame.draw.rect(screen,(124,252,0), (490, 550, 60, 90),1)

                    draw = shapes[32]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(520,595,15,15))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(520,595,15,15))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(520,595),7)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(520,595),7)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(520,595,15,15))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(520,595),7)

                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(520,595),7)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(520,595,15,15))

                    elif draw==9:

                        card_ver.append(9)

                        pygame.draw.circle(screen,(200,200,200),(520,595),7)

                    elif draw==10:

                        card_ver.append(10)

                        pygame.draw.rect(screen,(200,200,200),(520,595,15,15))

                    elif draw==11:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(0,50,10),(520,595),7)

                    elif draw==12:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(0,50,10),(520,595,15,15))

                    elif draw==13:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,100,0),(520,595),7)

                    elif draw==14:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,100,0),(520,595,15,15))

                    elif draw==15:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,100,100),(520,595,15,15))

                    elif draw==16:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(100,100,100),(520,595),7)

                    elif draw==17:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,20,200),(520,595,15,15))

                    elif draw==18:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(100,20,200),(520,595),7)
                        

                    pygame.display.flip()

                if card4x6.collidepoint(pos) and 34 not in turned_card and 34 not in removed_card:

                    turned_card.append(34)

                    screen.fill((0,0,20),card4x6)

                    card4x6 = pygame.draw.rect(screen,(124,252,0), (560, 550, 60, 90),1)

                    draw = shapes[33]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(590,595,15,15))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(590,595,15,15))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(590,595),7)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(590,595),7)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(590,595,15,15))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(590,595),7)

                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(590,595),7)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(590,595,15,15))

                    elif draw==9:

                        card_ver.append(9)

                        pygame.draw.circle(screen,(200,200,200),(590,595),7)

                    elif draw==10:

                        card_ver.append(10)

                        pygame.draw.rect(screen,(200,200,200),(590,595,15,15))

                    elif draw==11:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(0,50,10),(590,595),7)

                    elif draw==12:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(0,50,10),(590,595,15,15))

                    elif draw==13:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,100,0),(590,595),7)

                    elif draw==14:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,100,0),(590,595,15,15))

                    elif draw==15:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,100,100),(590,595,15,15))

                    elif draw==16:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(100,100,100),(590,595),7)

                    elif draw==17:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,20,200),(590,595,15,15))

                    elif draw==18:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(100,20,200),(590,595),7)
                        

                    pygame.display.flip()

                if card5x6.collidepoint(pos) and 35 not in turned_card and 35 not in removed_card:

                    turned_card.append(35)

                    screen.fill((0,0,20),card5x6)

                    card5x6 = pygame.draw.rect(screen,(124,252,0), (630, 550, 60, 90),1)

                    draw = shapes[34]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(660,595,15,15))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(660,595,15,15))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(660,595),7)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(660,595),7)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(660,595,15,15))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(660,595),7)

                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(660,595),7)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(660,595,15,15))

                    elif draw==9:

                        card_ver.append(9)

                        pygame.draw.circle(screen,(200,200,200),(660,595),7)

                    elif draw==10:

                        card_ver.append(10)

                        pygame.draw.rect(screen,(200,200,200),(660,595,15,15))

                    elif draw==11:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(0,50,10),(660,595),7)

                    elif draw==12:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(0,50,10),(660,595,15,15))

                    elif draw==13:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,100,0),(660,595),7)

                    elif draw==14:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,100,0),(660,595,15,15))

                    elif draw==15:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,100,100),(660,595,15,15))

                    elif draw==16:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(100,100,100),(660,595),7)

                    elif draw==17:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,20,200),(660,595,15,15))

                    elif draw==18:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(100,20,200),(660,595),7)
                        

                    pygame.display.flip()

                if card6x6.collidepoint(pos) and 36 not in turned_card and 36 not in removed_card:

                    turned_card.append(36)

                    screen.fill((0,0,20),card6x6)

                    card6x6 = pygame.draw.rect(screen,(124,252,0), (700, 550, 60, 90),1)

                    draw = shapes[35]

                    if draw==1:

                        card_ver.append(1)

                        pygame.draw.rect(screen,(200,0,0),(730,595,15,15))
                                    
                    elif draw==2:

                        card_ver.append(2)

                        pygame.draw.rect(screen,(0,200,0),(730,595,15,15))

                    elif draw==3:

                        card_ver.append(3)

                        pygame.draw.circle(screen,(200,0,0),(730,595),7)

                    elif draw==4:

                        card_ver.append(4)

                        pygame.draw.circle(screen,(0,200,0),(730,595),7)

                    elif draw==5:

                        card_ver.append(5)

                        pygame.draw.rect(screen,(0,0,200),(730,595,15,15))
                    
                    elif draw==6:

                        card_ver.append(6)

                        pygame.draw.circle(screen,(0,0,200),(730,595),7)

                    elif draw==7:

                        card_ver.append(7)

                        pygame.draw.circle(screen,(0,200,200),(730,595),7)

                    elif draw==8:

                        card_ver.append(8)

                        pygame.draw.rect(screen,(0,200,200),(730,595,15,15))

                    elif draw==9:

                        card_ver.append(9)

                        pygame.draw.circle(screen,(200,200,200),(730,595),7)

                    elif draw==10:

                        card_ver.append(10)

                        pygame.draw.rect(screen,(200,200,200),(730,595,15,15))

                    elif draw==11:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(0,50,10),(730,595),7)

                    elif draw==12:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(0,50,10),(730,595,15,15))

                    elif draw==13:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(200,100,0),(730,595),7)

                    elif draw==14:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(200,100,0),(730,595,15,15))

                    elif draw==15:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,100,100),(730,595,15,15))

                    elif draw==16:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(100,100,100),(730,595),7)

                    elif draw==17:

                        card_ver.append(draw)

                        pygame.draw.rect(screen,(100,20,200),(730,595,15,15))

                    elif draw==18:

                        card_ver.append(draw)

                        pygame.draw.circle(screen,(100,20,200),(730,595),7)
                        

                    pygame.display.flip()

                if len(turned_card)==2:

                    pygame.time.wait(1000)

                    if card_ver[0]==card_ver[1]:

                        score+=100

                        pygame.draw.rect(screen,(0,0,20),(0,0,100,100))
                        
                        score_display = my_font.render_to(screen, (10, 10), "Score: " + str(score), (255, 255, 0))

                        pygame.display.flip()

                        removed_card.append(turned_card[0])
                        removed_card.append(turned_card[1])

                        win+=2 
                    
                        for i in turned_card:

                            if i==1:
                                
                                screen.fill((0,0,20),card1x1)

                            if i==2:

                                screen.fill((0,0,20),card2x1)


                            if i==3:
                                
                                screen.fill((0,0,20),card3x1)

                            if i==4:

                                screen.fill((0,0,20),card4x1)

                            if i==5:
                                
                                screen.fill((0,0,20),card5x1)

                            if i==6:
                                
                                screen.fill((0,0,20),card6x1)
                                
                            if i==7:

                                screen.fill((0,0,20),card1x2)
                                
                            if i==8:

                                screen.fill((0,0,20),card2x2)

                            if i==9:

                                screen.fill((0,0,20),card3x2)

                            if i==10:

                                screen.fill((0,0,20),card4x2)
                            
                            if i==11:
                                
                                screen.fill((0,0,20),card5x2)

                            if i==12:
                                
                                screen.fill((0,0,20),card6x2)
                                
                            if i==13:

                                screen.fill((0,0,20),card1x3)
                                
                            if i==14:

                                screen.fill((0,0,20),card2x3)
                                
                            if i==15:

                                screen.fill((0,0,20),card3x3)
                                
                            if i==16:

                                screen.fill((0,0,20),card4x3)
                            
                            if i==17:
                                
                                screen.fill((0,0,20),card5x3)

                            if i==18:
                                
                                screen.fill((0,0,20),card6x3)
                            
                            if i==19:

                                screen.fill((0,0,20),card1x4)
                                
                            if i==20:

                                screen.fill((0,0,20),card2x4)
                                
                            if i==21:

                                screen.fill((0,0,20),card3x4)
                                
                            if i==22:

                                screen.fill((0,0,20),card4x4)
                            
                            if i==23:
                                
                                screen.fill((0,0,20),card5x4)

                            if i==24:
                                
                                screen.fill((0,0,20),card6x4)
                            
                            if i==25:

                                screen.fill((0,0,20),card1x5)
                                
                            if i==26:

                                screen.fill((0,0,20),card2x5)
                                
                            if i==27:

                                screen.fill((0,0,20),card3x5)
                                
                            if i==28:

                                screen.fill((0,0,20),card4x5)
                            
                            if i==29:
                                
                                screen.fill((0,0,20),card5x5)

                            if i==30:
                                
                                screen.fill((0,0,20),card6x5)

                            if i==31:

                                screen.fill((0,0,20),card1x6)
                                
                            if i==32:

                                screen.fill((0,0,20),card2x6)
                                
                            if i==33:

                                screen.fill((0,0,20),card3x6)
                                
                            if i==34:

                                screen.fill((0,0,20),card4x6)
                            
                            if i==35:
                                
                                screen.fill((0,0,20),card5x6)

                            if i==36:
                                
                                screen.fill((0,0,20),card6x6)

                    else:

                        for i in turned_card:

                            if i==1:

                                penalty1x1+=20

                                score=score-penalty1x1
                                
                                card1x1 = pygame.draw.rect(screen,(124,252,0), (350, 50, 60, 90),0)

                            if i==2:

                                penalty2x1+=20

                                score=score-penalty2x1
                                
                                card2x1 = pygame.draw.rect(screen,(124,252,0), (420, 50, 60, 90),0)

                            if i==3:

                                penalty3x1+=20

                                score=score-penalty3x1
                                
                                card3x1 = pygame.draw.rect(screen,(124,252,0), (490, 50, 60, 90),0)

                            if i==4:

                                penalty4x1+=20

                                score=score-penalty4x1

                                card4x1 = pygame.draw.rect(screen,(124,252,0), (560, 50, 60, 90),0)

                            
                            if i==5:

                                penalty5x1+=20

                                score=score-penalty5x1

                                card5x1 = pygame.draw.rect(screen,(124,252,0), (630, 50, 60, 90),0)

                            if i==6:

                                penalty6x1+=20

                                score=score-penalty6x1

                                card6x1 = pygame.draw.rect(screen,(124,252,0), (700, 50, 60, 90),0)
                                
                            if i==7:

                                penalty1x2+=20

                                score=score-penalty1x2

                                card1x2 = pygame.draw.rect(screen,(124,252,0), (350, 150, 60, 90),0)
                                
                            if i==8:

                                penalty2x2+=20

                                score=score-penalty2x2

                                card2x2 = pygame.draw.rect(screen,(124,252,0), (420, 150, 60, 90),0)

                            if i==9:

                                penalty3x2+=20

                                score=score-penalty3x2

                                card3x2 = pygame.draw.rect(screen,(124,252,0), (490, 150, 60, 90),0)

                            if i==10:

                                penalty4x2+=20

                                score=score-penalty4x2

                                card4x2 = pygame.draw.rect(screen,(124,252,0), (560, 150, 60, 90),0)
                                
                            if i==11:

                                penalty5x2+=20

                                score=score-penalty5x2

                                card5x2 = pygame.draw.rect(screen,(124,252,0), (630, 150, 60, 90),0)

                            if i==12:

                                penalty6x2+=20

                                score=score-penalty6x2

                                card6x2 = pygame.draw.rect(screen,(124,252,0), (700, 150, 60, 90),0)

                            if i==13:

                                penalty1x3+=20

                                score=score-penalty1x3

                                card1x3 = pygame.draw.rect(screen,(124,252,0), (350, 250, 60, 90),0)
                                
                            if i==14:

                                penalty2x3+=20

                                score=score-penalty2x3

                                card2x3 = pygame.draw.rect(screen,(124,252,0), (420, 250, 60, 90),0)
                                
                            if i==15:

                                penalty3x3+=20

                                score=score-penalty3x3

                                card3x3 = pygame.draw.rect(screen,(124,252,0), (490, 250, 60, 90),0)

                                
                            if i==16:

                                penalty4x3+=20

                                score=score-penalty4x3

                                card4x3 = pygame.draw.rect(screen,(124,252,0), (560, 250, 60, 90),0)
                            
                            if i==17:

                                penalty5x3+=20

                                score=score-penalty5x3

                                card5x3 = pygame.draw.rect(screen,(124,252,0), (630, 250, 60, 90),0)

                            if i==18:

                                penalty6x3+=20

                                score=score-penalty6x3

                                card6x3 = pygame.draw.rect(screen,(124,252,0), (700, 250, 60, 90),0)

                            if i==19:

                                penalty1x4+=20

                                score=score-penalty1x4

                                card1x4 = pygame.draw.rect(screen,(124,252,0), (350, 350, 60, 90),0)
                                     
                            if i==20:

                                penalty2x4+=20

                                score=score-penalty2x4

                                card2x4 = pygame.draw.rect(screen,(124,252,0), (420, 350, 60, 90),0)
                                
                            if i==21:

                                penalty3x4+=20

                                score=score-penalty3x4

                                card3x4 = pygame.draw.rect(screen,(124,252,0), (490, 350, 60, 90),0)
                                
                            if i==22:

                                penalty4x4+=20

                                score=score-penalty4x4

                                card4x4 = pygame.draw.rect(screen,(124,252,0), (560, 350, 60, 90),0)

                            if i==23:

                                penalty5x4+=20

                                score=score-penalty5x4

                                card5x4 = pygame.draw.rect(screen,(124,252,0), (630, 350, 60, 90),0)

                            if i==24:

                                penalty6x4+=20

                                score=score-penalty6x4

                                card6x4 = pygame.draw.rect(screen,(124,252,0), (700, 350, 60, 90),0)

                            if i==25:

                                penalty1x5+=20

                                score=score-penalty1x5

                                card1x5 = pygame.draw.rect(screen,(124,252,0), (350, 450, 60, 90),0)
                                     
                            if i==26:

                                penalty2x5+=20

                                score=score-penalty2x5

                                card2x5 = pygame.draw.rect(screen,(124,252,0), (420, 450, 60, 90),0)
                                
                            if i==27:

                                penalty3x5+=20

                                score=score-penalty3x5

                                card3x5 = pygame.draw.rect(screen,(124,252,0), (490, 450, 60, 90),0)
                                
                            if i==28:

                                penalty4x5+=20

                                score=score-penalty4x5

                                card4x5 = pygame.draw.rect(screen,(124,252,0), (560, 450, 60, 90),0)

                            if i==29:

                                penalty5x5+=20

                                score=score-penalty5x5

                                card5x5 = pygame.draw.rect(screen,(124,252,0), (630, 450, 60, 90),0)
                                
                            if i==30:

                                penalty6x5+=20

                                score=score-penalty6x5

                                card6x5 = pygame.draw.rect(screen,(124,252,0), (700, 450, 60, 90),0)

                            if i==31:

                                penalty1x6+=20

                                score=score-penalty1x6

                                card1x6 = pygame.draw.rect(screen,(124,252,0), (350, 550, 60, 90),0)
                                     
                            if i==32:

                                penalty2x6+=20

                                score=score-penalty2x6

                                card2x6 = pygame.draw.rect(screen,(124,252,0), (420, 550, 60, 90),0)
                                
                            if i==33:

                                penalty3x6+=20

                                score=score-penalty3x6

                                card3x6 = pygame.draw.rect(screen,(124,252,0), (490, 550, 60, 90),0)
                                
                            if i==34:

                                penalty4x6+=20

                                score=score-penalty4x6

                                card4x6 = pygame.draw.rect(screen,(124,252,0), (560, 550, 60, 90),0)

                            if i==35:

                                penalty5x6+=20

                                score=score-penalty5x6

                                card5x6 = pygame.draw.rect(screen,(124,252,0), (630, 550, 60, 90),0)
                                
                            if i==36:

                                penalty6x6+=20

                                score=score-penalty6x6

                                card6x6 = pygame.draw.rect(screen,(124,252,0), (700, 550, 60, 90),0)
                                

                    turned_card=[]

                    card_ver=[]

                    pygame.draw.rect(screen,(0,0,20),(0,0,200,200))

                    if score<0:

                        score = 0
                        
                    score_display = my_font.render_to(screen, (10, 10), "Score: " + str(score), (255, 255, 0))

                
                    pygame.display.flip()

                    if win==36:
                        
                        my_font.render_to(screen, (540, 360), "CONGRATULATIONS, YOU WON!", (255, 255, 0))

                        pygame.display.flip()
#Esta função gera n números entre 1 e n+1, duplica-os e baralha-os
#Cada número está associado a uma forma e cada posição da lista retornada pela função está associada a uma carta
def shapes_pos(n):

    lista= list(range(1,n+1))

    lista.extend(lista)

    random.shuffle(lista)

    return lista 

main()

    





