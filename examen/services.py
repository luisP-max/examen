def crear_nuevo_estudiante(estudiante, codigo, name, edad, curso, estado):
    """
    Creates a new product dictionary and inserts it into the list.
    Ensures data has the correct format (string, float, integer).
    """
    estudiante.append({
        "ID": float(codigo),
        "name": str (name),
        "edad": float(edad),
        "curso": str (curso),
        "estado": str (estado)
    })  
    
def consultar_lista_estudiante(estudiante):
    """
    Iterates through the list and generates a visual table in the console.
    Uses f-strings with alignment (< for left, > for right) for an organized look.
    """
    if not estudiante:
        print("\n[!] no hay estudiantes registrados.")
        return
    
    # Table header with fixed widths
    print(f"\n{'ID':<20} | {'name':<10} | {'edad':<10} | {'curso':<10} | {'estado':<10}")
    print("-" * 45)
    
    for p in estudiante:
        # :>8.2f formats the price with 2 decimals and aligns it to the right
        print(f"{p['ID']:<20} | {p['name']:>10} | {p['edad']:>8.2f} | {p['curso']:>10} | {p['estado']:>10}")

def buscar_estudiante(estudiante, name):
    """
    Searches for a product ignoring case sensitivity (.lower()).
    Returns the complete dictionary if found, or None if it doesn't exist.
    """
    for p in estudiante:
        if p["name"].lower() == name.lower():
            return p
    return None

def actualizar_informacion_estudiante(estudiante, name, new_edad=None, new_curso=None):
    """Actualiza solo los campos que el usuario decida cambiar."""
    p = buscar_estudiante(estudiante, name)
    if p:
        if new_edad is not None: 
            p["edad"] = float(new_edad)
        if new_curso is not None: 
            p["curso"] = str(new_curso) # Corregido: antes estaba como int()
        return True
    return False
def eliminar_estudiante(estudiante, name):
    """
    Locates the exact object in the list and removes it.
    Returns True if the deletion was successful.
    """
    p = buscar_estudiante(estudiante, name)
    if p:
        estudiante.remove(p)
        return True
    return False