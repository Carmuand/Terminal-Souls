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