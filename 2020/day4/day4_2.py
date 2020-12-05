import re
required_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']


class Passport:

    def __init__(self, creds):
        self._creds = {}
        self.add(creds)

    def add(self, creds):
        for cred in creds.strip().split():
            key, value = cred.split(':')
            self._creds[key] = value

    def _check_number(self, value, min, max):
        try:
            return min <= int(value) <= max
        except:
            return False

    def _check_year(self, field, min, max):
        return self._check_number(self._creds[field], min, max)

    def check_byr(self):
        return self._check_year('byr', 1920, 2002)

    def check_iyr(self):
        return self._check_year('iyr', 2010, 2020)

    def check_eyr(self):
        return self._check_year('eyr', 2020, 2030)

    def check_hgt(self):
        if self._creds['hgt'].endswith('in'):
            return self._check_number(self._creds['hgt'][:-2], 59, 76)
        elif self._creds['hgt'].endswith('cm'):
            return self._check_number(self._creds['hgt'][:-2], 150, 193)
        else:
            return False

    def check_hcl(self):
        return re.match('^#[0-9a-f]{6}$', self._creds['hcl']) != None

    def check_ecl(self):
        return self._creds['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

    def check_pid(self):
        return re.match('^\d{9}$', self._creds['pid']) != None

    def is_valid(self):
        return all(k in self._creds.keys() for k in required_keys) and self.check_byr() and self.check_iyr() and self.check_eyr() and self.check_hgt() and self.check_hcl() and self.check_ecl() and self.check_pid()

    def __str__(self):
        return str(self._creds)


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

# for p in passports:
# if 'byr' in p._creds and not p.check_byr():
#     print(f"bad byr: {p._creds['byr']}")
# if 'iyr' in p._creds and not p.check_iyr():
#     print(f"bad iyr: {p._creds['iyr']}")
# if 'eyr' in p._creds and not p.check_eyr():
#     print(f"bad eyr: {p._creds['eyr']}")
# if 'hgt' in p._creds and not p.check_hgt():
#     print(f"bad hgt: {p._creds['hgt']}")
