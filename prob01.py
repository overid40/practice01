# 키보드로 정수 수치를 입력 받아 그것이 3의 배수인지 판단하세요

a = input('수를 입력하세요 :')
if int(a) % 3 == 0:
    print('3의 배수입니다.')
elif int(a) % 3 != 0:
    print('3의 배수가 아닙니다')
elif isinstance(a, str):
    print('3의 배수가 아닙니다')

