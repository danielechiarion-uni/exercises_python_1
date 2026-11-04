import string

try:
    file_path = input("Inserisci il percorso del file: ")
    with open(file_path, "r") as file:
        content = file.read().lower()
    
    # count the occurences for every letter
    content_length = 0
    for character in content:
        if character >= 'a' and character <= 'z':
            content_length += 1
    
    for i in string.ascii_lowercase:
        letter_freq = content.count(i) / content_length * 100
        print(f"{i}\t{letter_freq:.2f}%")
except FileNotFoundError:
    print("File non trovato")
