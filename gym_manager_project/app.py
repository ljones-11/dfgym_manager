from flask import Flask, render_template

#import blueprints from controllers
from controllers.booking_controller import bookings_blueprint
from controllers.workout_controller import workouts_blueprint
from controllers.member_controller import members_blueprint

app = Flask(__name__
)
#register blueprints
app.register_blueprint(bookings_blueprint)
app.register_blueprint(workouts_blueprint)
app.register_blueprint(members_blueprint)

#@app.route homepage '/' . "index.html", render homeepage

if __name__ == '__main__':
    app.run(debug=True)