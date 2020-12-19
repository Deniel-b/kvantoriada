from peewee import Model, SqliteDatabase
from peewee import PrimaryKeyField, TextField, IntegerField, BooleanField, ForeignKeyField

db = SqliteDatabase('databases/persons.db')


class Users(Model):
    ID = PrimaryKeyField(unique=True, primary_key=True)
    Surname = TextField()
    Name = TextField()
    Patronymic = TextField()
    Email = TextField(null=False, unique=True)
    Password = TextField(null=False)
    Age = IntegerField()
    Birth = TextField()
    Gender = TextField()
    Type = BooleanField()
    Snils = TextField()
    Polis = TextField()

    class Meta:
        database = db
        db_table = "Users"


class Diseases(Model):
    Key = ForeignKeyField(Users)
    Diseases = TextField()

    class Meta:
        database = db
        db_table = "Appointments"


class Directions(Model):
    id = PrimaryKeyField(primary_key=True, unique=True)
    direction = TextField()

    class Meta:
        database = db
        db_table = "Directions"


class Rooms(Model):
    id = PrimaryKeyField(primary_key=True, unique=True)
    room_num = IntegerField()

    class Meta:
        database = db
        db_table = "Rooms"


class Doctors(Model):
    id = PrimaryKeyField(primary_key=True, unique=True)
    Name = TextField()
    direction_id = ForeignKeyField(Directions)
    room_id = ForeignKeyField(Rooms)
    login = TextField(unique=True, null=False)

    class Meta:
        database = db
        db_table = "Doctors"


class Appointments(Model):
    id = PrimaryKeyField(primary_key=True, unique=True)
    Key_id = ForeignKeyField(Users)
    TimeStart = IntegerField()
    TimeEnd = IntegerField()
    Data = TextField()
    is_busy = BooleanField()
    doctor_id = ForeignKeyField(Doctors)
    is_ended = BooleanField()
    is_reg = BooleanField()
    direction_id = ForeignKeyField(Directions)

    class Meta:
        database = db
        db_table = "Appointments"
