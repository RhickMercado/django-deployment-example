import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')
import django
django.setup()


import random
from first_app.models import User
from faker import Faker

fakegen = Faker()

def populate(N=5):
    for entry in range(N):
        fake_lname = fakegen.name
        fake_fname = fakegen.name
        fake_email = fakegen.email

        User.objects.get_or_create(lastName = fake_lname, firstName = fake_fname, eMail = fake_email)

if __name__ == '__main__':
    print("populating script!")
    populate(20)
    print("populating complete!")
