# 2025년 11월 26일 문제 풀이 정리

## 📚 학습 내용 요약

### 1. 문자열 패턴 매칭 및 KMP 알고리즘

#### 문제: 2941 (크로아티아 알파벳)
- **핵심 문법**: `replace()`, 문자열 치환
- **학습 포인트**:
  - 문자열 패턴 매칭 및 치환
  - 크로아티아 알파벳 처리: `c=`, `c-`, `dz=`, `d-`, `lj`, `nj`, `s=`, `z=`
  - **KMP 알고리즘**에 대한 이해 필요 (문자열 패턴 매칭 알고리즘)

**현재 풀이**:
```python
word = input()
word = word.replace("c=", 'a')
word = word.replace("c-", 'a')
word = word.replace("dz=", 'a')
word = word.replace("d-", 'a')
word = word.replace("lj", 'a')
word = word.replace("nj", 'a')
word = word.replace("s=", 'a')
word = word.replace("z=", 'a')
print(len(word))
```

**개선된 코드 예시**:
```python
# 더 간결한 버전
word = input()
croatian = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for pattern in croatian:
    word = word.replace(pattern, 'a')
print(len(word))
```

#### 🔍 KMP 알고리즘 (Knuth-Morris-Pratt Algorithm)

**KMP 알고리즘이란?**
- 문자열 검색 알고리즘 중 하나로, 텍스트에서 패턴을 찾는 효율적인 방법
- 시간 복잡도: O(n + m) (n: 텍스트 길이, m: 패턴 길이)
- 일반적인 브루트 포스 방식(O(nm))보다 효율적

**핵심 아이디어**:
1. **실패 함수(Failure Function) / 부분 일치 테이블(Partial Match Table)**: 
   - 패턴의 각 위치에서 접두사와 접미사가 일치하는 최대 길이를 미리 계산
   - 이를 통해 불필요한 비교를 건너뛸 수 있음

2. **이동 규칙**:
   - 매칭 실패 시, 이미 일치한 부분을 활용하여 패턴을 최대한 앞으로 이동

**KMP 알고리즘 구현 예시**:
```python
def build_failure_table(pattern):
    """실패 함수(부분 일치 테이블) 생성"""
    m = len(pattern)
    table = [0] * m
    j = 0
    
    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = table[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            table[i] = j
    return table

def kmp_search(text, pattern):
    """KMP 알고리즘으로 패턴 검색"""
    n, m = len(text), len(pattern)
    if m == 0:
        return []
    
    failure_table = build_failure_table(pattern)
    result = []
    j = 0  # 패턴 인덱스
    
    for i in range(n):  # 텍스트 인덱스
        while j > 0 and text[i] != pattern[j]:
            j = failure_table[j - 1]
        
        if text[i] == pattern[j]:
            j += 1
            if j == m:  # 패턴 전체 매칭
                result.append(i - m + 1)
                j = failure_table[j - 1]  # 다음 매칭을 위해
    
    return result

# 사용 예시
text = "ababcababa"
pattern = "aba"
matches = kmp_search(text, pattern)
print(f"패턴 '{pattern}'가 발견된 위치: {matches}")  # [0, 5, 7]
```

**KMP 알고리즘의 장점**:
- 시간 복잡도가 O(n + m)으로 효율적
- 텍스트를 한 번만 순회하면서 패턴을 찾을 수 있음
- 실패 함수를 미리 계산하여 재사용 가능

**2941번 문제와의 연관성**:
- 현재 문제는 `replace()` 메서드를 사용하여 간단히 해결 가능
- 하지만 더 복잡한 패턴 매칭 문제에서는 KMP 알고리즘이 유용
- 예: 여러 패턴을 동시에 찾거나, 패턴이 겹치는 경우 처리

### 2. 문자열 빈도 분석

#### 문제: 1157 (단어 공부)
- **핵심 문법**: 리스트 인덱싱, `ord()`, `chr()`, `max()`, `enumerate()`
- **학습 포인트**:
  - 알파벳 빈도 계산
  - 대소문자 통일 처리 (`lower()`)
  - 최댓값이 여러 개일 때 처리

**개선된 코드 예시**:
```python
# 1157번 - collections.Counter 활용 (더 간결)
from collections import Counter

word = input().upper()
counter = Counter(word)
max_count = max(counter.values())
most_common = [char for char, count in counter.items() if count == max_count]

if len(most_common) > 1:
    print('?')
else:
    print(most_common[0])
```

