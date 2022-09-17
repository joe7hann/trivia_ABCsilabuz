#trivia
# Camino del Inka
# Las aventuras del CHASKI
#config
import random
import time
import os
#constantes
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

#variables
iniciar_trivia = True #
intentos = 0
puntaje = 0
#Bienvenida
print(CYAN+'█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█'+RESET)
print(CYAN+"█░░"+RESET,"  Bienvenido a ",CYAN+"░░█"+RESET)
print(CYAN+"█░░"+RESET,"  la trivia    ",CYAN+"░░█"+RESET)
print(CYAN+"█░░"+RESET,"CAMINO DEL INKA",CYAN+"░░█"+RESET)
print(CYAN+"█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█"+RESET)
time.sleep(2)

nombre = input(CYAN +"\nCual es tu nombre: "+RESET)

print(MAGENTA+"Hola",nombre,"\nEn este juego, eres un Viajero del tiempo y llegas a 1532, en la llegada de los espanoles a cajamarca. \nComo CHASKI tienes la responsabilidad de avisar a Cusco la llegada de los espanoles al Tahuantinsuyo."+RESET)


#SELECION DE NICKNAME

nicknames = {
        0: ['Illari','Amanecer'], #amanecer, fulgurante
        1: ['Sami','Venturoso'] ,#afortunada, venturoso
        2: ['Asiri','Sonriente'],#Sonriente
        3: ['Yuriana','Alborada'], #Alborada, aurora
        4: ['Nuna','Espiritu'], # Espiritu
    }

