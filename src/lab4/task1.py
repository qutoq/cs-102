def parse_data(films_path, views_path):
    films = {}
    with open(films_path, 'r', encoding="utf-8") as file:
        for line in file:
            movie_id, movie_name = line.strip().split(',')
            films[int(movie_id)] = movie_name

    views = []
    with open(views_path, 'r', encoding="utf-8") as file:
        for line in file:
            if len(line) > 0:
                viewed_films = list(map(int, line.strip().split(',')))
                views.append(viewed_films)

    return films, views


class Cinema:

    def __init__(self, films_path, views_path, user_views):
        self.films, self.views = parse_data(films_path, views_path)
        self.user_views = {int(el) for el in user_views.split(',')}

    def like_users(self):
        result = []
        for user in self.views:
            user_set = set(user)
            if len(user_set.intersection(self.user_views)) >= len(self.user_views) / 2:
                result.append(user)
        return result

    def delete_watched_films(self, users):
        unwatched_films = []
        for user in users:
            for film in user:
                if film not in self.user_views:
                    unwatched_films.append(film)
        return unwatched_films

    def recommend_movie(self):
        unwatched_films = self.delete_watched_films(self.like_users())
        count = {}
        for movie in unwatched_films:
            if movie in count:
                count[movie] += 1
            else:
                count[movie] = 1

        id = max(count, key=count.get)
        return self.films[id]


films_path, views_path = 'data/films.txt', 'data/views.txt'
user_views = '1, 2'

if __name__ == '__main__':
    system = Cinema(films_path, views_path, user_views)
    print("Рекомендуемый фильм:", system.recommend_movie())
