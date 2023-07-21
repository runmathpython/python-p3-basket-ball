def game_dict():

    #returns a dictionary that has two items, one uses "home" as the key
    # and the other uses "away" as the key. So two teams, a home team and an away team
    # each key value is a dictionary that shows the specs of each team's.
    # the dictionary used as the key value has three items, one is for a team name,
    # another is for team colors, and the other is for players.
    # and the key value of the key "players" is a list of dictionaries,
    # each of which shows the stats of each player's.

    return {
        "home": {
            "team_name": "Cleveland Cavaliers",
            "colors": ["Wine", "Gold"],
            "players": [
                {
                    "name": "Jarrett Allen",
                    "number": 31,
                    "position": "Center",
                    "points_per_game": 16.1,
                    "rebounds_per_game": 10.8,
                    "assists_per_game": 1.6,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 1.3,
                    "career_points": 3945,
                    "age": 24,
                    "height_inches": 82,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Darius Garland",
                    "number": 10,
                    "position": "Point Guard",
                    "points_per_game": 21.7,
                    "rebounds_per_game": 3.3,
                    "assists_per_game": 8.6,
                    "steals_per_game": 1.3,
                    "blocks_per_game": 0.1,
                    "career_points": 3142,
                    "age": 22,
                    "height_inches": 73,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Evan Mobley",
                    "number": 4,
                    "position": "Center",
                    "points_per_game": 15.0,
                    "rebounds_per_game": 8.3,
                    "assists_per_game": 2.5,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 1.7,
                    "career_points": 1034,
                    "age": 21,
                    "height_inches": 83,
                    "shoe_brand": "Adidas",
                },
                {
                    "name": "Kevin Love",
                    "number": 0,
                    "position": "Power Forward",
                    "points_per_game": 13.6,
                    "rebounds_per_game": 7.2,
                    "assists_per_game": 2.2,
                    "steals_per_game": 0.4,
                    "blocks_per_game": 0.2,
                    "career_points": 14305,
                    "age": 34,
                    "height_inches": 80,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Isaac Okoro",
                    "number": 35,
                    "position": "Small Forward",
                    "points_per_game": 8.8,
                    "rebounds_per_game": 3.0,
                    "assists_per_game": 1.8,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 0.3,
                    "career_points": 1234,
                    "age": 21,
                    "height_inches": 77,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Ricky Rubio",
                    "number": 99,
                    "position": "Point Guard",
                    "points_per_game": 13.1,
                    "rebounds_per_game": 4.1,
                    "assists_per_game": 6.6,
                    "steals_per_game": 1.4,
                    "blocks_per_game": 0.2,
                    "career_points": 7399,
                    "age": 31,
                    "height_inches": 74,
                    "shoe_brand": "Adidas",
                },
            ],
        },
            
        "away": {
            "team_name": "Washington Wizards",
            "colors": ["Red", "White", "Navy Blue"],
            "players": [   
                {
                    "name": "Bradley Beal",
                    "number": 3,
                    "position": "Shooting Guard",
                    "points_per_game": 23.2,
                    "rebounds_per_game": 4.7,
                    "assists_per_game": 6.6,
                    "steals_per_game": 0.9,
                    "blocks_per_game": 0.4,
                    "career_points": 14231,
                    "age": 29,
                    "height_inches": 76,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Kyle Kuzma",
                    "number": 33,
                    "position": "Power Forward",
                    "points_per_game": 17.1,
                    "rebounds_per_game": 8.5,
                    "assists_per_game": 3.5,
                    "steals_per_game": 0.6,
                    "blocks_per_game": 0.9,
                    "career_points": 5336,
                    "age": 27,
                    "height_inches": 81,
                    "shoe_brand": "Puma",
                },
                {
                    "name": "Kentavious Caldwell-Pope",
                    "number": 1,
                    "position": "Shooting Guard",
                    "points_per_game": 13.2,
                    "rebounds_per_game": 3.4,
                    "assists_per_game": 1.9,
                    "steals_per_game": 1.1,
                    "blocks_per_game": 0.3,
                    "career_points": 7911,
                    "age": 29,
                    "height_inches": 77,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Davis Bertans",
                    "number": 42,
                    "position": "Power Forward",
                    "points_per_game": 5.6,
                    "rebounds_per_game": 2.1,
                    "assists_per_game": 0.6,
                    "steals_per_game": 0.3,
                    "blocks_per_game": 0.3,
                    "career_points": 3165,
                    "age": 29,
                    "height_inches": 82,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Kristaps Porzingis",
                    "number": 6,
                    "position": "Power Forward",
                    "points_per_game": 22.1,
                    "rebounds_per_game": 8.8,
                    "assists_per_game": 2.9,
                    "steals_per_game": 0.7,
                    "blocks_per_game": 1.5,
                    "career_points": 6371,
                    "age": 27,
                    "height_inches": 87,
                    "shoe_brand": "Adidas",
                },
                {
                    "name": "Rui Hachimura",
                    "number": 8,
                    "position": "Power Forward",
                    "points_per_game": 11.3,
                    "rebounds_per_game": 3.8,
                    "assists_per_game": 1.1,
                    "steals_per_game": 0.5,
                    "blocks_per_game": 0.2,
                    "career_points": 1913,
                    "age": 24,
                    "height_inches": 80,
                    "shoe_brand": "Jordan",
                },
            ]
        }
    }

