import random

# ─────────────────────────────
# ATTRIBUTES
# ─────────────────────────────
hero_hp = 100
enemy_hp = 120
potions = 3
enemy_potions = 1

# ─────────────────────────────
# GENERATE DAMAGE
# ─────────────────────────────
def generate_damage(minimum, maximum):
    return random.randint(minimum, maximum)

# ─────────────────────────────
# HEALTH BAR
# ─────────────────────────────
def health_bar(hp, max_hp):
    total = int(max_hp / 5)  # proportional scale
    filled = int((hp / max_hp) * total)
    return "█" * filled + "-" * (total - filled)

# ─────────────────────────────
# SHOW STATUS
# ─────────────────────────────
def show_status():
    print("\n" + "="*50)
    print("        ⚔️  COMBAT STATUS ⚔️")
    print("="*50)

    print(f"HERO    ❤️ {hero_hp}/100")
    print(f"[{health_bar(hero_hp, 100)}]")

    print(f"\nENEMY   🎃 {enemy_hp}/120")
    print(f"[{health_bar(enemy_hp, 120)}]")

    print(f"\n💉 Potions: {potions}")
    print("="*50)

# ─────────────────────────────
# PLAYER TURN
# ─────────────────────────────
def player_turn():
    global hero_hp, enemy_hp, potions

    print("\n🎮 YOUR TURN")
    print("1. 🏹 Attack")
    print("2. 💉 Heal")
    print("3. 💥 Special Ability")

    option = input("👉 Choose (1, 2 or 3): ")

    if option == "1":
        damage = generate_damage(10, 25)
        enemy_hp -= damage
        print(f"🥊 You hit the enemy for {damage} damage 🥊")

    elif option == "2":
        if potions > 0:
            potions -= 1
            hero_hp += 20
            if hero_hp > 100:
                hero_hp = 100
            print("💉 You used a potion (+20 HP)")
        else:
            print("❌ You have no potions")

    elif option == "3":
        if random.randint(1, 2) == 1:
            print("❌ You missed the ability")
        else:
            damage = generate_damage(30, 50)
            enemy_hp -= damage
            print(f"🔥 Special ability deals {damage} damage")

    else:
        print("❌ Invalid option")
        player_turn()

# ─────────────────────────────
# ENEMY TURN
# ─────────────────────────────
def enemy_turn():
    global hero_hp, enemy_hp, enemy_potions

    print("\n🎃 ENEMY TURN")

    # If below 20% health
    if enemy_hp <= 24:
        if enemy_potions > 0:
            healing = int(120 * 0.30)  # 36 HP
            enemy_hp += healing
            enemy_potions -= 1

            if enemy_hp > 120:
                enemy_hp = 120

            print(f"💉 The enemy heals {healing} HP")
            print(f"💉 Remaining potions: {enemy_potions}")
            return  # 🚨 IMPORTANT: end turn here

        else:
            print("❌ The enemy tried to heal but has no potions")

    # If NOT healing → attacks
    damage = generate_damage(15, 20)
    hero_hp -= damage
    print(f"💥 The enemy attacks and deals {damage} damage")

# ─────────────────────────────
# CHECK WINNER
# ─────────────────────────────
def check_winner():
    if hero_hp <= 0 or enemy_hp <= 0:
        return True
    return False

# ─────────────────────────────
# MAIN LOOP
# ─────────────────────────────
print("="*50)
print("        🎮 TERMINAL SOULS 🎮")
print("="*50)
print("🏹 The Hero faces the Enemy!\n")

while not check_winner():
    show_status()
    player_turn()

    if check_winner():
        break

    enemy_turn()

# FINAL RESULT
print("\n" + "="*50)
if hero_hp <= 0:
    print("☠️ The Hero was defeated! ☠️")
else:
    print("🎇🎇🎇🎇🎇🎇🎇🎇🎇🎇🎇🎇🎇🎇🎇🎇 The Hero won the battle! 🎇🎇🎇🎇🎇🎇🎇🎇🎇🎇🎇🎇🎇🎇🎇🎇")
print("="*50)
