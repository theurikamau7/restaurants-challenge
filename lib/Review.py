class Review:
    all_reviews = []

    def __init__(self, customer, restaurant, rating):
        self.customer_obj = customer
        self.restaurant_obj = restaurant
        self.rating_value = rating
        Review.all_reviews.append(self)

    def customer(self):
        return self.customer_obj

    def restaurant(self):
        return self.restaurant_obj

    def rating(self):
        return self.rating_value

    @classmethod
    def all(cls):
        return cls.all_reviews