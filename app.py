from peewee import PostgresqlDatabase, Model, CharField, DateField, IntegerField
from datetime import date


db = PostgresqlDatabase("contactbook", user="stacyleitstein",
                        password="", host="localhost", port=5432)

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

sara = ContactBook(name="Sara Sanchez", address="55 Park Ave., NY, NY", zipcode=11165,
                   phoneNumber="212-555-8964", cellPhone="738-423-9933", business="Web Store", birthday=date(1987, 11, 13))

john = ContactBook(name="John Rocks", address="59 Corner Ave., Union, NJ", zipcode=11435,
                   phoneNumber="973-523-8964", cellPhone="718-893-9763", business="construction", birthday=date(1980, 12, 12))

kyle = ContactBook(name="Kyle Flys", address="43 Pine Ave., Holden, NJ", zipcode=18965,
                   phoneNumber="632-755-8994", cellPhone="776-343-9930", business="barber", birthday=date(1997, 10, 15))

kim = ContactBook(name="Kim Pentz", address="23 Highland Ave., York, PA", zipcode=19865,
                  phoneNumber="322-585-1964", cellPhone="468-523-8833", business="Childcare", birthday=date(1969, 11, 23))

chris = ContactBook(name="Chris Star", address="75 Venture Ave., Main, MA", zipcode=13485,
                    phoneNumber="432-985-1264", cellPhone="938-323-0753", business="Doctor", birthday=date(1977, 12, 24))

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


chris.name = "Crystal"
chris.save()

chris.delete.instance()


def contact_Book():
    print("Hello, and welcome to your contacts! please choose from the following... \n 1: Show all Contacts \n 2: Search for a Contact \n 3: Add a contact \n 4: Delete a contact \n 5: Update a contact \n 6: Quit")
    choice = int(input('Enter Number: '))
    if choice == 1:
        all_contacts()
    elif choice == 2:
        search_contacts()
    elif choice == 3:
        contact_add()
    elif choice == 4:
        delete_contact()
    elif choice == 5:
        update_contacts()


def all_contacts():
    contacts = Contact.select()
    for contact in contacts:
         print(
             f'Full Name: {contact.first_name} {contact.last_name}, Phone: {contact.phone}, Email: {contact.email}')

    contact_Book()


def search_contacts():
     search_name = str(
          input('Which first name would you like to search for?: '))
      result = Contact.select().where(Contact.first_name == search_name)
       for contact in result:
            print(
                f'Full Name: {contact.first_name} {contact.last_name}, Phone: {contact.phone}, Email: {contact.email}')
        contact_Book()


def contact_add():
      new_first_name = str(input('What is the new first name?: ')).lower()
       new_last_name = str(input('What is the new last name?: ')).lower()
        new_phone = str(input('What is the new phone number?: '))
        new_email = str(input('What is the new email address?: ')).lower()
        new_contact = Contact(first_name=new_first_name, last_name= new_last_name, phone = new_phone, email = new_email).save()
        for contact in Contact:
            print(
                f'Full Name: {contact.first_name} {contact.last_name}, Phone: {contact.phone}, Email: {contact.email}')
        contact_Book()


def update_contacts():
     update_person = str(input('Which contact would you like to edit by first name?: '))
      new_first_name = str(input('What is the new first name?: ')).lower()
       new_last_name = str(input('What is the new last name?: ')).lower()
        new_phone = str(input('What is the new phone number?: '))
        new_email = str(input('What is the new email address?: ')).lower()
        result = Contact.update(first_name=new_first_name, last_name= new_last_name, phone = new_phone, email = new_email).where(Contact.first_name == update_person).execute()
        for contact in Contact:
            print(
                f'Full Name: {contact.first_name} {contact.last_name}, Phone: {contact.phone}, Email: {contact.email}')
        contact_Book()


def delete_contact():
    update_person = str(input('Which contact would you like to delete by first name?: '))
     result = Contact.delete().where(Contact.first_name == update_person).execute()
      print(f"Deleted: {update_person}")
       contact_Book()


contact_Book()
