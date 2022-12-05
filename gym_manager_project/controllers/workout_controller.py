from flask import Flask, Blueprint, render_template, redirect, request
from models.workout import Workout
import repositories.workout_repository as workout_repository
import repositories.booking_repository as booking_repository

workouts_blueprint = Blueprint("workouts", __name__)


#GET list workouts '/workouts' repo.select_all, render list

@workouts_blueprint.route("/workouts")
def members():
    workouts = workout_repository.select_all()
    return render_template("workouts/index.html", workouts = workouts)

#GET show workout '/workouts/<id>' repo.select(id), render 

@workouts_blueprint.route("/workouts/<int:id>")
def workout(id):
    workout = workout_repository.select(id)
    member_list = workout_repository.members(workout)
    return render_template("workouts/show.html", workout=workout, member_list = member_list)

#DELETE POSTmethod, /workouts/<id>/delete, repo.delete redirect

@workouts_blueprint.route("/workouts/<int:id>/delete", methods=['POST'])
def delete_workout(id):
    workout_repository.delete(id)
    return redirect("/workouts")

#NEW render form page

@workouts_blueprint.route("/workouts/new")
def new_workout():
    return render_template("workouts/new.html")

#CREATE POSTmethod, /workouts, request.form[''] data, workout=workout, repo.save(workout)

@workouts_blueprint.route("/workouts", methods=['POST'])
def add_workout():
    name = request.form['name']
    description = request.form['description']
    duration = request.form['duration']
    date = request.form['date']
    time = request.form['time']
    capacity = request.form['capacity']
    status = request.form['status']

    new_workout = Workout(name, description, duration, date, time, capacity, status)
    workout_repository.save(new_workout) 
    return redirect("/workouts")  

#EDIT render edit form

@workouts_blueprint.route("/workouts/<int:id>/edit")  
def edit_workout(id):
    workout_to_edit = workout_repository.select(id)
    return render_template("workouts/edit.html", workout=workout_to_edit)

#UPDATE POSTmethod, /workouts/<id>, request.form[''] data repo.update(workout)

@workouts_blueprint.route("/workouts/<int:id>", methods = ['POST'])
def update_workout(id):
    name = request.form['name']
    description = request.form['description']
    duration = request.form['duration']
    date = request.form['date']
    time = request.form['time']
    capacity = request.form['capacity']
    status = request.form['status']

    edited_workout = Workout(name, description, duration, date, time, capacity, status, id)
    workout_repository.update(edited_workout)
    return redirect("/workouts")
