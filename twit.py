from model.user import User

import json

class Twit:
    def __init__(self, id: str, body: str, author: User):
        self.id = id
        self.body = body
        self.author = author

    def to_dict(self):
        return dict(id=self.id, body=self.body, author=self.author)

    




