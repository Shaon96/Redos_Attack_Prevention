
from numpy import index_exp


def match_star(start,front,end,inp,match_len):

    matched_len = 0

    while(1):
        to_check = front * matched_len
        [is_matched,start_len,end_len] = match(
            start,to_check,inp,match_len
        )
        if(not is_matched):
            break
        else:
            matched_len+=1
     
    while(matched_len >= 0):
        to_check = (front * matched_len)+end
        [is_matched,start_len,end_len] = match(
            start,to_check,inp,match_len
        )
        if(not is_matched):
            matched_len-=1
        else:
            return [is_matched,start_len,end_len]
    
    return [False,None,None]



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

    list_of_op = ["*","?","+","."]
    close_brac = 0
    front,end,opr = None,None,None
    flag = False

    # if it is a open[] bracket
    if(regex[0] == "["):
        close_brac = regex.find("]")
        front = regex[:close_brac+1]
        end = regex[close_brac+1:]
        flag = True
        # return [front,"[",end]
    
    # if it is a () bracket
    elif(regex[0] == "("):
        close_brac = regex.find(")")
        front = regex[:close_brac+1]
        end = regex[close_brac+1:]
        flag = True
        # return [front,"(",end]
    
    # print(regex,close_brac)
    if(flag and len(regex) > 1 and regex[close_brac+1] in list_of_op) :
        # index_op = 1
        front = regex[:close_brac+1]
        end = regex[close_brac+2:]
        opr = regex[close_brac+1]
    
    # any symbol
    elif(len(regex) > 1 and regex[close_brac+1] in list_of_op) :
        # index_op = 1
        front = regex[:close_brac+1]
        end = regex[close_brac+2:]
        opr = regex[close_brac+1]
        # return [front,opr,end]
        # index_op = find_op(regex)
    else:
        front = regex[0]
        end = regex[1:]
        # # if there is no operator
        # if(index_op == -1):
        # return [regex[0],None,regex[1:]]
        # front = regex[:index_op]
        # end = regex[index_op+1:]
        # opr = regex[index_op]
        # return [front,opr,end]
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
    
    if(opr == "*"):
        if(front[0] == "["):
            return match_star(start,front[1:-1],end,inp,match_len)
        else:
            return match_star(start,front,end,inp,match_len)
    
    elif(opr == "["):
        for i in range(1,len(front)):
            if(inp[0] == front[i]):
                # print(inp[0])
                return match(start,end,inp[1:],match_len+1)
    elif(opr == "."):
        return match(start,end,inp[1:],match_len+1)

    
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
    regex = "ab*c"
    inp = "aababc"
    # front,opr,end = split_inp(regex)
    # print(front,opr,end)
    # print(parse(regex,inp))
    # parse(regex,inp)
    for i in parse(regex,inp):
        print(inp[i[0]:i[1]])

if __name__  == "__main__":
    main()