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

def select_all():
    bookings = []
    sql = "SELECT * from bookings"
    results = run_sql(sql)

    for row in results:
        member = member_repository.select(row['member_id'])
        workout = workout_repository.select(row['workout_id'])
        booking = Booking(member, workout, row['id'])
        bookings.append(booking)
    return bookings    

def delete_all():
    sql = "DELETE from bookings"
    run_sql(sql)

def delete(id):
    sql = "DELETE from bookings WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def member(booking):
    sql = " SELECT * from members where id = %s"
    values = [booking.member.id]
    results = run_sql(sql, values)
    result = results[0]
    member = Member(result['name'], result['email'], result['status'], result['type'], result['id'])
    return member

def workout(booking):
    sql = "SELECT * from workouts where id = %s"
    values = [booking.workout.id]
    results = run_sql(sql, values)
    result = results[0]
    workout = Workout(result['name'], result['description'], result['duration'], result['date'], result['time'], result['capacity'], result['status'], result['id'])
    return workout

#no reason to update booking id's
# def update(booking):
#     sql = """UPDATE bookings 
#     SET (member_id, workout_id) = (%s, %s) 
#     WHERE id = %s"""
#     values = [booking.member.id, booking.workout.id, booking.id]
#     run_sql(sql,values)

