
olympic_medal_count = [
    {"country": "United States", "gold": 39, "silver": 41, "bronze": 33},
    {"country": "China", "gold": 38, "silver": 32, "bronze": 18},
    {"country": "Japan", "gold": 27, "silver": 14, "bronze": 17},
    {"country": "Great Britain", "gold": 22, "silver": 21, "bronze": 22},
    {"country": "Russia", "gold": 20, "silver": 28, "bronze": 23},
    {"country": "Australia", "gold": 17, "silver": 7, "bronze": 22},
    {"country": "Netherlands", "gold": 10, "silver": 12, "bronze": 14},
    {"country": "France", "gold": 10, "silver": 12, "bronze": 11},                         
    {"country": "Germany", "gold": 10, "silver": 11, "bronze": 16},
    {"country": "Italy", "gold": 10, "silver": 10, "bronze": 20}
]

 # country mist most number of gold medals

top_medal_country=max(olympic_medal_count,key=lambda med:med["gold"])
# print(top_medal_country)

 #medal count of each countries 

medal_count=len(olympic_medal_count)
# print(medal_count)


 # country with least number of medals



 # sort countries with medal count

sorted_medal=sorted(olympic_medal_count,key=lambda med:med["country"])

# print(sorted_medal)


 # extra 5 questions

top_bronze=max(olympic_medal_count,key=lambda med:med ["bronze"])
print(top_bronze)

top_silver=max(olympic_medal_count,key=lambda med:med ["silver"])
print(top_silver)

