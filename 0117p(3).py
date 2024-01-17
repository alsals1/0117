# map 함수

# map(function, iterable) 
# pos arg1 = 함수, pos arg2 = 이터러블, 반복 가능한 것, 시퀀스


# zip 함수

girls = ['제인', '애슐리']
boys = ['Peter', 'Jay', 'John']
pair = zip(girls, boys)

print(pair)
print(list(pair))


# 람다 함수(일회성) (한줄 함수)
# map 의 func 자리에 lambda 활용하기



# 공식문서의 내장함수인 print 응용하기 

print(1, 2, 3, end=' ') # end 기본인자 변경
print(4, 5, 6)



packed_values = 1, 2, 3
a, b, c = packed_values


print(a, b, c)



# **는 딕셔너리 키-밸류 쌍을 함수의 키워드 인자로 언패킹


def my_function(x, y, z):
    
def calculate_area(radius):
    return math.pi * radius**2

list(map(calculate_area, radius))
