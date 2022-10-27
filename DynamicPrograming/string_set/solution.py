#!/bin/python3

# Find all the ways to form the target string, using a given set of strings
# allConstruct("purple", ["purp","p", "ur", "le", "purpl"]) -> [['purp', 'le'], ['p', 'ur', 'p', 'le']]
def isPrefix(target, s):
    return target[:len(s)] == s


def getConstruction(original_string, this_target, set_strings, construction_list):
    for s in set_strings:
        if isPrefix(this_target, s):
            construction_list.append(s)
            this_target = this_target.replace(s, "", 1)
            if len(this_target) < 1:
                return construction_list
            construction_list = getConstruction(original_string, this_target, set_strings, construction_list)
            if ''.join(construction_list) == original_string:
                return construction_list
    return construction_list


def allConstruct(target_string, set_strings):
    constructions = []
    for s in set_strings:
        if isPrefix(target_string, s):
            construction_list = [s]
            construction_list = getConstruction(target_string, target_string.replace(s, "", 1), set_strings, construction_list)
            if ''.join(construction_list) == target_string:
                constructions.append(construction_list)
    return constructions


if __name__ == '__main__':
    print(allConstruct("purple", ["purp","p", "ur", "le", "purpl"]))