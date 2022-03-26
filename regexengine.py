
def find_op(regex):

    """finds the first occurance
     of the opeartor"""
    
    list_of_op = ['*','?','+','.','(','[']
    min_index= -1
    for i in list_of_op:
        ind = regex.index(i)
        if(min_index < ind):
            min_index = ind
    return min_index


def split_inp(regex):

    """splits the regex"""

    index_op = find_op(regex)
    front = regex[:index_op]
    opr = regex[index_op]
    end = regex[index_op+1:]
    return [front,opr,end]



def match(start,regex,inp,regex_len):

    # print(regex,inp)
    front,opr,end = split_inp(regex)
    if(inp == "" and regex == ""):
        return [True, start, start+regex_len]
    if(inp == ""):
        return [False]
    if(regex == ""):
        return [True, start, start+regex_len]
        
    if(regex[0] == inp[0]):
        return match(start,regex[1:],inp[1:],regex_len)
    else:
        return [False]


def parse(regex,inp):


    matched_strings = []
    match_details = ""
    for i in range(len(inp)):
        match_details = match(i,regex,inp[i:],len(regex))
        if(match_details[0]):
           matched_strings.append([match_details[1],match_details[2]]) 
        # print(match_details)
        # if(not match_details[0]):
        #     return False
    return matched_strings


def main():
    regex = "abc"
    inp = "xabcdyabc"
    for i in parse(regex,inp):
        print(i)
        print(inp[i[0]:i[1]])

if __name__  == "__main__":
    main()