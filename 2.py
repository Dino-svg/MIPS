import tkinter as tk
from tkinter import messagebox

def generar_instruccion_r(opcode=0, rs=0, rt=0, rd=0, shamt=0, funct=0):
    """
    Genera una instrucción tipo R en formato binario de 32 bits.
    Formato: opcode(6) | rs(5) | rt(5) | rd(5) | shamt(5) | funct(6)
    """
    instruccion = (opcode << 26) | (rs << 21) | (rt << 16) | (rd << 11) | (shamt << 6) | funct
    return format(instruccion, '032b')

def mostrar_instruccion(inst_bin):
    """Muestra una instrucción en formato legible"""
    return (f"Binario completo: {inst_bin}\n"
            f"OP: {inst_bin[0:6]}, Rs: {inst_bin[6:11]}, Rt: {inst_bin[11:16]}, "
            f"Rd: {inst_bin[16:21]}, Shamt: {inst_bin[21:26]}, Funct: {inst_bin[26:32]}")

def generar_instruccion():
    """Generar la instrucción a partir de los valores ingresados"""
    try:
        # Obtener valores de la interfaz
        opcode = int(opcode_entry.get())
        rs = int(rs_entry.get())
        rt = int(rt_entry.get())
        rd = int(rd_entry.get())
        shamt = int(shamt_entry.get())
        funct = int(funct_entry.get())
        
        # Generar la instrucción
        inst = generar_instruccion_r(opcode, rs, rt, rd, shamt, funct)
        
        # Mostrar la instrucción generada
        result_text = mostrar_instruccion(inst)
        
        # Agregar la instrucción generada al área de resultados sin borrarlas
        instrucciones_label.config(text=instrucciones_label.cget("text") + "\n" + result_text)
        
        # Limpiar los campos para que el usuario pueda generar otra instrucción
        opcode_entry.delete(0, tk.END)
        rs_entry.delete(0, tk.END)
        rt_entry.delete(0, tk.END)
        rd_entry.delete(0, tk.END)
        shamt_entry.delete(0, tk.END)
        funct_entry.delete(0, tk.END)
        
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa valores numéricos válidos.")

def mostrar_manual():
    """Mostrar la interfaz de generación manual de instrucciones"""
    # Limpiar la pantalla de opciones
    for widget in root.winfo_children():
        widget.grid_forget()
    
    # Crear los campos de entrada para instrucciones manuales
    tk.Label(root, text="Opcode (6 bits):").grid(row=0, column=0)
    opcode_entry.grid(row=0, column=1)

    tk.Label(root, text="Rs (5 bits):").grid(row=1, column=0)
    rs_entry.grid(row=1, column=1)

    tk.Label(root, text="Rt (5 bits):").grid(row=2, column=0)
    rt_entry.grid(row=2, column=1)

    tk.Label(root, text="Rd (5 bits):").grid(row=3, column=0)
    rd_entry.grid(row=3, column=1)

    tk.Label(root, text="Shamt (5 bits):").grid(row=4, column=0)
    shamt_entry.grid(row=4, column=1)

    tk.Label(root, text="Funct (6 bits):").grid(row=5, column=0)
    funct_entry.grid(row=5, column=1)

    # Botón para generar la instrucción
    generate_button.grid(row=6, columnspan=2)

    # Etiqueta para mostrar las instrucciones generadas
    instrucciones_label.grid(row=7, columnspan=2)

    # Botón para generar otra instrucción sin volver
    new_instruction_button = tk.Button(root, text="Generar otra instrucción", command=generar_instruccion)
    new_instruction_button.grid(row=8, columnspan=2)

    # Botón para volver al menú principal
    back_button = tk.Button(root, text="Volver", command=inicio)
    back_button.grid(row=9, columnspan=2)

def inicio():
    """Mostrar la pantalla de inicio con las opciones"""
    # Limpiar la pantalla de opciones anteriores
    for widget in root.winfo_children():
        widget.grid_forget()

    # Crear las opciones principales
    tk.Label(root, text="=== Generador de Instrucciones MIPS ===").grid(row=0, columnspan=2)
    tk.Button(root, text="Generar instrucciones manualmente", command=mostrar_manual).grid(row=1, columnspan=2)
    tk.Button(root, text="Salir", command=root.quit).grid(row=2, columnspan=2)

# Configuración de la ventana principal
root = tk.Tk()
root.title("Generador de Instrucciones MIPS")

# Configuración de los campos de entrada (vacíos inicialmente)
opcode_entry = tk.Entry(root)
rs_entry = tk.Entry(root)
rt_entry = tk.Entry(root)
rd_entry = tk.Entry(root)
shamt_entry = tk.Entry(root)
funct_entry = tk.Entry(root)

# Botón para generar la instrucción
generate_button = tk.Button(root, text="Generar Instrucción", command=generar_instruccion)

# Etiqueta para mostrar las instrucciones generadas
instrucciones_label = tk.Label(root, text="", justify="left")

# Llamar a la función de inicio para mostrar el menú principal
inicio()

# Ejecutar la interfaz gráfica
root.mainloop()
