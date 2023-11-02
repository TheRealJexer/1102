sample = "380 339 420 308 448"
cols = sample.split()
numList = []
for col in cols:
    num = int(col)
    numList.append(num)
start = min(numList)
for count in range(start, max(numList)):
    print(count)
    if count in numList:
        # we have membership
        pass
    else:
        # otherwise
        print(f"{count} is missing")    

    """Does the same thing that lines 10 to 15 does"""
    if count not in numList:
        print(f"{count} is missing")
