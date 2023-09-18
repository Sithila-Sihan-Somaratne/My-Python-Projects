#This is UOM Python 2 
#Lesson 1.4: Sets

############# Tuples #############

data_type = ("String", 10, 5.7, True)
print(type(data_type))

benelux = "Luxembourg", "Belgium", "Netherlands"
print(benelux)

bear_land = ("Russia")
print(type(bear_land))
print(bear_land)
bear_land = ("Russia",)
print(type(bear_land))
print(bear_land)

super_powers = ("USA", "URSS")

print(super_powers[0]+" is the current super power.")
print(super_powers[1]+" was an old super power dissoluted in 1990/1991 (End of Cold War).")

potential_super_powers = ("China", "India", "Russia")
print(potential_super_powers[-3])
print(potential_super_powers[-2])
print(potential_super_powers[-1])

all_super_powers = ("USA", "Russia", "China", "India")
print(all_super_powers[1:4])

allies_enemies = (("German Empire", "Austria-Hungary", "Ottoman Empire"),("Nazi Germany", "Fascist Italy", "Nationalist Japan"))

SAARC = ("India", "Pakistan", "Bangaldesh", "Afghanistan", "Nepal", "Bhutan", "Sri Lanka", "Maldives")
print(len(SAARC))

British_Raj = ("India", "Pakistan", "Bangladesh", "Maldive")
Ex_British_Colonies = ("Myanmar", "Sri Lanka", "Afghanistan")
Indipendent_Nations = ("Nepal", "Bhutan")

Akhand_Bharat = British_Raj + Ex_British_Colonies + Indipendent_Nations

print(Akhand_Bharat)

my_tuple = ("tuple",) * 5

print(my_tuple)

trueorfalse = "Tibet" in Akhand_Bharat
print(trueorfalse)

for country in Akhand_Bharat:
    print(country)
