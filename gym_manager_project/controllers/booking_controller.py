from flask import Flask, Blueprint
from models.booking import Booking
import repositories.booking_repository as booking_repository

bookings_blueprint = Blueprint("bookings", __name__)

#blueprint

# GET /bookings
# # def visits():
#     bookings = bookings_repository.select_all()
#     return render_template("bookings/index.html", bookings = bookings)

# # GET '/bookings/new'


# CREATE POST method, redirect, request.form['data'], memebr and workout repo's.select new booking, bookingrepo.save 

# DELETE bookings/delete POST method, redirect, booking.repo.delete(id)
