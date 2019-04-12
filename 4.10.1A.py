print("4.10.1 answer:")

def chlist_str(spam):
    spam[-1] = 'and ' + spam[-1]
    str_list = ', '.join(spam)
    return str_list

new_str = chlist_str(['apple','banana','tofu','cats'])
print("convert str is:")
print(new_str)
