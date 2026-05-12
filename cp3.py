temperaturas = [[28, 31, 34, 33], [25, 27, 29, 28], [32, 35, 36, 34], [24, 26, 25, 27]]

maior_criticos = -1
maior_sala = -1
for sala, temps in enumerate(temperaturas):
    soma = 0
    criticas = 0
    for i in temps:
        soma += i
        if i >= 33:
            criticas += 1
    
    if criticas > maior_criticos:
        maior_criticos = criticas
        maior_sala = sala + 1

    print(f"Sala {sala + 1}")
    print(f"Média: {soma/len(temps)}")
    print(f"Registros críticos: {criticas}\n")

print(f'Sala com maior risco: Sala {maior_sala}')

    