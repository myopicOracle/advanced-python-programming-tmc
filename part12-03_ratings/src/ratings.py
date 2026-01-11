# TEE RATKAISUSI TÄHÄN:

def sort_by_ratings(items: list) -> list: 

    def return_rating_value(item: list):
        return item["rating"]

    return sorted(items, key=return_rating_value, reverse=True)


if __name__ == "__main__":
    shows = [{ "name": "Dexter", "rating" : 8.6, "seasons":9 }, { "name": "Friends", "rating" : 8.9, "seasons":10 },  { "name": "Simpsons", "rating" : 8.7, "seasons":32 }  ]

    print("Rating according to IMDB")
    for show in sort_by_ratings(shows):
        print(f"{show['name']}  {show['rating']}")