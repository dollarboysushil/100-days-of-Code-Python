    new_car = Turtle('square')
            new_car.shapesize(1,2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250,250)
            new_car.goto(300 , random_y)
            self.all_cars.append(new_car)