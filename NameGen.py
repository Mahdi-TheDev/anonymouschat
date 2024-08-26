import random


flowers = [
    "Sorkh", "Laleh", "Narges", "Yas", "Sadaf", "Sogand", "Zafaran", "Sambal", "Bahar Narenj", "Shirin Gol",
    "Shahdad", "Marzam", "Nabati", "Khar", "Khazar", "Fars", "NargisMah", "Yasamin", "Mohammadi", "Shirin",
    "Khargosh", "Nasim", "Yek", "Ghazal", "Keshmesh", "Khat", "Naz", "Anar", "Ashk", "Mahi", 
    "Del", "Beh", "Bagh", "Fariyad", "Shab", "Raheb", "Morteza", "Aftab", "Sogand", "Hadaf", "Aftabi", 
    "Sang", "Kermani", "Malek", "Firoozeh", "Sabz", "Tohid", "Noor", "Baran"
]


adjectives = [
    "Derakhshan", "Khamoosh", "Marmooz", "Derakhshan", "Malaem", "Shahaneh", "Zarif", "Derakhshan", "Zendeh", "Latif",
    "Derakhshan", "Khirehkonnandeh", "Khoshayand", "Latif", "Faribandeh", "Zarif", "Jazab", "Derakhshan", "Daqiq", "Khoshboo",
    "Seharamiz", "Shadab", "Marasemi", "Bavqar", "Malaem",  "Delpazir", "Khub",
    "Bozorg", "Gavi", "Shegfte-engiz", "Malaem", "Ziba", "Faribandeh", "Nader",  "Puranerji", "Sahar-amiz",
    "Shadab", "Delroba", "Seharamiz",  "Ziba", "Khoshmazeh", "Khireh-konnandeh", "Delneshin", "Malaem"
]

def generate_name():
    flower = random.choice(flowers)
    adjective = random.choice(adjectives)
    number = random.randint(10, 99)  
    return f"{flower}-{adjective}-{number}"



print(generate_name())
