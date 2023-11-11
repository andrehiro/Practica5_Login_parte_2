class User:
    def __init__(self, id, username, password, usertype, fullname="") -> None:
        self.id = id
        self.username = username
        self.password = password
        self.fullname = fullname
        self.usertype = usertype