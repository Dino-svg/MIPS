import tkinter as tk
from tkinter import messagebox

def detectar_tipo(opcode_str):
    try:
        # Detectar si el opcode viene en binario o decimal
        if set(opcode_str) <= {"0", "1"} and len(opcode_str) <= 6:
            opcode = int(opcode_str, 2)
        else:
            opcode = int(opcode_str)

        if opcode == 0:
            return "R"
        elif opcode in [2, 3]:  # J, JAL
            return "J"
        else:
            return "I"
    except ValueError:
        return None

def actualizar_campos(event=None):
    tipo = detectar_tipo(opcode_entry.get())

    for widget in campos_dinamicos:
        widget.grid_remove()

    if tipo == "R":
        rs_label.grid(row=1, column=0)
        rs_entry.grid(row=1, column=1)

        rt_label.grid(row=2, column=0)
        rt_entry.grid(row=2, column=1)

        rd_label.grid(row=3, column=0)
        rd_entry.grid(row=3, column=1)

        shamt_label.grid(row=4, column=0)
        shamt_entry.grid(row=4, column=1)

        funct_label.grid(row=5, column=0)
        funct_entry.grid(row=5, column=1)

    elif tipo == "I":
        rs_label.grid(row=1, column=0)
        rs_entry.grid(row=1, column=1)

        rt_label.grid(row=2, column=0)
        rt_entry.grid(row=2, column=1)

        immediate_label.grid(row=3, column=0)
        immediate_entry.grid(row=3, column=1)

    elif tipo == "J":
        address_label.grid(row=1, column=0)
        address_entry.grid(row=1, column=1)

def generar_instruccion():
    try:
        tipo = detectar_tipo(opcode_entry.get())
        if tipo is None:
            messagebox.showerror("Error", "Opcode inválido.")
            return

        opcode = int(opcode_entry.get(), 2) if set(opcode_entry.get()) <= {"0", "1"} else int(opcode_entry.get())

        if tipo == "R":
            rs = int(rs_entry.get())
            rt = int(rt_entry.get())
            rd = int(rd_entry.get())
            shamt = int(shamt_entry.get())
            funct = int(funct_entry.get())
            instruccion = (opcode << 26) | (rs << 21) | (rt << 16) | (rd << 11) | (shamt << 6) | funct
            binario = format(instruccion, '032b')
            result = f"Tipo R\nBinario: {binario}"

        elif tipo == "I":
            rs = int(rs_entry.get())
            rt = int(rt_entry.get())
            immediate = int(immediate_entry.get()) & 0xFFFF
            instruccion = (opcode << 26) | (rs << 21) | (rt << 16) | immediate
            binario = format(instruccion, '032b')
            result = f"Tipo I\nBinario: {binario}"

        elif tipo == "J":
            address = int(address_entry.get()) & 0x3FFFFFF
            instruccion = (opcode << 26) | address
            binario = format(instruccion, '032b')
            result = f"Tipo J\nBinario: {binario}"

        instrucciones_label.config(text=instrucciones_label.cget("text") + "\n\n" + result)
        limpiar_campos()

    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa valores numéricos válidos.")

def limpiar_campos():
    rs_entry.delete(0, tk.END)
    rt_entry.delete(0, tk.END)
    rd_entry.delete(0, tk.END)
    shamt_entry.delete(0, tk.END)
    funct_entry.delete(0, tk.END)
    immediate_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

def mostrar_manual():
    for widget in root.winfo_children():
        widget.grid_forget()

    tk.Label(root, text="Opcode (decimal o binario de 6 bits):").grid(row=0, column=0)
    opcode_entry.grid(row=0, column=1)
    opcode_entry.bind("<KeyRelease>", actualizar_campos)

    generate_button.grid(row=10, columnspan=2)
    instrucciones_label.grid(row=11, columnspan=2)
    back_button.grid(row=12, columnspan=2)

def inicio():
    for widget in root.winfo_children():
        widget.grid_forget()

    tk.Label(root, text="=== Generador de Instrucciones MIPS ===").grid(row=0, columnspan=2)
    tk.Button(root, text="Generar instrucciones manualmente", command=mostrar_manual).grid(row=1, columnspan=2)
    tk.Button(root, text="Salir", command=root.quit).grid(row=2, columnspan=2)

# --- Interfaz
root = tk.Tk()
root.title("Generador de Instrucciones MIPS")

opcode_entry = tk.Entry(root)
rs_entry = tk.Entry(root)
rt_entry = tk.Entry(root)
rd_entry = tk.Entry(root)
shamt_entry = tk.Entry(root)
funct_entry = tk.Entry(root)
immediate_entry = tk.Entry(root)
address_entry = tk.Entry(root)

rs_label = tk.Label(root, text="Rs (5 bits):")
rt_label = tk.Label(root, text="Rt (5 bits):")
rd_label = tk.Label(root, text="Rd (5 bits):")
shamt_label = tk.Label(root, text="Shamt (5 bits):")
funct_label = tk.Label(root, text="Funct (6 bits):")
immediate_label = tk.Label(root, text="Immediate (16 bits):")
address_label = tk.Label(root, text="Address (26 bits):")

campos_dinamicos = [
    rs_label, rs_entry,
    rt_label, rt_entry,
    rd_label, rd_entry,
    shamt_label, shamt_entry,
    funct_label, funct_entry,
    immediate_label, immediate_entry,
    address_label, address_entry
]

generate_button = tk.Button(root, text="Generar Instrucción", command=generar_instruccion)
instrucciones_label = tk.Label(root, text="", justify="left")
back_button = tk.Button(root, text="Volver", command=inicio)

inicio()
root.mainloop()
