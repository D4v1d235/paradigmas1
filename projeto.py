import random

# ===== PERSONAGEM =====
jogador = {
    "nome": "Aventureiro",
    "vida": 100,
    "vida_maxima": 100,
    "ataque": 15,
    "nivel": 1,
    "xp": 0,
    "pocoes": 3,
    "ouro": 0,
    "x": 0,
    "y": 0
}

# ===== MAPA =====
mapa = [
    ["🌲", "🌲", "🌿", "🌲", "🌲"],
    ["🌲", "🌿", "🌿", "🏰", "🌲"],
    ["🌿", "🌿", "🌲", "🌿", "🌿"],
    ["🌲", "🌿", "🌿", "🌿", "🌲"],
    ["🌲", "🌲", "🌿", "🌲", "🌲"]
]

# ===== MOSTRAR MAPA =====
def mostrar_mapa():
    print("\n===== MAPA =====")

    for y, linha in enumerate(mapa):
        for x, terreno in enumerate(linha):
            if jogador["x"] == x and jogador["y"] == y:
                print("🧙", end=" ")
            else:
                print(terreno, end=" ")
        print()

    print("\n🧙 Você | 🌲 Floresta | 🌿 Grama | 🏰 Castelo")


# ===== STATUS =====
def mostrar_status():
    print("\n===== PERSONAGEM =====")
    print("Nome:", jogador["nome"])
    print("Nível:", jogador["nivel"])
    print("Vida:", jogador["vida"], "/", jogador["vida_maxima"])
    print("Ataque:", jogador["ataque"])
    print("XP:", jogador["xp"])
    print("Ouro:", jogador["ouro"])
    print("Poções:", jogador["pocoes"])


# ===== MOVIMENTAÇÃO =====
def mover(direcao):
    x = jogador["x"]
    y = jogador["y"]

    if direcao == "w":
        y -= 1
    elif direcao == "s":
        y += 1
    elif direcao == "a":
        x -= 1
    elif direcao == "d":
        x += 1
    else:
        print("Comando inválido!")
        return

    if 0 <= x < 5 and 0 <= y < 5:
        jogador["x"] = x
        jogador["y"] = y
        print("Você se movimentou!")

        if random.random() < 0.35:
            encontrar_monstro()
    else:
        print("Você não pode sair dos limites do mapa!")


# ===== COMBATE =====
def encontrar_monstro():
    monstro = {
        "nome": random.choice(["Goblin", "Esqueleto", "Lobo"]),
        "vida": random.randint(25, 45),
        "ataque": random.randint(5, 12)
    }

    print(f"\nUm {monstro['nome']} apareceu!")

    while monstro["vida"] > 0 and jogador["vida"] > 0:
        print(f"\nSua vida: {jogador['vida']}")
        print(f"Vida do {monstro['nome']}: {monstro['vida']}")
        print("1 - Atacar")
        print("2 - Usar poção")
        print("3 - Fugir")

        escolha = input("> ").strip()

        if escolha == "1":
            dano = random.randint(
                jogador["ataque"] - 3,
                jogador["ataque"] + 5
            )
            monstro["vida"] -= dano
            print(f"Você causou {dano} de dano!")

            if monstro["vida"] <= 0:
                break

        elif escolha == "2":
            if jogador["pocoes"] > 0:
                jogador["pocoes"] -= 1
                cura = 30
                jogador["vida"] = min(
                    jogador["vida_maxima"],
                    jogador["vida"] + cura
                )
                print("Você recuperou vida!")
            else:
                print("Você não tem poções!")
                continue

        elif escolha == "3":
            print("Você fugiu!")
            return

        else:
            print("Escolha inválida!")
            continue

        dano_monstro = monstro["ataque"]
        jogador["vida"] -= dano_monstro
        print(f"O monstro causou {dano_monstro} de dano!")

    if jogador["vida"] <= 0:
        print("\nVocê foi derrotado!")
        return

    print(f"\nVocê derrotou o {monstro['nome']}!")
    jogador["xp"] += 20
    jogador["ouro"] += random.randint(5, 15)
    subir_nivel()


# ===== EVOLUÇÃO =====
def subir_nivel():
    xp_necessario = jogador["nivel"] * 50

    if jogador["xp"] >= xp_necessario:
        jogador["xp"] -= xp_necessario
        jogador["nivel"] += 1
        jogador["ataque"] += 5
        jogador["vida_maxima"] += 20
        jogador["vida"] = jogador["vida_maxima"]

        print("\n🎉 VOCÊ SUBIU DE NÍVEL!")
        print("Novo nível:", jogador["nivel"])


# ===== INVENTÁRIO =====
def mostrar_inventario():
    print("\n===== INVENTÁRIO =====")
    print("Poções:", jogador["pocoes"])
    print("Ouro:", jogador["ouro"])


# ===== JOGO PRINCIPAL =====
def iniciar_jogo():
    print("================================")
    print("       RPG: AVENTURA PYTHON")
    print("================================")

    jogador["nome"] = input("Digite o nome do herói: ").strip()
    if not jogador["nome"]:
        jogador["nome"] = "Aventureiro"

    print(f"\nBem-vindo, {jogador['nome']}!")

    while True:
        if jogador["vida"] <= 0:
            print("\nFim de jogo! Você pode reiniciar o programa.")
            break

        mostrar_mapa()

        print("\n===== MENU =====")
        print("W - Mover para cima")
        print("S - Mover para baixo")
        print("A - Mover para esquerda")
        print("D - Mover para direita")
        print("1 - Ver status")
        print("2 - Ver inventário")
        print("3 - Descansar")
        print("0 - Sair")

        comando = input("\nO que deseja fazer? ").lower().strip()

        if comando in ["w", "a", "s", "d"]:
            mover(comando)

        elif comando == "1":
            mostrar_status()

        elif comando == "2":
            mostrar_inventario()

        elif comando == "3":
            jogador["vida"] = min(
                jogador["vida_maxima"],
                jogador["vida"] + 20
            )
            print("Você descansou e recuperou até 20 de vida!")

        elif comando == "0":
            print("Obrigado por jogar!")
            break

        else:
            print("Comando inválido!")


iniciar_jogo()