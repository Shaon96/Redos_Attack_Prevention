
def find_op(regex):

    """finds the first occurance
     of the opeartor"""
    
    list_of_op = ["*","?","+","."]
    index = -1
    for i in range(len(regex)):
        if(regex[i] in list_of_op):
            index = i
            break
    return index


def split_inp(regex):

    """splits the regex"""

    # if it is a open[] bracket
    if(regex[0] == "["):
        close_brac = regex.find("]")
        front = regex[:close_brac+1]
        end = regex[close_brac+1:]
        return [front,"[",end]
    
    # if it is a () bracket
    elif(regex[0] == "("):
        close_brac = regex.find(")")
        front = regex[:close_brac+1]
        end = regex[close_brac+1:]
        return [front,"(",end]

    # any literal
    else:
        index_op = find_op(regex)

        # if there is no operator
        if(index_op == -1):
            return [regex[0],None,regex[1:]]
        front = regex[:index_op]
        end = regex[index_op+1:]
        opr = regex[index_op]
        return [front,opr,end]




def match(start,regex,inp,match_len = 0):

    # print(regex,inp)
    if(inp == "" and regex == ""):
        return [True, start, start+match_len]

    if(inp == ""):
        return [False,4,5]

    if(regex == ""):
        return [True, start, start+match_len]
    
    front,opr,end = split_inp(regex)

    # print(front,opr,end)

    # print(inp)
    
    
    if(opr == "["):
        for i in range(1,len(front)):
            if(inp[0] == front[i]):
                # print(inp[0])
                return match(start,end,inp[1:],match_len+1)
    elif(opr == "."):
        return match(start,end,inp[1:],match_len+1)
        pass
    else:
        if(front[0] == inp[0]):
            # print(front,"hh")
            return match(start,end,inp[1:],match_len+1)
    
    return [False,None,None]



def parse(regex,inp):


    matched_strings = []
    match_details = ""
    for i in range(len(inp)):
        match_details = match(i,regex,inp[i:],0)
        # print(match_details)
        if(match_details[0]):
           matched_strings.append([match_details[1],match_details[2]]) 
        # print(match_details)
        # if(not match_details[0]):
            # matched_strings.append([False])
    return matched_strings


def main():
    regex = "[abc].[fv]"
    inp = "agbgv"
    # front,opr,end = split_inp(regex)
    # print(front,opr,end)
    # print(parse(regex,inp))
    # parse(regex,inp)
    for i in parse(regex,inp):
        print(inp[i[0]:i[1]])

if __name__  == "__main__":
    main()