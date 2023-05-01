import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone

class phone_number_information:

    def __init__(self):
        self.stored_phone_numbers = []

    def save_phone_number(self, phone_number):
        try:
            parsed_number = phonenumbers.parse(phone_number, None)
            if not phonenumbers.is_valid_number(parsed_number):
                return "Invalid phone number."
            else:
                self.stored_phone_numbers.append(phone_number)

        except phonenumbers.phonenumberutil.NumberParseException as e:
            return e

    def information(self, phone_number):
        pn = phonenumbers.parse(phone_number)
        self.country_code = phonenumbers.region_code_for_country_code(pn.country_code)
        self.country_name = geocoder.description_for_number(pn, "en")
        self.valid = phonenumbers.is_valid_number(pn)
        self.possible = phonenumbers.is_possible_number(pn)
        self.timezone = timezone.time_zones_for_number(pn)
        self.carrier = carrier.name_for_number(pn, self.country_name)
        print(
            f"\n Phone number: {phone_number}\n Country code: {self.country_code}\n Country name: {self.country_name}\n Is valid?: {self.valid}\n Is possible?: {self.possible}\n Potential timezone: {self.timezone}\n Potential carrier: {self.carrier}")
