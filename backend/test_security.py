from app.database.session import SessionLocal
from app.schemas.user import UserRegisterRequest
from app.services.auth_service import AuthService

db = SessionLocal()

service = AuthService()

user = service.register_user(
    db,
    UserRegisterRequest(
        first_name="Lokeshwari",
        last_name="Busam",
        email="lokeshwari@test.com",
        password="Password@123",
    ),
)

print(user.uuid)
print(user.email)

db.close()