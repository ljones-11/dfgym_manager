from flask import Flask, Blueprint, render_template, request, redirect
from models.booking import Booking
from datetime import date, time
import repositories.booking_repository as booking_repository
import repositories.member_repository as member_repository
import repositories.workout_repository as workout_repository

bookings_blueprint = Blueprint("bookings", __name__)


# GET /bookings

@bookings_blueprint.route("/bookings")
def bookings():
    bookings = booking_repository.select_all()
    return render_template("bookings/index.html", bookings = bookings)

@bookings_blueprint.route("/bookings/<int:id>")
def booking(id):
    booking = booking_repository.select(id)
    return render_template("bookings/show.html", booking=booking)


# # GET '/bookings/new'

@bookings_blueprint.route("/bookings/new")
def new_booking():
    active_members = []
    active_workouts = []
    members = member_repository.select_all()
    workouts = workout_repository.select_all()
    todays_date = date.today()

    for member in members:
        if member.status == '1':
            active_members.append(member)

    for workout in workouts:
        if workout.status == '1' and workout.date > todays_date:
            active_workouts.append(workout)

    premium_members = []
    for member in active_members:
        if member.type =='premium':
            premium_members.append(member)
        
    standard_members = []
    for member in active_members:
        if member.type =='standard':
            standard_members.append(member)

    return render_template("bookings/new.html", members=members, workouts=workouts, active_members = active_members, active_workouts = active_workouts)


# start_of_peak_time = 1800
    # end_of_peak_time = 2000

# CREATE POST method, redirect, request.form['data'], memebr and workout repo's.select new booking, bookingrepo.save 

@bookings_blueprint.route("/bookings", methods = ['POST'])
def add_booking():
    member_id = request.form['member_id']
    workout_id = request.form['workout_id']

    member = member_repository.select(member_id)
    workout = workout_repository.select(workout_id)
    new_booking = Booking(member, workout)
    exisiting_bookings = booking_repository.select_all()
    members_in_workout = workout_repository.members(workout)
    todays_date = date.today()


    for booking in exisiting_bookings:
        if booking.workout.id == workout.id and member.id == booking.member.id:
            return render_template("errors/booked-in-error.html")
            
        elif workout.date < todays_date:
            return render_template("errors/old-workout-error.html")

    if len(members_in_workout) < workout.capacity:
        booking_repository.save(new_booking)
        return redirect("/bookings")
    else:
        return render_template("errors/workout-full.html")


    

# DELETE bookings/delete POST method, redirect, booking.repo.delete(id)

@bookings_blueprint.route("/bookings/<int:id>/delete", methods = ['POST'])
def delete_booking(id):
    booking_repository.delete(id)
    return redirect("/bookings")



