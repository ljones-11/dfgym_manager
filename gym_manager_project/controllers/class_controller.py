#imports

#blueprint

#GET list classes '/classes' repo.select_all, render list

#GET show class '/classes/<id>' repo.select(id), render 

#DELETE POSTmethod, /classes/<id>/delete, repo.delete redirect

#CREATE POSTmethod, /classes, request.form[''] data, class=class, repo.save(class)

#UPDATE POSTmethod, /classes/<id>, request.form[''] data repo.update(class)