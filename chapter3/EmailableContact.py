from chapter3.Contact import Contact
from chapter3.MailSender import MailSender


class EmailableContact(Contact, MailSender):
    pass
