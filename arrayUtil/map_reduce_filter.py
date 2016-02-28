
def my_filter(list , methodtorun):
    res= []
    for item in list:
        if methodtorun(item) == True:
            res.append(item)
    return res

def my_map(list ,methodtorun):
    res= []
    for item in list:
        res.append(methodtorun(item))
    return res

def my_reduce(list , methodtorun , init):
    if init == None:
        init = list[0]
    else:
        init = methodtorun(init , list[0])
    for i in range(len(list)-1):
        init = methodtorun(init , list[i+1])
    return init
