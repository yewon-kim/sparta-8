# 예외 처리
try:
    print("나누기 전용 계산기입니다.")
    nums = []
    num1 = int(input("첫 번째 숫자 : "))
    num2 = int(input("두 번째 숫자 : "))
    nums.append(num1)
    nums.append(num2)
    nums.append(int(nums[0] / nums[1]))
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
except ValueError:
    print("에러! 잘못된 값 입력")
except ZeroDivisionError as err:
    print(err)
except Exception as err:
    print(err)
# 또는
except:
    print("알 수 없는 오류가 발생했습니다.")