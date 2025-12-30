# Write your solution here:

# Class definition
class Series: 
    def __init__(self, title: str, seasons: int, genres: list):
        self.title = title
        self.seasons = seasons
        self.genres = genres
        self.ratings = []

    def rate(self, rating: int):
        self.ratings.append(rating)
    
    def get_avg_rating(self):
        if self.ratings:
            return round(sum(self.ratings)/len(self.ratings), 1)
        else:
            return 0.0

    def __str__(self):
        avg_score_string = f", average {self.get_avg_rating()} points" if self.ratings else ""
        
        return f"{self.title} ({self.seasons} seasons)\ngenres: {', '.join(self.genres)}\n{len(self.ratings) if self.ratings else 'no'} ratings{avg_score_string}"

# Search functions
def minimum_grade(rating: float, series_list: list):
    filtered_list = []

    for series in series_list:
        average_rating = series.get_avg_rating()
        if average_rating >= rating:
            filtered_list.append(series)

    return filtered_list


def includes_genre(genre: str, series_list: list):
    filtered_list = []

    for series in series_list:
        if genre in series.genres:
            filtered_list.append(series)
    
    return filtered_list


# # Test Series 1

# dexter = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])

# dexter.rate(4)
# dexter.rate(5)
# dexter.rate(5)
# dexter.rate(3)
# dexter.rate(0)

# print(dexter)


# # Test Series 2

# s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
# s1.rate(5)

# s2 = Series("South Park", 24, ["Animation", "Comedy"])
# s2.rate(3)

# s3 = Series("Friends", 10, ["Romance", "Comedy"])
# s3.rate(2)

# series_list = [s1, s2, s3]

# print("a minimum grade of 4.5:")
# for series in minimum_grade(4.5, series_list):
#     print(series.title)

# print("genre Comedy:")
# for series in includes_genre("Comedy", series_list):
#     print(series.title)