def evalPostFix(expression:str):
    values=[]
    for token in expression:
        if token.isdigit():
            values.append(int(token))
    else:
        right=values.pop()
        left=values.pop()
        values.append(eval(str(left)+token+str(right)))
return values[0]

def main():
    post=input('Enter a postfix expression: ')
    val=evalPostFix(post)
    print('Result of expression evaluation:',val)
    
if __name__ == '__main__':
    main()