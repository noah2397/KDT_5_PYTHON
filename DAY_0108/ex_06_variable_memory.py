#---------------------------------
# 참조형 변수 => 데이터의 주소 저장
#---------------------------------
#- 저장된 데이터 & 변수 타입 관계---------------------------

num2=[11,22.1]
print(f'num => {id(num2)}, {type(num2)}')
print(f'num => {id(num2[0])}, {type(num2[0])}')

print("=====================값 변경========================")
#리스트의 원소를 변경하는 경우
num2[0]=100
print(f'num => {id(num2)}, {type(num2)}')
print(f'num => {id(num2[0])}, {type(num2[0])}')

#리스트를 다른 리스트로 새로 변경
num1=num2
