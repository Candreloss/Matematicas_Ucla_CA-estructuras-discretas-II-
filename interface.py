#Importación de las librerías
import tkinter as tk
from tkinter import ttk
import constantes


#Incialización del programa, configuración y personalización de las características de la ventana principal
app = tk.Tk()
app.title("Estructuras Discretas II. Grafos")
app.config(bg="#C4C5E5")
app.geometry("800x550")
style = ttk.Style(app)
style.theme_use("clam")

#Implementación de los estilos de la interfaz

style.configure("label_title.TLabel", background=constantes.AZULP, foreground="#FFFFFF", relief=tk.FLAT, font=("Verdana", 27, "bold", "italic"), anchor="center")

style.configure("org.TButton", background="#2f2978", foreground="#ffffff", relief=tk.FLAT, font=("Verdana", 12, "bold" ))
style.map("org.TButton", background=[("active", "#38A4DD")], foreground=[("active", "#ffffff")])
style.configure("bfs.TButton", background="#2f2978", foreground="#ffffff", relief=tk.FLAT, font=("Verdana", 12, "bold" ))
style.map("bfs.TButton", background=[("active", "#38A4DD")], foreground=[("active", "#ffffff")])
style.configure("dfs.TButton", background="#2f2978", foreground="#ffffff", relief=tk.FLAT, font=("Verdana", 8, "bold" ))
style.map("dfs.TButton", background=[("active", "#38A4DD")], foreground=[("active", "#ffffff")])
style.configure("kruskal.TButton", background="#2f2978", foreground="#ffffff", relief=tk.FLAT, font=("Verdana", 8, "bold" ))
style.map("kruskal.TButton", background=[("active", "#38A4DD")], foreground=[("active", "#ffffff")])
style.configure("prim.TButton", background="#2f2978", foreground="#ffffff", relief=tk.FLAT, font=("Verdana", 8, "bold" ))
style.map("prim.TButton", background=[("active", "#38A4DD")], foreground=[("active", "#2f2978")])
style.configure("integrantes.TButton", background="#38A4DD", foreground="#2f2978", relief=tk.FLAT, font=("Verdana", 8, "bold" ))
style.map("integrantes.TButton", background=[("active", "#C4C5E5")], foreground=[("active", "#2f2978")])


#Título

frame_title = tk.Frame(master=app)
frame_title.config(bg="#2f2978")
frame_title.place(x=0, y=0, width=800, height=50)

label_title = ttk.Label(master=frame_title, text="Estructuras Discretas II. Grafos", style="label_title.TLabel")
label_title.configure(anchor= "center")
label_title.place(x=0, y=0, width=800, height=50)

#Menú principal
frame_menu = tk.Frame(master=app)
frame_menu.config(bg="#C4C5E5")
frame_menu.place(x=20, y=75, width=270, height=400)

org = ttk.Button(master=frame_menu, text="Grafo", style="bfs.TButton")
org.place(x= 0, y=0, width=270, height=60)

bfs = ttk.Button(master=frame_menu, text="Recorrido de anchura (BFS)", style="bfs.TButton")
bfs.place(x=0, y=85, width=270, height=60)


dfs = ttk.Button(master=frame_menu, text="Recorrido de búsqueda en profundidad (DFS)", style="dfs.TButton")
dfs.place(x=0, y=170, width=270, height=60)


kruskal = ttk.Button(master=frame_menu, text="Árbol generador de mínimo peso (Por medio de Kruskal)", style="kruskal.TButton")
kruskal.place(x=0, y=255, width=270, height=60)

prim = ttk.Button(master=frame_menu, text="Árbol generador de mínimo peso (Por medio de Prim)", style="prim.TButton")
prim.place(x=0, y=340, width=270, height=60)

# Área del grafo

frame_grafo = tk.Frame(master=app)
frame_grafo.config(bg="#FFFFFF")
frame_grafo.place(x=310, y=90, width=470, height=370)

# Footer

frame_footer = tk.Frame(master=app)
frame_footer.config(bg="#2f2978")
frame_footer.place(x=0, y=500, width=800, height=50)

integrantes = ttk.Button(master=frame_footer, text="👤", style="integrantes.TButton")

integrantes.place(x=750, y=5, width=40, height=40)


app.mainloop()