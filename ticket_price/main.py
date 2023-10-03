from ticket_price.age_check import age_and_benefit_check
from ticket_price.discount_percent import discount_percent


# [입장권 계산]
# 나이를 입력해 주세요(숫자):
# 입장시간을 입력해 주세요(숫자):
# 국가유공자 여부를 입력해 주세요(y/n):
# 복지카드 여부를 입력해 주세요(y/n):
# 입장료:

# 입장료 할인은 일반 할인, 특별 할인 2종류
# 할인은 중복 적용이 불가하며 중복 시 할인율이 높은 항목이 적용됨
# 3세 미만은 무료 입장
# 복지카드, 국가 유공자  = 특별 할인
# 13세 미만 = 일반 할인
# 17세 이후 입장 시 = 일반 할인
# 기본 입장료 : 10,000원
# 특별할인 : 4,000원 (60% 할인)
# 일반할인 : 8,000원 (20% 할인)

def print_value(age, enter_time, national_merit, welfare_care, primary_ticket_price, discounted_ticket_price):
    print("====="*10)
    print("나이 : ", age)
    print("입장시간 : ", enter_time)
    print("국가유공자 여부 : ", national_merit)
    print("복지카드 여부 : ", welfare_care)
    print("기본 티켓 가격 : ", primary_ticket_price)
    print("할인된 티켓 가격 : ", discounted_ticket_price)
    print("====="*10)


def cal_ticket_price(primary_ticket_price, discount_percent):
    return primary_ticket_price * discount_percent


def number_check(num):
    if num.isdigit():
        return print("입력하신 것이 숫자가 아닙니다.")
    else:
        return num


age = int(input("나이를 입력해 주세요 : "))
enter_time = int(input("입장시간을 입력해 주세요(24시 기준 앞자리 숫자) : "))
national_merit = input("국가유공자 여부를 입력해 주세요 (y/n) : ")
welfare_card = input(" 복지카드 여부를 입력해 주세요 (y/n) : ")
primary_ticket_price = int(input("입장료 티켓 가격을 입력해 주세요 : "))

person_type = age_and_benefit_check.return_type(age, national_merit, welfare_card)

if person_type == discount_percent.BABY_DISCOUNT:
    print(print_value(age, enter_time, national_merit, welfare_card, primary_ticket_price, cal_ticket_price(primary_ticket_price, discount_percent.BABY_DISCOUNT.value)))
elif  person_type == discount_percent.SPECIAL_DISCOUNT:
    print(print_value(age, enter_time, national_merit, welfare_card, primary_ticket_price, cal_ticket_price(primary_ticket_price, discount_percent.SPECIAL_DISCOUNT.value)))
elif person_type == discount_percent.NORMAL_DISCOUNT:
    print(print_value(age, enter_time, national_merit, welfare_card, primary_ticket_price, cal_ticket_price(primary_ticket_price, discount_percent.NORMAL_DISCOUNT.value)))
else:
    print(print_value(age, enter_time, national_merit, welfare_card, primary_ticket_price, cal_ticket_price(primary_ticket_price, discount_percent.NO_DISCOUNT.value)))
