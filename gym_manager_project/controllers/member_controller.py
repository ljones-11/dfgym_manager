from flask import Flask, Blueprint, render_template, redirect
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


#CREATE POSTmethod, /members, request.form[''] data, member=Member, repo.save(member)

#UPDATE POSTmethod, /members/<id>, request.form[''] data repo.update(member)

