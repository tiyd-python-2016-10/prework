import operator


operators = {"+": operator.add,
             "-": operator.sub}

def calculate(expression):
    expression = expression.split()
    for index, item in enumerate(expression):
        try:
            expression[index] = int(item)
        except:
            #if item == "+":
            #    expression[index] = operator.add
            #elif item == "-":
            #    expression[index] = operator.sub
            expression[index] = operators[item]
    print(expression)
    return expression[1](expression[0], expression[2])
