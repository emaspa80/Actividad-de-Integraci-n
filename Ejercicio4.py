#4.Escribir una función que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y la cantidad de veces que aparece (frecuencia). Escribir otra función que reciba el diccionario generado con la función anterior y devuelva una tupla con la palabra más repetida y su frecuencia.

def count_words(text):
    text = text.split()
    words = {}
    for i in text:
        if i in words:
            words[i] += 1
        else:
            words[i] = 1
    return words

def most_repeated(words):
    max_word = ''
    max_freq = 0
    for word, freq in words.items():
        if freq > max_freq:
            max_word = word
            max_freq = freq
    return max_word, max_freq

text = '''Por aquello que encontré en tus ojos
por aquello que perdí en la lucha
conocer la otra mitad es poco
comprender que solo estar es más puro'''
print(count_words(text))
print(most_repeated(count_words(text)))