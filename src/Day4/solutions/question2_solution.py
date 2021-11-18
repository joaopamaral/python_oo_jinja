class Address:
    def __init__(self, street, num):
        self.street_name = street
        self.number = num


class CampusAddress(Address):
    def __init__(self, office_number):
        super().__init__(street="Massachusetts Ave", num=77)
        self.office_number = office_number


if __name__ == '__main__':
    Sarina_addr = CampusAddress("32-G904")
    print(Sarina_addr.office_number)
    print(Sarina_addr.street_name)
    print(Sarina_addr.number)