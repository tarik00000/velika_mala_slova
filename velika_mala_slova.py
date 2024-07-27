# Napiši program koji unosi string (velikim slovima) i broj n, a zatim pretvara prvih n slova stringa u mala slova.
string = input("Unesi string: ")
n = int(input("Unesi broj: "))
novi_string = string[:n].lower()+string[n:]
print(novi_string)
