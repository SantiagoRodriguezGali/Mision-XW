import pygame
import sys
import random

# Inicializa Pygame
pygame.init()

#Sonidos
explosion_sonido = pygame.mixer.Sound("explosion.wav")
sonido_disparo_jug = pygame.mixer.Sound("laser_jugador.mp3")
sonido_disparo_jefe = pygame.mixer.Sound("laser_jefe.mp3")
sonido_victoria = pygame.mixer.Sound("victoria.mp3")
pygame.mixer.music.load("mfondo.mp3")  
pygame.mixer.music.set_volume(0.5)         
pygame.mixer.music.play(-1)

# Tamaño, fondo y título de la pantalla
ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
fondo = pygame.image.load("universo.jpg").convert()
fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))
pygame.display.set_caption("🚀 Esquiva los Meteoritos")

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
AZUL = (0, 100, 255)

# Reloj
clock = pygame.time.Clock()

# Jugador
imagen_jugador = pygame.image.load("Nave.png").convert_alpha()
imagen_jugador = pygame.transform.scale(imagen_jugador, (50, 50))
jugador = pygame.Rect(375, 500, 50, 50)
vel_jugador = 7
disparos = []
vel_disparo = 8

# Enemigos (meteoritos)
meteorito_img = pygame.image.load("Meteoro.png").convert_alpha()
meteorito_img = pygame.transform.scale(meteorito_img, (40, 40))
meteoritos = []
vel_meteorito = 5
nuevo_meteorito_evento = pygame.USEREVENT + 1
pygame.time.set_timer(nuevo_meteorito_evento, 900)


# Puntaje
puntaje = 0
fuente = pygame.font.SysFont(None, 36)

# Estado del juego
en_menu = True
jugando = True
en_fin = False

#Jefe Final
disparo_jefe_evento = pygame.USEREVENT + 2
pygame.time.set_timer(disparo_jefe_evento, 1200)
imagen_jefe = pygame.image.load("Jefe.png").convert_alpha()
imagen_jefe = pygame.transform.scale(imagen_jefe, (200, 100))
modo_jefe = False
jefe = pygame.Rect(300, -100, 200, 100)
vida_jefe = 10
vel_jefe = 1
dir_jefe = 1
disparos_jefe = []
vel_disparo_jefe = 10
mostrar_aviso_jefe = False

