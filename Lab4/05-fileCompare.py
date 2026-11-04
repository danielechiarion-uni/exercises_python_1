try:
    file_path1 = input("Inserisci il primo percorso: ").strip()
    file_path2 = input("Inserisci il secondo percorso: ").strip()
    
    with open(file_path1, "r") as file:
        content1 = file.read().strip()
    with open(file_path2, "r") as file:
        content2 = file.read().strip()
        
    if content1 == content2:
        print("Il contenuto dei due file corrisponde")
    else:
        print("Il contenuto dei due file non corrisponde")
except FileNotFoundError:
    print("File non trovato")
