class User:                                                                                 # parent class User
    def __init__(self, first_name, last_name, address, email, phone,
                 password, pass_check, user_id, access="User", client_type="individual"):   # class constructor
        self._first_name = first_name
        self._last_name = last_name
        self._address = address
        self._email = email
        self._phone = phone
        self._password = password
        self._pass_check = pass_check
        self._user_id = user_id
        self._access = access
        self._client_type = client_type

    def get_first_name(self):                                                               # first_name getter
        return self._first_name

    def get_last_name(self):                                                                # last_name getter
        return self._last_name

    def get_address(self):                                                                  # address getter
        return self._address

    def get_email(self):                                                                    # email getter
        return self._email

    def get_phone(self):                                                                    # phone getter
        return self._phone

    def get_password(self):                                                                 # password getter
        return self._password

    def get_pass_check(self):                                                               # password check getter
        return self._pass_check

    def get_id(self):                                                                       # id getter
        return self._user_id

    def get_access(self):
        return self._access                                                                 # access getter

    def get_client_type(self):                                                              # client type getter
        return self._client_type


class Employee(User):                                                     # class Employee inheriting parent class User
    def __init__(self, first_name, last_name, address, email, phone,      # using superclass constructor
                 password, pass_check, user_id, access="Employee", client_type="individual"):
        super().__init__(first_name, last_name, address, email, phone,
                         password, pass_check, user_id, client_type)      # using the parent class constructor
        self._access = access                                             # changing access parameter to "employee"


class Admin(User):                                                        # class Admin inheriting parent class User
    def __init__(self, first_name, last_name, address, email, phone,      # using superclass constructor
                 password, pass_check, user_id, access="Admin", client_type="individual"):
        super().__init__(first_name, last_name, address, email, phone,
                         password, pass_check, user_id, client_type)      # using the parent class constructor
        self._access = access                                             # changing access parameter to "admin"
