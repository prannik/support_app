from dataclasses import dataclass

from app.account.models import CustomUser


@dataclass
class UserDataClass:
    first_name: str
    last_name: str
    username: str
    email: str
    password: str = None
    id: int = None

    @classmethod
    def from_instance(cls, user: 'CustomUser') -> 'UserDataClass':
        return cls(
            first_name=user.first_name,
            last_name=user.last_name,
            username=user.username,
            email=user.email,
            id=user.id,
        )


def create_user(user_dc: 'UserDataClass') -> 'UserDataClass':
    instance = CustomUser(
        first_name=user_dc.first_name,
        last_name=user_dc.last_name,
        username=user_dc.username,
        email=user_dc.email
    )
    if user_dc.password is not None:
        instance.set_password(user_dc.password)

    instance.save()

    return UserDataClass.from_instance(instance)
