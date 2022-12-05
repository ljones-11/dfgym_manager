from flask import Flask, Blueprint, render_template, request, redirect
from models.booking import Booking
import repositories.booking_repository as booking_repository
import repositories.member_repository as member_repository
import repositories.workout_repository as workout_repository

bookings_blueprint = Blueprint("bookings", __name__)


# GET /bookings

@bookings_blueprint.route("/bookings")
def bookings():
    bookings = booking_repository.select_all()
    return render_template("bookings/index.html", bookings = bookings)

# # GET '/bookings/new'

@bookings_blueprint.route("/bookings/new")
def new_booking():
    members = member_repository.select_all()
    workouts = workout_repository.select_all()
    return render_template("bookings/new.html", members=members, workouts=workouts)

# CREATE POST method, redirect, request.form['data'], memebr and workout repo's.select new booking, bookingrepo.save 

@bookings_blueprint.route("/bookings", methods = ['POST'])
def add_booking():
    member_id = request.form['member_id']
    workout_id = request.form['workout_id']

    member = member_repository.select(member_id)
    workout = workout_repository.select(workout_id)
    new_booking = Booking(member, workout)
    booking_repository.save(new_booking)
    return redirect("/bookings")

# DELETE bookings/delete POST method, redirect, booking.repo.delete(id)
