'''Game_24'''
lv1 = [['1', '2', '3', '4'], ['4', '4', '4', '4'], ['2', '2', '3', '3'], ['5', '5', '5', '5'], ['7', '6', '3', '6']]
lv2 = [['2', '1', '7', '7'], ['1', '1', '8', '1'], ['2', '7', '7', '1'], ['3', '6', '1', '4'], ['5', '6', '4', '1']]
lv3 = [['3', '3', '6', '6'], ['3', '3', '5', '5'], ['3', '3', '7', '7'], ['3', '3', '8', '8'], ['3', '3', '3', '3']]
lv4 = [['4', '4', '4', '5'], ['4', '5', '5', '7'], ['4', '5', '5', '8'], ['4', '5', '9', '9'], ['4', '7', '7', '7']]    
lv5 = [['5', '5', '8', '8'], ['5', '5', '9', '9'], ['5', '6', '6', '6'], ['5', '6', '7', '7'], ['9', '8', '5', '2']]
lv6 = [['1', '3', '6', '9'], ['2', '8', '8', '9'], ['7', '8', '3', '5'], ['1', '6', '2', '1'], ['4', '9', '5', '7']]
lv7 = [['8', '8', '5', '4'], ['7', '1', '2', '7'], ['1', '1', '8', '5'], ['5', '6', '2', '4'], ['6', '5', '3', '4']]
lv8 = [['8', '2', '7', '8'], ['2', '2', '6', '9'], ['9', '7', '3', '3'], ['7', '8', '2', '4'], ['7', '6', '3', '6']]
lv9 = [['1', '7', '9', '2'], ['9', '8', '6', '2'], ['5', '5', '5', '1'], ['1', '3', '4', '6'], ['5', '4', '2', '6']]
lv10 = [['9', '8', '5', '4'], ['6', '3', '1', '3'], ['6', '7', '4', '3'], ['8', '8', '8', '3'], ['7', '5', '2', '4']]
lis = [lv1, lv2, lv3, lv4, lv5, lv6, lv7, lv8, lv9, lv10]
check = ['+', '-', '*', '/', '(', ')']
def menu():
    print 'GAME 24-FOR-FUN'
    print 'PRESS 1 Play'
    print 'PRESS 2 How to play'
    choice = input()
    if choice == 1:
        game()
    elif choice == 2:
        howtoplay()
    else:
        menu()
def howtoplay():
    print 'Use 4 number and operator(+,-,*,/) to calculate it to 24'
    print 'Press any key to Menu'
    print 'Press 1 Play'
    choice = input()
    if choice == 1:
        game()
    else:
        menu()
def game():
    lv_count = 1
    score = 0
    for i in lis:
        for j in i:
            print 'LV '+str(lv_count)
            print j[0], j[1], j[2], j[3]
            ans = calculate(raw_input(),j)
            if ans == 24:
                print 'Correct'
                score += 1
                print 'Your Score '+str(score)
                print 'Next question'  
                lv_count +=1
            else:
                print 'GAME OVER'
                print 'Your answer is : '+str(ans)
                print 'Your score : '+str(score)+' Point'
                print 'Press any key to Menu'
                print 'Press 1 How to play'
                print 'Press 2 Try agin'
                choice = input()
                if choice == 1:
                    howtoplay()
                elif choice == 2:
                    game()
                else:
                    menu()
    print 'Congratulation'
    print 'Yor Score is '+str(score)
    print 'Thank you For Playing'
    print 'Press any key to Menu'
    menu()
def calculate(ans, j):
    lis_ans = []
    for k in ans:
        print k
        print j
        if k not in j:
            if k not in check:
                print 'Can not use '+k
                print 'plese try again'
                print j[0], j[1], j[2], j[3]
                calculate(raw_input(), j)
        elif k in j:
            k = float(k)
        lis_ans.append(k)
    ans = eval(str(ans))
    return ans
menu()
