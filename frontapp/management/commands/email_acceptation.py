import csv

from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from django.conf import settings


class Command(BaseCommand):
    help = '''run: python manage email_acceptation participant.csv accept/reject
            participant.csv is a csv file with its absolute path
            A line of participants.csv is made of the participant first name
            last name, email, and number of votes
            Send an email of acceptation/rejection.'''

    def add_arguments(self, parser):
        parser.add_argument('user_csv')
        parser.add_argument('type_email')

    def handle(self, *args, **options):
        user_csv = options['user_csv']
        type_email = options['type_email']

        # Read csv file
        with open(user_csv) as ff:
            reader = csv.reader(ff, delimiter=';')

            for i, row in enumerate(reader):
                row = row[0].split(',')
                print(row)
                first_name = row[0]
                last_name = row[1]
                email = row[2]
                try:
                    subject = ('Workshop Telecom - Scientific Programming '
                               'with Python and Software Engineering Best '
                               'Practices')
                    if type_email == 'accept':
                        message = ('Hi %s,\n\nwe are pleased to inform '
                                   'you that you have been selected to '
                                   'participate to the workshop about '
                                   'scientific programming with Python and '
                                   'Software Engineering Best Practices at '
                                   'Telecom ParisTech on 28-29 April.\n'
                                   'If you can not attend the workshop, '
                                   'please reply to this email.\n\n'
                                   'See you in April,\n'
                                   'The organisation team.\n\n'
                                   'More information about the workshop:'
                                   ' http://telecom-python.telenczuk'
                                   '.pl') % (first_name)
                    elif type_email == 'reject':
                        message = ('Hi %s,\n\nDue to a large number of '
                                   'applicants, we are sorry to inform you that'
                                   ' your application has not been selected for'
                                   ' the workshop.\n'
                                   'Do not hesitate to apply again when other '
                                   'workshop are organised.\n\nThanks for your'
                                   ' application.\n'
                                   'The organisation Team') % (first_name)
                        print(email, message)
                    send_mail(subject, message, settings.EMAIL_HOST_USER,
                              [email], fail_silently=False)
                except:
                    print('!!!!!!!!! Problem sending email to %s' % last_name)
