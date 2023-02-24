import random
from itertools import combinations

# Define the list of soccer teams
teams = [
    "Team A", "Team B", "Team C", "Team D", "Team E", "Team F",
    "Team G", "Team H", "Team I", "Team J", "Team K", "Team L",
    "Team M", "Team N", "Team O", "Team P"
]

# Shuffle the teams randomly
random.shuffle(teams)

# Divide the teams into 4 groups of 4
groups = [teams[i:i+4] for i in range(0, len(teams), 4)]

# Define the start date for the games
start_date = "14/09/2022"

# Define the time for the games
game_time = "22:45"

# Define the number of game weeks
num_weeks = 8

# Define the interval between game weeks in days
week_interval = 14

# Define the interval between games in hours
game_interval = 2

# Calculate the dates for each game
game_dates = []
for week in range(num_weeks):
    for day in range(3):
        game_date = start_date
        game_date = game_date.split("/")
        game_date = [int(d) for d in game_date]
        game_date[0] += week * week_interval
        game_date[1] += day
        if game_date[1] > 30:
            game_date[1] = 1
            game_date[2] += 1
        game_date = "{}/{}/{}".format(game_date[0], game_date[1], game_date[2])
        game_dates.append(game_date)

# Generate the calendar of games
games = []
for week, date in enumerate(game_dates):
    games.append("Week {} ({})\n".format(week+1, date))
    for group in groups:
        group_games = list(combinations(group, 2))
        for game in group_games:
            games.append("{} vs {}\n".format(game[0], game[1]))
    games.append("\n")

# Print the calendar of games
print("Calendar of Games")
print("=================")
for game in games:
    print(game.strip())