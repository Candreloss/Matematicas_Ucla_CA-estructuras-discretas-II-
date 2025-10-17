# Importación de las librerías
import tkinter as tk
from tkinter import ttk
import constantes 
from Modelo_Grafo import Grafo

# --- NUEVAS IMPORTACIONES DE MATPLOTLIB ---
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg #, NavigationToolbar2Tk  Opcional barra herramientas
# ------------------------------------------

# Incialización del programa, configuración y personalización de las características de la ventana principal
app = tk.Tk()
app.title("Estructuras Discretas II. Grafos")
app.config(bg="#C4C5E5")
app.geometry("800x550")
app.resizable(False, False)
verdanaCursivaN, verdanaCursiva, verdanaNegra, verdanaN = constantes.get_fonts(app)
style = ttk.Style(app)
style.theme_use("clam")

# Implementación de los estilos de la interfaz
# ... (El código de estilos, se mantiene igual) 

# Título
style.configure("label_title.TLabel", background=constantes.AZULP, foreground="#FFFFFF", relief=tk.FLAT, font= verdanaCursivaN)
#Botones
style.configure("orig.TButton", background="#2f2978", foreground="#FFFFFF", relief=tk.FLAT, font=("Verdana", 12, "bold" ))
style.map("orig.TButton", background=[("active", "#38A4DD")], foreground=[("active", "#2f2978")])
style.configure("bfs.TButton", background="#2f2978", foreground="#ffffff", relief=tk.FLAT, font=verdanaNegra)
style.map("bfs.TButton", background=[("active", "#38A4DD")], foreground=[("active", "#2f2978")])
style.configure("dfs.TButton", background="#2f2978", foreground="#ffffff", relief=tk.FLAT, font=verdanaNegra)
style.map("dfs.TButton", background=[("active", "#38A4DD")], foreground=[("active", "#2f2978")])
style.configure("kruskal.TButton", background="#2f2978", foreground="#FFFFFF", relief=tk.FLAT, font=verdanaNegra)
style.map("kruskal.TButton", background=[("active", "#38A4DD")], foreground=[("active", "#2f2978")])
style.configure("prim.TButton", background="#2f2978", foreground="#FFFFFF", relief=tk.FLAT, font=verdanaNegra)
style.map("prim.TButton", background=[("active", "#38A4DD")], foreground=[("active", "#2f2978")])
style.configure("integrantes.TButton", background="#38A4DD", foreground="#2f2978", relief=tk.FLAT, font=verdanaNegra)
style.map("integrantes.TButton", background=[("active", "#C4C5E5")], foreground=[("active", "#2f2978")])

# Título Dibujo

frame_title = tk.Frame(master=app)
frame_title.config(bg="#2f2978")
frame_title.place(x=0, y=0, width=800, height=50)

label_title = ttk.Label(master=frame_title, text="Estructuras Discretas II. Grafos", style="label_title.TLabel")
label_title.configure(anchor= "center")
label_title.place(x=0, y=0, width=800, height=50)

# Menú principal Recuadro lateral
frame_menu = tk.Frame(master=app)
frame_menu.config(bg="#C4C5E5")
frame_menu.place(x=20, y=75, width=270, height=400)

orig = ttk.Button(master=frame_menu, text="Grafo de la Red", style="bfs.TButton")
orig.place(x= 0, y=0, width=270, height=60)

bfs = ttk.Button(master=frame_menu, text="Recorrido de anchura (BFS)", style="bfs.TButton")
bfs.place(x=0, y=85, width=270, height=60)

dfs = ttk.Button(master=frame_menu, text="Recorrido de búsqueda\n en profundidad (DFS)", style="dfs.TButton")
dfs.place(x=0, y=170, width=270, height=60)

kruskal = ttk.Button(master=frame_menu, text=" Árbol generador de mínimo\npeso (Por medio de Kruskal)", style="kruskal.TButton")
kruskal.place(x=0, y=255, width=270, height=60)

prim = ttk.Button(master=frame_menu, text="Árbol generador de mínimo\n  peso (Por medio de Prim)", style="prim.TButton")
prim.place(x=0, y=340, width=270, height=60)

# Área del grafo

frame_grafo = tk.Frame(master=app)
frame_grafo.config(bg="#FFFFFF")
frame_grafo.place(x=310, y=90, width=470, height=370)

# --- CÓDIGO PARA INSERTAR LA GRÁFICA ---
# 1. Creamos una instancia de tu Grafo
grafo_instance = Grafo()

# 2. Generamos la figura de Matplotlib
figura = grafo_instance.generar_figura_matplotlib()

# 3. Creamos el lienzo de Tkinter a partir de la figura, y lo adjuntamos a frame_grafo
canvas = FigureCanvasTkAgg(figura, master=frame_grafo)
canvas.draw()

# 4. Empaquetamos el widget de Tkinter del lienzo para que ocupe todo el frame
widget_grafo = canvas.get_tk_widget()
widget_grafo.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

"""""
# Opcional: Agregar la barra de herramientas de navegación
toolbar = NavigationToolbar2Tk(canvas, frame_grafo)
toolbar.update()
widget_grafo.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
# ---------------------------------------
"""""

# Función para mostrar ventana de integrantes
def mostrar_integrantes():
    ventana_integrantes = tk.Toplevel(app)
    ventana_integrantes.geometry("300x200")
    ventana_integrantes.config(bg="#FFFFFF")
    label_info = tk.Label(ventana_integrantes, text="Integrantes del Proyecto:\n\n- Karen Rangel\n- Carlos Paradas\n- Nelson Hernandez\n- Ricardo Pérez\n- Angel Curé ", font=verdanaN, bg="#C4C5E5")
    label_info.pack(pady=20)

# Footer Recuadro
frame_footer = tk.Frame(master=app)
frame_footer.config(bg="#2f2978")
frame_footer.place(x=0, y=500, width=800, height=50)

#Boton Integrantes
integrantes = ttk.Button(master=frame_footer, text="👤", style="integrantes.TButton")
master=frame_footer
integrantes.place(x=750, y=5, width=40, height=40)
integrantes.config(command=mostrar_integrantes)



#No tocar please
app.mainloop()