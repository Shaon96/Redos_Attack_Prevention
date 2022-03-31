import time

vertex_offset_map = {}
index_vertex_map = {}
vertex_count = 0
regex_g = "A[BC]D"

def checkKey(dict, key):
    if key in dict.keys():
        return True
    else:
        return False




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

    matched_len = 0

    while(1):
        to_check = front * matched_len
        [is_matched, start_len, end_len] = match(
            start, to_check, inp, match_len
        )
        if(not is_matched):
            break
        else:
            matched_len += 1

    while(matched_len >= 1):
        to_check = (front * matched_len)+end
        [is_matched, start_len, end_len] = match(
            start, to_check, inp, match_len
        )
        if(not is_matched):
            matched_len -= 1
        else:
            return [is_matched, start_len, end_len]
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
    # print("front = ")
    # print(front)
    # print("opr = ")
    # print(opr)
    # print("end = ")
    # print(end)
    return [front, opr, end]


def match_set(start, end, inp, splitted_words, match_len, regex_offset=0):

    """It matches the set the data
    present in small brackets"""
    is_matched, start_len, end_len = 0,0,0
    word_offset = 0
    for i in splitted_words:
        to_check = i+end
        vertex_offset = index_vertex_map[regex_offset + word_offset]

        if checkKey(vertex_offset_map, vertex_offset):
            if checkKey(vertex_offset_map[vertex_offset], inp):
                return vertex_offset_map[vertex_offset][inp]
            [is_matched, start_len, end_len] = match(
                start, to_check, inp, match_len, regex_offset + word_offset
            )
        word_offset+=len(i)+1
        if(is_matched):
            if checkKey(vertex_offset_map, regex_offset):
                vertex_offset_map[vertex_offset][inp] = [is_matched, start_len, end_len]
            else:
                vertex_offset_map[vertex_offset] = {}
                vertex_offset_map[vertex_offset][inp] = [is_matched, start_len, end_len]
            return [is_matched, start_len, end_len]
    if checkKey(vertex_offset_map, regex_offset):
        vertex_offset_map[vertex_offset][inp] = [False, None, None]
    else:
        vertex_offset_map[vertex_offset] = {}
        vertex_offset_map[vertex_offset][inp] = [False, None, None]
    return [False, None, None]

def match_star(start, front, end, inp, match_len, regex,regex_offset=0):

    """It matches the data in input 
    which is suurounded by *
    """
    # print("Inside match_star :")
    # print("start = ")
    # print(start)
    # print("front = ")
    # print(front)
    # print("end = ")
    # print(end)
    # print("inp = ")
    # print(inp)
    # print("match_len = ")
    # print(match_len)
    matched_len = 0

    
    regex_offset = len(regex_g) - len(regex)
    print(regex_offset)
    vertex_offset = index_vertex_map[regex_offset]

    

    # matches the letter by increasing inp
    # by one at each step
    while(1):
        to_check = front * matched_len
        [is_matched, start_len, end_len] = match(
            start, to_check, inp, match_len,
        )
        
        if(not is_matched):
            break
        else:
            matched_len += 1
            # break


    # If the enumeration is more than requied
    # it decreases the length 
    while(matched_len >= 0):
        to_check = (front * matched_len)+end
        [is_matched, start_len, end_len] = match(
            start, to_check, inp, match_len, regex_offset, regex
        )
        if(not is_matched):
            matched_len -= 1
        else:
            if checkKey(vertex_offset_map, regex_offset):
                vertex_offset_map[vertex_offset][inp] = [is_matched, start_len, end_len]
            else:
                vertex_offset_map[vertex_offset] = {}
                vertex_offset_map[vertex_offset][inp] = [is_matched, start_len, end_len]

            return [is_matched, start_len, end_len]

    if checkKey(vertex_offset_map, regex_offset):
        vertex_offset_map[vertex_offset][inp] = [False, None, None]
    else:
        vertex_offset_map[vertex_offset] = {}
        vertex_offset_map[vertex_offset][inp] = [False, None, None]
    return [False, None, None]

