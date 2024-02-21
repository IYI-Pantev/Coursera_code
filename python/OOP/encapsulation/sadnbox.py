#changed the name of the private attribute from self.email to self._email.
# This avoids the conflict between the property and the setter method.

class Profile:

    email_min_length = 5

    def __init__(self, email) -> None:
        self._email = email

    @property
    def email(self):
        return f'{self._email}@gmail.com'

    @email.setter
    def email(self, new_email):
        if len(new_email) >= Profile.email_min_length:
            self._email = new_email
        else:
            raise ValueError(f'Length must be minimum {Profile.email_min_length} characters long.')

# Example usage:
profile_name = Profile('pepsi')
print(profile_name.email)

profile_name.email = 'colagen'
print(profile_name.email)