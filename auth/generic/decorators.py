from functools import wraps

class TokenAuthorization:
    __slots__ = 'storage', 'label', 'new', 'id', 'secret', 'type'

    def __init__(self, storage, new, id: str, secret: str, t_label: str = '<service>-token', t_type: str = 'Bearer'):
        self.storage = storage
        self.label = t_label
        self.new = new
        self.id, self.secret = id, secret

        self.type = t_type

    def _header(self, token: str) -> str:
            return {'Authorization' : f'{self.type} {token}'}

    def _update(self):
        json, code = self.new(self.id, self.secret)

        if code == 200:
            self.token = json['token']

    @property
    def token(self) -> str:
        return self.storage.get(self.label)

    @token.setter
    def token(self, value: str):
        self.storage.set(self.label, value)

    def __call__(self, wrapped_func):
        return self.decorate(wrapped_func)

    def decorate(self, function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            return self.call(function, *args, **kwargs)

        return wrapper

    def call(self, f, *args, **kwargs):
        token = self.token

        if token:
            kwargs.update({'headers' : self._header(token)})
            json, code = f(*args, **kwargs)

            if code not in (401, 402):
                # token is valid
                return (json, code)

        # token expired or not set
        self._update()
        kwargs.update({'headers' : self._header(self.token)})
        return f(*args, **kwargs)