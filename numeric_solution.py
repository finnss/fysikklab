mass = 2.7  # m (gram)
radius = 2  # r (cm)

inertia = (2/3) * mass * radius  # I
air_resistance = 0.001436236  # L

c = inertia/(mass * radius ** 2)

acceleration = 