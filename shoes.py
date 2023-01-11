class Shoe:		
    def __init__(self, brand, shoe_type, price):
        self.brand = brand
        self.type = shoe_type
        self.price = price
        self.in_stock = True

skater_shoe = Shoe("Vans", "Low-top Trainers", 59.99)
dress_shoe = Shoe("Jack & Jill Bootery", "Ballet Flats", 29.99)
print(skater_shoe.type)
print(dress_shoe.type)

'''skater_shoe = Shoe()
dress_shoe = Shoe()

print(skater_shoe.type)
print(dress_shoe.type)

skater_shoe.type = "Low-top Trainers"
print(skater_shoe.type)

dress_shoe.type = "Ballet Flats"
print(dress_shoe.type)'''