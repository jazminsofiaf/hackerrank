#!/bin/python3

# Find all the ways to form the target string, using a given set of strings
# allConstruct("purple", ["purp","p", "ur", "le", "purpl"]) -> [['purp', 'le'], ['p', 'ur', 'p', 'le']]

'''
def isPrefix(target, s):
    return target[:len(s)] == s

def getConstruction(original_string, this_target, set_strings, construction_list, memory):
    if this_target in memory:
        return memory[this_target]
    for s in set_strings:
        if isPrefix(this_target, s):
            construction_list.append(s)
            this_target = this_target.replace(s, "", 1)
            if len(this_target) < 1:
                memory[this_target] = construction_list
                return construction_list
            construction_list = getConstruction(original_string, this_target, set_strings, construction_list, memory)
            if ''.join(construction_list) == original_string:
                return construction_list
    return construction_list


def allConstruct(target_string, set_strings):
    constructions = []
    memory = {}
    for s in set_strings:
        if isPrefix(target_string, s):
            construction_list = [s]
            construction_list = getConstruction(target_string, target_string.replace(s, "", 1), set_strings, construction_list, memory)
            if ''.join(construction_list) == target_string:
                constructions.append(construction_list)
    return constructions
'''

def allConstruct(target, wordBank):
    if len(target) == 0:
        solution = [[]]
        return solution

    result = []

    for word in wordBank:
        if target.find(word) == 0:
            suffix = target[len(word):]
            suffixWays = allConstruct(suffix, wordBank)
            targetWays = []
            for suffixWay in suffixWays:
                targetWay = suffixWay
                targetWay.insert(0,word)
                targetWays.append(targetWay)
            result.extend(targetWays)
    return result

if __name__ == '__main__':
    print(allConstruct("purple", ["purp","p", "ur", "le", "purpl"]))
    print(allConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]))
    print(allConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
    print(allConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
    print(allConstruct("eeeeeeeeeeeeeeez", ["e", "eee", "eeeee", "eeeeee"]))