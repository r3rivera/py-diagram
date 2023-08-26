from flask_bcrypt import Bcrypt

b_crypt = Bcrypt()
pass_word = 'test12345'
hash_value = b_crypt.generate_password_hash(password=pass_word)
print(hash_value)

check = b_crypt.check_password_hash(hash_value, 'test12345')
print(check)