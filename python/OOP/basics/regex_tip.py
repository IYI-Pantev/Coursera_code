import re

email = 'jeremy64@gmail.com'

(name, mail, domain) = re.split('[@.]', email)
print(name, mail, domain)