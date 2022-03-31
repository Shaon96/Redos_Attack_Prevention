
import time


# vertex_offset_map =  \
# { \
#     "A": \
#         {"ABCD":[True, 0, 4], \
#         }, \
#     "B": \
#         {"BCD":[True, 0, 2], \
#         }, \
#         "C":  \
#             {"CD": [True, 0, 3], \
#               "D": [False, None, None], \
#              "BCD": [False, None, None]\
#             },\
#     "(B|C+)" :
#             {"BCD": [True, 0, 2]
#             },
#     "CC" : {"CD": [False, None, None]},
#     "C+" :{ "D": [False, None, None]}
# }
vertex_offset_map = {}

def checkKey(dict, key):
    if key in dict.keys():
        return True
    else:
        return False


def match_star(start, front, end, inp, match_len):

    """It matches the data in input 
    which is suurounded by *
    """

    matched_len = 0

    # matches the letter by increasing inp
    # by one at each step

    while(1):
        to_check = front * matched_len
        if checkKey(vertex_offset_map, to_check):
            if checkKey(vertex_offset_map[to_check], inp):
                if(not vertex_offset_map[to_check][inp][0]):
                    break
                else:
                    matched_len += 1
            else:
                    matched_len += 1
        else:
            [is_matched, start_len, end_len] = match(
                start, to_check, inp, match_len
            )
            if(not is_matched):
                break
            else:
                x = {}
                x[inp] = [is_matched, start_len, end_len]
                vertex_offset_map[to_check] = x
                matched_len += 1

    # If the enumeration is more than requied
    # it decreases the length
    while(matched_len >= 0):
        to_check = (front * matched_len)+end

        if checkKey(vertex_offset_map, to_check):
            if checkKey(vertex_offset_map[to_check], inp):
                if(not vertex_offset_map[to_check][inp][0]):
                    matched_len -= 1
                else:
                    return vertex_offset_map[to_check][inp]

        [is_matched, start_len, end_len] = match(
            start, to_check, inp, match_len
        )
        if(not is_matched):
            matched_len -= 1
        else:
            return [is_matched, start_len, end_len]
    
    x = {}
    x[inp] = [False, None, None]
    vertex_offset_map[to_check] = x
    return [False, None, None]


def match_question(start, front, end, inp, match_len):
    """It matches the data in input 
    which is suurounded by ?
    """

    matched_len = 0

    while(matched_len <= 1):
        to_check = front * matched_len
        [is_matched, start_len, end_len] = match(
            start, to_check, inp, match_len
        )
        if(not is_matched):
            break
        else:
            matched_len += 1

    while(matched_len >= 0):
        to_check = (front * matched_len)+end
        [is_matched, start_len, end_len] = match(
            start, to_check, inp, match_len
        )
        if(not is_matched):
            matched_len -= 1
        else:
            return [is_matched, start_len, end_len]
    return [False, None, None]


def match_plus(start, front, end, inp, match_len):
    """It matches the data in input 
    which is suurounded by +
    """

    matched_len = 1

    while(1):
        to_check = front * matched_len
        if checkKey(vertex_offset_map, to_check):
            if checkKey(vertex_offset_map[to_check], inp):
                if(not vertex_offset_map[to_check][inp][0]):
                    break
                else:
                    matched_len += 1
            else:
                    matched_len += 1
        else:
            [is_matched, start_len, end_len] = match(
                start, to_check, inp, match_len
            )
            if(not is_matched):
                break
            else:
                x = {}
                x[inp] = [is_matched, start_len, end_len]
                vertex_offset_map[to_check] = x
                matched_len += 1

    while(matched_len >= 1):
        to_check = (front * matched_len)+end

        if checkKey(vertex_offset_map, to_check):
            if checkKey(vertex_offset_map[to_check], inp):
                if(not vertex_offset_map[to_check][inp][0]):
                    matched_len -= 1
                else:
                    return vertex_offset_map[to_check][inp]

        [is_matched, start_len, end_len] = match(
            start, to_check, inp, match_len
        )
        if(not is_matched):
            matched_len -= 1
        else:
            return [is_matched, start_len, end_len]
    
    x = {}
    x[inp] = [False, None, None]
    vertex_offset_map[to_check] = x
    return [False, None, None]


