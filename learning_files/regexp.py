import re

regex = r"[\w]"

test_str = ("abc123DEF\n")

matches = re.finditer(regex, test_str)

for matchNum, match in enumerate(matches, start=1):

    print("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum=matchNum, start=match.start(),
                                                                        end=match.end(), match=match.group()))

    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1

        print("Group {groupNum} found at {start}-{end}: {group}".format(groupNum=groupNum, start=match.start(groupNum),
                                                                        end=match.end(groupNum),
                                                                        group=match.group(groupNum)))


# email validation

regexp = r"([a-zA-Z]+) (\d+)"
match = re.search(regexp, "My son birthday is on July 20")
if match != None:
    print("Match at index %s, %s" % (match.start(), match.end()))   #This provides index of matched string
    print("Full match: %s" % (match.group(0)))
    print("Month: %s" % (match.group(1)))
    print("Day: %s" % (match.group(2)))
else:
    print("The given regex pattern does not match")

# regex = r"/^([a-z0-9_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$/"

