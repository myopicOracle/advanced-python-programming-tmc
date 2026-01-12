# Write your solution here

import json


def read_file():
    file_name = input("file name: ")

    with open(file_name) as f:
        raw = f.read()

    data = json.loads(raw)
    print(f"read the data of {len(data)} players")

    return data


def show_help():
    print("commands:")
    print("0 quit")
    print("1 search for player")
    print("2 teams")
    print("3 countries")
    print("4 players in team")
    print("5 players from country")
    print("6 most points")
    print("7 most goals")


def player_string(obj: dict):
    name = f"{obj['name']:<21}"
    team = f"{obj['team']:>3}"
    goals = f"{obj['goals']:>2}"
    assists = f"{obj['assists']:>2}"
    total = f"{obj['goals'] + obj['assists']:>3}"
    
    return f"{name}{team}  {goals} + {assists} = {total}"


def search_for_player(player_name: str, data: list):
    obj = [player for player in data if player["name"] == player_name][0]
    print(player_string(obj))


def get_teams(data: list):
    return sorted(list(set([player['team'] for player in data])))

def get_countries(data: list):
    return sorted(list(set([player['nationality'] for player in data])))


def filter_by_teams(data: list, team: str):
    return sorted([player for player in data if player['team'] == team], key = lambda x : x['goals'] + x['assists'], reverse = True)

def filter_by_country(data: list, country: str):
    return sorted([player for player in data if player['nationality'] == country], key = lambda x : x['goals'] + x['assists'], reverse = True)


def most_points(data: list, limit: int): 
    sorted_list = sorted(data, key = lambda x : (x['goals'] + x['assists'], x['goals']), reverse = True)
    return sorted_list[:limit]

def most_goals(data: list, limit: int): 
    sorted_list = sorted(data, key = lambda x : (x['goals'], -x['games']), reverse = True)
    return sorted_list[:limit]


def execute():
    data = read_file()
    show_help()

    while True: 
        command = int(input("command: "))

        if command == 0:
            break

        elif command == 1: 
            player_name = input("name: ")
            search_for_player(player_name, data)

        elif command == 2: 
            teams = get_teams(data)
            for team in teams:
                print(team)

        elif command == 3:
            countries = get_countries(data)
            for country in countries:
                print(country)

        elif command == 4:
            team = input("team: ")
            players_list = filter_by_teams(data, team)
            for player in players_list:
                print(player_string(player))

        elif command == 5:
            country = input("country: ")
            players_list = filter_by_country(data, country)
            for player in players_list:
                print(player_string(player))

        elif command == 6:
            limit = int(input("how many: "))
            players_list = most_points(data, limit)
            for player in players_list:
                print(player_string(player))

        elif command == 7:
            limit = int(input("how many: "))
            players_list = most_goals(data, limit)
            for player in players_list:
                print(player_string(player))


execute()





