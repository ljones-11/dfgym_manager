from db.run_sql import run_sql

from models.booking import Booking
from models.workout import Workout
from models.member import Member

import repositories.member_repository as member_repository
import repositories.workout_repository as workout_repository

def save(booking):
    sql = """ INSERT into bookings
    (member_id, workout_id) VALUES (%s, %s)
    RETURNING *"""
    values = [booking.member.id, booking.workout.id]
    results = run_sql(sql, values)
    booking.id = results[0]['id']
    return booking