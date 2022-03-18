replace_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','!','"','£','$','%','^','&','*','(',')','<','>','-','+','{','}','#','~','[',']']

def replace(s):
    for rep in replace_list:
        s = str(s).replace(rep,'')
        s = str(s).replace(str(rep).upper(),'')
    return s

entry_price = input('Enter Entry Price:')
entry_price = replace(entry_price)
print(entry_price)
entry_price = float(entry_price)
print()
print('long')
take_profit = round(entry_price + (entry_price * 0.01),4)
stop_loss = round(entry_price - (entry_price * 0.015),4)
print(f'TP:{take_profit}')
print(f'SL:{stop_loss}')
print()
print('short')
take_profit = round(entry_price - (entry_price * 0.01),4)
stop_loss = round(entry_price + (entry_price * 0.015),4)
print(f'TP:{take_profit}')
print(f'SL:{stop_loss}')