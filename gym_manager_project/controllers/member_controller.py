from flask import Flask, Blueprint, render_template, redirect, request
from models.member import Member
import repositories.member_repository as member_repository

members_blueprint = Blueprint("members", __name__)


#GET list members '/members' repo.select_all, render list

@members_blueprint.route("/members")
def members():
    members = member_repository.select_all()
    return render_template("members/index.html", members = members)

#GET show member '/members/<id>' repo.select(id), render 

@members_blueprint.route("/members/<int:id>")
def member(id):
    member = member_repository.select(id)
    return render_template("members/show.html", member=member)

#DELETE POSTmethod, /members/<id>/delete, repo.delete redirect

@members_blueprint.route("/members/<int:id>/delete", methods=['POST'])
def delete_member(id):
    member = member_repository.delete(id)
    return redirect("/members")

#NEW

@members_blueprint.route("/members/new")
def new_member():
    return render_template("members/new.html")

#CREATE POSTmethod, /members, request.form[''] data, repo.save(member)

@members_blueprint.route("/members", methods=['POST'])
def add_member():
    name = request.form['name']
    email = request.form['email']
    status = request.form['status']
    type = request.form['type']

    new_member = Member(name, email, status, type)
    member_repository.save(new_member) 
    return redirect("/members")     

#UPDATE POSTmethod, /members/<id>, request.form[''] data repo.update(member)

