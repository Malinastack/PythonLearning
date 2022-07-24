class Settings:
    def __init__(self):
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # Ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3
        # Bullet settings
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 10
        # Alien settings
        self.alien_speed = 0.3
        self.fleet_drop_speed = 15

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        #scoring
        self.alien_points = 50
        self.score_scale = 1.5

    def increase_speed(self):
        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)