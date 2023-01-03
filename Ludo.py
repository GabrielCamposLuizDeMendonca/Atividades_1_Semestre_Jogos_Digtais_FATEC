import pygame 
from pygame.locals import*

Black = (0, 0, 0)
Blue = (11, 63, 132)
Green = (0, 255, 0)
Orange = (246, 126, 34)
Pink = (235, 109, 95)
Red = (186, 12, 12)
Purple = (126, 33, 147)
White = (255, 255, 255)
CorFundo = (255, 255, 255)
largura = 600 #
altura = 600 #
TamAreaGraf = (largura, altura) #
xL = largura / 2 #
yA = altura / 2 #
TamQuadradoma = (240)
TamQuadradome = (160)
TamQuamen = (40)
Ret= (200)
meio = (300)
Raio = (20)
x = list([x*40 for x in range(16)])
y = list([y*40 for y in range(16)])
#x e y = [0, 40, 80, 120, 160, 200, 240, 280, 320, 360, 400, 440, 480, 520, 560, 600]
pygame.init()


tela = pygame.display.set_mode((TamAreaGraf))
pygame.display.set_caption("LUDO!!! Ei amigo!! porque não testa as teclas W, A, S, D?")
Frames = pygame.time.Clock() #
fim = False
while not fim:
    tela.fill(CorFundo)
    i = 0
    
    #caminhos
    pygame.draw.rect(tela, Blue, (x[1], y[6], TamQuamen, TamQuamen),0)
    pygame.draw.rect(tela, Blue, (x[1], y[7], Ret, TamQuamen), 0)
    pygame.draw.rect(tela, Purple, (x[6], y[13], TamQuamen, TamQuamen), 0)
    pygame.draw.rect(tela, Purple, (x[7], y[9], TamQuamen, Ret), 0)
    pygame.draw.rect(tela, Pink, (x[13], y[8], TamQuamen, TamQuamen), 0)
    pygame.draw.rect(tela, Pink, (x[9], y[7], Ret, TamQuamen), 0)
    pygame.draw.rect(tela, Orange, (x[8], y[1], TamQuamen, TamQuamen), 0)
    pygame.draw.rect(tela, Orange, (x[7], y[1], TamQuamen, Ret), 0)
    
    #linhas
    while i < 600:
        Inih = (0+i, 0)
        Fimh = (0+i, 600)
        pygame.draw.line(tela, Black, Inih, Fimh, 1)
        Iniv = (0, 0+i)
        Fimv = (600, 0+i)
        pygame.draw.line(tela, Black, Iniv, Fimv, 1)
        i += 40

    #Quadrado 1 sup.esq.
    pygame.draw.rect(tela, Blue , (x[0], y[0], TamQuadradoma, TamQuadradoma), 0)
    pygame.draw.rect(tela, Black , (x[0], y[0], TamQuadradoma, TamQuadradoma), 1)
    pygame.draw.rect(tela, White, (x[1], y[1], TamQuadradome, TamQuadradome), 0)
    pygame.draw.circle(tela, Blue, (x[2], y[2]), Raio, 0)
    pygame.draw.circle(tela, Black, (x[2], y[2]), Raio, 3)
    pygame.draw.circle(tela, Blue, (x[4], y[2]), Raio, 0)
    pygame.draw.circle(tela, Black, (x[4], y[2]), Raio, 3)
    pygame.draw.circle(tela, Blue, (x[2], y[4]), Raio, 0)
    pygame.draw.circle(tela, Black, (x[2], y[4]), Raio, 3)
    pygame.draw.circle(tela, Blue, (x[4], y[4]), Raio, 0)
    pygame.draw.circle(tela, Black, (x[4], y[4]), Raio, 3)
    
    
    
    #Quadrado 2 sup.dir.
    pygame.draw.rect(tela, Orange, (x[9],y[0], TamQuadradoma, TamQuadradoma) , 0)
    pygame.draw.rect(tela, Black, (x[9], y[0], TamQuadradoma, TamQuadradoma), 1)
    pygame.draw.rect(tela, White, (x[10], y[1], TamQuadradome, TamQuadradome), 0)
    pygame.draw.circle(tela, Orange, (x[11], y[2]), Raio, 0)
    pygame.draw.circle(tela, Black, (x[11], y[2]), Raio, 3)
    pygame.draw.circle(tela, Orange, (x[13], y[2]), Raio, 0)
    pygame.draw.circle(tela, Black, (x[13], y[2]), Raio, 3)
    pygame.draw.circle(tela, Orange, (x[11], y[4]), Raio, 0)
    pygame.draw.circle(tela, Black, (x[11], y[4]), Raio, 3)
    pygame.draw.circle(tela, Orange, (x[13], y[4]), Raio, 0)
    pygame.draw.circle(tela, Black, (x[13], y[4]), Raio, 3)



    #Quadrado 3 inf.esq.
    pygame.draw.rect(tela, Purple, (x[0], y[9], TamQuadradoma, TamQuadradoma), 0)
    pygame.draw.rect(tela, Black, (x[0], y[9], TamQuadradoma, TamQuadradoma), 1)
    pygame.draw.rect(tela, White, (x[1], y[10], TamQuadradome, TamQuadradome), 0)
    pygame.draw.circle(tela, Purple, (x[2], y[11]),Raio, 0)
    pygame.draw.circle(tela, Black, (x[2], y[11]), Raio, 3)
    pygame.draw.circle(tela, Purple, (x[2], y[13]), Raio, 0)
    pygame.draw.circle(tela, Black, (x[2], y[13]), Raio, 3)
    pygame.draw.circle(tela, Purple, (x[4], y[13]), Raio, 0)
    pygame.draw.circle(tela, Black, (x[4], y[13]), Raio, 3)
    pygame.draw.circle(tela, Purple, (x[4], y[11]),Raio, 0)
    pygame.draw.circle(tela, Black, (x[4], y[11]), Raio, 3)


    #Quadrado 4 inf.dir.
    pygame.draw.rect(tela, Pink, (x[9], y[9], TamQuadradoma, TamQuadradoma), 0)
    pygame.draw.rect(tela, Black, (x[9], y[9], TamQuadradoma, TamQuadradoma), 1)
    pygame.draw.rect(tela, White, (x[10], y[10], TamQuadradome, TamQuadradome), 0)
    pygame.draw.circle(tela, Pink, (x[11], y[11]), Raio, 0)
    pygame.draw.circle(tela, Black, (x[11], y[11]), Raio, 3)
    pygame.draw.circle(tela, Pink, (x[13], y[11]), Raio, 0)
    pygame.draw.circle(tela, Black, (x[13], y[11]), Raio, 3)
    pygame.draw.circle(tela, Pink, (x[13], y[13]), Raio, 0)
    pygame.draw.circle(tela, Black, (x[13], y[13]), Raio, 3)
    pygame.draw.circle(tela, Pink, (x[11], y[13]), Raio, 0)
    pygame.draw.circle(tela, Black, (x[11], y[13]), Raio, 3)

    #Quadrado do meio
    pygame.draw.polygon(tela, Blue,[(x[6],y[6]), (x[6], y[9]),(meio, meio)], 0)
    pygame.draw.polygon(tela, Black,[(x[6],y[6]), (x[6], y[9]),(meio, meio)], 1)
    pygame.draw.polygon(tela, Purple, [(x[6], y[9]),(x[9], y[9]),(meio, meio)], 0)
    pygame.draw.polygon(tela, Black, [(x[6], y[9]),(x[9], y[9]),(meio, meio)], 1)
    pygame.draw.polygon(tela, Pink, [(x[9], y[9]), (x[9], y[6]), (meio, meio)], 0)
    pygame.draw.polygon(tela, Black, [(x[9], y[9]), (x[9], y[6]), (meio, meio)], 1)
    pygame.draw.polygon(tela, Orange, [(x[9], y[6]), (x[6], y[6]), (meio, meio)], 0)
    pygame.draw.polygon(tela, Black, [(x[9], y[6]), (x[6], y[6]), (meio, meio)], 1)

    #borda
    pygame.draw.lines(tela, Green, True, [(x[0], y[0]), (x[0], y[15]), (x[15], y[15]), (x[15], y[0])], 7)   

    #animação da bolinha
    Frames.tick(30)
    CorFundo = ((255, 255, 255))                
    pygame.draw.circle(tela, Red, (xL, yA), Raio, 0)
    pygame.draw.circle(tela, Black, (xL, yA), Raio, 3)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_a:
                  xL = xL - TamQuamen                 
            if event.key == K_d:
                  xL = xL + TamQuamen                  
            if event.key == K_w:
                  yA = yA - TamQuamen                  
            if event.key == K_s:
                  yA = yA + TamQuamen
                  
        if event.type == QUIT:
            fim = True

pygame.display.quit()

print("Fim do programa")
