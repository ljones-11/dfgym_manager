DROP TABLE bookings;
DROP TABLE members;
DROP TABLE workouts;

CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255),
    status BIT,
    type VARCHAR(255)
);

CREATE TABLE workouts (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    description VARCHAR(255),
    duration INT,
    date DATE,
    time time,
    capacity INT,
    status BIT
);

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    member_id INT REFERENCES members(id) ON DELETE CASCADE,
    workout_id INT REFERENCES workouts(id) ON DELETE CASCADE
);