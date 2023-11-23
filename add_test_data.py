from database import db

test_template1 = {
    "name": "Appointment Booking Form",
    "client_name": "text",
    "client_email": "email",
    "appointment_date": "date"
}

test_template2 = {
    "name": "Quiz Form",
    "question_1": "text",
    "question_2": "text",
    "question_3": "text"
}

test_template3 = {
    "name": "Newsletter Subscription Form",
    "email": "email"
}


db.insert(test_template1)
db.insert(test_template2)
db.insert(test_template3)