def split_inp(regex):
    """splits the regex"""

    list_of_op = ["*", "?", "+"]
    close_brac = 0
    front, end, opr = None, None, None
    flag = False

    # if starting part is an square bracket
    if(regex[0] == "["):
        close_brac = regex.find("]")
        front = regex[:close_brac+1]
        end = regex[close_brac+1:]
        opr = "["
        flag = True

    # if starting part is an small bracket
    elif(regex[0] == "("):
        close_brac = regex.find(")")
        front = regex[:close_brac+1]
        end = regex[close_brac+1:]
        flag = True
        opr = "("

    # If it is any other opearator
    else:
        front = regex[0]
        end = regex[1:]

    # If the next charcter is any symbol
    if(len(regex) > 1 and (close_brac+1) < len(regex) and regex[close_brac+1] in list_of_op):

        front = regex[:close_brac+1]
        end = regex[close_brac+2:]
        opr = regex[close_brac+1]

    return [front, opr, end]


def match_set(start, end, inp, splitted_words, match_len):
    """It matches the set the data
    present in small brackets"""

    for i in splitted_words:
        to_check = i+end
        if checkKey(vertex_offset_map, to_check):
            if checkKey(vertex_offset_map[to_check], inp):
                # print("1")
                return vertex_offset_map[to_check][inp]
        [is_matched, start_len, end_len] = match(
            start, to_check, inp, match_len
        )
        if(is_matched):
            x = {}
            x[inp] = [is_matched, start_len, end_len]
            vertex_offset_map[to_check] = x
            return [is_matched, start_len, end_len]
        else:
            x = {}
            x[inp] = [False, None, None]
            vertex_offset_map[to_check] = x
    return [False, None, None]


def match(start, regex, inp, match_len=0):
    """Matches the regex with inp"""


    # print(vertex_offset_map)
    if(inp == "" and regex == ""):
        return [True, start, start+match_len]

    if(inp == ""):
        return [False, None, None]

    if(regex == ""):
        # print(inp,[True, start, start+match_len])
        return [True, start, start+match_len]

    if(regex == "$"):
        if(inp == ""):
            return [True, start, start+match_len]
        else:
            return [False, None, None]

    front, opr, end = split_inp(regex)
    # print(front, opr, end, inp)

    if(opr == "*"):
        if(front[0] == "["):
            return match_star(start, front, end, inp, match_len)
        else:
            if checkKey(vertex_offset_map, regex):
                if checkKey(vertex_offset_map[regex], inp):
                    return vertex_offset_map[regex][inp]
            x = match_star(start, front, end, inp, match_len)
            k = {}
            k[inp] = x
            vertex_offset_map[regex] = k
            return x

    if(opr == "+"):
        if(front[0] == "["):
            if checkKey(vertex_offset_map, regex):
                if checkKey(vertex_offset_map[regex], inp):
                    return vertex_offset_map[regex][inp]
            x = match_plus(start, front[1:-1], end, inp, match_len)
            k = {}
            k[inp] = x
            vertex_offset_map[regex] = k
            return x
        else:
            if checkKey(vertex_offset_map, regex):
                if checkKey(vertex_offset_map[regex], inp):
                    return vertex_offset_map[regex][inp]
            x = match_plus(start, front, end, inp, match_len)
            k = {}
            k[inp] = x
            vertex_offset_map[regex] = k
            return x

    if(opr == "?"):
        if(front[0] == "["):
            return match_question(start, front[1:-1], end, inp, match_len)
        else:
            return match_question(start, front, end, inp, match_len)

    elif(opr == "["):
        for i in range(1, len(front)):
            if(inp[0] == front[i]):
                # print(inp[0])
                return match(start, end, inp[1:], match_len+1)

    elif(opr == "("):
        splitted_words = front[1:-1].split("|")
        return match_set(start, end, inp, splitted_words, match_len)

    else:
        if(front[0] == inp[0] or front[0] == "."):
            if checkKey(vertex_offset_map, regex):
                if checkKey(vertex_offset_map[regex], inp):
                    return vertex_offset_map[regex][inp]
            x = match(start, end, inp[1:], match_len+1)
            k = {}
            k[inp] = x
            vertex_offset_map[regex] = k
            return x

    return [False, None, None]


def parse(regex, inp):
    """It will parse the input with regex"""

    matched_strings = []
    match_details = ""
    for i in range(len(inp)):
        match_details = match(0, regex, inp[i:], i)
        if(match_details[0]):
            matched_strings.append(
                [match_details[0], match_details[1], match_details[2]])
            return matched_strings

    return matched_strings


def match_regex_inp(inp):

    start_time = time.time()
    regex = "A(B|C+)+D"
    # regex = "[a*]*a"
    for i in parse(regex, inp):
        print("--- %s seconds ---" % (time.time() - start_time))
        # print(json.dumps(vertex_offset_map))
        return i[0]

    print("--- %s seconds ---" % (time.time() - start_time))
    return False


# print(match_regex_inp("a"*994))
# print(match_regex_inp("ABCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCE"))
# print(match_regex_inp("ABCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCD"))
print(match_regex_inp("ABCCCCCCCCCCCCCCCCCCCCCD"))