def get_all_players():

    # make a dictionary for all the players.
    # so make a dictionary, where each item uses a player's name as a key and the key value is a dictionary
    # that shows the stats of the player's as the name, the number, the position, etc.

    all_players = {}

    # there are two teams, one is a home team, and the other is an away team.
    # and of course, each team has a group of players.

    for team in ["home", "away"]:
        for player in game_dict()[team]["players"]:

            # update() method inserts a specific item to a dictionary.
            # in this case, each key is a player's name, and the key value is a dictionary
            # which has items that show the stats of the player's as the name, the number, the position, etc.
            # so each item is put the way as follows
            # name: the name, number: the number, position: the position, etc.

            all_players.update(
                {player["name"]: {
                    "name": player["name"],
                    "number": player["number"],
                    "position": player["position"],
                    "points_per_game": player["points_per_game"],
                    "rebounds_per_game": player["rebounds_per_game"],
                    "assists_per_game": player["assists_per_game"],
                    "steals_per_game": player["steals_per_game"],
                    "blocks_per_game": player["blocks_per_game"],
                    "career_points": player["career_points"],
                    "age": player["age"],
                    "height_inches": player["height_inches"],
                    "shoe_brand": player["shoe_brand"]
                }}
            )
    
    # see if this function works as intended
    #for player in all_players:
        #print(all_players[player]["name"], ": ", all_players[player]["points_per_game"])
    

    return all_players

def num_points_per_game(player_name):

    # get the stats for every player and return the points per game for the player with the name
    return(get_all_players()[player_name]["points_per_game"])

def player_age(player_name):

    #get the stats for all the players and return the age of the player with the name
    return get_all_players()[player_name]["age"]

def team_colors(team_name):

    # make the dictionary for the two teams and return the team colors of the team's
    for team in game_dict():
        if game_dict()[team]["team_name"] == team_name:
            return game_dict()[team]["colors"]

def team_names():

    # make the dictionary for the two teams and return the array of team names
    team_names = []
    for team in game_dict():
        team_names.append(game_dict()[team]["team_name"])
    return team_names

def player_numbers(team_name):

    # make the dictionary for the two teams, and return the list of player numbers
    # that the players of the team with the team name have

    player_numbers = []
    for team in game_dict():
        if game_dict()[team]["team_name"] == team_name:
            team_players = game_dict()[team]["players"]
            for player in team_players:
                player_numbers.append(player["number"])
    
    return player_numbers

def player_stats(player_name):

    # get all the players and return the stats of the player with the player name

    return(get_all_players()[player_name])

def average_rebounds_by_shoe_brand():

    # make a dictioinary for shoe brands that the players wear
    shoe_brand_dict = {}

    # make a dictionary for all the players that shows the stats for each player.
    # for each item in the dictionary, the key is the player's name
    # and the key value is a dictionary that shows the stats for the player
    players = get_all_players()
    
    for player in players:
        brand = players[player]["shoe_brand"]
        rebounds = players[player]["rebounds_per_game"]

        # if the brand exists in the shoe barnd dict, add the rebounds per game for the player
        # to the list of rebounds per game
        if (brand in shoe_brand_dict):
            shoe_brand_dict[brand].append(rebounds)
            #print("add to list: ", shoe_brand_dict)
        else:
            # if the brand does not exist, add an item to the dictionary
            shoe_brand_dict[brand] = [rebounds]
            #print("add to dict: ", shoe_brand_dict)
    for brand in shoe_brand_dict:
        average = sum(shoe_brand_dict[brand]) / len(shoe_brand_dict[brand])
        print(f'{brand}: ', "{0:.2f}".format(average))



# test some functions to see if they work as intended

#for player in get_all_players():
    #print(get_all_players()[player]["name"], ": ", get_all_players()[player]["points_per_game"])

#average_rebounds_by_shoe_brand()