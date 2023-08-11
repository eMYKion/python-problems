nums = [0,1,2,9,10,11,18,19,20,21,50,99,100,101,199,200,201,299,999,9999]
sols = [x+1 for x in nums]

def ints2lists(int_list):
    
    int_list = map(lambda x: [*str(x)], int_list)
    int_list = map(lambda x: list(map(lambda y: int(y), x)), int_list)
    return int_list

cases = {
    i: ((n,),s) for i,(n,s) in enumerate(zip(ints2lists(nums), ints2lists(sols)))
}
