math = int(input('數學成績?'))
English = int(input('英文成績?'))
if math and English > 89:
   input('有獎學金')
elif math == 100 or English == 100:
    input('有獎學金')    
else:
    input('沒有獎學金')