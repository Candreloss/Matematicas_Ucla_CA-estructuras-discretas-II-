# Importación de las librerías
import tkinter as tk
from tkinter import ttk
import constantes 
from Modelo_Grafo import Grafo

# --- NUEVAS IMPORTACIONES DE MATPLOTLIB ---
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
# ------------------------------------------

# Incialización del programa, configuración y personalización de las características de la ventana principal
app = tk.Tk()
app.title("Mátemáticas UCLA C.A")
app.config(bg="#050505")
app.geometry("800x550")
app.resizable(False, False)
verdanaCursivaN, verdanaCursiva, verdanaNegra, verdanaN = constantes.get_fonts(app)
style = ttk.Style(app)
style.theme_use("clam")

# Implementación de los estilos de la interfaz
# ... (Tu código de estilos, se mantiene igual)

style.configure("label_title.TLabel", background=constantes.AZULP, foreground="#FFFFFF", relief=tk.FLAT, font= verdanaCursivaN)
style.configure("bfs.TButton", background="#2f2978", foreground="#ffffff", relief=tk.FLAT, font=verdanaNegra)
style.map("bfs.TButton", background=[("active", "#38A4DD")], foreground=[("active", "#ffffff")])
style.configure("dfs.TButton", background="#2f2978", foreground="#ffffff", relief=tk.FLAT, font=verdanaNegra)
style.map("dfs.TButton", background=[("active", "#38A4DD")], foreground=[("active", "#ffffff")])
style.configure("kruskal.TButton", background="#2f2978", foreground="#ffffff", relief=tk.FLAT, font=verdanaNegra)
style.map("kruskal.TButton", background=[("active", "#38A4DD")], foreground=[("active", "#ffffff")])
style.configure("prim.TButton", background="#2f2978", foreground="#ffffff", relief=tk.FLAT, font=verdanaNegra)
style.map("prim.TButton", background=[("active", "#38A4DD")], foreground=[("active", "#2f2978")])
style.configure("integrantes.TButton", background="#38A4DD", foreground="#2f2978", relief=tk.FLAT, font=verdanaNegra)
style.map("integrantes.TButton", background=[("active", "#C4C5E5")], foreground=[("active", "#2f2978")])


# Título

frame_title = tk.Frame(master=app)
frame_title.config(bg="#2f2978")
frame_title.place(x=0, y=0, width=800, height=50)

label_title = ttk.Label(master=frame_title, text="Matemáticas UCLA C.A", style="label_title.TLabel")
label_title.configure(anchor= "center")
label_title.place(x=0, y=0, width=800, height=50)

# Menú principal

frame_menu = tk.Frame(master=app)
frame_menu.config(bg="#C4C5E5")
frame_menu.place(x=20, y=70, width=270, height=410)

bfs = ttk.Button(master=frame_menu, text="Recorrido de \nanchura (BFS)", style="bfs.TButton")
bfs.place(x=10, y=35, width=250, height=65)


dfs = ttk.Button(master=frame_menu, text="Recorrido de búsqueda\n en profundidad (DFS)", style="dfs.TButton")
dfs.place(x=10, y=125, width=250, height=65)


kruskal = ttk.Button(master=frame_menu, text="Árbol generador de mínimo\n peso (Por medio de Kruskal)", style="kruskal.TButton")
kruskal.place(x=10, y=215, width=250, height=65)

prim = ttk.Button(master=frame_menu, text="Árbol generador de mínimo\n peso (Por medio de Prim)", style="prim.TButton")
prim.place(x=10, y=305, width=250, height=65)

# Área del grafo

frame_grafo = tk.Frame(master=app)
frame_grafo.config(bg="#e2e2e2")
frame_grafo.place(x=311, y=96, width=460, height=344)


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

# Opcional: Agregar la barra de herramientas de navegación
toolbar = NavigationToolbar2Tk(canvas, frame_grafo)
toolbar.update()
widget_grafo.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
# ---------------------------------------


# Footer

frame_footer = tk.Frame(master=app)
frame_footer.config(bg="#2f2978")
frame_footer.place(x=0, y=500, width=800, height=50)

integrantes = ttk.Button(master=frame_footer, text="👤", style="integrantes.TButton")

integrantes.place(x=750, y=5, width=40, height=40)


app.mainloop()
