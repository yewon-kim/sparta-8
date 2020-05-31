# 08. class 사용하여 부동산 정보 표시

class House:
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    def show_detail(self):
        print("지역: {0}\t타입: {1}\t{2}\t가격: {3}\t준공년도: {4}"\
            .format(self.location, self.house_type, self.deal_type, self.price, self.completion_year))

houses = []
house1 = House("강남", "아파트", "매매", "20억", "2010년")
house2 = House("마포", "오피스텔", "전세", "7억", "2007년")
house3 = House("송파", "빌라", "월세", "1000/50", "2000년")
houses.append(house1)
houses.append(house2)
houses.append(house3)

print("총 {0}개의 매물이 있습니다.".format(len(houses)))
for house in houses:
    house.show_detail()