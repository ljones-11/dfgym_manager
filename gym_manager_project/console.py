import pdb

from models.booking import Booking
from models.member import Member
from models.workout import Workout

import repositories.member_repository as member_repository
import repositories.workout_repository as workout_repository


member_repository.delete_all()
workout_repository.delete_all()

member1 = Member('Jack Bauer', 'jackbauer@24.com', '1', 'standard')
member_repository.save(member1)
member2 = Member('Tony Almeda', 'tonymole@24.com', '1', 'standard')
member_repository.save(member2)
member2 = Member('Nina Myers', 'ninamyers@24.com', '1', 'standard')
member_repository.save(member2)

workout1 = Workout('Yoga', 'Vinyasa style flow', 45, '22/12/22', '1930', 20, '1')
workout_repository.save(workout1)
workout2 = Workout('Strength', 'Barbell based movements', 50, '23/12/22', '0700', 12, '1')
workout_repository.save(workout2)
workout3 = Workout('Cardio', 'Rowing based intervals', 40, '23/12/22', '0800', 12, '1')
workout_repository.save(workout3)

workout_repository.delete(2)

member_repository.delete(2)

workout1.time = "2000"
workout_repository.update(workout1)

member1.email = "jb@24.com"
member_repository.update(member1)

for member in member_repository.select_all():
    print (member.name, member.email)

for workout in workout_repository.select_all():
    print(workout.name, workout.capacity, workout.time)




pdb.set_trace()