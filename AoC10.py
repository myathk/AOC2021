import math

with open('AoC10input.txt') as f:
    contents = f.readlines()

    contents = list(map(lambda x: x.strip(), contents))

    contents = list(map(lambda x: list(map(lambda y: y, x)), contents)) 

    def matching(bracket1, bracket2):
        if bracket1 == '(':
            return bracket2 == ')'
        elif bracket1 == '[':
            return bracket2 == ']'
        elif bracket1 == '{':
            return bracket2 == '}'
        else:
            return bracket2 == '>'

    filtered_contents = contents.copy()



    total_errors = 0
    for i in contents:
        stack = []
        for j in i:
            each_error = 0
            if j == '(' or j == '[' or j == '{' or j == '<':
                stack.append(j)
            else:
                curr = stack.pop()
                if not matching(curr, j):
                    filtered_contents.remove(i)
                    if j == ')':
                        each_error = 3
                        break
                    elif j == ']':
                        each_error = 57
                        break
                    elif j == '}':
                        each_error = 1197
                        break
                    else:
                        each_error = 25137
                        break
        
        total_errors+=each_error

    all_stack_brackets = []

    def calculate_score(total_stack):
        scores_arr = []
        for each_stack in total_stack:
            each_stack_score = 0
            for i in range(0, len(each_stack)):
                curr = each_stack.pop()
                adder = 0
                if curr == '(':
                    adder = 1
                elif curr == '[':
                    adder = 2
                elif curr == '{':
                    adder = 3 
                else:
                    adder = 4
                      
                each_stack_score = each_stack_score * 5 + adder
            scores_arr.append(each_stack_score)

        return scores_arr

    for i in filtered_contents:
        stack = []
        for j in i:
            
            if j == '(' or j == '[' or j == '{' or j == '<':
                stack.append(j)
            else:
                curr = stack.pop()

        all_stack_brackets.append(stack)

    scores = calculate_score(all_stack_brackets)
    scores.sort()
    middle = scores[math.floor(len(scores)/2)]
    print(middle)