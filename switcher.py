spam = ['apple','banana','tofu','cats']
true_value = "apple, banana, tofu and cats"

def switch(someList):
    the_value = ''
    second_last_value = someList[-2]
    last_value = someList[-1]
    for i in someList:
        if i == someList[-1]:
            the_value = the_value + i
            continue
                
        
        if i == someList[-2]:
            the_value = the_value + i + ' and '
            continue
        the_value = the_value + i +',' + ' '
            
    return the_value



 

