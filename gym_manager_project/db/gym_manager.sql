DROP TABLE bookings;
DROP TABLE members;
DROP TABLE workouts;

CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255),
    member_status BOOLEAN,
    member_type VARCHAR(255)
);

CREATE TABLE workouts (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    description VARCHAR(255),
    duration INT,
    date VARCHAR(255),
    time VARCHAR(255),
    capacity INT,
    status BOOLEAN
);

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    member_id INT REFERENCES members(id) ON DELETE CASCADE,
    workout_id INT REFERENCES workouts(id) ON DELETE CASCADE
);