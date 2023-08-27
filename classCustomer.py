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
        