class ThailandPackage:
    def detail(self):
        print("[태국 패키지 3박 5일] 방콕, 파타야 여행 (야시장 투어) 50만원")

if __name__ == "__main__":
    print("Thailand module을 직접 실행")
    print("이 문장은 module을 직접 실행할 때만 표시됨.")
    trip_to = ThailandPackage()
    trip_to.detail()
else:
    print("Thailand 외부에서 module 호출")