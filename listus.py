
def wr(wrd):
    file = open('to_do.txt','a')
    if wrd == 'конец':
        pass
    else:
        file.write(wrd)
        file.write(',')
        file.write('\n')
