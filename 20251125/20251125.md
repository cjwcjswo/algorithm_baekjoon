# 2025년 11월 25일 문제 풀이 정리

## 📚 학습 내용 요약

### 1. 리스트 기본 연산

#### 문제: 10807, 10871, 10818, 2562
- **핵심 문법**: `list()`, `count()`, `min()`, `max()`, 리스트 컴프리헨션
- **학습 포인트**:
  - `list.count(value)`: 특정 값의 개수 세기
  - `min()`, `max()`: 최솟값, 최댓값 찾기
  - 리스트 순회 및 조건 필터링

**개선된 코드 예시**:
```python
# 10807번 - 이미 효율적
count = int(input())
numbers = list(map(int, input().split()))
v = int(input())
print(numbers.count(v))

# 10871번 - 리스트 컴프리헨션 활용
n, x = map(int, input().split())
a = list(map(int, input().split()))
result = [num for num in a if num < x]
print(*result)  # 언패킹 연산자로 출력

# 10818번 - 이미 효율적
n = int(input())
numbers = list(map(int, input().split()))
print(min(numbers), max(numbers))

# 2562번 - enumerate 활용
numbers = [int(input()) for _ in range(9)]
max_value = max(numbers)
max_index = numbers.index(max_value) + 1
print(max_value)
print(max_index)
```

### 2. 리스트 조작 및 슬라이싱

#### 문제: 10810, 10813, 10811
- **핵심 문법**: 리스트 초기화, 인덱싱, 슬라이싱, 리스트 역순
- **학습 포인트**:
  - `[0] * n`: n개의 0으로 초기화된 리스트
  - `[i+1 for i in range(n)]`: 1부터 n까지 리스트 생성
  - `list[::-1]`: 리스트 역순
  - `list[start:end] = reversed_list`: 슬라이스 할당

**개선된 코드 예시**:
```python
# 10810번 - 리스트 컴프리헨션으로 초기화
n, m = map(int, input().split())
bucket = [0] * n
for _ in range(m):
    i, j, k = map(int, input().split())
    bucket[i-1:j] = [k] * (j - i + 1)
print(*bucket)

# 10813번 - Pythonic한 스왑
n, m = map(int, input().split())
bucket = [i+1 for i in range(n)]
for _ in range(m):
    i, j = map(int, input().split())
    bucket[i-1], bucket[j-1] = bucket[j-1], bucket[i-1]  # 튜플 언패킹
print(*bucket)

# 10811번 - reversed() 함수 활용
n, m = map(int, input().split())
bucket = [i+1 for i in range(n)]
for _ in range(m):
    i, j = map(int, input().split())
    bucket[i-1:j] = reversed(bucket[i-1:j])
print(*bucket)
```

### 3. 집합(Set) 활용

#### 문제: 3052, 5597
- **핵심 문법**: `set()`, `len()`, 중복 제거
- **학습 포인트**:
  - `set()`: 중복 제거 및 집합 연산
  - `len(set())`: 고유한 값의 개수
  - `in` 연산자로 포함 여부 확인

**개선된 코드 예시**:
```python
# 3052번 - 이미 효율적
numbers = [int(input()) % 42 for _ in range(10)]
print(len(set(numbers)))

# 5597번 - set 차집합 활용
all_students = set(range(1, 31))
submitted = {int(input()) for _ in range(28)}
missing = sorted(all_students - submitted)
print(*missing, sep='\n')
```

### 4. 문자열 처리

#### 문제: 2743, 9086, 11654, 27866, 11720, 10809, 2675, 1152, 2908, 11718
- **핵심 문법**: 문자열 인덱싱, `len()`, `ord()`, `chr()`, `find()`, `index()`, 문자열 슬라이싱
- **학습 포인트**:
  - `len(string)`: 문자열 길이
  - `ord(char)`: 문자를 ASCII 코드로 변환
  - `chr(code)`: ASCII 코드를 문자로 변환
  - `string.find(char)`: 문자 위치 찾기 (없으면 -1)
  - `string.index(char)`: 문자 위치 찾기 (없으면 ValueError)
  - `string[::-1]`: 문자열 역순
  - `string.split()`: 공백으로 분리

