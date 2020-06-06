# 기본값(default)을 설정하면 작성하지 않은 부분은 기본값 호출
def profile(name, age=16, job="학생"):
    print("이름: {0}, 나이: {1}, 직업:{2}".format(name, age, job))

profile("도일")
profile("미란")

# keyword를 쓰면 parameter 순서가 바뀌어도 정상 호출 가능
def profile(name, age, job):
    print("이름: {0}, 나이: {1}, 직업:{2}".format(name, age, job))

profile(job="탐정", name="코난", age=7)