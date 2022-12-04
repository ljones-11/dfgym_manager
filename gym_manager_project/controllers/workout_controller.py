from flask import Flask, Blueprint, render_template, redirect, request
from models.workout import Workout
import repositories.workout_repository as workout_repository

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
    return render_template("workouts/show.html", workout=workout)

#DELETE POSTmethod, /workouts/<id>/delete, repo.delete redirect

#NEW render form page

#CREATE POSTmethod, /workouts, request.form[''] data, workout=workout, repo.save(workout)

#EDIT render edit form

#UPDATE POSTmethod, /workouts/<id>, request.form[''] data repo.update(workout)