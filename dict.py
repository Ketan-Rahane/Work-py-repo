# Big database containing a small movies_db per year
bigmovies_db = {
    2022: {
        "movies_db": [
            {"Movie Name": "Bramhastra", "casting": ["Amitabh Bachchan", "Ranvir Kapoor","Aalia Bhatt","Nagarjun"]},
            {"Movie Name": "Drishyam 2", "casting": ["Ajay Devgan","Akshay Khanna","Tabu","Shriya Saran"]}
        ]
    }
,
2023: {
        "movies_db": [
            {"Movie Name": "The Kerala Story", "casting": ["Adah Sharma", "Siddhi Idnanai","Yogita Bihani","Sonia Balani",]},
            {"Movie Name": "dashera", "casting": ["Nani", "keerthy Suresh","Sai Kumar","shamna"]}
        ]
    },
2024: {
        "movies_db": [
            {"Movie Name": "Stree2", "casting": ["Rajkumar Rao", "Shradhha Kapoor","Pankaj Tripathi","Abhishek Banarjee"]},
            {"Movie Name": "Fighter", "casting": ["Hritik Roshan", "Deepika Padukone","Anil Kapoor","Karan Grover"]}
        ]
    },
2025: {
        "movies_db": [
            {"Movie Name": "Avatar 3", "casting": ["Sam Worthington", "Zoe Saldana","Kate Winslate","Sigourney Weaver"]},
            {"Movie Name": "Fantastic Four", "casting": ["Pedro Pascal", "Vanessa Kirby","Margot Robbie","John Krasinski"]}
        ]
    }
}
print(bigmovies_db)

l=bigmovies_db.keys()
print(type(l))
print(bigmovies_db.keys())
print(bigmovies_db.values())

for year, data in bigmovies_db.items():
    print(f"Year: {year}")

print("All movie names:")
for year_data in bigmovies_db.values():
    for movie in year_data["movies_db"]:
        print("Movie Name",movie["Movie Name"])

print("All Castings names:")
for year_data in bigmovies_db.values():
    for movies in year_data["movies_db"]:
        for casting in movies["casting"]:
            print("casting:",casting)

for t in bigmovies_db.items():
    print("touples in dictionary:",t)

for k, v in bigmovies_db.items():
    print(k,"---->",v)



