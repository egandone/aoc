import collections
import itertools

with open("input.txt") as input:
    lines = input.readlines()

print(f'len(lines) = {len(lines)}')

adapters = [int(l.strip()) for l in lines]
adapters.append(0)
adapters.append(max(adapters)+3)
adapters = sorted(adapters)
print(f'{adapters}')

# Find all the adapters that could be removed individually.
removal_candidates = [adapters[n] for n in range(
    1, len(adapters) - 1) if adapters[n+1] - adapters[n-1] <= 3]
print(f'removals {removal_candidates}')

# Now we reverse iterate down the removals and double
# the choice count for each one.  However, if the candidate
# is part of a string of 3 contiguous adapters then the count
# is not quiet double because all three cannot be removed.
# So, in this case, count is reduced by half the total of the
# count of the third one
counts = dict()
total_count = 1
for candidate in sorted(removal_candidates, reverse=True):
    #    print(f'{total_count} - checking {candidate}')
    total_count *= 2
    if (candidate + 2) in removal_candidates and (candidate + 1) in removal_candidates:
        total_count -= int(counts[candidate + 2] / 2)
    counts[candidate] = total_count

print(f'{total_count}')
