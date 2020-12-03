from peewee import *


db = SqliteDatabase('databases/persons.db')


class Humans(Model):
    ID = PrimaryKeyField(null=False, unique=True)
    Name = TextField(null=False)
    Surname = TextField()
    TimeStart = IntegerField()
    TimeEnd = IntegerField()
    Age = IntegerField()
    Birth = TextField()
    Gender = BooleanField()
    Diseases = TextField()
    Doctor = TextField()

    class Meta:
        database = db
        db_table = 'Persons'


