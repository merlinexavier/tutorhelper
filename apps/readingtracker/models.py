from django.db import models

from django.contrib.auth.models import User


class Student(models.Model):

    # Link to the user model
    user = models.OneToOneField(User)

    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)

    date_of_birth = models.DateField()

    school = models.CharField(max_length=30)

    def __unicode__(self):
        return "%s %s" % (self.first_name, self.last_name)


class Book(models.Model):

    title = models.CharField(max_length=40)
    author = models.CharField(max_length=25)

    isbn = models.PositiveIntegerField(max_length=13)

    ease = models.DecimalField(max_digits=5, decimal_places=2,
                             null=True, blank=True)
    grade_level = models.DecimalField(max_digits=4, decimal_places=2,
                                    null=True, blank=True)

    def __unicode__(self):
        return "'%s' by %s" % (self.title, self.author)


class ReadingSession(models.Model):

    student = models.ForeignKey('Student')

    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    book = models.ForeignKey('Book')
    pages = models.IntegerField()

    def __unicode__(self):
        return "%s read from %s to %s" % (self.student,
                                          self.start_time, self.end_time)
