class Review:
     all_reviews=[]

     def __init__(self,customer,restaurant,rating=int):
        self.customer = customer
        self.restaurant= restaurant
        self.rating= rating
        Review.all_reviews.append(self)


     def rating(self):
         return self.rating
     
     def all(self):
         return all
     
     @classmethod
     def customer(self):
        return self.customer
     
     def restaurant(self):
        return self.restaurant
