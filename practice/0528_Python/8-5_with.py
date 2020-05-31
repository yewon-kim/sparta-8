import pickle

with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))

# with만으로 파일을 만들고 불러올 수 있다!
with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("Python을 공부하고 있어요.")

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())