import pdb

from models.booking import Booking
from models.member import Member
from models.workout import Workout

import repositories.member_repository as member_repository
import repositories.workout_repository as workout_repository
import repositories.booking_repository as booking_repository


member_repository.delete_all()
workout_repository.delete_all()
booking_repository.delete_all()

member1 = Member('Jack Bauer', 'jackbauer@24.com', '1', 'standard')
member_repository.save(member1)
member2 = Member('Tony Almeda', 'tonymole@24.com', '1', 'standard')
member_repository.save(member2)
member2 = Member('Nina Myers', 'ninamyers@24.com', '0', 'standard')
member_repository.save(member2)

workout1 = Workout('Yoga', 'Vinyasa style flow', 45, '22/12/22', '1930', 20, '1')
workout_repository.save(workout1)
workout2 = Workout('Strength', 'Barbell based movements', 50, '23/12/22', '0700', 12, '1')
workout_repository.save(workout2)
workout3 = Workout('Cardio', 'Rowing based intervals', 40, '23/12/22', '0800', 12, '1')
workout_repository.save(workout3)

booking1 = Booking(member1, workout1)
booking_repository.save(booking1)
booking2 = Booking(member1, workout3)
booking_repository.save(booking2)
booking3 = Booking(member2, workout1)
booking_repository.save(booking3)

# workout_repository.delete(2)
# member_repository.delete(2)
# booking_repository.delete(1)

workout1.time = "2000"
workout_repository.update(workout1)

member1.email = "jb@24.com"
member_repository.update(member1)

for member in member_repository.select_all():
    print (member.name, member.email, member.status, member.id)

# for workout in workout_repository.select_all():
#     print(workout.name, workout.capacity, workout.time)

for booking in booking_repository.select_all():
    print(booking.member, booking.workout, booking.id)

# members in a given workout
members = workout_repository.members(workout1)
print (members)
# workouts for a given member
workouts = member_repository.workouts(member1)
print (workouts)
# member for a booking
member = booking_repository.member(booking1)
print(member)
# workout for a booking
workout = booking_repository.workout(booking2)
print(workout)




pdb.set_trace()