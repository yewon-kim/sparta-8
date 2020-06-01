### Module 외장함수

# glob : 경로 내의 폴더/파일 목록 조회
import glob
print(glob.glob("*.py"))

# os : 운영체제에서 제공하는 기본 기능
import os
print(os.getcwd()) # 현재 디렉토리

# folder = "folder_example"
# if os.path.exists(folder):
#     os.rmdir(folder) # 폴더삭제
#     print("폴더를 삭제하였습니다.")
# else:
#     os.makedirs(folder) # 폴더생성
#     print(folder, "폴더를 생성하였습니다.")

# time
import time
print(time.localtime())
print(time.strftime("%Y-%m-%d %H-%M-%S"))

### datetime
import datetime
print("오늘 날짜는 {0}입니다.".format(datetime.date.today()))

# timedelta : 두 날짜 사이의 간격
today = datetime.date.today() # 오늘 날짜
td = datetime.timedelta(days=100) # 100일
print("오늘부터 100일 뒤 날짜는 {0}입니다.".format(today + td))