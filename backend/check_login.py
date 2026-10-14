from getpass import getpass
from database import SessionLocal
from models import User
from security import verify_password

email = input("Registered email: ").strip().lower()
password = getpass("Original registration password: ")

db = SessionLocal()
try:
    user = db.query(User).filter(User.email == email).first()
    if user is None:
        print("RESULT: User not found")
    else:
        print("RESULT:", "Password matches" if verify_password(password, user.password_hash) else "Password does not match")
finally:
    db.close()
