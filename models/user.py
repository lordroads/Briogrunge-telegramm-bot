class User:
    user_id: int
    is_bot: bool
    is_admin: bool = False
    first_name: str
    last_name: str
    username: str
    language_code: str

    def __init__(self,
                 obj: tuple = None,
                 user_id: int = None,
                 is_bot: bool = None,
                 is_admin: bool = None,
                 first_name: str = None,
                 last_name: str = None,
                 username: str = None,
                 language_code: str = None
                 ):
        if obj:
            self.user_id = obj[0]
            self.is_bot = obj[1]
            self.is_admin = obj[2]
            self.first_name = obj[3]
            self.last_name = obj[4]
            self.username = obj[5]
            self.language_code = obj[6]
        else:
            self.user_id = user_id
            self.is_bot = is_bot
            self.is_admin = is_admin
            self.first_name = first_name
            self.last_name = last_name
            self.username = username
            self.language_code = language_code

    def get_tuple(self) -> tuple:
        return (self.user_id, self.is_bot, self.is_admin, self.first_name, self.last_name, self.username, self.language_code)

    def get_tuple_for_update(self) -> tuple:
        return (self.is_bot, self.is_admin, self.first_name, self.last_name, self.username, self.language_code, self.user_id)

    def get_info(self) -> str:
        return f'{self.user_id}, {self.is_bot}, {self.is_admin}, {self.first_name}, {self.last_name}, {self.username}, {self.language_code}'
