# Projeto EcoSort - Express-Cargo

pesos = []
fretes = []

total_peso = 0
total_frete = 0

print("===== SISTEMA ECOSORT =====")

for i in range(10):
    print(f"\nPacote {i + 1}")

    # Validação do peso
    while True:
        peso = float(input("Digite o peso do pacote (kg): "))
        if peso >= 0:
            break
        print("ERRO! O peso não pode ser negativo.")

    # Validação do destino
    while True:
        destino = input("Destino (Nacional/Internacional): ").strip().lower()

        if destino == "nacional" or destino == "internacional":
            break

        print("ERRO! Digite apenas Nacional ou Internacional.")

    # Classificação e valor base
    if peso <= 2:
        categoria = "Leve"
        frete = 10.0

    elif peso <= 10:
        categoria = "Padrão"
        frete = 20.0

    else:
        categoria = "Pesado"
        frete = 30.0

    # Acréscimo para internacional
    if destino == "internacional":
        frete = frete * 1.20

    # Armazenamento nos vetores
    pesos.append(peso)
    fretes.append(frete)

    # Acumuladores
    total_peso += peso
    total_frete += frete

    print(f"Categoria: {categoria}")
    print(f"Frete: R$ {frete:.2f}")

# Relatório final
ticket_medio = total_frete / 10

print("\n========== RESULTADO FINAL ==========")
print(f"Total de pacotes: {len(pesos)}")
print(f"Carga total acumulada: {total_peso:.2f} kg")
print(f"Faturamento bruto do lote: R$ {total_frete:.2f}")
print(f"Ticket médio por pacote: R$ {ticket_medio:.2f}")
print("====================================")