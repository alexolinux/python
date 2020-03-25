# -*- coding: UTF-8 -*-

def poem(person, adjective, animal):
    print("\nJardim de " + person)
    print("Todo mundo " + adjective)
    print("Até " + animal)

person = input("Informe uma pessoa: ")
adj = input("Escreva um adjetivo: ")
animal = input("Escolha um animal: ")

print(poem(person.capitalize(), adj.lower(), animal.lower()))