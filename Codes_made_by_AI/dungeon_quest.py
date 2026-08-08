import random

# ==========================
# PLAYER DATA
# ==========================

player = {
    "name": "",
    "hp": 100,
    "max_hp": 100,
    "attack": 10,
    "level": 1,
    "xp": 0,
    "gold": 0
}

inventory = {
    "potion": 3,
    "elixir": 1
}

# ==========================
# ENEMY DATA
# ==========================

enemies = [
    {"name": "Goblin", "hp": 30, "attack": 5, "xp": 10},
    {"name": "Skeleton", "hp": 40, "attack": 7, "xp": 15},
    {"name": "Orc", "hp": 60, "attack": 10, "xp": 25},
    {"name": "Dark Knight", "hp": 80, "attack": 12, "xp": 35}
]

# ==========================
# FUNCTIONS
# ==========================

def show_status():
    print("\n📊 PLAYER STATUS")
    print("----------------")
    print(f"Name   : {player['name']}")
    print(f"Level  : {player['level']}")
    print(f"HP     : {player['hp']}/{player['max_hp']}")
    print(f"Attack : {player['attack']}")
    print(f"XP     : {player['xp']}")
    print(f"Gold   : {player['gold']}")
    print(f"Items  : {inventory}")

def level_up():
    need_xp = player["level"] * 30
    if player["xp"] >= need_xp:
        player["level"] += 1
        player["xp"] -= need_xp
        player["max_hp"] += 20
        player["hp"] = player["max_hp"]
        player["attack"] += 5
        print("\n⬆️ LEVEL UP!")
        print("Your power has increased!")

def use_item():
    print("\n🎒 INVENTORY")
    print("1. Potion (+30 HP)")
    print("2. Elixir (+50 HP)")
    print("3. Back")

    choice = input("Choose item: ")

    if choice == "1" and inventory["potion"] > 0:
        inventory["potion"] -= 1
        player["hp"] += 30
        if player["hp"] > player["max_hp"]:
            player["hp"] = player["max_hp"]
        print("🧪 You used a potion!")
    elif choice == "2" and inventory["elixir"] > 0:
        inventory["elixir"] -= 1
        player["hp"] += 50
        if player["hp"] > player["max_hp"]:
            player["hp"] = player["max_hp"]
        print("✨ You used an elixir!")
    else:
        print("Nothing used.")

def fight():
    enemy = random.choice(enemies).copy()

    print(f"\n⚔️ A wild {enemy['name']} appears!")

    while enemy["hp"] > 0 and player["hp"] > 0:
        print(f"\nYour HP: {player['hp']} | Enemy HP: {enemy['hp']}")
        print("1. Attack")
        print("2. Use item")
        print("3. Run")

        action = input("Choose action: ")

        if action == "1":
            dmg = random.randint(player["attack"] - 3, player["attack"] + 5)
            enemy["hp"] -= dmg
            print(f"💥 You deal {dmg} damage!")

            if enemy["hp"] > 0:
                edmg = random.randint(1, enemy["attack"])
                player["hp"] -= edmg
                print(f"😵 Enemy hits
