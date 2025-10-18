# Importación de las librerías
import tkinter as tk # Librería de interfaz
from tkinter import ttk # Librería de interfaz
from tkinter import messagebox
import constantes # Librería con datos de diseño
from Modelo_Grafo import Grafo # Modelo del grafo
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk #Librería Matplotlib

# -----Funciones del programa------------

def mostrar_integrantes():
    #Limpiamos el frame donde se muestran los datos
    for widget in frame_grafo.winfo_children():
        widget.destroy()
    
    #Creamos el bloque donde están guardados y definidos los datos de los integrantes, y el como se mostrarán
    integrantes_label= tk.Label(frame_grafo, text= "Integrantes\n-Ángel Curé\n -Nelson Hernández\n -Karen Rangel\n -Carlos Paradas\n -Ray Yépez\n -Ricardo Pérez", font=(verdanaCursivaN), bg="#FFFFFF", justify= "center")
    integrantes_label.place(x=230, y=170, width=470, height=370, anchor="center")
    

def mostrar_grafo():
    #Limpiamos el lienzo, por si hay otro contenido presente.
    for widget in frame_grafo.winfo_children():
        widget.destroy()

    # --- CÓDIGO PARA INSERTAR LA GRÁFICA ---
    # Generamos la figura de Matplotlib

    figura = grafo_instance.generar_figura_matplotlib()

    #Creamos el lienzo de Tkinter a partir de la figura, y lo adjuntamos a frame_grafo
    canvas = FigureCanvasTkAgg(figura, master=frame_grafo)
    canvas.draw()

    #Empaquetamos el widget de Tkinter del lienzo para que ocupe todo el frame

    widget_grafo = canvas.get_tk_widget()
    widget_grafo.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    # Opcional: Agregar la barra de herramientas de navegación
    """"
    toolbar = NavigationToolbar2Tk(canvas, frame_grafo)
    toolbar.update()
    widget_grafo.pack(side=tk.TOP, fill=tk.BOTH, expand=1)"""

def mostrar_kruskal():
    try:
        figura_kruskal = grafo_instance.generar_figura_kruskal()
        for widget in frame_grafo.winfo_children():
            widget.destroy()

        canvas_kruskal = FigureCanvasTkAgg(figura_kruskal, master=frame_grafo)
        canvas_kruskal.draw()
        canvas_kruskal.get_tk_widget().pack(side="top", fill="both", expand=True)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def modificar_grafo():
    #Limpiamos el lienzo, por si hay otro contenido presente.
    for widget in frame_grafo.winfo_children():
        widget.destroy()
    #Diseño, título
    modificar_title_label= tk.Label(frame_grafo, text= "Modificación del grafo", font=(verdanaCursivaN), bg="#FFFFFF", justify= "center")
    modificar_title_label.place(x=230, y=50, width=470, height=370, anchor="center")

    #Frame para agrupar los botones
    frame_botones = tk.Frame(frame_grafo)
    frame_botones.configure(bg="#FFFFFF")
    frame_botones.place(x=235, y=200, anchor="center", width=400, height=250)

    #Botones con las opciones de modificación del grafo
    btn_agregar_vertice = ttk.Button(frame_botones, text="Agregar vértice", style="modificacion.TButton", command=agregar_vertice_button)
    btn_agregar_vertice.place(x=20, y=20, width=160, height=50)

    btn_agregar_arista = ttk.Button(frame_botones, text="Agregar arista", style="modificacion.TButton", command=agregar_arista_button)
    btn_agregar_arista.place(x=210, y=20, width=160, height=50)

    btn_eliminar_vertice = ttk.Button(frame_botones, text="Eliminar vértice", style="modificacion.TButton", command=eliminar_vertice_button)
    btn_eliminar_vertice.place(x=20, y=100, width=160, height=50)

    btn_eliminar_arista = ttk.Button(frame_botones, text="Eliminar arista", style="modificacion.TButton",command=eliminar_arista_button)
    btn_eliminar_arista.place(x=210, y=100, width=160, height=50)


