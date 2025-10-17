from tkinter import font
#Colores para la interfaz gráfica
AZULP = ("#2f2978")
AZULS = ("#38A4DD")
LILA = ("#C4C5E5")
BLANCO = ("#FFFFFF")
NEGRO = ("#000000")
GRIS = ("#666666")

#Tipografias
def get_fonts(app):
    verdanaCursivaN = font.Font(root=app, family="Verdana", size=23, slant="italic", weight="bold")
    verdanaCursiva  = font.Font(root=app, family="Verdana", size=16, slant="italic")
    verdanaNegra    = font.Font(root=app, family="Verdana", size=13, weight="bold")
    verdanaN        = font.Font(root=app, family="Verdana", size=12)
    return verdanaCursivaN, verdanaCursiva, verdanaNegra, verdanaN