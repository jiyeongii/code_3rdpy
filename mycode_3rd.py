#학생 10명의 성적을 입력받아 평균을 계산하는 코드를 작성하자
total = 0 # 변수 total 초기값은 0이다.
counter = 1 # 변수 counter의 값은 1이다.
while counter <= 10 : # 반복문으로 counter의 값이 10이 될때까지
    grade = int(input("성적을 입력하시오.:")) # 변수 grade는 정수형 변화문 int를 이용하여 입력받는다.
    total = grade + total # 변수 grade의  값과 total의 값을 게산하여 다시 total
    counter = counter + 1 # 변수 counter의 값을 한번 실행시킬때마다 1씩 증가
average = total // 10  # 변수 average 위 반복문에서 결과값에 10으로 나눈다.
print(average) # 평균값을 출력
# write by 전지영
