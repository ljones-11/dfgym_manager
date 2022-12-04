from flask import Flask, Blueprint
from models.workout import Workout
import repositories.workout_repository as workout_repository

workouts_blueprint = Blueprint("workouts", __name__)

#blueprint

#GET list workouts '/workouts' repo.select_all, render list

#GET show workout '/workouts/<id>' repo.select(id), render 

#DELETE POSTmethod, /workouts/<id>/delete, repo.delete redirect

#CREATE POSTmethod, /workouts, request.form[''] data, workout=workout, repo.save(workout)

#UPDATE POSTmethod, /workouts/<id>, request.form[''] data repo.update(workout)