### 폴더 만들어서 Package 만들기

import travel.thailand
trip_to = travel.thailand.ThailandPackage()
trip_to.detail()

from travel import vietnam
trip_to = travel.vietnam.VietnamPackage()
trip_to.detail()

### __init__.py에 __all__ = ["module"] 세팅해주기!
from travel import *
trip_to = vietnam.VietnamPackage()
trip_to.detail()

### package, module 위치
import inspect
import random
print(inspect.getfile(random))
# ㄴrandom 이라는 module이 어느 위치에 있는지 파일 정보 출력
print(inspect.getfile(vietnam))