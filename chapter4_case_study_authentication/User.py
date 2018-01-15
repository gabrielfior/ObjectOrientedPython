import hashlib


class User:
    def __init__(self, username, password):
        """
        Creates new user object. Password will be encrypted before storing
        :param username: Username for login
        :param password: Password as plain text
        """
        self.username = username
        self.password = self._encrypt_pw(password)
        self.is_logged_in = False

    def _encrypt_pw(self, password):
        """
        Encrypt password with the username and return the sha digest
        :param password: Password to be encrypted
        :return:
        """
        hash_string = (self.username + password)
        hash_string = hash_string.encode("utf8")
        return hashlib.sha256(hash_string).hexdigest()

    def check_password(self, password):
        encrypted = self._encrypt_pw(password)
        return encrypted == self.password

    # STOPPED PAGE 116
