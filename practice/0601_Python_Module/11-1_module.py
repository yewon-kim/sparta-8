import theater_module
theater_module.price(3)
theater_module.price_morning(4)
theater_module.price_soldier(5)

# as로 import 하는 모듈명 줄이기
import theater_module as mv
mv.price(3)
mv.price_morning(4)
mv.price_soldier(5)

# from 모듈명 import *
from theater_module import *
price(3)
price_morning(4)
price_soldier(5)

# from 모듈명 import 필요한 함수명
from theater_module import price, price_morning
price(3)
price_morning(4)

from theater_module import price_soldier as p_s
p_s(1)