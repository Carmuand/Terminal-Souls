def barra_vida(hp, max_hp):
    total = int(max_hp / 5)  # escala proporcional
    llenas = int((hp / max_hp) * total)
    return "█" * llenas + "-" * (total - llenas)