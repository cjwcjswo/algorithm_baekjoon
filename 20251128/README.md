# 2025년 11월 28일 문제 풀이 정리

## 📚 학습 내용 요약

### 1. 진법 변환 (Base Conversion)

#### 문제: 11005 (진법 변환 2), 2745 (진법 변환)
- **핵심 문법**: 나눗셈과 나머지 연산, 문자열 역순, ASCII 변환
- **학습 포인트**:
  - 10진수를 B진법으로 변환: 나머지를 역순으로 나열
  - B진법을 10진수로 변환: 각 자리수에 진법의 거듭제곱을 곱하여 합산
  - 10 이상의 숫자는 알파벳으로 표현 (A=10, B=11, ...)

**개선된 코드 예시**:
```python
# 11005번 - 10진수를 B진법으로 변환 (더 간결한 버전)
n, b = map(int, input().split())
result = ''

while n > 0:
    remainder = n % b
    if remainder >= 10:
        result += chr(remainder - 10 + ord('A'))
    else:
        result += str(remainder)
    n //= b

print(result[::-1])

# 또는 재귀 함수 활용
def convert_base(n, b):
    if n == 0:
        return ''
    remainder = n % b
    char = chr(remainder - 10 + ord('A')) if remainder >= 10 else str(remainder)
    return convert_base(n // b, b) + char

n, b = map(int, input().split())
print(convert_base(n, b) if n > 0 else '0')

# 2745번 - B진법을 10진수로 변환 (더 간결한 버전)
n, b = input().split()
b = int(b)
result = 0

for i, char in enumerate(n):
    if char.isdigit():
        digit = int(char)
    else:
        digit = ord(char.upper()) - ord('A') + 10
    result = result * b + digit

print(result)

# 또는 내장 함수 활용 (Python의 int 함수는 진법 변환 지원)
n, b = input().split()
print(int(n, int(b)))  # 가장 간단한 방법!
```

### 2. 그리디 알고리즘 (Greedy Algorithm)

#### 문제: 2720 (세탁소 사장 동혁)
- **핵심 문법**: 나눗셈과 나머지 연산, 그리디 알고리즘
- **학습 포인트**:
  - 거스름돈 문제: 큰 동전부터 최대한 많이 사용
  - 그리디 알고리즘의 대표적인 예시
  - 각 동전의 개수를 순차적으로 계산

**개선된 코드 예시**:
```python
# 2720번 - 거스름돈 계산 (더 간결한 버전)
t = int(input())
coins = [25, 10, 5, 1]

for _ in range(t):
    change = int(input())
    result = []
    for coin in coins:
        result.append(str(change // coin))
        change %= coin
    print(' '.join(result))
```

### 3. 수학적 패턴 분석

#### 문제: 2903 (중앙 이동 알고리즘)
- **핵심 문법**: 거듭제곱, 수학적 패턴 분석
- **학습 포인트**:
  - 패턴 분석: 2 → 3 → 5 → 9 → 17 → ...
  - 점의 개수: (2^n + 1)²
  - 수학적 규칙을 찾아 공식화

**개선된 코드 예시**:
```python
# 2903번 - 중앙 이동 알고리즘 (더 간결한 버전)
n = int(input())
# 점의 개수: (2^n + 1)²
points_per_side = 2 ** n + 1
print(points_per_side ** 2)

# 또는 한 줄로
print((2 ** int(input()) + 1) ** 2)
```

### 4. 2차원 격자 및 영역 계산

#### 문제: 2563 (색종이)
- **핵심 문법**: 2차원 배열, 격자 처리, 영역 계산
- **학습 포인트**:
  - 100×100 격자에 색종이 영역 표시
  - 겹치는 영역 처리
  - 전체 색칠된 영역의 넓이 계산

**개선된 코드 예시**:
```python
# 2563번 - 색종이 (더 효율적인 버전)
grid = [[False] * 100 for _ in range(100)]
n = int(input())

for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            grid[i][j] = True

# True인 칸의 개수 세기
area = sum(sum(row) for row in grid)
print(area)

# 또는 set을 활용한 방법
covered = set()
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            covered.add((i, j))
print(len(covered))
```

