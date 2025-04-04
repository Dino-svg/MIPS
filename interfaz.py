def generar_instruccion_r(opcode=0, rs=0, rt=0, rd=0, shamt=0, funct=0):
    """
    Genera una instrucción tipo R en formato binario de 32 bits
    Formato: opcode(6) | rs(5) | rt(5) | rd(5) | shamt(5) | funct(6)
    
    Parámetros:
    - opcode: 6 bits (0 para instrucciones tipo R)
    - rs: registro fuente 1 (5 bits)
    - rt: registro fuente 2 (5 bits)
    - rd: registro destino (5 bits)
    - shamt: desplazamiento (5 bits, normalmente 0)
    - funct: código de función (6 bits)
    """
    instruccion = (opcode << 26) | (rs << 21) | (rt << 16) | (rd << 11) | (shamt << 6) | funct
    return format(instruccion, '032b')

def mostrar_instruccion(inst_bin):
    """Muestra una instrucción en formato legible"""
    print(f"Binario completo: {inst_bin}")
    print(f"OP: {inst_bin[0:6]}, Rs: {inst_bin[6:11]}, Rt: {inst_bin[11:16]}, Rd: {inst_bin[16:21]}, Shamt: {inst_bin[21:26]}, Funct: {inst_bin[26:32]}")

def guardar_instrucciones(instrucciones, archivo="instructions.txt"):
    """
    Guarda las instrucciones en el formato requerido por memoryInst
    Cada instrucción de 32 bits se divide en 4 bytes (8 bits cada uno)
    """
    with open(archivo, 'w') as f:
        for inst in instrucciones:
            # El módulo memoryInst espera el byte más significativo primero (big-endian)
            f.write(inst[0:8] + "\n")   # Bits 31-24
            f.write(inst[8:16] + "\n")  # Bits 23-16
            f.write(inst[16:24] + "\n") # Bits 15-8
            f.write(inst[24:32] + "\n") # Bits 7-0

def interfaz_generador():
    """
    Interfaz de usuario para generar instrucciones manualmente
    """
    print("Generador de instrucciones MIPS Tipo R")
    print("Formato: OP(6) | Rs(5) | Rt(5) | Rd(5) | shamt(5) | funct(6)")
    print("\nInstrucciones comunes:")
    print("ADD: funct=32, SUB: funct=34, AND: funct=36, OR: funct=37, SLT: funct=42")
    
    instrucciones = []
    
    while True:
        print("\n--- Nueva instrucción ---")
        try:
            # Valores por defecto para instrucción tipo R
            opcode = int(input("Opcode (0 para tipo R): ") or 0)
            rs = int(input("Registro fuente Rs (0-31, ej. 0 para $0): ") or 0)
            rt = int(input("Registro fuente Rt (0-31, ej. 1 para $1): ") or 0)
            rd = int(input("Registro destino Rd (0-31, ej. 4 para $4): ") or 0)
            shamt = int(input("Desplazamiento shamt (0-31, normalmente 0): ") or 0)
            funct = int(input("Código de función funct (0-63): ") or 32)
            
            inst = generar_instruccion_r(opcode, rs, rt, rd, shamt, funct)
            instrucciones.append(inst)
            
            print("\nInstrucción generada:")
            mostrar_instruccion(inst)
            
            if input("\n¿Agregar otra instrucción? (s/n): ").lower() != 's':
                break
                
        except ValueError:
            print("Error: Ingrese valores numéricos válidos")
    
    if instrucciones:
        archivo = input("\nNombre del archivo de salida (default: instructions.txt): ") or "instructions.txt"
        guardar_instrucciones(instrucciones, archivo)
        print(f"\n¡Instrucciones guardadas en {archivo}!")
        print(f"Total de instrucciones generadas: {len(instrucciones)}")
        print("Recuerda copiar este archivo al directorio de tu proyecto Verilog.")
    else:
        print("\nNo se generaron instrucciones.")

# Ejemplo de instrucciones predefinidas (ADD $4, $0, $1 y otras)
def generar_ejemplo():
    print("\nGenerando ejemplo con instrucciones predefinidas...")
    instrucciones = [
        # ADD $4, $0, $1
        generar_instruccion_r(0, 0, 1, 4, 0, 32),
        
        # SUB $5, $2, $3
        generar_instruccion_r(0, 2, 3, 5, 0, 34),
        
        # AND $6, $7, $8
        generar_instruccion_r(0, 7, 8, 6, 0, 36),
        
        # OR $9, $10, $11
        generar_instruccion_r(0, 10, 11, 9, 0, 37)
    ]
    
    print("\nInstrucciones generadas:")
    for i, inst in enumerate(instrucciones, 1):
        print(f"\nInstrucción {i}:")
        mostrar_instruccion(inst)
    
    guardar_instrucciones(instrucciones)
    print("\n¡Ejemplo guardado en instructions.txt!")

if __name__ == "__main__":
    print("=== Generador de Instrucciones MIPS ===")
    print("1. Generar instrucciones manualmente")
    print("2. Generar ejemplo automático (ADD $4, $0, $1 y otras)")
    print("3. Salir")
    
    opcion = input("\nSeleccione una opción (1-3): ")
    
    if opcion == "1":
        interfaz_generador()
    elif opcion == "2":
        generar_ejemplo()
    else:
        print("Saliendo del programa.")