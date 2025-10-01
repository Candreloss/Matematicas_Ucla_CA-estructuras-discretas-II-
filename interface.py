#Importación de las librerías
import tkinter as tk
from tkinter import ttk

#Incialización del programa, configuración y personalización de las características de la ventana principal
app = tk.Tk()
app.title("Mátemáticas UCLA C.A")
app.config(bg="#050505")
app.geometry("800x550")
style = ttk.Style(app)
style.theme_use("clam")

#Implementación de los estilos de la interfaz

style.configure("label_title.TLabel", background="#17738F", foreground="#E7E7E7", relief=tk.FLAT, font=("Forte", 20, ), anchor="center")
style.configure("bfs.TButton", background="#17738F", foreground="#ffffff", relief=tk.FLAT, font=("Tahoma", 8, ))
style.map("bfs.TButton", background=[("active", "#8585f7")], foreground=[("active", "#ffffff")])
style.configure("dfs.TButton", background="#17738F", foreground="#ffffff", relief=tk.FLAT, font=("Tahoma", 8, ))
style.map("dfs.TButton", background=[("active", "#8585f7")], foreground=[("active", "#ffffff")])
style.configure("kruskal.TButton", background="#17738F", foreground="#ffffff", relief=tk.FLAT, font=("Tahoma", 8, ))
style.map("kruskal.TButton", background=[("active", "#8585f7")], foreground=[("active", "#ffffff")])
style.configure("prim.TButton", background="#17738F", foreground="#ffffff", relief=tk.FLAT, font=("Tahoma", 8, ))
style.map("prim.TButton", background=[("active", "#8585f7")], foreground=[("active", "#ffffff")])
style.configure("integrantes.TButton", background="#050505", foreground="#ffffff", relief=tk.FLAT, font=("Tahoma", 8, ))
style.map("integrantes.TButton", background=[("active", "#17738F")], foreground=[("active", "#ffffff")])


#Título

frame_title = tk.Frame(master=app)
frame_title.config(bg="#17738F")
frame_title.place(x=0, y=0, width=800, height=50)

label_title = ttk.Label(master=frame_title, text="Matemáticas UCLA C.A", style="label_title.TLabel")
label_title.configure(anchor= "center")
label_title.place(x=0, y=0, width=800, height=50)

#Menú principal

frame_menu = tk.Frame(master=app)
frame_menu.config(bg="#f7f7f7")
frame_menu.place(x=20, y=70, width=270, height=410)

bfs = ttk.Button(master=frame_menu, text="Recorrido de anchura (BFS)", style="bfs.TButton")
bfs.place(x=10, y=35, width=250, height=65)


dfs = ttk.Button(master=frame_menu, text="Recorrido de búsqueda en profundidad (DFS)", style="dfs.TButton")
dfs.place(x=10, y=125, width=250, height=65)


kruskal = ttk.Button(master=frame_menu, text="Árbol generador de mínimo peso (Por medio de Kruskal)", style="kruskal.TButton")
kruskal.place(x=10, y=215, width=250, height=65)

prim = ttk.Button(master=frame_menu, text="Árbol generador de mínimo peso (Por medio de Prim)", style="prim.TButton")
prim.place(x=10, y=305, width=250, height=65)

# Área del grafo

frame_grafo = tk.Frame(master=app)
frame_grafo.config(bg="#e2e2e2")
frame_grafo.place(x=311, y=96, width=460, height=344)

# Footer

frame_footer = tk.Frame(master=app)
frame_footer.config(bg="#17738F")
frame_footer.place(x=0, y=500, width=800, height=50)

integrantes = ttk.Button(master=frame_footer, text="👤", style="integrantes.TButton")
integrantes.place(x=750, y=5, width=40, height=40)


app.mainloop()