def agregar_vertice_button():
    #Limpiamos el lienzo, por si hay otro contenido presente.
    for widget in frame_grafo.winfo_children():
        widget.destroy()

    #Diseño, título
    agregar_v_title_label= tk.Label(frame_grafo, text= "Agregar vertice", font=(verdanaCursivaN), bg="#FFFFFF", justify= "center")
    agregar_v_title_label.place(x=230, y=50, width=470, height=370, anchor="center")

    #Solicitud de datos, Nombre del vértice, posición en X y Y

    tk.Label(frame_grafo, text="Nombre del vértice:", bg="#FFFFFF", font=verdanaN).place(x=100, y=90)
    entry_nombre = tk.Entry(frame_grafo, font=verdanaN, justify="center")
    entry_nombre.place(x=260, y=90, width=120)

    tk.Label(frame_grafo, text="Posición X:", bg="#FFFFFF", font=verdanaN).place(x=100, y=140)
    entry_x = tk.Entry(frame_grafo, font=verdanaN, justify="center")
    entry_x.place(x=260, y=140, width=120)

    tk.Label(frame_grafo, text="Posición Y:", bg="#FFFFFF", font=verdanaN).place(x=100, y=190)
    entry_y = tk.Entry(frame_grafo, font=verdanaN, justify="center")
    entry_y.place(x=260, y=190, width=120)
    
    # Botón para agregar el vértice
    def agregar_v():
        #Verificación de los datos

        nombre = entry_nombre.get().strip()
        if not nombre:
            tk.messagebox.showerror("Error", "Debe ingresar un nombre para el vértice.")
            return
        
        if nombre in grafo_instance.G.nodes:
            tk.messagebox.showwarning("Vértice existente", f"El vértice '{nombre}' ya existe.")
            return

        try:
            x = float(entry_x.get())
            y = float(entry_y.get())
        except ValueError:
            tk.messagebox.showerror("Error", "Las posiciones X e Y deben ser numéricas.")
            return
        
        #Se añade el grafo al confirmar que está todo correcto
        grafo_instance.agregar_vertice(nombre, (x,y))

        # Mostrar la gráfica actualizada
        mostrar_grafo()

    btn_agregar_v = ttk.Button(frame_grafo, text="Agregar vértice", style="modificacion.TButton", command=agregar_v)
    btn_agregar_v.place(x=170, y=260, width=160, height=40)

def agregar_arista_button():
    #Limpiamos el lienzo, por si hay otro contenido presente.
    for widget in frame_grafo.winfo_children():
        widget.destroy()

    #Diseño, título
    agregar_a_title_label= tk.Label(frame_grafo, text= "Agregar arista", font=(verdanaCursivaN), bg="#FFFFFF", justify= "center")
    agregar_a_title_label.place(x=230, y=50, width=470, height=370, anchor="center")

    #Elementos de solicitud de datos
    tk.Label(frame_grafo, text="Vértice inicial:", bg="#FFFFFF").place(x=100, y=80)
    vertice_inicial = ttk.Combobox(frame_grafo, values=grafo_instance.vertice, state="readonly")
    vertice_inicial.place(x=220, y=80, width=120)

    tk.Label(frame_grafo, text="Vértice final:", bg="#FFFFFF").place(x=100, y=120)
    vertice_final = ttk.Combobox(frame_grafo, values=grafo_instance.vertice, state="readonly")
    vertice_final.place(x=220, y=120, width=120)

    # Solicitud del peso de la arista
    tk.Label(frame_grafo, text="Peso:", bg="#FFFFFF").place(x=100, y=160)
    peso_entry = tk.Entry(frame_grafo)
    peso_entry.place(x=220, y=160, width=120)

    # Verifica que no exista ningún error en la recolección de datos
    def agregar_a():
        u = vertice_inicial.get().strip()
        v = vertice_final.get().strip()
        if not u or not v:
            tk.messagebox.showerror("Error", "Debe seleccionar tanto el vértice inicial como el final.")
            return
        if u == v:
            tk.messagebox.showerror("Error", "No puede crear lazos.")
            return

        try:
            peso = int(peso_entry.get())
        except ValueError:
            tk.messagebox.showerror("Error", "El peso debe ser un número.")
            return
    #Al verificar que todo está correcto, añade la arista.
        grafo_instance.agregar_arista(u, v, peso)
        mostrar_grafo()  # Muestra el grafo ya actualizado

    ttk.Button(frame_grafo, text="Agregar", command=agregar_a).place(x=180, y=210, width=100, height=30)


def eliminar_vertice_button():

    #Limpiamos el lienzo, por si hay otro contenido presente.
    for widget in frame_grafo.winfo_children():
        widget.destroy()
    
    #Diseño, título
    eliminar_v_title_label= tk.Label(frame_grafo, text= "Eliminar vertice", font=(verdanaCursivaN), bg="#FFFFFF", justify= "center")
    eliminar_v_title_label.place(x=230, y=50, width=470, height=370, anchor="center")

    #Solicitud de dato para eliminar
    tk.Label(frame_grafo, text="Seleccione el vértice:", bg="#FFFFFF").place(x=100, y=100)
    vertice_combo = ttk.Combobox(frame_grafo, values=grafo_instance.vertice, state="readonly")
    vertice_combo.place(x=240, y=100, width=120)

    def eliminar_v():
        v = vertice_combo.get().strip()
        if not v:
            tk.messagebox.showerror("Error", "Debe seleccionar un vértice.")
            return
        if v not in grafo_instance.G.nodes:
            tk.messagebox.showerror("Error", f"El vértice {v} no existe.")
            return
        
        grafo_instance.G.remove_node(v)
        grafo_instance.vertice.remove(v)
        mostrar_grafo()

    ttk.Button(frame_grafo, text="Eliminar", command=eliminar_v).place(x=180, y=180, width=100, height=30)

