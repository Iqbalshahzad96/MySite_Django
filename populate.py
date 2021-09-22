import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','mysite.settings')

import django
django.setup()

import random
from firstApp.models import AccessRecord,Webpage,Topic
from firstApp.models import User
from faker import Faker

fakegen = Faker()
topics = ['search', 'social', 'Marketplace', 'News', 'Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populateWebpages (n=5):
        for entry in range(n):
            top = add_topic()

            # Create Fake Data for entry
            fake_url = fakegen.url()
            fake_date = fakegen.date()
            fake_name = fakegen.company()

            webpg = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]
            webpg.save()

            acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]
            acc_rec.save()
            print(entry)

def populateUsers (n=5):
        for entry in range(n):
            
            # Create Fake Data for entry
            fake_name = fakegen.name().split()
            fake_first_name = fake_name[0]
            fake_last_name = fake_name[1]
            fake_email = fakegen.email()

            # Create new User Entry
            user = User.objects.get_or_create(firstName=fake_first_name,
                                          lastName=fake_last_name,
                                          email=fake_email)[0]

if __name__ == '__main__':
    print("Populating the databases...Please Wait")
    # populateWebpages(20)
    # populateUsers(20)
    print('Populating Complete')