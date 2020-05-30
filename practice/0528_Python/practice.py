def weight():
    gender = input("성별(male/female): ")
    height = float(input("키(m): "))
    if gender == "male":
        weight = height ** 2 * 22
        print("표준체중: ", weight, "kg")
    elif gender == "female":
        weight = height ** 2 * 21
        print("표준체중: ", weight, "kg")
    return weight

weight()