sobrenombre = random.randint(0,4)
#nicknames[str(random.randint(0,4))])
print(CYAN+"\nTu sobrenombre en quechua es:"+RESET, nicknames[sobrenombre][0])
print(CYAN+"Que en espanol significa:"+RESET, nicknames[sobrenombre][1])
time.sleep(5)
#
# Inicio Pregunta 1
while iniciar_trivia == True:
  print("\nLa Trivia comenzara en:")
  for x in range (5,0,-1):
    print(RED,x,RESET)
    time.sleep(1)
  time.sleep(1)
  os.system("cls" if os.name == "nt" else "clear")
  print(GREEN+"██╗░░░░░███████╗████████╗  ░██████╗░░█████╗░██╗\n██║░░░░░██╔════╝╚══██╔══╝  ██╔════╝░██╔══██╗██║\n██║░░░░░█████╗░░░░░██║░░░  ██║░░██╗░██║░░██║██║\n██║░░░░░██╔══╝░░░░░██║░░░  ██║░░╚██╗██║░░██║╚═╝\n███████╗███████╗░░░██║░░░  ╚██████╔╝╚█████╔╝██╗\n╚══════╝╚══════╝░░░╚═╝░░░  ░╚═════╝░░╚════╝░╚═╝"+RESET)
  time.sleep(1)
  os.system("cls" if os.name == "nt" else "clear")
  print(YELLOW+"Tu puntaje inicial es de:", puntaje,"puntos"+RESET)
  time.sleep(1)
  #pregunta1
  print(MAGENTA+"\n1) Cual es la capital historica de Peru?"+RESET)
  print(GREEN+"a.Arequipa")
  print("b.Lima")
  print("c.Cuzco")
  print("d.Caral"+RESET)

  for x in range(3,0,-1):
    print(RED,"Responde en:",x,RESET)
    time.sleep(1)
  t0 = time.time()
  respuesta_1 = input("\nIngresa tu respuesta: ")
  
  t1 = time.time()
  tf = round(t1-t0,2)#timepo final
  print ("Te demoraste", tf,"segundos, en responder la pregunta")
  
  while respuesta_1 not in ("a","b","c","d"):
    respuesta_1 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta:")
  
  # verificacion de respuesta
  if respuesta_1 == "c":
    puntaje+= 10 -tf
    print("Correcto,", nombre,"bien hecho!\n")
    print(YELLOW,"Tu puntaje es de:",puntaje,"puntos",RESET)
  else:
    print("Inconrrecto")
  time.sleep(3)
  os.system("cls" if os.name == "nt" else "clear")
  
  # Final Pregunta 1

    #pregunta2
  print(MAGENTA+"\n2) Cual es la montanha mas alta del Peru?"+RESET)
  print(GREEN+"a.Huascaran")
  print("b.Yerupaja")
  print("c.Coropuna")
  print("d.Nevado Auzangate"+RESET)

  for x in range(3,0,-1):
    print(RED,"Responde en:",x,RESET)
    time.sleep(1)
  t0 = time.time()
  respuesta_1 = input("\nIngresa tu respuesta: ")
  
  t1 = time.time()
  tf = round(t1-t0,2)#timepo final
  print ("Te demoraste", tf,"segundos, en responder la pregunta")
  
  while respuesta_1 not in ("a","b","c","d"):
    respuesta_1 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta:")
  
  # verificacion de respuesta
  if respuesta_1 == "a":
    puntaje+= 10 -tf
    print("Correcto,", nombre,"bien hecho!\n")
    print(YELLOW,"Tu puntaje es de:",puntaje,"puntos",RESET)
  else:
    print("Inconrrecto")
  time.sleep(3)
  os.system("cls" if os.name == "nt" else "clear")
  
  # Final Pregunta 2

    #pregunta3
  print(MAGENTA+"\n3) Quien? escribio la obra 'Los comentarios reales'?"+RESET)
  print(GREEN+"a.Mario Vargas Llosa")
  print("b.Inca Garcilazo de la Vega")
  print("c.Cesar Acunha")
  print("d.Friedrich Nietzsche"+RESET)

  for x in range(3,0,-1):
    print(RED,"Responde en:",x,RESET)
    time.sleep(1)
  t0 = time.time()
  respuesta_1 = input("\nIngresa tu respuesta: ")
  
  t1 = time.time()
  tf = round(t1-t0,2)#timepo final
  print ("Te demoraste", tf,"segundos, en responder la pregunta")
  
  while respuesta_1 not in ("a","b","c","d"):
    respuesta_1 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta:")
  
  # verificacion de respuesta
  if respuesta_1 == "b":
    puntaje+= 10 -tf
    print("Correcto,", nombre,"bien hecho!\n")
    print(YELLOW,"Tu puntaje es de:",puntaje,"puntos",RESET)
  else:
    print("Inconrrecto")
  time.sleep(3)
  os.system("cls" if os.name == "nt" else "clear")
  
  # Final Pregunta 3

    #pregunta4
  print(MAGENTA+"\n4) Cuantos anohs duro la guerra entre Peru y Chile?"+RESET)
  print(GREEN+"a.4")
  print("b.5")
  print("c.3")
  print("d.6"+RESET)

  for x in range(3,0,-1):
    print(RED,"Responde en:",x,RESET)
    time.sleep(1)
  t0 = time.time()
  respuesta_1 = input("\nIngresa tu respuesta: ")
  
  t1 = time.time()
  tf = round(t1-t0,2)#timepo final
  print ("Te demoraste", tf,"segundos, en responder la pregunta")
  
  while respuesta_1 not in ("a","b","c","d"):
    respuesta_1 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta:")
  
  # verificacion de respuesta
  if respuesta_1 == "a":
    puntaje+= 10 -tf
    print("Correcto,", nombre,"bien hecho!\n")
    print(YELLOW,"Tu puntaje es de:",puntaje,"puntos",RESET)
  else:
    print("Inconrrecto")
  time.sleep(3)
  os.system("cls" if os.name == "nt" else "clear")
  
  # Final Pregunta 4

    #pregunta5
  print(MAGENTA+"\n5) En que anho fue la Independencia del Peru?"+RESET)
  print(GREEN+"a.1822")
  print("b.1824")
  print("c.1823")
  print("d.1821"+RESET)

  for x in range(3,0,-1):
    print(RED,"Responde en:",x,RESET)
    time.sleep(1)
  t0 = time.time()
  respuesta_1 = input("\nIngresa tu respuesta: ")
  
  t1 = time.time()
  tf = round(t1-t0,2)#timepo final
  print ("Te demoraste", tf,"segundos, en responder la pregunta")
  
  while respuesta_1 not in ("a","b","c","d"):
    respuesta_1 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta:")
  
  # verificacion de respuesta
  if respuesta_1 == "d":
    puntaje+= 10 -tf
    print("Correcto,", nombre,"bien hecho!\n")
    print(YELLOW,"Tu puntaje es de:",puntaje,"puntos",RESET)
  else:
    print("Inconrrecto")
  time.sleep(3)
  os.system("cls" if os.name == "nt" else "clear")

  print(CYAN,"Puntaje Final obtenido:",puntaje,"puntos",RESET)
  time.sleep(3)
  # Final Pregunta 5
  print("\nDeseas intentar la trivia nuevamente?")
  repetir_trivia = input("Ingresa 'si' para repetir, o cualquier tecla para finalizar: ").lower()
  if repetir_trivia != "si":  
   print("\nEspero",nombre,"que lo hayas pasado bien, hasta pronto!")
   iniciar_trivia = False  