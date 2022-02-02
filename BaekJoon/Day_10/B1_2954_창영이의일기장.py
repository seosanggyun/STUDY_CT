
## 문자열이 공백을 기준으로
## 여러개 들어와야 되니까 리스트로 저장
D = list(map(str, input().split()))

## 모음이 있을 경우 p 와 해당 모음을 덧붙이는 구조
## 정정당당하게 바꿔줘라

## 좀 더 똑똑하게 하는 방법은 없을까

for i in D:
    i = i.replace('apa', 'a')
    i = i.replace('epe', 'e')
    i = i.replace('ipi', 'i')
    i = i.replace('opo', 'o')
    i = i.replace('upu', 'u')
    
    print(i)

