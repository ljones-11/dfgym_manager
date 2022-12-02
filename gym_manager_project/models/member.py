class Member:
    def __init__(self, name, email, member_status, member_type, id = None):
        self.name = name
        self.email = email
        self.member_status = member_status
        self.member_type = member_type
        self.id = id