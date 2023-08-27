class Customer:
    def __init__(self, given_name="George", family_name="Washington"):
        self.given_name = given_name
        self.family_name = family_name

    def given_name(self):
        return self.given_name
    

    def set_given_name(self, given_name):
      self.given_name = given_name


    def family_name(self):
        return self.family_name
    
    def set_family_name(self, family_name):
     self.family_name = family_name

    
    def full_name(self):
        return f"{self.given_name} {self.family_name}"
    
    def all(self):
        return all
    
    @classmethod

    def restaurants(self):
        return [review.restaurant() for review in self.reviews]
    
    def add_review(self, restaurant, rating):
        new_review = Review(self, restaurant, rating)
        self.reviews.append(new_review)
        restaurant.add_review(new_review)

    @classmethod

    def num_reviews(self):
        return len(self.reviews)
    
    def find_by_name(cls, name):
        for customer in cls.all_customers:
            if customer.full_name() == name:
                return customer
        return None
    
    def find_all_by_given_name(cls, name):
        return [customer for customer in cls.all_customers if customer.given_name == name]

        