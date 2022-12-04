import unittest
from models.workout import Workout

class TestWorkout(unittest.TestCase):
    def setUp(self):
        self.workout1 = Workout("Pilates", "Introduction to pilates class", 40, '28/06/23', '1700', 12, '1')

    def test_workout_has_name(self):
        self.assertEqual('Pilates', self.workout1.name)

    def test_workout_has_description(self):
        self.assertEqual('Introduction to pilates class', self.workout1.description)

    def test_workout_has_duration(self):
        self.assertEqual(40, self.workout1.duration)

    def test_workout_has_date(self):
        self.assertEqual('28/06/23', self.workout1.date)
    
    def test_workout_has_time(self):
        self.assertEqual('1700', self.workout1.time)

    def test_workout_has_capacity(self):
        self.assertEqual(12, self.workout1.capacity)
    
    def test_workout_has_status(self):
        self.assertEqual('1', self.workout1.status)
        