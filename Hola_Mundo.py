print("PROGRAMA DE ESTUDIO \n\n (Tienes que escribir lo que se te pide y en cuanto acabes presionas enter)")
t=input ("Pon nombre a una tarea:   ")# Pon una pequeña descripcion de la tarea a realizar
n=input ("Ahora dime para quien es esta tarea:   ")# Introduce quien es la persona que debe de hacer esta tarea

while True:
    p_input = input("Ahora cuantos puntos va a tener esta tarea:")#ibtroduce los puntos que vaya a tenwr esta tarea
    
    try:
        # Intenta convertir la entrada a un número entero
        p = int(p_input) 
        break  # Si lo logra, sale del bucle
    except ValueError:
        # Si el usuario puso una letra, se ejecuta esto en vez de crashear
        print("¡Error! Por favor, introduce un número válido, no una letra.")#Error pusiste un carracter erroneo 
        
if t!="" and n!="" and p!=0:# verificador de datos

    print("Ok entonces esta tarea es para: ", n ," y tiene que hacer: ",t," la cual tiene un valor de: ",p)
else:
    print("No llenaste bien los datos requeridos")