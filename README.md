# Acerca del juego
Misión XW es un juego que permite al usuario moverse de izquierda a derecha para que su nave no se choque con los meteoritos, y luego de un puntaje obtenido tiene acceso de jugar contra el jefe final que es un ovni que empieza a dispararle al usuario, este debe esquivar cada tiro y así mismo dispararle a la nave para ganar. En caso de chocar con un meteorito o ser disparado una vez, el usuario pierde. A continuación se muestra cómo se hizo el juego con Pygame:

![image](https://github.com/user-attachments/assets/d76f3adc-43bc-4624-9ffa-8ea15f676170)

Primero importamos Pygame para cargar la biblioteca de Pygame, también importamos sys para acceder a funciones del sistema, y random para generar números al azar. Ahora usamos pygame.init () para inicializar Pygame

![image](https://github.com/user-attachments/assets/8dd089cf-5d70-476a-a75f-36161e99ac00)

Ahora se muestran los sonidos que se usarán en el juego, usamos pygame.mixer.Sound() para cargar el sonido. Usamos pygame.mixer.music.load() para cargar la música de fondo, pygame.mixer.music.set_volume() para ajustar el volumen entre 0 y 1. Y pygame.mixer.music.play() para reproducir la música, usamos -1 para que no se detenga nunca.

![image](https://github.com/user-attachments/assets/e14d6624-12a5-476f-bf46-033c8f34bdaa)

Definimos un acho y alto para nuestra pantalla de juego y confirmamos esto con pygame.display.set_mode((ANCHO, ALTO)). Como queremos una imagen de fondo la cargamos y al esta tener fondo sin transparencia usamos pygame.image.load().convert(). Y para que este fondo tenga la escala de la pantalla de juego colocamos pygame.transform.scale(fondo, (ANCHO, ALTO)). Y cuando queremos cuando queremos cambiar el título de la pantalla usamos pygame.display.set_caption(). 

![image](https://github.com/user-attachments/assets/bdf07ffb-f0e6-4299-bbbf-e3f5ec2162bc)

Ingresamos los colores con sus comandos (a,b,c) y el reloj nos permitirá manejar la velocidad de juego.

![image](https://github.com/user-attachments/assets/8a47b0fc-1286-4ca8-b03b-9d5c34d570e7)

Ahora para hacer nuestro personaje principal que es la nave, importamos la imagen igual, pero al ser una imagén con fondo transparente usamos pygame.image.load().convert_alpha() y al igual que el fondo la ajustamos al tamaño que va a tener nuestro jugador. Pero también debemos crear a nuestro jugador y esto lo hacemos con pygame.Rect(375, 500, 50, 50) que nos dice que nuestro jugador empezará en la posición x=337, y=500 y su tamaño es de 50x50. La velocidad del jugador es 7 que es lo que se moverá hacia sus lados, los disparos = [] es una lista donde se guardarán los disparos que hagamos y se tiene la velocidad de disparo.

![image](https://github.com/user-attachments/assets/ba141480-2922-47a2-8249-041eb5155e78)

Hacemos lo mismo con los meteoritos, cargamos su imagen y la ajustamos al tamaño que queremos, la lista que contendrá a los meteoritos que se tiren y tendremos nuetsro propio evento llamado nuevo_meteorito_evento donde haremos que se tire uno cada cierto tiempo que es 900 (0,9 segundos), esto lo hacemos con pygame.time.set_timer(nuevo_meteorito_evento, 900)

![image](https://github.com/user-attachments/assets/0adc310d-0a4a-4112-97eb-7a16184ca433)

Emepzamos con un puntaje de 0 y la fuente que usaremos para los textos definida con pygame.font.SysFont(None, 36). Y el estado del juego es si estaremos en el menú, jugando o cuando perdemos, donde son verdaderas menos está última.

![image](https://github.com/user-attachments/assets/43155e44-d31b-4de6-bf73-070e82ae78cc)

Respecto al jefe final haremos que sus disparos sean un evento al igual que los meteoritos que se accionará cada 1,2 segundos. Cargamos su imagen y la ajustamos al tamaño que queremos que tenga, se tiene el modo_jefe falso ya que este hará parte de la parte final del juego, creamos al jefe con la posición que queremos y el tamaño que habíamos escogido. Colocamos la vida que este tendrá, su velocidad y la dirección que tendrá. Guardamos sus disparos en una lista por eso se debe crear esta y los disparos tendrán su velocidad. Vamos a mostrar un aviso justo antes de la batlla final pero después de un evento por eso lo mantenemos aún como falso 

![image](https://github.com/user-attachments/assets/12950106-8fb6-42b5-b28f-da7b92272cef)

Ahora empezamos con el bucle donde se mantiene mientras el estado de jugando sea verdadero con while jugando:, luego si el menú es verdadero entraremos en la función dibujar_menu() y entremos a un bucle donde por cada evento que se haga se ingresa al bucle con for evento in pygame.event.get():, y se tendrán dos condiciones, la primera si se sale del juego al darle x ya no se está en el modo jugando y sale del bucle principal, esto es con if evento.type == pygame.QUIT: y la segunda condición consta de si apretamos la tecla espacio el menu se vuelve falso y sale de este pequeño bucle

![image](https://github.com/user-attachments/assets/4fb35d05-cc49-4208-916f-bc3cf86deee8)

La función dibujar_menu() se hará para hacer el menú teniendo el fondo negro con pantalla.fill(NEGRO), ahora vamos a convertir texto en imagen con titulo = fuente.render("Presiona ESPACIO para comenzar", True, BLANCO) y colocamos ese texto con pantalla.blit(titulo, (ANCHO//2 - titulo.get_width()//2, ALTO//2 - 50)). De esta manera logramos ubicar el texto centrado y un poco más arriba de la pantalla del juego. Hacemos lo mismo con los demás textos modificando el alto para que no se sobrepongan entre ellos. Finalmente usamos  pygame.display.flip() para actualizar la pantalla de juego.

![image](https://github.com/user-attachments/assets/59271f58-339c-48cf-acce-3277e69e2230)


Continuando con el bucle del juego, suponemos ahora que en_menu es falso. Entonces también vemos un bucle para los eventos que se hagan donde tenemos el que es dar click sobre la x de la pantalla para quitar el estado jugando, también tenemos el condicional de en caso de que se cree un nuevo evento que es el del meteorito y no estamos en el modo_jefe (if evento.type == nuevo_meteorito_evento and not modo_jefe) se hará la función de crear_meteorito(). También esta el de si tocamos una tecla (if evento.type == pygame.KEYDOWN:) vamos a disparar(evento), esto quiere decir que nos llevamos el evento a la función. Y también vemos la condición de si se va a ser el disparo del jefe estando en modo jefe (if evento.type == disparo_jefe_evento and modo_jefe:) lo que nos lleva a la función disparar_jefe().

![image](https://github.com/user-attachments/assets/16c27661-584f-4031-b047-193865048f92)

La función crear_meteorito() nos genera una posición de x que será un valor al azar con x = random.randint(0, ANCHO - 40). Vamos a crear el meteorito al igual que con el jugador y el jefe final solo que con la variable x, meteorito_rect = pygame.Rect(x, 0, 40, 40). Y como vamos a hacer que gire mientras sigue una rutas, usamos: meteorito = {"rect": meteorito_rect,"angulo": random.randint(0, 360)}. Y añadimos este meteorito a la lista con meteoritos.append(meteorito).

![image](https://github.com/user-attachments/assets/fbf5f65d-2b34-452d-b911-d046060138c8)

En la función disparar(evento) debemos tener en cuenta que estamos recibiendo un evento previo y lo que haremos es evaluar si este evento fue toca la barra espaciadora y si estamos en el modo jefe, esto generara un disparo, se añadirá a la lista de disparos, muy parecido a los meteroritos, solo que le daremos como origen de x donde se encuentra el jugador, la y es encima del jugado, y damos el tamaño que le queremos dar. Tener en cuenta que le restamos 5 ya que el ancho del disparo es 10, entonces se hace esto para centrarlo. Por último, reproducimos un sonido que hace con sonido_disparo_jug.play().

![image](https://github.com/user-attachments/assets/5953bdad-f94e-4d00-b5cd-f7e6dbc42030)

Hacemos algo muy parecido en disparar_jefe() y en disparar(evento) que es generar un disparo con las coordenadas del jefe final, ahora usamos jefe.bottom para que el disparo de este sea por debajo y se guarda en una lista con un sonido cada vez que se haga el disparo.

![image](https://github.com/user-attachments/assets/3336038b-ec54-4827-a4cc-3e0ef056a3d8)

Ahora, siguiendo el bucle del juego vamos a guardar la tecla que se presiona con teclas = pygame.key.get_pressed() y luego continuamos con la función mover_jugador(teclas) donde vemos que llevamos información que es la tecla que se oprime. Y luego se continua con la función mover_meteoritos().

![image](https://github.com/user-attachments/assets/d22c62e3-174d-407c-a524-99b83cf58c0f)

En la función mover_jugador(teclas) recibimos una información y preguntamos si es la flecha izquierda o derecha, además tenemos presente que no podemos salirnos de los límites de la pantalla por lo que se pone  if teclas[pygame.K_LEFT] and jugador.left > 0: para moverse a la izquierda o if teclas[pygame.K_RIGHT] and jugador.right < ANCHO: para moverse a la derecha.

![image](https://github.com/user-attachments/assets/e1701d0c-6c67-4888-a7ca-cc5feb64cfda)

Para la función de mover_meteoritos() tenemos en cuenta el úntaje ya que cada vez que un meteorito pasa sin chocarnos recibimos un punto por lo que modificamos a este con global puntaje ya que es una variable general, no local. Tenemos un bucle for m in meteoritos[:]:, donde usamos [:] para generar una copia de la lista que existe de meteoritos sin que ocurran posibles errores y acá decimos que el meteorito debe seguir un curso recto a su velocidad con m["rect"].y += vel_meteorito y va ir girando con m["angulo"] += 5. Y para sumar puntos y eliminar el meteorito que ya nos paso usamos: i
f m["rect"].y > ALTO:
     meteoritos.remove(m)
    puntaje += 1

![image](https://github.com/user-attachments/assets/c419c8e8-799b-409d-a0b3-6c17962e2a2c)
Ahora si seguimos con el bucle del juego, queremos añadir dificultad por lo que usamos el puntaje como guía para aumnetar este, decimos que si el puntaje es multiplo de 10 va a umentar la velocidad del meteorito y la velocidad de generación de estos en función del puntaje. Ahora si superamos un puntaje que en este ejemplo es 10, no estamos en el modo_jefe y no se ha mostrado el aviso del jefe, activamos este con mostrar_aviso_jefe = True. 

![image](https://github.com/user-attachments/assets/cefbbabb-a3c6-4ae5-8082-15016c0dea6c)

Como se activa el modo_jefe podemos entrar a este condicional donde vamos a una función mostrar_aviso_boss() y del resultado de esta la mantenemos por 3 segundos en pantalla con: pygame.time.delay(3000). Luego quitamos esto con, mostrar_aviso_jefe = False y activamos el modo_jefe. Por último eliminamos a los posibles meteoritos que se encuentren alrededor con meteoritos.clear().

![image](https://github.com/user-attachments/assets/baa2f3dd-d3b8-4a7b-a4bb-983941a9d921)

En mostrar_aviso_boss() realizamos algo similar al menú, con un fondo negro, pasar texto a imagen y pegandola en la pantalla de juego, para después actualizar la pantalla.

![image](https://github.com/user-attachments/assets/3b7984e2-bbab-4f0f-899d-6fc60779555b)

Cuando estamos en el modo_jefe entramos a diferentes funciones que se ven en la imagén y se irán explicando.

![image](https://github.com/user-attachments/assets/8fbf02d7-6890-4bbd-bc1c-1d9ed002e263)

Aquí vamos a hacer que se mueva el jefe y que cambie la dirección cada vez que llegue a un límite de la pantalla. Primero hacemos que baje y lo podamos observar hasta cierto punto en y. Y una vez este ahí este se mueve hacia un lado y cuando llegue a un límite se devuelve. 

![image](https://github.com/user-attachments/assets/df0f0fef-f1a8-4a4b-b0ef-9ba7da3ec616)

En mover_disparos_jefe() hacemos algo muy similar que los meteoritos para que se muevan de manera recta y eliminar los que se salgan de la pantalla. 

![image](https://github.com/user-attachments/assets/a3036acf-938c-476a-9bcd-9893bb552ea4)

En detectar_golpes_jefe vamos a mirar lo que pasa cuando le damos con un disparo al jefe. Y es que usamos igual el bucle con la lista de los disparos [:] y la condición es que pasa cuando choca el jefe con un disparo y usamos jefe.colliderect(d), cuando ocurre esto quitamos el disparo, sumammos un puntaje, reducimos la vida del jefe y hacemos un sonido de explosión. Pero si la vida del jefe llega a ser 0 nos vamos a una función llamada mostrar_victoria()

![image](https://github.com/user-attachments/assets/523d867c-ae55-4df0-a7ea-e408e54ca3e0)

En esta función de mostrar_victoria vamos a parar la música de fondo, colocar un sonido de victoria y hacer lo mismo que en el menú. Colocar un fondo de un color que esta vez es azul, pasar el texto a imagen, pegarlo en la pantalla y actualizar. Ahora, tenemos un modo de esperando que es para que la persona pueda disfrutar de su victoria y si quiere cerrar el juego le de a la x para salir de jugando o si quiere volver a jugar debe sarle a la barra espaciadora y aquí nos lleva a otra función que es reinicar_juego() y luego el modo esperando se elimina para dar paso al menú.

![image](https://github.com/user-attachments/assets/564aa3f8-f2b3-4529-aafb-53f988cd812e)

reiniciar_juego es una función que toma todos los valores globales y los restaura como al principio del juego donde se activa el menú precisamnete para empezar desde aquí.

![image](https://github.com/user-attachments/assets/e79da1fe-1765-4e6f-837b-74cbc2ec2c93)

En trayecto_disparo() hacemos lo mismo con los disparos del jugador que con los del jefe, que es darles una dirección recta y removerlos cuando salen de la pantalla.

![image](https://github.com/user-attachments/assets/571f1c63-c00b-4310-b691-e8198191bdec)

Vemos que iniciamos con la función de detectar_colisiones que si es verdadera para la música de fondo, hace un sonido de explosión, se activa en_fin y tenemos un bucle cuando este es verdadero que es para la función dibujar_Game_Over y hacer algo aprecido que cuando se ganaba, que es dar la opción de darle a x y salir de jugando o volver al menú si se toca la barra espaciadora, desactivando modo_jefe, en_fin y activa en_menu. Por último se reinician todos los valores y se limpia todo lo que había para preparar la siguiente partida.  

![image](https://github.com/user-attachments/assets/10c82b27-cd7c-4029-99ff-757eb647ec80)

En la función detectar_colisiones() lo que hacemos es mirar meteorito por meteorito si impacto al jugador con if jugador.colliderect(m["rect"]):, si es así devuelve verdadero. Lo mismo pasa con los disparos del jefe. En caso de que no ocurra nada de colisiones se devuelve falso

![image](https://github.com/user-attachments/assets/d0cb72a9-8993-440f-b00a-4a760b9e6242)

dinujar_Game_Over es parecida a la pantalla de victoria solo que esta es el de la derrota donde se sigue llenando un fondo de un color que ahora es rojo, se convierte texto en imagen y se pga a la pantalla, y finalizando con la actualización de esta pygame.display.flip()

![image](https://github.com/user-attachments/assets/7b9f9122-d315-4edf-b8cc-5f18c1b843b5)

La última parte del bucle del juego es una función de dibujar_todo(), un clock-tick(60) que nos indica que limita el juego a 60 fotogramas por segundo o 60 FPS. Pygame.quit() cierra los modulos de Pygame y sys.exit cierra el programa completamente. 

![image](https://github.com/user-attachments/assets/247301d9-e813-4b8f-8b94-eae2264b8146)

En esta función de dinujar_todo vamos a poner en la pantalla todo lo que hemos hecho. Primero un fonndo del universo en (0,0) para ubicar la imagen. Ponemos con  pantalla.blit(imagen_jugador, jugador) que la imagen del jugador se usa en donde se ubica el jugador. Se crea un bucle para cada meteorito para ir rotando a estos con imagen_rotada = pygame.transform.rotate(meteorito_img, m["angulo"]) y el ángulo que asignamos. Usamos nueva_pos = imagen_rotada.get_rect(center=m["rect"].center) para ir creando el nuevo rectángulo del meteorito, pero con el mismo centro del original. Y se pega esta imagen con pantalla.blit(imagen_rotada, nueva_pos). El puntaje es un texto que se vuelve imagen y se pega aunque va cambiando por ellos usamos fuente.render(f"Puntaje: {puntaje}", True, BLANCO). Y para los disparos del jugador y del jefe hacemos algo parecido que es pegar los disparos que se van generando. También ponemos la imagen del jefe al igual que la del jugador y actualizamos siempre.






