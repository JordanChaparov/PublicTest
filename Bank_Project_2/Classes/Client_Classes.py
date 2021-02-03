class Client:                                                                               # parent class Client
    def __init__(self, client_name, client_address, client_password, client_pass_check,
                 client_id, client_type="firm", client_access="User"):
        self._client_name = client_name
        self._client_address = client_address
        self._client_password = client_password
        self._client_pass_check = client_pass_check
        self._client_id = client_id
        self._client_type = client_type
        self._client_access = client_access

    def get_client_name(self):                                                              # getter for client name
        return self._client_name

    def get_client_address(self):                                                           # getter for client address
        return self._client_address

    def get_client_password(self):                                                          # getter for client password
        return self._client_password

    def get_client_pass_check(self):                                                        # getter for password check
        return self._client_pass_check

    def get_client_id(self):                                                                # getter for client id
        return self._client_id

    def get_client_type(self):                                                              # getter for client type
        return self._client_type

    def get_client_access(self):                                                            # getter for client access
        return self._client_access


class Individual(Client):                                                    # subclass to parent class Client
    def __init__(self, client_name, client_last_name, client_address, client_email, client_phone,
                 client_password, client_pass_check, client_id, client_type="individual", client_access="User"):
        super().__init__(client_name, client_address,                        # using the constructor of the parent class
                         client_password, client_pass_check, client_id)
        self._client_last_name = client_last_name                            # adding new parameters for this subclass
        self._client_email = client_email
        self._client_phone = client_phone
        self._client_type = client_type
        self._client_access = client_access

    def get_client_last_name(self):                                          # getter for the last name of the subclass
        return self._client_last_name

    def get_client_email(self):                                              # getter for the email of the subclass
        return self._client_email

    def get_client_phone(self):                                              # getter for the phone of the subclass
        return self._client_phone


class Firm(Client):                                                            # subclass to the parent class Client
    def __init__(self, client_name, client_address, manager, client_password,  # using the constructor of the superclass
                 client_pass_check, client_id, client_type="firm", client_access="User"):
        super().__init__(client_name, client_address, client_password,
                         client_pass_check, client_id)
        self._manager = manager                                                # adding new parameters for this subclass
        self._client_type = client_type
        self._client_access = client_access

    def get_manager(self):                                                     # getter for manager of the subclass
        return self._manager
