import unittest
from models.member import Member

class TestMember(unittest.TestCase):
    def setUp(self):
        self.member1 = Member('Jack Bauer', 'jb@24.com', '0', 'premium')

    def test_member_has_name(self):
        self.assertEqual('Jack Bauer', self.member1.name)

    def test_member_has_email(self):
        self.assertEqual('jb@24.com', self.member1.email)

    def test_member_has_status(self):
        self.assertEqual('0', self.member1.status)

    def test_member_has_type(self):
        self.assertEqual('premium', self.member1.type)
    
