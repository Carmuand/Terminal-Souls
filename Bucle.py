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