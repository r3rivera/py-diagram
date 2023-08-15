from dba import db, User

# Creates the database table base on the model provided in the db.py
db.create_all()

user_1 = User('Ryan Rivera', 'rr.rivs@gmail.com')
user_2 = User('Kristine Niduelan', 'tin.niduelan@gmail.com')
user_3 = User('Wela Galang', 'wella.galang@gmail.com')
user_4 = User('Jonalyn Severo', 'jona.severo@yahoo.com')

# Pre-Add to table
print(user_1.user_id)
print(user_2.user_id)
print(user_3.user_id)
print(user_4.user_id)

db.session.add_all([user_1, user_2, user_3, user_4])
db.session.commit()

print(user_1.user_id)
print(user_2.user_id)
print(user_3.user_id)
print(user_4.user_id)
