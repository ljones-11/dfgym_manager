class Workout:
    def __init__(self, name, description, duration, date, time, capacity, status, id = None):
        self.name = name
        self.description = description
        self.duration = duration
        self.date = date
        self.time = time
        self.capacity = capacity
        self.status = status
        self.id = id