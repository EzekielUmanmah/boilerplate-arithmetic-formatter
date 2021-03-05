def arithmetic_arranger(*args):
    firstLine = ''
    secondLine = ''
    dashes = ''
    problems = args[0]
    evals = ''

    if len(problems) > 5: return 'Error: Too many problems.'


    for thing in problems:
        things = thing.split()
        largest = len(max(things, key=len))+1

        if things[1] != '+' and things[1] != '-': 
          return "Error: Operator must be '+' or '-'."
          
        try:
          int(things[0])
          int(things[2])
        except:
          return 'Error: Numbers must only contain digits.'

        if len(things[0]) > 4 or len(things[2]) > 4:
          return 'Error: Numbers cannot be more than four digits.'

        firstLine+=' ' + '{:>{width}}'.format(things[0], width=largest) + '{:>{space}}'.format('', space=4)

        secondLine+=things[1] + '{:>{width}}'.format(things[2], width=largest) + '{:>{space}}'.format('', space=4)

        dashes+='{}'.format('-'*(largest+1)) + '{:>{width}}'.format('', width=4)

        output = firstLine.rstrip()+'\n'+secondLine.rstrip()+'\n'+dashes.rstrip()

        if len(args) == 2 and args[1] == True:
            evals+=' ' + '{:>{width}}'.format(str(eval(thing)), width=largest) + '{:>{width}}'.format('', width=4)
            output = firstLine.rstrip()+'\n'+secondLine.rstrip()+'\n'+dashes.rstrip()+'\n'+str(evals).rstrip()
    # print(repr(output)) => prints output without triggering newline
    return output.rstrip()