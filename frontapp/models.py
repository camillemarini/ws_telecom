from __future__ import unicode_literals

from django.db import models


class Probicipant(models.Model):
    """
    This table is about people who would like to participate to the workshop
    """
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(max_length=80)
    affiliation = models.CharField(max_length=100)
    POSITION_CHOICES = (
        ('MAS', 'Master student'),
        ('PHD', 'PhD Student'),
        ('POS', 'Postdoctoral Fellow'),
        ('ENG', 'Research Engineer'),
        ('RES', 'Researcher'),
        ('OTH', 'Other'),
    )
    position = models.CharField(max_length=3,
                                choices=POSITION_CHOICES,
                                default='OTH')
    position_other = models.CharField('If other, specify', max_length=30,
                                      default='', blank=True)
    doctoral_school = models.CharField(max_length=30, default='', blank=True,
                                       help_text='for PhD students')
    research_domain = models.CharField(max_length=40)
    motivations = models.TextField(max_length=300,
                                   help_text='Explain why you want to attend \
                                              this workshop (max 300 char)')
    programming_languages = models.CharField(max_length=40, default='',
                                             blank=True,
                                             help_text='What are the \
                                                        programming languages\
                                                        you are familiar with')
    LEVEL_CHOICES = (
        ('BEG', 'Beginner'),
        ('INT', 'Intermediate'),
        ('ADV', 'Advanced'),
    )
    python_level = models.CharField(max_length=3,
                                    choices=LEVEL_CHOICES,
                                    default='BEG')

    DIET_CHOICES = (
        ('OMN', 'Omnivore'),
        ('VEG', 'Vegetarian'),
    )
    dietary = models.CharField('Dietary restrictions', max_length=3,
                               choices=DIET_CHOICES,
                               default='OMN')

    def __unicode__(self):
        return self.first_name, self.last_name
