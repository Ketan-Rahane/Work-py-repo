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
            {"Movie Name": "Fighter", "casting": ["Hritik Roshan", "Deepika Padukone","Anil Kapoor","Ranvir Kapoor"]}
        ]
    },
2025: {
        "movies_db": [
            {"Movie Name": "Avatar 3", "casting": ["Sam Worthington", "Zoe Saldana","Kate Winslate","Sigourney Weaver"]},
            {"Movie Name": "Fantastic Four", "casting": ["Pedro Pascal", "Vanessa Kirby","Margot Robbie","John Krasinski"]}
        ]
    }
}
print("bigmovis_db : \n",bigmovies_db)

l=bigmovies_db.keys()
print(type(l))

total_movies = sum(len(year_data["movies_db"]) for year_data in bigmovies_db.values())
print(f"Total movies: {total_movies}")

print("keys : \n",bigmovies_db.keys())

print("vlaues : \n",bigmovies_db.values())

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
    print("touples in dictionary: \n ",t)

actor_name ="Ranvir Kapoor"
found_movies =[]
for year,year_data in bigmovies_db.items():
    for movie in year_data["movies_db"]:
        if actor_name in movie["casting"]:
             print(f"{actor_name} appeared in '{movie['Movie Name']}' ({year})")

#Outputs :
           bigmovis_db : 
 {2022: {'movies_db': [{'Movie Name': 'Bramhastra', 'casting': ['Amitabh Bachchan', 'Ranvir Kapoor', 'Aalia Bhatt', 'Nagarjun']}, 
                       {'Movie Name': 'Drishyam 2', 'casting': ['Ajay Devgan', 'Akshay Khanna', 'Tabu', 'Shriya Saran']}]}, 
  2023: {'movies_db': [{'Movie Name': 'The Kerala Story', 'casting': ['Adah Sharma', 'Siddhi Idnanai', 'Yogita Bihani', 'Sonia Balani']}, 
                       {'Movie Name': 'dashera', 'casting': ['Nani', 'keerthy Suresh', 'Sai Kumar', 'shamna']}]}, 
  2024: {'movies_db': [{'Movie Name': 'Stree2', 'casting': ['Rajkumar Rao', 'Shradhha Kapoor', 'Pankaj Tripathi', 'Abhishek Banarjee']}, 
                       {'Movie Name': 'Fighter', 'casting': ['Hritik Roshan', 'Deepika Padukone', 'Anil Kapoor', 'Ranvir Kapoor']}]}, 
  2025: {'movies_db': [{'Movie Name': 'Avatar 3', 'casting': ['Sam Worthington', 'Zoe Saldana', 'Kate Winslate', 'Sigourney Weaver']},
                       {'Movie Name': 'Fantastic Four', 'casting': ['Pedro Pascal', 'Vanessa Kirby', 'Margot Robbie', 'John Krasinski']}]}}

<class 'dict_keys'>

Total movies: 8

keys : 
 dict_keys([2022, 2023, 2024, 2025])

vlaues : 
 dict_values([{'movies_db': [{'Movie Name': 'Bramhastra', 'casting': ['Amitabh Bachchan', 'Ranvir Kapoor', 'Aalia Bhatt', 'Nagarjun']},
                             {'Movie Name': 'Drishyam 2', 'casting': ['Ajay Devgan', 'Akshay Khanna', 'Tabu', 'Shriya Saran']}]}, 
              {'movies_db': [{'Movie Name': 'The Kerala Story', 'casting': ['Adah Sharma', 'Siddhi Idnanai', 'Yogita Bihani', 'Sonia Balani']}, 
                             {'Movie Name': 'dashera', 'casting': ['Nani', 'keerthy Suresh', 'Sai Kumar', 'shamna']}]}, 
              {'movies_db': [{'Movie Name': 'Stree2', 'casting': ['Rajkumar Rao', 'Shradhha Kapoor', 'Pankaj Tripathi', 'Abhishek Banarjee']}, 
                             {'Movie Name': 'Fighter', 'casting': ['Hritik Roshan', 'Deepika Padukone', 'Anil Kapoor', 'Ranvir Kapoor']}]},
              {'movies_db': [{'Movie Name': 'Avatar 3', 'casting': ['Sam Worthington', 'Zoe Saldana', 'Kate Winslate', 'Sigourney Weaver']}, 
                             {'Movie Name': 'Fantastic Four', 'casting': ['Pedro Pascal', 'Vanessa Kirby', 'Margot Robbie', 'John Krasinski']}]}])

Year: 2022
Year: 2023
Year: 2024
Year: 2025

All movie names:
Movie Name Bramhastra
Movie Name Drishyam 2
Movie Name The Kerala Story
Movie Name dashera
Movie Name Stree2
Movie Name Fighter
Movie Name Avatar 3
Movie Name Fantastic Four

All Castings names:
casting: Amitabh Bachchan
casting: Ranvir Kapoor
casting: Aalia Bhatt
casting: Nagarjun
casting: Ajay Devgan
casting: Akshay Khanna
casting: Tabu
casting: Shriya Saran
casting: Adah Sharma
casting: Siddhi Idnanai
casting: Yogita Bihani
casting: Sonia Balani
casting: Nani
casting: keerthy Suresh
casting: Sai Kumar
casting: shamna
casting: Rajkumar Rao
casting: Shradhha Kapoor
casting: Pankaj Tripathi
casting: Abhishek Banarjee
casting: Hritik Roshan
casting: Deepika Padukone
casting: Anil Kapoor
casting: Ranvir Kapoor
casting: Sam Worthington
casting: Zoe Saldana
casting: Kate Winslate
casting: Sigourney Weaver
casting: Pedro Pascal
casting: Vanessa Kirby
casting: Margot Robbie
casting: John Krasinski

touples in dictionary:
  (2022, {'movies_db': [{'Movie Name': 'Bramhastra', 'casting': ['Amitabh Bachchan', 'Ranvir Kapoor', 'Aalia Bhatt', 'Nagarjun']}, {'Movie Name': 'Drishyam 2', 'casting': ['Ajay Devgan', 'Akshay Khanna', 'Tabu', 'Shriya Saran']}]})
touples in dictionary:
  (2023, {'movies_db': [{'Movie Name': 'The Kerala Story', 'casting': ['Adah Sharma', 'Siddhi Idnanai', 'Yogita Bihani', 'Sonia Balani']}, {'Movie Name': 'dashera', 'casting': ['Nani', 'keerthy Suresh', 'Sai Kumar', 'shamna']}]})
touples in dictionary:
  (2024, {'movies_db': [{'Movie Name': 'Stree2', 'casting': ['Rajkumar Rao', 'Shradhha Kapoor', 'Pankaj Tripathi', 'Abhishek Banarjee']}, {'Movie Name': 'Fighter', 'casting': ['Hritik Roshan', 'Deepika Padukone', 'Anil Kapoor', 'Ranvir Kapoor']}]})
touples in dictionary:
  (2025, {'movies_db': [{'Movie Name': 'Avatar 3', 'casting': ['Sam Worthington', 'Zoe Saldana', 'Kate Winslate', 'Sigourney Weaver']}, {'Movie Name': 'Fantastic Four', 'casting': ['Pedro Pascal', 'Vanessa Kirby', 'Margot Robbie', 'John Krasinski']}]})

Ranvir Kapoor appeared in 'Bramhastra' (2022)
Ranvir Kapoor appeared in 'Fighter' (2024)

