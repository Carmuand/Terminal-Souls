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
# BARRA DE VIDA
# ─────────────────────────────
def barra_vida(hp, max_hp):
    total = 20
    llenas = int((hp / max_hp) * total)
    return "█" * llenas + "-" * (total - llenas)

# ─────────────────────────────
# MOSTRAR ESTADO
# ─────────────────────────────
def mostrar_estado():
    print("\n" + "="*50)
    print("        ⚔️  ESTADO DEL COMBATE ⚔️")
    print("="*50)

    print(f"HÉROE   ❤️ {hp_heroe}/100")
    print(f"[{barra_vida(hp_heroe, 100)}]")

    print(f"\nENEMIGO 🎃 {hp_enemigo}/120")
    print(f"[{barra_vida(hp_enemigo, 120)}]")

    print(f"\n💉 Pociones: {pociones}")
    print("="*50)

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

# ─────────────────────────────
# TURNO DEL ENEMIGO
# ─────────────────────────────
def turno_enemigo():
    global hp_heroe, hp_enemigo, pociones_enemigo

    print("\n🎃 TURNO DEL ENEMIGO")

    # Si está por debajo del 20% de vida
    if hp_enemigo <= 24:
        if pociones_enemigo > 0:
            curacion = int(120 * 0.30)  # 36 HP
            hp_enemigo += curacion
            pociones_enemigo -= 1

            if hp_enemigo > 120:
                hp_enemigo = 120

            print(f"💉 El enemigo se cura {curacion} HP")
            print(f"💉 Pociones restantes: {pociones_enemigo}")
            return  # 🚨 IMPORTANTE: termina el turno aquí

        else:
            print("❌ El enemigo intentó curarse pero no tiene pociones")

    # Si NO se cura → ataca
    daño = generar_daño(15, 20)
    hp_heroe -= daño
    print(f"💥 El enemigo ataca y causa {daño} de daño")

# ─────────────────────────────
# VERIFICAR GANADOR
# ─────────────────────────────
def verificar_ganador():
    if hp_heroe <= 0 or hp_enemigo <= 0:
        return True
    return False

# ─────────────────────────────
# BUCLE PRINCIPAL
# ─────────────────────────────
print("="*50)
print("        🎮 TERMINAL SOULS 🎮")
print("="*50)
print("🏹 ¡El Héroe se enfrenta al Enemigo!\n")

while not verificar_ganador():
    mostrar_estado()
    turno_jugador()

    if verificar_ganador():
        break

    turno_enemigo()

# RESULTADO FINAL
print("\n" + "="*50)
if hp_heroe <= 0:
    print("☠️¡El Héroe fue derrotado!☠️")
else:
    print("🎇🎇🎇🎇🎇🎇🎇🎇🎇🎇🎇🎇🎇🎇🎇🎇 ¡El Héroe ganó la batalla!🎇🎇🎇🎇🎇🎇🎇🎇🎇🎇🎇🎇🎇🎇🎇🎇")
print("="*50)