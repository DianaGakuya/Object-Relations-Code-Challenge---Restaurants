from review import Review

class Restaurant:
    all_restaurants = []

    def __init__(self, name):
        self.name_val = name
        self.reviews = []
        Restaurant.all_restaurants.append(self)

    def get_name(self):
        return self.name_val

    @classmethod
    def all(cls):
        return cls.all_restaurants

    def get_reviews(self):
        return self.reviews

    def customers(self):
        return list(set(review.get_customer() for review in self.reviews))

    def average_star_rating(self):
        if not self.reviews:
            return 0
        total_ratings = sum(review.get_rating() for review in self.reviews)
        return total_ratings / len(self.reviews)

    def add_review(self, review):
        self.reviews.append(review)