def eliminar_arista_button():
    #Elimina el contenido actual presente en el frame
    for widget in frame_grafo.winfo_children():
        widget.destroy()
    
    #Diseño, título
    eliminar_a_title_label= tk.Label(frame_grafo, text= "Eliminar arista", font=(verdanaCursivaN), bg="#FFFFFF", justify= "center")
    eliminar_a_title_label.place(x=230, y=50, width=470, height=370, anchor="center")

    #Solicita el dato de la arista a eliminar
    tk.Label(frame_grafo, text="Vértice inicial:", bg="#FFFFFF").place(x=100, y=80)
    vertice_inicial = ttk.Combobox(frame_grafo, values=grafo_instance.vertice, state="readonly")
    vertice_inicial.place(x=220, y=80, width=120)

    tk.Label(frame_grafo, text="Vértice final:", bg="#FFFFFF").place(x=100, y=120)
    vertice_final = ttk.Combobox(frame_grafo, values=grafo_instance.vertice, state="readonly")
    vertice_final.place(x=220, y=120, width=120)

    def eliminar_a():
        u = vertice_inicial.get().strip()
        v = vertice_final.get().strip()
        if not u or not v:
            tk.messagebox.showerror("Error", "Debe seleccionar ambos vértices.")
            return
        if not grafo_instance.G.has_edge(u, v):
            tk.messagebox.showerror("Error", f"No existe una arista entre {u} y {v}.")
            return
        
        grafo_instance.G.remove_edge(u, v)
        # También eliminamos del arreglo de pesos
        grafo_instance.peso = [(a, b, p) for (a, b, p) in grafo_instance.peso if not ((a == u and b == v) or (a == v and b == u))]
        mostrar_grafo()

    ttk.Button(frame_grafo, text="Eliminar", command=eliminar_a).place(x=180, y=180, width=100, height=30)

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

style.configure("label_title.TLabel", background=constantes.AZULP, foreground="#FFFFFF", relief=tk.FLAT, font= verdanaCursivaN)
style.configure("org.TButton", background="#2f2978", foreground="#ffffff", relief=tk.FLAT, font=verdanaNegra)
style.map("org.TButton", background=[("active", "#38A4DD")], foreground=[("active", "#ffffff")])
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
style.configure("modificacion.TButton", background="#38A4DD", foreground="#2f2978", relief=tk.FLAT, font=verdanaNegra)
style.map("modificacion.TButton", background=[("active", "#C4C5E5")], foreground=[("active", "#2f2978")])

# Título

frame_title = tk.Frame(master=app)
frame_title.config(bg="#2f2978")
frame_title.place(x=0, y=0, width=800, height=50)

label_title = ttk.Label(master=frame_title, text="Estructuras Discretas II. Grafos", style="label_title.TLabel")
label_title.configure(anchor= "center")
label_title.place(x=0, y=0, width=800, height=50)

# Menú principal

frame_menu = tk.Frame(master=app)
frame_menu.config(bg="#C4C5E5")
frame_menu.place(x=20, y=75, width=270, height=400)

grafo = ttk.Button(master=frame_menu, text="Grafo", style="bfs.TButton", command=mostrar_grafo)
grafo.place(x= 0, y=0, width=270, height=60)

bfs = ttk.Button(master=frame_menu, text="Recorrido de anchura (BFS)", style="bfs.TButton")
bfs.place(x=0, y=85, width=270, height=60)


dfs = ttk.Button(master=frame_menu, text="Recorrido de búsqueda\n en profundidad (DFS)", style="dfs.TButton")
dfs.place(x=0, y=170, width=270, height=60)


kruskal = ttk.Button(master=frame_menu, text="Árbol generador de mínimo\n peso (Por medio de Kruskal)", style="kruskal.TButton", command=mostrar_kruskal)
kruskal.place(x=0, y=255, width=270, height=60)

prim = ttk.Button(master=frame_menu, text="Árbol generador de mínimo\n peso (Por medio de Prim)", style="prim.TButton")
prim.place(x=0, y=340, width=270, height=60)

# Área del grafo

frame_grafo = tk.Frame(master=app)
frame_grafo.config(bg="#FFFFFF")
frame_grafo.place(x=310, y=90, width=470, height=370)

# -Creamos la instancia del Grafo
grafo_instance = Grafo()

# Footer

frame_footer = tk.Frame(master=app)
frame_footer.config(bg="#2f2978")
frame_footer.place(x=0, y=500, width=800, height=50)

integrantes = ttk.Button(master=frame_footer, text="👤", style="integrantes.TButton", command=mostrar_integrantes)
integrantes.place(x=750, y=5, width=40, height=40)

modificar= ttk.Button(master=frame_footer, text="Modificar Grafo", style="modificacion.TButton", command=modificar_grafo)
modificar.place(x=300, y=5, width=200, height=40)

integrantes = ttk.Button(master=frame_footer, text="👤", style="integrantes.TButton", command=mostrar_integrantes)
integrantes.place(x=750, y=5, width=40, height=40)

mostrar_grafo()
app.mainloop()