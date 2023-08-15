from dba import db, User

# Create a new table entry
#user = User('Dianne Naag', 'diana.naag@gmail.com')
#db.session.add(user)
#db.session.commit() 


# Read the table 
all_user = User.query.all()
for user in all_user:
    print(user)
    
print("####### Query")
by_column_user = User.query.filter_by(email='jona.severo@yahoo.com')
for user in by_column_user:
    print(user)
    