## 🎯 핵심 파이썬 문법 정리

### 1. 진법 변환
- **10진수 → B진법**:
  - 나머지를 구하고 몫을 계속 나눔
  - 나머지를 역순으로 나열
  - 10 이상은 알파벳으로 변환

- **B진법 → 10진수**:
  - 각 자리수에 진법의 거듭제곱을 곱하여 합산
  - Python의 `int(string, base)` 함수 활용 가능

### 2. 그리디 알고리즘
- **특징**: 각 단계에서 최선의 선택을 하는 알고리즘
- **적용 조건**: 
  - 최적 부분 구조 (Optimal Substructure)
  - 탐욕 선택 속성 (Greedy Choice Property)
- **예시**: 거스름돈 문제, 최소 신장 트리 등

### 3. 수학적 패턴 분석
- **접근 방법**:
  1. 작은 케이스부터 분석
  2. 패턴 찾기
  3. 공식 도출
  4. 일반화

### 4. 2차원 격자 처리
- **격자 초기화**: `[[False] * width for _ in range(height)]`
- **영역 표시**: 불리언 배열 또는 집합 활용
- **넓이 계산**: True인 칸의 개수 세기

## 💡 효율성 개선 팁

1. **진법 변환**:
   - Python의 내장 함수 `int(string, base)` 활용
   - 재귀 함수로 간결하게 구현 가능

2. **그리디 알고리즘**:
   - 동전을 큰 순서대로 정렬
   - 나눗셈과 나머지 연산으로 간단히 계산

3. **수학적 패턴**:
   - 작은 케이스부터 분석하여 패턴 찾기
   - 공식을 찾으면 코드가 매우 간단해짐

4. **2차원 격자**:
   - 불리언 배열로 메모리 효율적
   - 집합을 활용하면 중복 자동 처리

## 🔍 문제별 핵심 포인트

### 11005번 (진법 변환 2)
- **핵심**: 10진수를 B진법으로 변환
- **주의**: 나머지를 역순으로 출력해야 함
- **팁**: `int()` 함수로 간단히 변환 가능하지만, 직접 구현 연습

### 2745번 (진법 변환)
- **핵심**: B진법을 10진수로 변환
- **주의**: 알파벳 대소문자 처리
- **팁**: Python의 `int(string, base)` 함수 활용

### 2720번 (세탁소 사장 동혁)
- **핵심**: 그리디 알고리즘으로 거스름돈 계산
- **주의**: 동전을 큰 순서대로 사용
- **팁**: 나눗셈과 나머지 연산으로 간단히 계산

### 2903번 (중앙 이동 알고리즘)
- **핵심**: 수학적 패턴 분석
- **주의**: 점의 개수는 (2^n + 1)²
- **팁**: 패턴을 찾으면 코드가 매우 간단해짐

### 2563번 (색종이)
- **핵심**: 2차원 격자에서 영역 계산
- **주의**: 겹치는 영역은 한 번만 계산
- **팁**: 불리언 배열 또는 집합 활용

## 📖 진법 변환 상세 설명

### 진법이란?
- **진법(Base)**: 숫자를 표현하는 방법
- **10진법**: 0~9의 숫자 사용
- **2진법**: 0, 1 사용
- **16진법**: 0~9, A~F 사용

### 진법 변환 방법

#### 10진수 → B진법 변환
1. 10진수를 B로 나눔
2. 나머지를 기록
3. 몫을 다시 B로 나눔
4. 몫이 0이 될 때까지 반복
5. 나머지를 역순으로 나열

**예시**: 10진수 255를 16진법으로
```
255 ÷ 16 = 15 ... 15 (F)
15 ÷ 16 = 0 ... 15 (F)
결과: FF
```

#### B진법 → 10진수 변환
1. 각 자리수에 진법의 거듭제곱을 곱함
2. 모든 값을 합산

**예시**: 16진법 FF를 10진수로
```
F × 16¹ + F × 16⁰ = 15 × 16 + 15 × 1 = 240 + 15 = 255
```

