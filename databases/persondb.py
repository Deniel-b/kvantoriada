from peewee import *

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


class Room(Model):
    id = PrimaryKeyField(primary_key=True, unique=True)
    room_num = IntegerField()

    class Meta:
        database = db
        db_table = "Rooms"


class Doctor(Model):
    id = PrimaryKeyField(primary_key=True, unique=True)
    Name = TextField()
    direction_id = ForeignKeyField(Directions)
    room_id = ForeignKeyField(Room)

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
    doctor_key = ForeignKeyField(Doctor)

    class Meta:
        database = db
        db_table = "Appointments"
