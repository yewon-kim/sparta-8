# pickle
# 프로그램 상 데이터를 파일 형태로 저장하거나 불러오기

# "wb" : write, binary 쓰기
import pickle
profile_file = open("profile.pickle", "wb")
profile = {"이름": "코난", "나이": 7, "직업": ["탐정", "학생"]}
print(profile)
pickle.dump(profile, profile_file) # profile에 있는 정보를 profile_file에 저장
profile_file.close()

# "rb" : read, binary 읽기
profile_file = pickle.load("profile.pickle", "rb")
profile = pickle.load(profile_file) # profile_file에 있는 정보를 profile에 불러오기
print(profile)
profile_file.close()