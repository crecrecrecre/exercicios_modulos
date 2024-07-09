from uteis import calcular_filtragem, calcular_volume, calcular_potencia_termostato

comprimento = float(input("Digite o comprimento do aquário (cm): "))
altura = float(input("Digite a altura do aquário (cm): "))
largura = float(input("Digite a largura do aquário (cm): "))
temp_desejada = float(input("Digite a temperatura desejada (°C): "))
temp_ambiente = float(input("Digite a temperatura ambiente (°C): "))

volume = calcular_volume(comprimento, altura, largura)

potencia_termostato = calcular_potencia_termostato(volume, temp_desejada, temp_ambiente)

filtragem_min, filtragem_max = calcular_filtragem(volume)

print(f"\nVolume do aquário: {volume:.2f} litros")
print(f"Potência do termostato necessária: {potencia_termostato:.2f} watts")
print(f"Quantidade de filtragem por hora: entre {filtragem_min:.2f} e {filtragem_max:.2f} litros por hora")