def match(start, regex, inp, original_regex,match_len=0,regex_offset=0):

    """Matches the regex with inp"""

    # print(start)
    # print("regex_offset")
    # print(regex_offset)    
    if(inp == "" and regex == ""):
        return [True, start, start+match_len]

    if(inp == ""):
        return [False, None, None]
    
    if(regex == ""):
        # print(inp)
        # if inp != "":
        #     return [False, None, None]
        # print("start")
        # print(start)
        # print("match_len")
        # print(match_len)
        return [True, start, start+match_len]

    if(regex == "$"):
        if(inp == ""):
            return [True, start, start+match_len]
        else:
            return [False, None, None]

    front, opr, end = split_inp(regex)
    print(front,opr,end)
   
    # regexStateOffset = len(front)

    if(opr == "*"):
        if(front[0] == "["):
            print("h1")
            return match_star(start, front[1:-1], end, inp, match_len, regex,regex_offset+1)
        else:
            print("h2")
            [is_matched, start_len, end_len] = match_star(start, front, end, inp, match_len, regex,regex_offset)
            # print("is_matched")            
            # print(is_matched)
            # print("start_len")           
            # print(start_len)
            # print("end_len")            
            # print(end_len)
            return [is_matched, start_len, end_len] 

    if(opr == "+"):
        if(front[0] == "["):
            print("h3")
            return match_plus(start, front[1:-1], end, inp, match_len)
        else:
            print("h4")
            return match_plus(start, front, end, inp, match_len)

    if(opr == "?"):
        if(front[0] == "["):
            print("h4")
            return match_question(start, front[1:-1], end, inp, match_len)
        else:
            print("h5")
            return match_question(start, front, end, inp, match_len)

    elif(opr == "["):
        for i in range(1, len(front)):
            if(inp[0] == front[i]):
                # print(inp[0])
                # print("h6")
                regex_offset = len(regex_g) - len(regex)+i
                print(front,end,"h6",regex_offset)
                vertex_offset = index_vertex_map[regex_offset]
                if checkKey(vertex_offset_map, vertex_offset):
                    if checkKey(vertex_offset_map[vertex_offset], inp):
                        return vertex_offset_map[vertex_offset][inp]
                vertex_offset_map[vertex_offset][inp] = match(start, end, inp[1:], match_len+1, regex_offset+1)
                return vertex_offset_map[vertex_offset][inp]
                # return match(start, end, inp[1:], match_len+1, regex_offset+1)

    elif(opr == "("):
        splitted_words = front[1:-1].split("|")
        print("h7")
        return match_set(start, end, inp, splitted_words, match_len, regex_offset+2)

    else:
        if(front[0] == inp[0] or front[0] == "."):
            # print(front,"hh")
            regex_offset = len(regex_g) - len(regex)
            print(front,"hh",regex_offset,regex,regex_g)
            vertex_offset = index_vertex_map[regex_offset]
            if checkKey(vertex_offset_map, vertex_offset):
                if checkKey(vertex_offset_map[vertex_offset], inp):
                    return vertex_offset_map[vertex_offset][inp]
                    #  match(start, regex, inp, match_len=0, regex_offset=0,original_regex="A"):
            vertex_offset_map[vertex_offset][inp] = match(start, end, inp[1:], match_len+1, regex_offset+1)
            return vertex_offset_map[vertex_offset][inp]

    return [False, None, None]


def parse(regex, inp):


    """It will parse the input with regex"""

    matched_strings = []
    match_details = ""
    # for i in range(len(inp)):
    match_details = match(0, regex, inp[0:], 0)
    # print(match_details)
    if(match_details[0]):
        if(match_details[2] != len(inp)):
            print("did not match.")
        matched_strings.append([match_details[0],match_details[1], match_details[2]])

    return matched_strings

def initialize_vertex_offset_map(regex, index = 0):
    global vertex_count
    front, opr, end =  split_inp(regex)
    if front != "":
        if len(front) != 1:
            if front[0] == '(' or front[0] == '[':
                splitted_words = front[1:-1].split("|")
                # word_len = 0
                for word in splitted_words:
                    initialize_vertex_offset_map(word,)
        else:
            vertex_count += 1
            print(vertex_count,"---",front)
            vertex_offset_map[vertex_count] = {}
            index_vertex_map[index] = vertex_count
    if end != "":
        if len(end) != 1:
            initialize_vertex_offset_map(end)
        else:
            vertex_count += 1
            print(vertex_count,"---",end)
            vertex_offset_map[vertex_count] = {}

    # print(front)
    # print(opr)
    # print(end)


def match_regex_inp(inp):

    start_time = time.time()
    regex = "A[BC]D"
    # regex = "(a*)a"
    initialize_vertex_offset_map(regex)
    print(vertex_offset_map)
    print(index_vertex_map)
    count = 1
    for i in range(len(regex)):
        if ((regex[i] >= 'a' and regex[i] <= 'z') or (regex[i] >= 'A' and regex[i] <= 'Z') or regex[i] == '.'):
            index_vertex_map[i] = count
            # print(i,"======",count)
            count+=1
    # for i in vertex_offset_map.keys():
    #     print(i)
    for i in parse(regex, inp):
        print("--- %s seconds ---" % (time.time() - start_time))
        print(vertex_offset_map)
        return i[0]
    
    print(vertex_offset_map)
    
    # print("--- %s seconds ---" % (time.time() - start_time))
    return False

print(match_regex_inp("ABD"))