# Funciones personalizadas
def dibujar_menu():
    pantalla.fill(NEGRO)
    titulo = fuente.render("Presiona ESPACIO para comenzar", True, BLANCO)
    pantalla.blit(titulo, (ANCHO//2 - titulo.get_width()//2, ALTO//2 - 50))
    subtitulo = fuente.render("Muévete con las flechas hacia la izquierda y la derecha", True, BLANCO)
    pantalla.blit(subtitulo, (ANCHO//2 -subtitulo.get_width()//2, ALTO//2))
    subtitulo2 = fuente.render("Esquiva los asteroides y protege la nave", True, BLANCO)
    pantalla.blit(subtitulo2, (ANCHO//2 -subtitulo2.get_width()//2, ALTO//2 + 50))
    pygame.display.flip()

def mover_jugador(teclas):
    if teclas[pygame.K_LEFT] and jugador.left > 0:
        jugador.x -= vel_jugador
    if teclas[pygame.K_RIGHT] and jugador.right < ANCHO:
        jugador.x += vel_jugador

def disparar(evento):
    if evento.key == pygame.K_SPACE and modo_jefe:
                disparo = pygame.Rect(jugador.centerx - 5, jugador.y, 10, 20)
                disparos.append(disparo)
                sonido_disparo_jug.play()


def trayecto_disparos():
    for d in disparos[:]:
        d.y -= vel_disparo
        if d.y < 0:
            disparos.remove(d)

def crear_meteorito():
    x = random.randint(0, ANCHO - 40)
    meteorito_rect = pygame.Rect(x, 0, 40, 40)  
    meteorito = {
        "rect": meteorito_rect,
        "angulo": random.randint(0, 360)
    }
    meteoritos.append(meteorito)

def mover_meteoritos():
    global puntaje
    for m in meteoritos[:]:
        m["rect"].y += vel_meteorito
        m["angulo"] += 5  

        if m["rect"].y > ALTO:
            meteoritos.remove(m)
            puntaje += 1

def disparar_jefe():
    disparo = pygame.Rect(jefe.centerx - 5, jefe.bottom, 10, 20)
    disparos_jefe.append(disparo)
    sonido_disparo_jefe.play()


def mover_disparos_jefe():
    for d in disparos_jefe[:]:
        d.y += vel_disparo_jefe
        if d.y > ALTO:
            disparos_jefe.remove(d)

def mover_jefe():
     global dir_jefe
     if jefe.y < 50:
        jefe.y += vel_jefe  
     else:
        jefe.x += vel_jefe * dir_jefe
        if jefe.left <= 0 or jefe.right >= ANCHO:
            dir_jefe *= -1

def detectar_golpes_jefe():
    global vida_jefe, modo_jefe, puntaje
    for d in disparos[:]:
        if jefe.colliderect(d):
            disparos.remove(d)
            puntaje += 10
            vida_jefe -= 1
            explosion_sonido.play()
            if vida_jefe <= 0:
                modo_jefe = False
                mostrar_victoria()

def mostrar_aviso_boss():
    pantalla.fill(NEGRO)
    aviso = fuente.render("¡Prepárate! Algo se aproxima...", True, BLANCO)
    pantalla.blit(aviso, (ANCHO//2 - aviso.get_width()//2, ALTO//2-50))
    aviso2 = fuente.render("Utiliza ESPACIO para disparar", True, BLANCO)
    pantalla.blit(aviso2, (ANCHO//2 - aviso.get_width()//2, ALTO//2))
    pygame.display.flip()

def mostrar_victoria():
    pygame.mixer.music.stop()
    sonido_victoria.play()
    pantalla.fill(AZUL)
    mensaje = fuente.render("¡GANASTE!", True, BLANCO)
    pantalla.blit(mensaje, (ANCHO // 2 - mensaje.get_width() // 2, ALTO // 2 - 50))
    reiniciar = fuente.render("Presiona ESPACIO para volver al menú", True, BLANCO)
    pantalla.blit(reiniciar, (ANCHO // 2 - reiniciar.get_width() // 2, ALTO // 2))
    texto = fuente.render(f"Puntaje: {puntaje}", True, BLANCO)
    pantalla.blit(texto, (ANCHO //2 -texto.get_width()//2, ALTO//2 + 50))
    pygame.display.flip()

    esperando = True
    while esperando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
                reiniciar_juego()
                esperando = False

def reiniciar_juego():
    global en_menu, vida_jefe, jefe, jugador, puntaje, disparos, vel_meteorito, intervalo
    pygame.mixer.music.play(-1)
    en_menu = True
    vida_jefe = 10
    jefe.y = -100
    jefe.x = 300
    jugador.x = 375
    puntaje = 0
    vel_meteorito = 5
    intervalo = 900
    pygame.time.set_timer(nuevo_meteorito_evento, intervalo) 
    disparos.clear()
    disparos_jefe.clear()

def detectar_colisiones():
    for m in meteoritos:
        if jugador.colliderect(m["rect"]):
            return True
    for d in disparos_jefe:
        if jugador.colliderect(d):
            return True
    return False

def dibujar_todo():
    pantalla.blit(fondo, (0, 0))
    pantalla.blit(imagen_jugador, jugador)
    for m in meteoritos:
        imagen_rotada = pygame.transform.rotate(meteorito_img, m["angulo"])
        nueva_pos = imagen_rotada.get_rect(center=m["rect"].center)
        pantalla.blit(imagen_rotada, nueva_pos)
    texto = fuente.render(f"Puntaje: {puntaje}", True, BLANCO)
    pantalla.blit(texto, (10, 10))
    for d in disparos:
        pygame.draw.rect(pantalla, AZUL, d)
    pantalla.blit(imagen_jefe, jefe)
    for d in disparos_jefe:
        pygame.draw.rect(pantalla, ROJO, d)
    pygame.display.flip()

def dibujar_Game_Over():
    pantalla.fill(ROJO)
    titulo = fuente.render("GAME OVER", True, BLANCO)
    pantalla.blit(titulo, (ANCHO//2 - titulo.get_width()//2, ALTO//2 - 50))
    subtitulo = fuente.render("Presiona ESPACIO para ir al menú",True,BLANCO)
    pantalla.blit(subtitulo,(ANCHO//2 - subtitulo.get_width()//2, ALTO//2))
    texto = fuente.render(f"Puntaje: {puntaje}", True, BLANCO)
    pantalla.blit(texto, (ANCHO //2 -texto.get_width()//2, ALTO//2 + 50))
    pygame.display.flip()

# Bucle del juego
while jugando:
    if en_menu:
        dibujar_menu()
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                jugando = False
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
                en_menu = False
    else:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                jugando = False
            if evento.type == nuevo_meteorito_evento and not modo_jefe:
                crear_meteorito()
            if evento.type == pygame.KEYDOWN:
                disparar(evento)
            if evento.type == disparo_jefe_evento and modo_jefe:
                disparar_jefe()

        teclas = pygame.key.get_pressed()
        mover_jugador(teclas)
        mover_meteoritos()
        

        if puntaje % 10 == 0 and puntaje > 0:
            vel_meteorito = 4 + puntaje // 10
            intervalo = max(100, 800 - puntaje * 10)
            pygame.time.set_timer(nuevo_meteorito_evento, intervalo)
        
        if puntaje >= 10 and not modo_jefe and not mostrar_aviso_jefe:
            mostrar_aviso_jefe = True

        if mostrar_aviso_jefe:
             mostrar_aviso_boss()
             pygame.time.delay(3000)  # espera 3 segundos
             mostrar_aviso_jefe = False
             modo_jefe = True
             meteoritos.clear()

        if modo_jefe:
            mover_jefe()
            mover_disparos_jefe()
            detectar_golpes_jefe()
            trayecto_disparos()

        if detectar_colisiones():
            pygame.mixer.music.stop()
            explosion_sonido.play()
            en_fin = True
            while en_fin:
                dibujar_Game_Over()
                for evento in pygame.event.get():
                    if evento.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
                        modo_jefe = False
                        en_fin = False
                        en_menu = True
            jugador.x = 375
            meteoritos.clear()
            puntaje = 0
            vida_jefe = 10
            jefe.y = -100
            jefe.x = 300
            disparos.clear()
            disparos_jefe.clear()
            vel_meteorito = 5
            intervalo = 800
            pygame.time.set_timer(nuevo_meteorito_evento, intervalo) 
            pygame.mixer.music.play(-1)
        
        
        dibujar_todo()
        clock.tick(60)

pygame.quit()
sys.exit()


