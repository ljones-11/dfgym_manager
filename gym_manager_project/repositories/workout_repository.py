from db.run_sql import run_sql

from models.workout import Workout
from models.member import Member

def save(workout):
    sql = """ INSERT into workouts
    (name, description, duration, date, time, capacity, status)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    RETURNING * """
    values = [workout.name, workout.description, workout.duration, workout.date, workout.time, workout.capacity, workout.status]
    results = run_sql(sql, values)
    workout.id = results[0]['id']
    return workout

def delete_all():
    sql = "DELETE from workouts"
    run_sql(sql)

def delete(id):
    sql = "DELETE from workouts where id = %s"
    values = [id]
    run_sql(sql, values)

def select_all():
    workouts = []
    sql = " SELECT * from workouts ORDER BY DATE, TIME "
    results = run_sql(sql)

    for row in results:
        workout = Workout(row['name'], row['description'], row['duration'], row['date'], row['time'], row['capacity'], row['status'], row['id'])
        workouts.append(workout)
    return workouts

def select(id):
    sql = "SELECT * FROM workouts WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        workout = Workout(result['name'], result['description'], result['duration'], result['date'], result['time'], result['capacity'], result['status'], result['id'])
    return workout

def members(workout):
    members = []

    sql = """SELECT members.* FROM members 
    INNER JOIN bookings ON bookings.member_id = members.id 
    WHERE workout_id = %s"""

    values = [workout.id]
    results = run_sql(sql, values)

    for row in results:
        member = Member(row['name'], row['email'], row['status'], row['type'], row['id'])
        members.append(member)
    return members
    

def update(workout):
    sql = "UPDATE workouts SET (name, description, duration, date, time, capacity, status) = (%s, %s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [workout.name, workout.description, workout.duration, workout.date, workout.time, workout.capacity, workout.status, workout.id]
    run_sql(sql, values) 