import random

# ─────────────────────────────
# ATRIBUTOS
# ─────────────────────────────
hp_heroe = 100
hp_enemigo = 120
pociones = 3
pociones_enemigo = 1

# ─────────────────────────────
# GENERAR DAÑO
# ─────────────────────────────
def generar_daño(minimo, maximo):
    return random.randint(minimo, maximo)

# ─────────────────────────────
# TURNO DEL JUGADOR
# ─────────────────────────────
def turno_jugador():
    global hp_heroe, hp_enemigo, pociones

    print("\n🎮 TU TURNO")
    print("1. 🏹 Atacar")
    print("2. 💉 Curarse")
    print("3. 💥 Habilidad especial")

    opcion = input("👉 Elige (1, 2 o 3): ")

    if opcion == "1":
        daño = generar_daño(10, 25)
        hp_enemigo -= daño
        print(f"🥊 Golpeas al enemigo por {daño} de daño🥊")

    elif opcion == "2":
        if pociones > 0:
            pociones -= 1
            hp_heroe += 20
            if hp_heroe > 100:
                hp_heroe = 100
            print("💉 Usaste una poción (+20 HP)")
        else:
            print("❌ No tienes pociones")

    elif opcion == "3":
        if random.randint(1, 2) == 1:
            print("❌ Fallaste la habilidad")
        else:
            daño = generar_daño(30, 50)
            hp_enemigo -= daño
            print(f"🔥 Habilidad especial causa {daño} de daño")

    else:
        print("❌ Opción inválida")
        turno_jugador()