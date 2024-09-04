def count_a_in_string(s):
    count = s.lower().count('a')
    return count

# String a ser verificada
string = input("Informe uma string: ")

count = count_a_in_string(string)

if count > 0:
    print(f"A letra 'a' aparece {count} vez(es) na string.")
else:
    print("A letra 'a' não aparece na string.")