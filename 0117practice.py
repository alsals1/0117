def greet(name, age, mention):
    print(f'안녕하세요, {name}님! {age}살이시군요. {mention}')
    


greet('앨리스', 25, '안녕')  # Positional위치 Arguments인자
greet('앨리스', mention = '좋은 아침.', age = 30)
# Keyword키워드 Arguments인자 
# 주의! Positional과 Keyword 혼용시, Position을 먼저 다 할당한 후, Keyword 순서 상관없이 할당한다. 



def calculate_sum(*args):
    print(args)  # tuple 처리, Packing 패킹
    total = sum(args)
    print(f'합계: {total}') 
    

calculate_sum(1, 2, 3)
calculate_sum(1, 2, 3, "a")

    

