# 3.Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y la cantidad de veces que aparece (frecuencia).

texto = """No estarás sola,
vendrán a buscarte batallones de soldados
que a tu guerrilla de paz se han enrolado.
Y yo en primera fila de combate
abriendo trincheras
para protegernos, mi guerrillera"""

#Caracteres que no cuentan como palabras
quitar = ",."
for caracter in quitar:
    texto = texto.replace(caracter,"") # Reemplazarlo por nada; es decir removerlo
#Convertir la palabra a mimuscula
texto = texto.lower()
#Covertir la cadena en un arreglo
palabras = texto.split(" ")
#Contar las palabras creando un diccionario 
#La clave del diccionario será palabra y el valor sera el conteo
diccionario_frecuencia ={}
for palabra in palabras:
    if palabra in diccionario_frecuencia:
        diccionario_frecuencia[palabra] += 1
    else:
        diccionario_frecuencia[palabra] = 1
        
for palabra in diccionario_frecuencia:
    frecuencia = diccionario_frecuencia[palabra]
    print(f"La palabra '{palabra}'tiene una frecuencia de {frecuencia}")
    
               


    
    
    

