class AuthenticationStrategy:
    def authenticate(self, credentials: dict) -> bool:
        pass

# Implement concrete strategies
class PasswordAuthentication(AuthenticationStrategy):
    def authenticate(self, credentials: dict) -> bool:
        # In a real-world scenario, you'd check the credentials against a database or another secure storage.
        return credentials.get('username') == 'user' and credentials.get('password') == 'pass'

class TokenAuthentication(AuthenticationStrategy):
    def authenticate(self, credentials: dict) -> bool:
        # Check the token against a list of valid tokens or a database.
        return credentials.get('token') == 'valid_token'

class OAuthAuthentication(AuthenticationStrategy):
    def authenticate(self, credentials: dict) -> bool:
        # Check the OAuth token and other parameters. This is a simplified example.
        return credentials.get('oauth_token') == 'valid_oauth_token'

# Context class
class Authenticator:
    def __init__(self, strategy: AuthenticationStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: AuthenticationStrategy):
        self._strategy = strategy

    def execute_authentication(self, credentials: dict) -> bool:
        return self._strategy.authenticate(credentials)


# Usage
password_credentials = {'username': 'user', 'password': 'pass'}
token_credentials = {'token': 'valid_token'}
oauth_credentials = {'oauth_token': 'valid_oauth_token'}

# Using PasswordAuthentication
authenticator = Authenticator(PasswordAuthentication())
print(f'PasswordAuthentication result: {authenticator.execute_authentication(password_credentials)}')

# Switching to TokenAuthentication
authenticator.set_strategy(TokenAuthentication())
print(f'TokenAuthentication result: {authenticator.execute_authentication(token_credentials)}')

# Switching to OAuthAuthentication
authenticator.set_strategy(OAuthAuthentication())
print(f'OAuthAuthentication result: {authenticator.execute_authentication(oauth_credentials)}')
