import random

def luhn_verification(num):
    num = [int(d) for d in str(num)]
    check_digit = num.pop()
    num.reverse()
    total = 0
    for i, digit in enumerate(num):
        if i % 2 == 0:
            digit *= 2
        if digit > 9:
            digit -= 9
        total += digit
    total *= 9
    return (total % 10) == check_digit

def cc_gen(cc, mes='x', ano='x', cvv='x'):
    ccs = []
    current_year = 2024
    current_month = 6
    
    while len(ccs) < 10:
        card = str(cc)
        digits = '0123456789'
        list_digits = list(digits)
        random.shuffle(list_digits)
        string_digits = ''.join(list_digits)
        card += string_digits
        new_list = list(card)
        list_empty = []

        for i in new_list:
            if i == 'x':
                list_empty.append(str(random.randint(0, 9)))
            else:
                list_empty.append(i)

        list_empty_string = ''.join(list_empty)
        card = list_empty_string

        if card[0] == '3':
            card = card[:15]
        else:
            card = card[:16]

        if mes == 'x':
            if ano == 'x' or int(ano) == current_year:
                mes_gen = random.randint(current_month, 12)
            else:
                mes_gen = random.randint(1, 12)
            if len(str(mes_gen)) == 1:
                mes_gen = '0' + str(mes_gen)
        else:
            mes_gen = mes

        if ano == 'x':
            ano_gen = random.randint(current_year, 2031)
        else:
            ano_gen = ano
            if len(str(ano_gen)) == 2:
                ano_gen = '20' + str(ano_gen)

        if cvv == 'x' or cvv == 'xx' or cvv == 'xxx':
            if card[0] == '3':
                cvv_gen = f'{random.randint(0, 9999):04}'
            else:
                cvv_gen = f'{random.randint(0, 999):03}'
        else:
            cvv_gen = cvv

        x = f'{card}|{mes_gen}|{ano_gen}|{cvv_gen}\n'
        a = luhn_verification(card)
        if a:
            ccs.append(x)
        else:
            continue

    return ccs
