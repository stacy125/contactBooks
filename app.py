from peewee import PostgresqlDatabase, Model, CharField, DateField, IntegerField
from datetime import date


db = PostgresqlDatabase("contactbook", user="stacyleitstein", password="", host="localhost", port=5432)

db.connect()


class BaseModel(Model):
    class Meta:
        database = db


class ContactBook(BaseModel):
    name = CharField()
    address = CharField()
    zipcode = IntegerField()
    phoneNumber = CharField()
    cellPhone = CharField()
    business = CharField()
    birthday = DateField()

db.create_tables([ContactBook])

sara = ContactBook(name="Sara Sanchez", address="55 Park Ave., NY, NY", zipcode=11165, phoneNumber="212-555-8964", cellPhone="738-423-9933", business="Web Store", birthday=date(1987, 11, 13))

john = ContactBook(name="John Rocks", address="59 Corner Ave., Union, NJ", zipcode=11435, phoneNumber="973-523-8964", cellPhone="718-893-9763", business="construction", birthday=date(1980, 12, 12))

kyle = ContactBook(name="Kyle Flys", address="43 Pine Ave., Holden, NJ", zipcode=18965, phoneNumber="632-755-8994", cellPhone="776-343-9930", business="barber", birthday=date(1997, 10, 15))

kim = ContactBook(name="Kim Pentz", address="23 Highland Ave., York, PA", zipcode=19865, phoneNumber="322-585-1964", cellPhone="468-523-8833", business="Childcare", birthday=date(1969, 11, 23))

chris = ContactBook(name="Chris Star", address="75 Venture Ave., Main, MA", zipcode=13485, phoneNumber="432-985-1264", cellPhone="938-323-0753", business="Doctor", birthday=date(1977, 12, 24))

sara.save()
john.save()
kyle.save()
kim.save()
chris.save()

ContactBook.get(ContactBook.name == "Sara Sanchez")
ContactBook.get(ContactBook.name == "John Rocks")
ContactBook.get(ContactBook.name == "Kim Pentz")
ContactBook.get(ContactBook.name == "Kyle Flys")
ContactBook.get(ContactBook.name == "Chris Star")

