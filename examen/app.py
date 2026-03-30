from services import *
from files import save_csv, load_csv

def run_menu():
    """
    Main function that controls the application flow.
    Maintains the inventory state in memory while the program is running.
    """
    # Initialize the main list that will contain the product dictionaries
    estudiante = []
    # Control variable for the loop
    continue_loop = True

    while continue_loop:
        # Visual Menu Interface
        print("\n" + "="*30)
        print("   INVENTORY SYSTEM")
        print("="*30)
        print("1. registrar estudiante\n2. consultar lista estudiante\n3. buscar estudiante")
        print("4. actualizar informacion estudiantil\n5. eliminar estudiante")
        print("6. guardar datos estudiantiles\n7. cargar datos estudiantiles\n8. Exit")
        
        option = input("\nSelect an option (1-8): ")

        # Add Product
        if option == "1":
            try:
                codigo = int(input("registrar tu ID: "))
                name = input("registrar tu nombre: ").strip()
                edad = float(input("registrar tu edad: "))
                curso = input("nombrar curso o programa que desea estudiar: ")
                estado = input("activo o inactivo: ")
                # Basic business validation
                
                if not codigo: # Corregido while por if para evitar bucle infinito
                    print("[!] Error codigo invalido.")
                else:
                    crear_nuevo_estudiante(estudiante, codigo, name, edad, curso, estado)
                    print("[+] estudiante añadido correctamente.")
            except ValueError:
                # Captures if the user enters letters in price or quantity
                print("[!] Error: por favor numero numerico.")

        # Show Data
        elif option == "2":
            consultar_lista_estudiante(estudiante)

        # Search
        elif option == "3":
            name = input("Name to search: ")
            p = buscar_estudiante(estudiante, name)
            if p:
                print(f"-> Found: ID: {p['ID']} | Nombre: {p['name']} | edad: {p['edad']} | curso: {p['curso']} | estado: {p['estado']}")
            else:
                print("[!] estudiante no encontrado.")

        # Update with validation
        elif option == "4":
            name = input("Nombre del estudiante a modificar: ")
            try:
                n_e = input("Nueva edad (Enter para omitir): ")
                n_c = input("Nuevo curso (Enter para omitir): ")
                
                # Conversión segura
                n_e = float(n_e) if n_e else None
                # El curso suele ser texto, no int
                n_c = n_c if n_c else None 
                
                if actualizar_informacion_estudiante(estudiante, name, n_e, n_c):
                    print("[+] Información actualizada.")
                else:
                    print("[!] Estudiante no encontrado.")
            except ValueError:
                print("[!] Error: La edad debe ser numérica.")

        # Deletion
        elif option == "5":
            name = input("nombre del estudiante que desea eliminar: ")
            if eliminar_estudiante(estudiante, name):
                print(f"[+] '{name}' deleted.")
            else:
                print("[!] estudiante no encontrado.")

        elif option == "6":
            # Calls the files.py module to write the physical CSV
            save_csv(estudiante, "datos_estudiantiles.csv")

        # Input Persistence (Load and Merge)
        elif option == "7":
            data, errors = load_csv("datos_estudiantiles.csv")
            if data is not None:
                confirm = input("deseas sobreescribir los datos actuales? (Y/N): ").upper()
                if confirm == "Y":
                    estudiante = data # Usamos 'estudiante' para mantener consistencia
                    print("[+] datos reemplazados.")
                else:
                    # Merge Logic: looks for matches by name
                    for new_nombre in data:
                        existing = buscar_estudiante(estudiante, new_nombre["name"])
                        if existing:
                            # If exists: add quantity and update to file price
                            existing["edad"] += new_nombre["edad"]
                            existing["curso"] = new_nombre["curso"] 
                        else:
                            # If new: add to the list
                            estudiante.append(new_nombre)
                    print("[+] Data merged successfully.")
                
                if errors > 0:
                    print(f"[!] Notice: {errors} corrupt rows in the file were skipped.")

        # Exit
        elif option == "8":
            print("Closing system... Goodbye!")
            continue_loop = False 

        else:
            print("[!] Invalid option. Please try again (1-8).")

# Script entry point
if __name__ == "__main__":
    run_menu()
