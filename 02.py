with open('02.txt') as f:
    pswds = [line.rstrip() for line in f]

def part_one(pswds):
    amount = 0
    for line in pswds:
        line = line.split(": ") # "1-16 b: cbbeh" => ["1-16 b", "cbbeh"]
        pswd = line[1] # "cbbeh"
        arr1 = line[0].split(" ") # "1-16 b" => ["1-16", "b"]
        char = arr1[1] # "b"
        range = arr1[0].split("-") # "1-16" => ["1", "16"]

        if pswd.count(char) >= int(range[0]) and pswd.count(char) <= int(range[1]):
            amount += 1

    print(str(amount))
'''
test = ["1-16 b: cbbeh"]
test = test[0].split(": ") # ["1-16 b: cbbeh"] => ["1-16 b", "cbbeh"]
pswd = str(test[-1]) #
arr1 = test[0].split(" ")
char = str(arr1[1])
range = str(arr1[0])
range = range.split("-")

print(pswd)
print(char)
print(str(range[0]), str(range[1]))
'''
part_one(pswds)
