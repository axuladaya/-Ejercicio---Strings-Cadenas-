#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print( " ¿Qué opina sobre la lavadora BlackDecker portatil? Le sugerimos utilizar las siguiente palabras para realizar su comentario")


palabras_positivas = ["bonita","eficiente","silenciosa","rapida","compacta","buenisima","facil","fantastica","recomendable","ecologica"]

palabras_negativas = ["molesta","ruidosa","mala","inconveniente","dificil","horrible","incompleta","estropea","defectuosa"]

print(palabras_positivas)
print(palabras_negativas)

my_string = input ('Escriba su opinion:').lower()

score = 0
for palabras_positivas in palabras_positivas:
    score = score + my_string.count(palabras_positivas)
    
for palabras_negativas in palabras_negativas:
    score = score - my_string.count(palabras_negativas)
    
if (score == 0): 
    result = "Neutro"
if (score > 0):
    result = "Positivo"
if (score < 0):
    result = "Negativo"
print("Analizador de sentimientos\n")
print("my_string: {}\nscore: {} \nresultado: {}".format(my_string, score, result))

respuesta = input("Volver a evaluar (si/no'): ").lower()
while (respuesta == 'si'):
    continue
    print ("¿Qué opina sobre la lavadora BlackDecker portatil? Le sugerimos utilizar las siguiente palabras para realizar su comentario")


# In[ ]:




