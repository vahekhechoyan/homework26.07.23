hour = int(input("jama@ asa"))
if hour > 0 and hour < 12:
    f = input('am or pm?>')
    if f == 'am':
        hour += 8
        if hour > 12:
            hour -= 12
            print(f'{hour}. pm')
        else:
            print(f"{hour}. am")
    elif f == 'pm':
        hour += 8
        if hour > 12:
            hour -= 12
            print(f'{hour}. am')
        else:
            print(f"{hour}. pm")
    else:
        print('kam am kam pm. Urish ban mi gri')
else:
    print('normal jam asa?')
