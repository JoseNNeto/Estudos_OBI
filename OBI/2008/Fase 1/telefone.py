texto = str(input().upper())
separado = texto.split(' ')
tamanho = len(texto)
numero = []
for letra in texto:
    if letra == '1':
        numero.append(int(1))
    elif letra == 'A' or letra == 'B' or letra == 'C':
        numero.append(int(2))
    elif letra == 'D' or letra == 'E' or letra == 'F':
        numero.append(int(3))
    elif letra == 'G' or letra == 'H' or letra == 'I':
        numero.append(int(4))
    elif letra == 'J' or letra == 'K' or letra == 'L':
        numero.append(int(5))
    elif letra == 'M' or letra == 'N' or letra == 'O':
        numero.append(int(6))
    elif letra == 'P' or letra == 'Q' or letra == 'R' or letra == 'S':
        numero.append(int(7))
    elif letra == 'T' or letra == 'U' or letra == 'V':
        numero.append(int(8))
    elif letra == 'W' or letra == 'X' or letra == 'Y':
        numero.append(int(9))
    elif letra == '-':
        numero.append('-')
numero = numero
resultado = "".join(map(str, numero))
print(resultado)