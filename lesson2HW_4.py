math = int (input('數學成績?'))
English = int (input('英文成績?'))

if math and English > 90:
    print('有獎學金')
elif math ==100 or English == 100: 
    print('有獎學金')
else: 
    print('有懲罰')
    
if math != 0:
    print('好險數學沒拿鴨蛋')
if English != 0:
    print('好險英文沒拿鴨蛋')
    
if math == 0 and English == 0:
    print('下次再努力')