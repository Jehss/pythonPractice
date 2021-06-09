def add(a,b):
    return a+b

print(add(3,4))

print("'I think, He's favorite food is chicken'")
print("I said \"He's favorite food is chicken\"") # 이게 더 편하네

# \n : 줄바꿈, \t : 탭 간격, \\ 문자 '\'를 표현,
# \r : 커서를 가장 앞으로 이동, \f : 커서를 다음 줄로 이동
# \a : alert, \b : 백 스페이스, \000 : Null

print("="*50)
# ''' 또는 """
print('''
Life is so strange
You need chill mind
''')
print("="*50)

# 문자열 길이
a = "123456789"
print(len(a))

# 문자열 인덱싱, 슬라이싱
b = "life is strange"
print(b[0:4]) # 0~3
print(b[5:8]) # 5~8
print(b[8:]) # 8~마지막
print(b[:]) # 처음부터 끝까지
print(b[8:]+"=="+b[-7:]) # 앞에서부터, 뒤에서부터

# 문자열의 요솟값은 변경 불가능
a = "Happy"
print(a[:3]+'iness')

# 문자열 포매팅
a = "I eat %d Ice-cream" % 10
print(a)
a = "I eat %s Ice-cream" % "chocolate"
print(a)
a = "I ate %d Ice-cream, %s favor" %(10, "chocolate")
print(a)

# 문자열 포맷 코드
# %s %c %d %f %o %x %%

# 포맷 코드와 숫자 함께 사용
print("%10s Jehss" % "hi")
print("%.4f" % 3.141592)
n=10
print("I ate {} apples with {} friends".format(n,5))
print("I ate {a} apples with {b} friends".format(a=2,b=5))
# :< 왼쪽정렬, :> 오른쪽정렬 :^ 가운데정렬
print("{:^10}".format("1 hi  2"))
print("{:-^5}".format("hi")) # 문자 뒤부터 빈칸 채워주네

# f 문자열 포매팅 - 딕셔너리
d = {'name':'박주현', 'age':26, 'job':'장교'}
print(f'제 이름은 {d["name"]}이고 나이는 {d["age"]}입니다. 현재 {d["job"]}를 하고 있습니다.')

# 문자열 관련 함수
## .count() : 개수 세기, .find() : 위치 알려주기 *없으면 -1, .index() : 위치 알려주기 *없으면 오류
a = "HIHIHIHIgher"
print(a.count('H'))
print(a.find('H')) # 0번부터 세기 시작하여 제일 처음 발견한 위치를 알려줌
print(a.index('H'))

ex1 = ['a','b','c','d'] # 기본
print(ex1)
ex2 = "1".join(ex1) # 문자 사이 '1' 추가
print(ex2)
ex3 = "1".join(ex1).split('c') # join 먼저 진행
print(ex3)
ex4 = "1".join(ex1).split() # 공백이 없어 문자열 나누기 x
print(ex4)