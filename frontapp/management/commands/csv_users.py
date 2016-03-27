import csv
import string
import random

from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.conf import settings


class Command(BaseCommand):
    help = '''run: python manage csv_users users.csv --email=True.
            user.csv is a csv file with its absolute path
            A line of users.csv is made of the user username and an email
            If you specify email, an email is sent to notify the new user.'''

    def add_arguments(self, parser):
        parser.add_argument('user_csv')
        parser.add_argument('--email',
                            action='store_true',
                            dest='email',
                            default=False,
                            help='Send email to new users')

    def handle(self, *args, **options):
        user_csv = options['user_csv']

        # Just alphanumeric characters
        chars = string.letters + string.digits
        pwd_size = 8

        # Read csv file
        with open(user_csv) as ff:
            reader = csv.reader(ff, delimiter=';')

            for i, row in enumerate(reader):
                row = row[0].split(' ')
                print row
                username = "_".join(row[:2])
                username = username.replace(" ", "_")
                email = row[2]
                password = ''.join((random.choice(chars))
                                   for x in range(pwd_size))
                print username, password
                try:
                    User.objects.create_user(username, email, password)
                    if options['email']:
                        subject = 'Telecom Workshop - Admin login'
                        message = (u'Hi,\nIf you want to help with the '
                                   u'registration process, go to this page: '
                                   u'http://127.0.0.1:8000/accounts/login/?'
                                   u'next=/registration_admin \n'
                                   u'Your login is %s and your password is %s.'
                                   u'\nCheers') % (username, password)
                        print message
                        send_mail(subject, message, settings.EMAIL_HOST_USER,
                                  [email], fail_silently=False)
                except Exception, e:
                    print('!!!!!!!!! Problem when creating User %s' % username)
                    raise e
