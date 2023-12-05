from review import Review  

class Customer:
    all_customers = []

    def __init__(self, given_name, family_name):
        self.given_name_val = given_name
        self.family_name_val = family_name
        self.reviews = []
        Customer.all_customers.append(self)

    def get_given_name(self):
        return self.given_name_val

    def get_family_name(self):
        return self.family_name_val

    def full_name(self):
        return f"{self.given_name_val} {self.family_name_val}"

    @classmethod
    def all(cls):
        return cls.all_customers

    def restaurants(self):
        return list(set(review.restaurant for review in self.reviews))

    def add_review(self, restaurant, rating):
        new_review = Review(self, restaurant, rating)
        self.reviews.append(new_review)
        restaurant.add_review(new_review)

    def num_reviews(self):
        return len(self.reviews)

    @classmethod
    def find_by_name(cls, name):
        return next((customer for customer in cls.all_customers if customer.full_name() == name), None)

    @classmethod
    def find_all_by_given_name(cls, name):
        return [customer for customer in cls.all_customers if customer.given_name_val == name]


class Customer:
    all_customers = []

    def __init__(self, given_name, family_name):
        self.given_name_val = given_name
        self.family_name_val = family_name
        self.reviews = []
        Customer.all_customers.append(self)

    def get_given_name(self):
        return self.given_name_val

    def get_family_name(self):
        return self.family_name_val

    def full_name(self):
        return f"{self.given_name_val} {self.family_name_val}"

    @classmethod
    def all(cls):
        return cls.all_customers

    def restaurants(self):
        return list(set(review.restaurant for review in self.reviews))

    def add_review(self, restaurant, rating):
        new_review = Review(self, restaurant, rating)
        self.reviews.append(new_review)
        restaurant.add_review(new_review)

    def num_reviews(self):
        return len(self.reviews)

    @classmethod
    def find_by_name(cls, name):
        return next((customer for customer in cls.all_customers if customer.full_name() == name), None)

    @classmethod
    def find_all_by_given_name(cls, name):
        return [customer for customer in cls.all_customers if customer.given_name_val == name]
