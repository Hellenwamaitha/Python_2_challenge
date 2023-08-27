class  Restaurant:
    def __init__(self,name=""):
        self.name = name

    def name(self):
        return self.name
    
    @classmethod
    
    def reviews(self):
        return self.reviews

    def customers(self):
        return list(set([review.customer() for review in self.reviews]))


    