class Gun:
    def __init__(self):
        self.count_shoot = 0

    def shoot(self):
        if self.count_shoot % 2:
            print("paf")
        else:
            print("pif")
        self.count_shoot += 1

gun = Gun()

gun.shoot()
gun.shoot()
gun.shoot()
gun.shoot()