def get_user_selection():
    number = -1
    while number < 0 or number > 4:

        number = int(input('''
        0. Exit
        1. Print a Diamond
        2. Print a Number Pattern
        3. Print a Cost Table
        Enter your choice   '''))

        if number < 0 or number > 4:
            print('Incorrect selection, please try again')

    return number

def make_odd_diamond():
    length = -1
    while length %2 != 0 or length < 0 or length > 20:
        length  = int(input('Enter the length (an even number between 0 and 20): '))
    
    charLeft = input('Enter the char used left to the diamond: ')
    charFill = input('Enter the char used to fill the diamond: ')
    output = build_odd_diamond(length,charLeft,charFill)
    return output

def build_odd_diamond(size,priorChar,fillChar):
    
    currentLength = size
    preSize = 0
    output= ''
    while currentLength > 0: 
        
        output += make_shape_line(currentLength,fillChar,preSize,priorChar,'/','\\')
        
        preSize += 1
        currentLength -= 2 

    while currentLength < size:

        currentLength += 2
        preSize -= 1

        output += make_shape_line(currentLength,fillChar,preSize,priorChar,'\\','/')

    return output

def make_shape_line(fillSize,fillChar,preSize = 0, preChar = '', leftChar ='', rightChar = ''):

    fill = rightChar + ((fillSize - 2)* fillChar) + leftChar
    output = f'\n{fill:{preChar}>{fillSize + preSize}}'
    return output

def make_pattern():
    num1 = -1
    num2 = -1
    check = True
    while num1 < 0 or num1 > 9:
        num1 = int(input('Enter the first number(between 0 and 9): '))

    while num2 < 0 or num2 > 9:
        num2 = int(input('Enter the second number(between 0 and 9): '))

    while check == True:
        choice = input('Use ascending order? (Y or N): ')
        if choice == 'Y' or choice == 'N':
            break
    output = build_percent_pattern(num1,num2,choice)
    return output


def build_percent_pattern(num1,num2,condition):
    
    output =''
    counter = 1
    if condition == 'Y':
        
        while num1 <= num2:
            
            num3 = num1
            while num3 <= num2:
                
                printed = round((num3 * .1) * num1,2)
                output += f'{printed:>6.2f}'
                num3 += 1
            
            output += '\n' + (counter * '      ')
            counter += 1
            num1 += 1
    elif condition == 'N':
        counter = num2 - num1
        while num2 >= num1:

            num3 = num2

            output += '\n' + (counter * '      ')
            while num3 <= 9 :
                printed = round((num3*.1)*num2,2)
                output += f'{printed:>6.2f}'
                num3 += 1

            counter -= 1
            num2 -= 1

    return output

def make_cost_table():

    number = -1 
    condition =  False
    while number < 0 or number > 9:
        number = int(input('Enter the maximum quantity (between 1 and 9): '))

    while condition == False:
        direction = input('Do you want horizontal (item\qnty) table (Yes or No): ')
        if direction == 'Yes':
            break
        elif direction == 'No':
            break
    
    items = ["Beans", "Rice", "Banana", "Ice", "Tea", "Bread", "Orange", "Sugar"]
    prices = [3.25, 4.31, 6.88, 3.3, 5.25, 4.89, 6.32, 2.25]
    output = build_cost_table(items,prices,number,direction)

    return output



def build_cost_table(items, prices, number, direction):

    output = ''
    if direction == 'Yes':
        output += 'Cost Table\nItem\Qty'
        z = 1
        count = 0
        while z <= number:
            output += f'{z:>8}'
            z += 1
        for x in items:
            counter = 1
            output += f'\n{x:<8s}'
            
            while counter <= number:
                total = counter * prices[count]
                output += f'{total:>8.2f}'
                counter += 1
            count += 1
    elif direction == 'No':
        output += 'Cost Table\nQty\Item'
        z = 0
        while z < len(items):
            heading = items[z]
            output += f'{heading:>8}'
            z += 1

        counter = 1
        while counter <= number:
            output += '\n'
            output += f'{counter:<8d}'
            for x in prices:
                total = x * counter
                output += f'{total:>8.2f}'
            counter += 1
            

    return output



def main():
    print('Project 2: Developed by Sai Ananthula')

    choice = ''
    while choice != 0:
        choice = get_user_selection()

        if choice == 1:
            output = make_odd_diamond()
        elif choice == 2:
            output = make_pattern()
        elif choice ==3:
            output = make_cost_table()
        else:
            print('Thank you for using this program, Good bye!')

        print(output)


if __name__ == "__main__":
    main()