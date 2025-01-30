class Gun:
    def __init__(self):
        self.count_shoot = 0

    def shoot(self):
        if self.count_shoot % 2:
            print("paf")
        else:
            print("pif")
        self.count_shoot += 1

    def shots_count(self):
        return self.count_shoot

    def shots_reset(self):
        self.count_shoot = 0

gun = Gun()

print(gun.shots_count())
gun.shoot()
print(gun.shots_count())
gun.shoot()
print(gun.shots_count())