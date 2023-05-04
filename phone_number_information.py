import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone

class phone_number_information:

    def __init__(self):
        self.region_code = None
        self.country_name = None
        self.timezone = None
        self.carrier = None
        self.stored_phone_numbers = []

    def save_phone_number(self, phone_number):
        try:
            parsed_number = phonenumbers.parse(phone_number, None)
            self.stored_phone_numbers.append(phone_number)
            print(f"{phone_number} added to the table.")

        except phonenumbers.phonenumberutil.NumberParseException as e:
            print("Invalid input.")
            return e

    def information(self, phone_number):
        pn = phonenumbers.parse(phone_number)
        self.region_code = phonenumbers.region_code_for_country_code(pn.country_code)
        self.country_name = geocoder.description_for_number(pn, "en")
        self.timezone = timezone.time_zones_for_number(pn)
        self.carrier = carrier.name_for_number(pn, self.country_name)
        print(
            f"\n Phone number: {phone_number}\n Region code: {self.region_code}\n Country name: {self.country_name}\n Potential timezone: {self.timezone}\n Potential carrier: {self.carrier}")
