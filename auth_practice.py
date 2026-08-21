from passlib.context import CryptContext

#use bcrypt algorithm
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

#turns plain password text to hash
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

#checks if a password is correct
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

#test
user_password = "Jordan"

hashed_db_entry = hash_password(user_password)

print(f"plain password: {user_password}")
print(f"Hashed Database Entry: {hashed_db_entry}")

#verify correct password
is_correct = verify_password("Jordan", hashed_db_entry)
print(f"Login Attempt (Jordan): {'success' if is_correct else 'Failed'}")


is_wrong = verify_password("Mcbeth", hashed_db_entry)
print(f"Login attempt (Mcbeth): {'success' if is_wrong else 'Failed'}")