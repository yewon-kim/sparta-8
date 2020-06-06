absent = [2, 5]
no_book = [7]
for student in range(1, 11):
    if student in absent:
        continue
    elif student in no_book:
        print("{0}번, 책 없으면 뒤에 나가 서 있어.".format(student))
    print("{0}번, 책 읽어보세요.".format(student))