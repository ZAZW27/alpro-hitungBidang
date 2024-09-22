import random, os, time
os.system('cls') if os.name == 'nt' else os.system('clear')
print(".:Pertualangan melawan naga:.")

my_hp = 100
naga_hp = 200

init_roll = 3

luck = 0
defend = 0
att = 0

print("Choose your initial 3 traits")
# ================================================= Start ==================================================================
# =============================================LOOP INIT TRAIT==============================================================
# ================================================= Start ==================================================================
while init_roll:
    print(f"1. Luck     : {luck}")
    print(f"2. Defend   : {defend}")
    print(f"3. Attack   : {att}")

    choice = input("------------- Choose the number: ")

    if choice == '1': 
        luck += 1
    elif choice == '2': 
        defend += 1
    elif choice == '3': 
        att += 1
    else: 
        print("Invalid! Coba lagi!")

    init_roll -= 1
# ================================================== END ===================================================================
# =============================================LOOP INIT TRAIT==============================================================
# ================================================== END ===================================================================

os.system('cls') if os.name == 'nt' else os.system('clear')

print(f"----------- Your initial traits!")
print(f"1. Luck     : {luck}")
print(f"2. Defend   : {defend}")
print(f"3. Attack   : {att}")

# ================================================= Start ==================================================================
# =============================================LOOP PERMAINAN===============================================================
# ================================================= Start ==================================================================
while my_hp > 0 and naga_hp > 0:
    input("\n---==== ENTER TO ROLL ====----")
    
    time.sleep(0.5)
    my_roll = int(random.randint(1 + luck, 13 + luck))
    input(f"Kamu mendapatkan {my_roll}. ENTER TO CONTINUE:")
    
    time.sleep(0.5)
    naga_roll = random.randint(5, 16)
    input(f"Naga mendapatkan {naga_roll}. ENTER TO CONTINUE:")
    
    if my_roll == 6 or my_roll == 12 or my_roll == 16: 
        print(f"\nAnda dapat trait point, coba pilih trait yang anda inginkan selain pilihan dibawah kamu akan diberi {my_roll}+ hp")
        print(f"1. Luck     : {luck}")
        print(f"2. Defend   : {defend}")
        print(f"3. Attack   : {att}")

        choice = input("------------- Choose the number: ")

        if choice == '1': 
            luck += 1
        elif choice == '2': 
            defend += 1
        elif choice == '3': 
            att += 1
        else: 
            my_hp += my_roll

    # User dapat pilihan reroll jika mendapatkan roll 4 / 8 / 14
    elif my_roll == 4 or my_roll == 8 or my_roll == 14: 
        if input("\nAnda dapat angka reroll, apakah mau reroll? y/n: ") == 'y': 
            continue
        else: 
            print("Kamu melanjut menyerang!")

    if my_roll > naga_roll: 
        damage = (my_roll + int(att * 1.7)) - int(naga_roll / 2)
        naga_hp -= damage
        
        print(f"\nKamu menyerang naga sebanyak \033[31m{damage}\033[37m damage!")
        
    elif my_roll < naga_roll: 
        damage = naga_roll - int((defend * 1.2) + (my_roll / 2)) 
        my_hp -= damage if damage > 0 else 0
        
        print(f"\nKamu diserang sebanyak \033[31m{damage if damage > 0 else 0}\033[37m damage!")

    print("------Current Hitpoints: ")
    print(f"My HP: {my_hp}")
    print(f"Naga HP: {naga_hp}")

if my_hp <= 0: 
    print("\033[31m==================== You Lose! ====================\033[37m")
elif naga_hp <= 0: 
    print("\033[32m==================== You Win! ====================\033[37m")
# ================================================== END ===================================================================
# =============================================LOOP PERMAINAN===============================================================
# ================================================== END ===================================================================