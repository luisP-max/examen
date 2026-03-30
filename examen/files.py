import csv

def save_csv(estudiante, path):
    """
    Saves the list of dictionaries into a physical .csv file.
    Parameters:
        - estudiante: lista de estudiantes.
        - path: file name or path (example: 'data.csv').
    """
    # Safety validation: do not save empty files
    if not estudiante:
        print("[!] Error: No data to save.")
        return False
    
    try:
        # Attempt to open file in write mode ('w')
        # newline='' prevents extra blank lines
        with open(path, 'w', newline='', encoding='utf-8') as f:
            # Define column names (header)
            fields = ["ID", "name", "edad", "curso", "estado"]
            writer = csv.DictWriter(f, fieldnames=fields)
            
            # Write the first row with titles
            writer.writeheader()
            # Write all dictionaries from the list
            writer.writerows(estudiante)
            
        print(f"[+] estudiante successfully saved to: {path}")
        return True
        
    except (PermissionError, IOError) as e:
        # Capture permission errors
        print(f"[!] Writing error: {e}")
        return False

def load_csv(path):
    """
    Reads a CSV file and transforms it into a Python list.
    Returns: (product_list, error_count)
    """
    cargar_estudiante = []
    row_errors = 0
    
    try:
        # Open file in read mode ('r')
        with open(path, 'r', encoding='utf-8') as f:
            # DictReader uses the first row (header) to create dictionaries for each line
            reader = csv.DictReader(f)
            
            for row in reader:
                try:
                    # Data cleaning and validation process
                    codigo = float(row['codigo'])
                    name = row['name'].strip()      # Remove extra spaces
                    edad = float(row['edad'])     # Convert text to decimal
                    curso = row['curso'] # Convert text to integer
                    
                    # Business rule: no negative values
                    if codigo < 0 or edad < 0: 
                        raise ValueError
                    
                    # If data is valid, add to the temporary list
                    cargar_estudiante.append({
                        "ID": codigo,
                        "name": name,
                        "edad": edad,
                        "curso": curso,
                    })
                except (KeyError, ValueError, TypeError):
                    # If a column is missing or data is not numeric, skip the row
                    row_errors += 1
                    
        return cargar_estudiante, row_errors
        
    except FileNotFoundError:
        # If the user tries to load something that doesn't exist
        print("[!] The file does not exist.")
        return None, 0
    except Exception as e:
        # Capture any other technical error (corrupt file, etc.)
        print(f"[!] Unexpected error while reading: {e}")
        return None, 0