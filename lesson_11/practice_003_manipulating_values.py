"""
2016 "Star Wars: Episode VII - The Force Awakens"
2017 "Star Wars: Episode VIII - The Last Jedi"
2018 "Black Panther"
2019 "Avengers: Endgame"
2020 "Bad Boys for Life"
"""

# Create a pre-populated dictionary with the year as the key and the title as the value.
movie = {
    2016: "Star Wars: Episode VII - The Force Awakens",
    2017: "Star Wars: Episode VIII - The Last Jedi",
    2018: "Black Panther",
    2019: "Avengers: Endgame",
    2020: "Bad Boys for Life"
}
# A mistake was made for 2016. The actual title for that year should be "Finding Dory".
# Update the dictionary accordingly.
movie[2016] = 'Finding Dory'
print(movie[2016])

# Since we all want to forget 2020 happened, remove 2020 from the dictionary.
del movie[2020]
print(movie)

# Print the title of the most successful movie of 2019.
print(movie[2019])