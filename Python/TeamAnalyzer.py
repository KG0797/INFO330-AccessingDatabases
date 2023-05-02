import sqlite3  # This is the package for all sqlite3 access in Python
import sys      # This helps with command-line parameters

conn = sqlite3.connect('pokemon.sqlite')
cursor = conn.cursor()

# All the "against" column suffixes:
types = ["bug","dark","dragon","electric","fairy","fight",
    "fire","flying","ghost","grass","ground","ice","normal",
    "poison","psychic","rock","steel","water"]

# Take six parameters on the command-line
if len(sys.argv) < 6:
    print("You must give me six Pokemon to analyze!")
    sys.exit()

team=[]
for i, arg in enumerate(sys.argv):
    if i == 0:
        continue
        
team = []    
for i in team:
    result = cursor.execute("SELECT name, type1, type2, against_bug, against_dark, against_dragon, against_electric, against_fairy, against_fight, against_fire, against_flying, against_ghost, against_grass, against_ground, against_ice, against_normal, against_poison, against_psychic, against_rock, against_steel, against_water FROM imported_pokemon_data WHERE pokedex_number = {}".format(i))
    pokemon_list = list(cursor.fetchone())
    strong = []
    weak = []
    against_list = pokemon_list[3:]
    print("Analyzing", i)

    for a in range(len(against_list)):
        if float(against_list[a]) > 1:
            strong.append(types[a])
        elif float(against_list[a]) < 1:
            weak.append(types[a])
        else:
            continue
    print("{} ({} {}) is strong against {} but weak against {}".format(pokemon_list[0], pokemon_list[1], pokemon_list[2], strong, weak))  
 
answer = input("Would you like to save this team? (Y)es or (N)o: ")
if answer.upper() == "Y" or answer.upper() == "YES":
    teamName = input("Enter the team name: ")

    # Write the pokemon team to the "teams" table
    print("Saving " + teamName + " ...")
else:
    print("Bye for now!")
    