**개선된 코드 예시**:
```python
# 9086번 - 더 간결한 버전
t = int(input())
for _ in range(t):
    s = input()
    print(s[0] + s[-1])

# 10809번 - find() 메서드 활용 (이미 효율적)
word = input()
for char in 'abcdefghijklmnopqrstuvwxyz':
    print(word.find(char), end=' ')

# 2675번 - 리스트 컴프리헨션 활용
t = int(input())
for _ in range(t):
    r, s = input().split()
    print(''.join([char * int(r) for char in s]))

# 2908번 - 더 간결한 버전
a, b = input().split()
print(max(int(a[::-1]), int(b[::-1])))

# 1152번 - 이미 효율적
words = input().split()
print(len(words))
```

### 5. 딕셔너리 및 문자열 매핑

#### 문제: 5622
- **핵심 문법**: 리스트 인덱싱, `find()`, 딕셔너리 활용 가능
- **학습 포인트**:
  - 문자열 매핑을 통한 값 계산
  - 딕셔너리를 활용한 더 효율적인 접근 가능

**개선된 코드 예시**:
```python
# 5622번 - 딕셔너리 활용 (더 효율적)
dial = {
    'ABC': 3, 'DEF': 4, 'GHI': 5, 'JKL': 6,
    'MNO': 7, 'PQRS': 8, 'TUV': 9, 'WXYZ': 10
}
word = input()
time = 0
for char in word:
    for key, value in dial.items():
        if char in key:
            time += value
            break
print(time)

# 또는 더 간결한 버전
dial_dict = {}
for i, chars in enumerate(['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ'], 3):
    for char in chars:
        dial_dict[char] = i
word = input()
print(sum(dial_dict[char] for char in word))
```

### 6. 수학 연산 및 평균 계산

#### 문제: 1546
- **핵심 문법**: 리스트 순회, 최댓값 활용, 평균 계산
- **학습 포인트**:
  - 리스트 요소 수정
  - `max()` 함수 활용
  - 평균 계산

**개선된 코드 예시**:
```python
# 1546번 - 리스트 컴프리헨션 활용
n = int(input())
scores = list(map(int, input().split()))
max_score = max(scores)
new_scores = [score / max_score * 100 for score in scores]
print(sum(new_scores) / n)
```

### 7. 예외 처리

#### 문제: 11718
- **핵심 문법**: `try-except`, EOF 처리
- **학습 포인트**:
  - `try-except`로 예외 처리
  - EOF(End of File) 처리 방법

**개선된 코드 예시**:
```python
# 11718번 - sys.stdin 활용 (더 효율적)
import sys
for line in sys.stdin:
    print(line.rstrip())
```

## 🎯 핵심 파이썬 문법 정리

1. **리스트**:
   - `[0] * n`: n개의 0으로 초기화
   - `[i+1 for i in range(n)]`: 리스트 컴프리헨션
   - `list.count(value)`: 개수 세기
   - `min()`, `max()`: 최솟값, 최댓값
   - `*list`: 언패킹 연산자

2. **리스트 슬라이싱**:
   - `list[start:end]`: 슬라이싱
   - `list[::-1]`: 역순
   - `list[start:end] = new_list`: 슬라이스 할당

3. **집합(Set)**:
   - `set()`: 중복 제거
   - `set1 - set2`: 차집합
   - `len(set)`: 고유 요소 개수

4. **문자열**:
   - `ord(char)`, `chr(code)`: ASCII 변환
   - `string.find(char)`: 위치 찾기 (없으면 -1)
   - `string.index(char)`: 위치 찾기 (없으면 에러)
   - `string[::-1]`: 역순
   - `' '.join(list)`: 리스트를 문자열로 결합

5. **딕셔너리**:
   - 키-값 쌍으로 데이터 저장
   - 빠른 조회 가능

6. **예외 처리**:
   - `try-except`: 예외 처리
   - EOF 처리 방법

## 💡 효율성 개선 팁

1. **리스트 컴프리헨션**: 반복문과 조건문을 한 줄로 표현
2. **언패킹 연산자**: `*list`로 리스트 요소를 개별 인자로 전달
3. **튜플 언패킹**: `a, b = b, a`로 변수 교환
4. **집합 활용**: 중복 제거나 포함 여부 확인 시 `set` 사용
5. **딕셔너리**: 문자열 매핑 문제에서 딕셔너리 활용으로 시간 복잡도 개선
6. **reversed()**: 리스트 역순 시 `[::-1]`보다 `reversed()`가 더 명확