### 3. 팰린드롬(Palindrome) 검사

#### 문제: 10988 (팰린드롬인지 확인)
- **핵심 문법**: 문자열 인덱싱, 슬라이싱
- **학습 포인트**:
  - 팰린드롬: 앞에서 읽으나 뒤에서 읽으나 같은 문자열
  - 문자열 역순 비교: `word[::-1]`
  - 중간 지점까지만 비교하면 됨

**개선된 코드 예시**:
```python
# 10988번 - 더 간결한 버전
word = input()
print(1 if word == word[::-1] else 0)

# 또는 슬라이싱 활용
word = input()
print(1 if word[:len(word)//2] == word[-(len(word)//2):][::-1] else 0)
```

### 4. 반복문과 문자열 조작

#### 문제: 2444 (별 찍기 - 7)
- **핵심 문법**: 반복문, 문자열 반복, 조건문
- **학습 포인트**:
  - 다이아몬드 모양 별 찍기
  - 상단과 하단을 나누어 처리
  - 공백과 별의 개수 계산

**개선된 코드 예시**:
```python
# 2444번 - 더 간결한 버전
n = int(input())
for i in range(1, n + 1):
    print(' ' * (n - i) + '*' * (2 * i - 1))
for i in range(n - 1, 0, -1):
    print(' ' * (n - i) + '*' * (2 * i - 1))
```

### 5. 리스트 연산 및 차이 계산

#### 문제: 3003 (킹, 퀸, 룩, 비숍, 나이트, 폰)
- **핵심 문법**: 리스트, `enumerate()`, 언패킹
- **학습 포인트**:
  - 정해진 값과 입력값의 차이 계산
  - 리스트 순회 및 인덱스 활용

**개선된 코드 예시**:
```python
# 3003번 - 리스트 컴프리헨션 활용
correct = [1, 1, 2, 2, 2, 8]
input_pieces = list(map(int, input().split()))
result = [correct[i] - input_pieces[i] for i in range(6)]
print(*result)
```

### 6. 아스키 아트 출력

#### 문제: 25083 (새싹)
- **핵심 문법**: 여러 줄 문자열, 이스케이프 문자
- **학습 포인트**:
  - 삼중 따옴표로 여러 줄 문자열 표현
  - 이스케이프 문자 처리

## 🎯 핵심 파이썬 문법 정리

1. **문자열 패턴 매칭**:
   - `replace()`: 문자열 치환
   - KMP 알고리즘: 효율적인 패턴 검색

2. **문자열 빈도 분석**:
   - `collections.Counter`: 빈도 계산
   - `max()`: 최댓값 찾기
   - 리스트 컴프리헨션으로 필터링

3. **팰린드롬 검사**:
   - `word[::-1]`: 문자열 역순
   - 슬라이싱으로 비교

4. **반복문과 문자열 조작**:
   - `range(n, 0, -1)`: 역순 반복
   - 문자열 반복: `' ' * n`

5. **리스트 연산**:
   - `enumerate()`: 인덱스와 값 동시 접근
   - 리스트 컴프리헨션으로 변환

## 💡 효율성 개선 팁

1. **문자열 패턴 매칭**: 
   - 간단한 치환은 `replace()` 사용
   - 복잡한 패턴 매칭은 KMP 알고리즘 고려

2. **빈도 분석**: 
   - `collections.Counter` 활용으로 간결하게 처리

3. **팰린드롬 검사**: 
   - `word == word[::-1]`로 간단히 확인 가능

4. **반복문 최적화**: 
   - 조건에 따라 반복 범위 조정
   - 불필요한 반복 제거

## 📖 KMP 알고리즘 추가 학습 자료

**KMP 알고리즘을 더 깊이 이해하려면**:
1. 실패 함수의 의미와 계산 방법
2. 패턴 이동 규칙의 원리
3. 다른 문자열 검색 알고리즘과의 비교 (Rabin-Karp, Boyer-Moore 등)
4. 실제 문제 적용 사례

**관련 백준 문제 추천**:
- 1786번: 찾기 (KMP 알고리즘 직접 구현)
- 1305번: 광고 (KMP 실패 함수 활용)
- 4354번: 문자열 제곱 (KMP 실패 함수 활용)

