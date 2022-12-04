from flask import Flask, Blueprint
from models.member import Member
import repositories.member_repository as member_repository

members_blueprint = Blueprint("members", __name__)

#blueprint

#GET list members '/members' repo.select_all, render list

#GET show member '/members/<id>' repo.select(id), render 

#DELETE POSTmethod, /members/<id>/delete, repo.delete redirect

#CREATE POSTmethod, /members, request.form[''] data, member=Member, repo.save(member)

#UPDATE POSTmethod, /members/<id>, request.form[''] data repo.update(member)

