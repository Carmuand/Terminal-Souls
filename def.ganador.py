# ─────────────────────────────
# VERIFICAR GANADOR
# ─────────────────────────────
def verificar_ganador():
    if hp_heroe <= 0 or hp_enemigo <= 0:
        return True
    return False

# RESULTADO FINAL
print("\n" + "="*50)
if hp_heroe <= 0:
    print("☠️¡El Héroe fue derrotado!☠️")
else:
    print("🎇🎇🎇🎇🎇🎇🎇🎇🎇🎇🎇🎇🎇🎇🎇🎇 ¡El Héroe ganó la batalla!🎇🎇🎇🎇🎇🎇🎇🎇🎇🎇🎇🎇🎇🎇🎇🎇")
print("="*50)