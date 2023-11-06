class Restaurant:
    def __init__(self,name=""):
        self.restaurant_name = name
        self.reviews = []

    def get_name(self):
        return self.restaurant_name

    def add_review(self, review):
        self.reviews.append(review)

    def customers(self):
        return list(set([review.customer() for review in self.reviews]))

    def average_star_rating(self):
        if not self.reviews:
            return 0
        total_ratings = sum([review.rating() for review in self.reviews])
        return total_ratings / len(self.reviews)