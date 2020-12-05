#required_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
required_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']


class Passport:

    def __init__(self, creds):
        self._creds = {}
        self.add(creds)

    def add(self, creds):
        for cred in creds.strip().split():
            key, value = cred.split(':')
            self._creds[key] = value

    def is_valid(self):
        return all(k in self._creds.keys() for k in required_keys)


passports = []
current_passport = None
with open("input.txt") as input:
    for line in input.readlines():
        if line.strip():
            if current_passport == None:
                current_passport = Passport(line)
                passports.append(current_passport)
            else:
                current_passport.add(line)
        else:
            current_passport = None

print(f'total number of passports = {len(passports)}')
all_valid = [p for p in passports if p.is_valid()]
print(f'total valid passports = {len(all_valid)}')
