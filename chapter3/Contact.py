class ContactList(list):
    def search(self, name):
        '''
        Returns all contacts that contain the search value in their name.
        :param name: Name to match name of contact.
        :return:
        '''
        matching_contacts = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)

        return matching_contacts

class Contact(object):
    # Property shared by all instances of class.
    all_contacts = ContactList()

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)


class Supplier(Contact):
    def order(self, order):
        print("If this were a real system we would send "
              "'{}' order to '{}'".format(order, self.name))

class Friend(Contact):
    def __init__(self, name, email, phone):
        super().__init__(name, email)
        self.phone = phone



if __name__== "__main__":
    c1 = Contact("John A", "johnA@john.de")
    c2 = Contact("John B", "johnB@john.de")
    c3 = Contact("Jenna C", "jennaC@john.de")
    print([c.name for c in Contact.all_contacts.search("John")])