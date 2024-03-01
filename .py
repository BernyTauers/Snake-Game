import pygame, sys, random
from pygame.math import Vector2


#Son los bloques que forman la serpiente
class Serpiente:
    def __init__(self):
        self.body =  [ Vector2(10, 10), Vector2(9, 10), Vector2(8, 10)]
        self.direccion = Vector2(0, 1)
        self.bloqueN=False
        
        
        
    def dibuja_serpiente(self):
        for bloque in self.body:
            x_pos = int(bloque.x * tamanoCelda)
            y_pos = int(bloque.y * tamanoCelda)
            bloque_rectangulo = pygame.Rect(x_pos, y_pos, tamanoCelda, tamanoCelda)
            pygame.draw.rect(pantalla, (201, 112, 112), bloque_rectangulo)

    def mover_serpiente(self):
        if self.bloqueN == True:
            copia_cuerpo=self.body[:]
            copia_cuerpo.insert(0,copia_cuerpo[0]+self.direccion)
            self.body=copia_cuerpo[:]
            self.bloqueN== False
            
        
        else:
            copia_cuerpo = self.body[:-1]
            copia_cuerpo.insert(0,copia_cuerpo[0]+self.direccion)
            self.body = copia_cuerpo[:]
        
    def anadir_bloque(self):
        self.bloqueN =True
        
        
        
#Aqui se va a crear la fruta en una posicion aleatoria 
class Fruta:
    def __init__(self):
        self.random()
#Crear el rectangulo de la fruta
    def dibuja_fruta(self):
        frutaRectangulo = pygame.Rect(int(self.pos.x * tamanoCelda), int(self.pos.y * tamanoCelda), tamanoCelda, tamanoCelda)
        pygame.draw.rect(pantalla, (146, 160, 154), frutaRectangulo)

    def random(self):
        self.x = random.randint(0, numCelda-1)
        self.y = random.randint(0, numCelda-1 )
        self.pos = Vector2(self.x, self.y)

class Main:
    def __init__(self):
        self.serpiente = Serpiente()
        self.fruta = Fruta()

    def actualizar(self):
        self.serpiente.mover_serpiente()
        self.revisar_colision()
        self.perder()

    def dibujar_elementos(self):
        self.dibuja_pasto()
        self.fruta.dibuja_fruta()
        self.serpiente.dibuja_serpiente()
        self.dibuja_score()
        

    def revisar_colision(self):
        if self.fruta.pos == self.serpiente.body[0]:
            self.fruta.random()
            self.serpiente.anadir_bloque()
            
    def perder(self):
        if not 0 <= self.serpiente.body[0].x < numCelda or not 0 <= self.serpiente.body[0].y < numCelda:
            self.game_over()
            
        for bloque in self.serpiente.body[1:]:
            if bloque == self.serpiente.body[0]:
                self.game_over()
            
    def game_over(self):
        pygame.quit()
        sys.exit()
            
    def dibuja_pasto(self):
        colorP= (143,200,61)
        for fila in range (numCelda):
            if fila %2 == 0:
                for columna in range (numCelda):
                    if columna %2 == 0:
                        pasto_rect=pygame.Rect(columna*tamanoCelda,fila*tamanoCelda,tamanoCelda,tamanoCelda)
                        pygame.draw.rect(pantalla,colorP,pasto_rect)
            else:
                for columna in range (numCelda):
                    if columna %2!= 0:
                        pasto_rect=pygame.Rect(columna*tamanoCelda,fila*tamanoCelda,tamanoCelda,tamanoCelda)
                        pygame.draw.rect(pantalla,colorP,pasto_rect)
            
    def dibuja_score(self):
        textoScore=str(len(self.serpiente.body)-3)
        scorePlana=textoJuego.render(textoScore,True,(56,74,12))
        scorex=int(tamanoCelda*numCelda-60)
        scorey=int(tamanoCelda*numCelda-40)
        scoreRect=scorePlana.get_rect(center=(scorex,scorey))
        pantalla.blit(scorePlana,scoreRect)
        
        
            
#representa el inicio de pygame, sin esto nada va a funcionar
pygame.init()
tamanoCelda = 40
numCelda = 20


pantalla = pygame.display.set_mode((numCelda * tamanoCelda, numCelda * tamanoCelda))

#La variable reloj, me permite manipular el tiempo dentro del juego
reloj = pygame.time.Clock()
actPantalla = pygame.USEREVENT
pygame.time.set_timer(actPantalla, 150)
main_juego = Main()
textoJuego= pygame.font.Font(None,50)
while True:
    

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            

        if evento.type == actPantalla:
            main_juego.actualizar()

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_UP:
                if main_juego.serpiente.direccion.y!=1:
                    main_juego.serpiente.direccion = Vector2(0, -1)
            if evento.key == pygame.K_RIGHT:
                if main_juego.serpiente.direccion.x!=-1:
                    main_juego.serpiente.direccion = Vector2(1, 0)
            if evento.key == pygame.K_DOWN:
                if main_juego.serpiente.direccion.y!=-1:
                    main_juego.serpiente.direccion = Vector2(0, 1)
            if evento.key == pygame.K_LEFT:
                if main_juego.serpiente.direccion.x!=1:
                    main_juego.serpiente.direccion = Vector2(-1, 0)
                           

    pantalla.fill((180, 230, 75))
    main_juego.dibujar_elementos()
    
    
#Pygame display mostrara todos los dibujos de los
#elementos, en este caso de la serpiente y el mapa dentro
#de la pantalla definida anteriormente
    pygame.display.update()
    reloj.tick(144	)  
