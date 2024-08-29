import m_funciones
'''
from m_funciones import imprimir as imp
from m_funciones import hacer_grandioso2 as h_grand2
'''

#l_magos = ["Harry Houdini", "David Blaine", "Teller"]

#l_cientificos = ["Newton", "Hawking", "Einstein"]

#l_otros = ["Messi", "Pele", "Juanes"]

lista = [{"nombre":"Harry Houdini", "categoria":"mago"},
        {"nombre":"Newton", "categoria":"cientifico"},
        {"nombre":"David Blaine", "categoria":"mago"},
        {"nombre":"Hawking", "categoria":"cientifico"},
        {"nombre":"Messi", "categoria":"otros"},
        {"nombre":"Teller", "categoria":"mago"},
        {"nombre":"Einstein", "categoria":"cientifico"},
        {"nombre":"Pele", "categoria":"otros"},
        {"nombre":"Juanes", "categoria":"otros"}
]

print("LISTA SIN MODIFICAR")
print("-------------------")
print("-------------------")
for elemento in lista:
    if elemento["nombre"]:
        m_funciones.imprimir(elemento["nombre"])
        
print("#######################################################")

for elemento in lista:
    nuevo_nombre = m_funciones.hacer_grandioso2(elemento["nombre"], elemento["categoria"])
    if nuevo_nombre:
        elemento["nombre"] = nuevo_nombre

print("LISTA MODIFICADA")
print("----------------")
print("----------------")
print("Magos:")
print("----------------")      

for elemento in lista:
    if elemento["categoria"] == "mago":
        m_funciones.imprimir(elemento["nombre"])


print("----------------")
print("Científicos:")
print("----------------")

for elemento in lista:
    if elemento["categoria"] == "cientifico":
        m_funciones.imprimir(elemento["nombre"])


print("----------------")
print("Otros:")
print("----------------")

for elemento in lista:
    if elemento["categoria"] == "otros":
        m_funciones.imprimir(elemento["nombre"])
