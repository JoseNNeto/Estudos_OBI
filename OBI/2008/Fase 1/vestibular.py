quest = int(input())
gabarito = str(input().upper())
resposta = str(input().upper())
acertos = 0
for c in range(0, quest):
    if gabarito[c] == resposta[c]:
        acertos += 1
print(acertos)