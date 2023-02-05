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

member1 = Member('JACK BAUER', 'jackbauer@24.com', '1', 'STANDARD')
member_repository.save(member1)
member2 = Member('TONY ALMEDA', 'tonymole@24.com', '1', 'STANDARD')
member_repository.save(member2)
member3 = Member('NINA MYERS', 'ninamyers@24.com', '0', 'STANDARD')
member_repository.save(member3)
member4 = Member('VICTOR DRAZEN', 'vdrazen@24.com', '1', 'STANDARD')
member_repository.save(member4)
member5 = Member('CHARLES LOGAN', 'clogan@24.com', '1', 'STANDRAD')
member_repository.save(member5)

workout1 = Workout('YOGA', 'Slow, restorative Vinyasa flow. Caters to all abilities', 45, '2023-12-01', '19:30', 12, '1')
workout_repository.save(workout1)
workout2 = Workout('STRENGTH', 'Intermediate class with barbell based movements', 50, '2023-12-23', '18:00', 8, '1')
workout_repository.save(workout2)
workout3 = Workout('CARDIO', 'Interval style session on the Concept II rower', 45, '2023-12-25', '08:00', 8, '1')
workout_repository.save(workout3)
workout4 = Workout('PILATES', 'Full-body intermediate pilates workout', 35, '2023-12-26', '19:00', 12, '0')
workout_repository.save(workout4)
workout5 = Workout('MOBILITY', 'Early morning hip focussed mobility session', 60, '2023-12-27', '06:15', 12, '1')
workout_repository.save(workout5)
workout6 = Workout('WEIGHTLIFTING', 'Weekly barbell weightlifting club', 60, '2023-12-28', '08:00', 4, '1')
workout_repository.save(workout6)

booking1 = Booking(member1, workout1)
booking_repository.save(booking1)
booking7 = Booking(member2, workout1)
booking_repository.save(booking7)

booking8 = Booking(member4, workout2)
booking_repository.save(booking8)
booking9 = Booking(member5, workout5)
booking_repository.save(booking9)

booking2 = Booking(member2, workout6)
booking_repository.save(booking2)
booking3 = Booking(member1, workout6)
booking_repository.save(booking3)
booking4 = Booking(member4, workout6)
booking_repository.save(booking4)
booking5 = Booking(member5, workout6)
booking_repository.save(booking5)




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