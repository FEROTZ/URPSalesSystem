from ..utils.jwt import Jwt
from ..exceptions.auth_exceptions import AuthErrors

class auth:
    async def __new__(
        cls,
        token: dict,

    ):
        decrypt: object = Jwt().decode(token.credentials)

        if not decrypt:
            AuthErrors.invalidToken()
            return False
        
        return True