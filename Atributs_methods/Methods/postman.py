class Postman:
    def __init__(self):
        self.delivery_data = []

    def add_delivery(self, street, house, flat):
        self.delivery_data.append((street, house, flat))

    def get_houses_for_street(self, street):
        return [i for i in dict.fromkeys([adress[1] for adress in self.delivery_data if street == adress[0]])]


    def get_flats_for_house(self, street, house):
        return [i for i in dict.fromkeys([adress[2] for adress in self.delivery_data if street == adress[0] and house == adress[1]])]


postman = Postman()

postman.add_delivery('Советская', 151, 74)
postman.add_delivery('Советская', 151, 75)
postman.add_delivery('Советская', 90, 2)
postman.add_delivery('Советская', 151, 74)

print(postman.get_houses_for_street('Советская'))
print(postman.get_flats_for_house('Советская', 151))