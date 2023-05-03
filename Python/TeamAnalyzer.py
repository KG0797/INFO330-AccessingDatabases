import sqlite3  # This is the package for all sqlite3 access in Python
import sys      # This helps with command-line parameters

# All the "against" column suffixes:
types = ["bug","dark","dragon","electric","fairy","fight",
    "fire","flying","ghost","grass","ground","ice","normal",
    "poison","psychic","rock","steel","water"]

# Take six parameters on the command-line
if len(sys.argv) < 6:
    print("You must give me six Pokemon to analyze!")
    sys.exit()
team=[sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6]]

conn = sqlite3.connect(r'C:\Users\Katherine Guo\Desktop\info330\INFO330-AccessingDatabases\pokemon.sqlite')
cursor = conn.cursor()
<<<<<<< HEAD



=======
print(cursor.execute('select * from pokemon limit ').fetchone())
print('hello world')
>>>>>>> a68c9113b4073eee42e150796ca9735604631ec0
for i, arg in enumerate(sys.argv):
    if i == 0:
        continue
for i in team:
    result = cursor.execute("""Select pokedex_number,name,pokemon_type1,pokemon_type2,against_bug,against_dark,against_dragon,against_electric,against_fairy,against_fight,against_fire,against_flying,against_ghost,against_grass,against_ground,against_ice,against_normal,against_poison,against_psychic,against_rock,against_steel,against_water from 
(
Select t1.pokemon_id,pokemon_type1,pokemon_type2,type_id1,type_id2 from 
(
Select a.pokemon_id,b.name as pokemon_type1,type_id as type_id1 from
(Select pokemon_id,type_id from pokemon_type
Where which=1 ) a
Left join 
(Select id, name from type) b on a. type_id=b.id) t1 
Left join 
(
Select a.pokemon_id,b.name as pokemon_type2,type_id as type_id2 from
(Select pokemon_id,type_id from pokemon_type
Where which=2 ) a
Left join 
(Select id, name from type) b on a. type_id=b.id
) t2 on t1.pokemon_id=t2.pokemon_id
) tt1
Left join 
(
Select id,pokedex_number,name from pokemon
) tt2 on tt1.pokemon_id=tt2.id
Left join 
(
Select * from against
) tt3 on tt1.type_id1=tt3.type_source_id1 and tt1.type_id2=tt3.type_source_id2 WHERE pokedex_number = {}""".format(i))
    pokemon_list = list(cursor.fetchone())
    strong = []
    weak = []
    against_list = pokemon_list[4:]
    print("Analyzing", i)

    for a in range(len(against_list)):
        if float(against_list[a]) > 1:
            strong.append(types[a])
        elif float(against_list[a]) < 1:
            weak.append(types[a])
        else:
            continue
    print("{} ({} {}) is strong against {} but weak against {}".format(pokemon_list[1], pokemon_list[2], pokemon_list[3], strong, weak))  
 
answer = input("Would you like to save this team? (Y)es or (N)o: ")
if answer.upper() == "Y" or answer.upper() == "YES":
    teamName = input("Enter the team name: ")

    # Write the pokemon team to the "teams" table
    print("Saving " + teamName + " ...")
else:
    print("Bye for now!")
