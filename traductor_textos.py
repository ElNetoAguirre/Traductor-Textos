"""
Traductor de Textos - Python + ChatGPT
"""

import os
import openai
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

# Función para traducir texto
def traducir_texto(texto, idioma, tokens, temperatura):
    """Función para traducir texto"""
    prompt = f"Traduce el texto '{texto}' al {idioma}."
    respuesta = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        n=1,
        max_tokens=tokens,
        temperature=temperatura
    )
    return respuesta.choices[0].text.strip()

# Generar las funciones de opciones e inicio
def app():
    """APP"""

    opciones = [
        "[1] - Traducir un Texto",
        "[q] - Salir"
    ]

    while True:
        os.system("clear" or "cls")
        print("-----------------------------------------------------------------------")
        print("                  Bienvenido al Traductor del El Neto                  ")
        print("-----------------------------------------------------------------------")

        for opcion in opciones:
            print(opcion)

        print("\n")
        entrada_usuario = input("Escoge una opción: ")

        match entrada_usuario:
            case "1":
                os.system("clear" or "cls")
                print("-----------------------------------------------------------------------")
                print("                            Traducir Texto                             ")
                print("-----------------------------------------------------------------------")
                print("\n")
                texto_original = input("Escribe el texto que quieres traducir: ").rstrip("\n")
                print("\n")
                idioma_traducir = input("A que idioma lo quieres traducir: ")
                print("\n")
                tokens = int(input("¿Cuantos tokens máximos tendrá tu artículo?: "))
                print("\n")
                temperatura = int(input("Del 1 al 10, ¿qué tan creativo quieres que sea tu artículo?: ")) / 10
                traduccion = traducir_texto(texto_original, idioma_traducir, tokens, temperatura)
                print("\n")
                print(traduccion)
                print("\n")
                input("\nEnter para continuar")

            case "q":
                os.system("clear" or "cls")
                print("------------------------------------------------------------------------")
                print("                Gracias por usar el Traductor de El Neto                ")
                print("------------------------------------------------------------------------")
                print("\n")
                break

            case otra:
                print(f"{otra} no es valido")
                input("\nEnter para continuar")

def inicio():
    """Inicio de APP"""
    app()

inicio()
