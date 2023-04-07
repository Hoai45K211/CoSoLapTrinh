def precedence(operator):
    if operator=='+' or operator=='-':
        op=1
    elif operator=='*' or operator == "/":
        op=2
    elif operator=='^':
        op=3
    else:
        op=('-1.This is not an operator!')
    return op
def main():
    operator=input('Enter the operator:')
    print('The precedence is',precedence(operator))
main()