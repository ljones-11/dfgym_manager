import pdb

from models.booking import Booking
from models.member import Member
from models.workout import Workout

import repositories.member_repository as member_repository


member_repository.delete_all()

member1 = Member('Jack Bauer', 'jackbauer@24.com', '1', 'standard')
member_repository.save(member1)
member2 = Member('Tony Almeda', 'tonymole@24.com', '1', 'standard')
member_repository.save(member2)
member2 = Member('Nina Myers', 'ninamyers@24.com', '1', 'standard')
member_repository.save(member2)

member_repository.delete(2)

member1.email = "jb@24.com"
member_repository.update(member1)

for member in member_repository.select_all():
    print (member.name, member.email)




pdb.set_trace()