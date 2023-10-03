from ticket_price.discount_percent import discount_percent


# 입장료 할인은 일반 할인, 특별 할인 2종류
# 할인은 중복 적용이 불가하며 중복 시 할인율이 높은 항목이 적용됨
# 3세 미만은 무료 입장
# 복지카드, 국가 유공자  = 특별 할인
# 13세 미만 = 일반 할인
# 17세 이후 입장 시 = 일반 할인
# 기본 입장료 : 10,000원
# 특별할인 : 4,000원 (60% 할인)
# 일반할인 : 8,000원 (20% 할인)

class age_and_benefit_check():

    def return_type(self, age, national_merit, welfare_card):
        if ( national_merit == "y" or national_merit == "Y") or (welfare_card == "y" or welfare_card == "Y"): # upper()를 쓰고 싶었으나 안먹힘.
            return discount_percent.SPECIAL_DISCOUNT
        elif age < 3:
            return discount_percent.BABY_DISCOUNT
        elif age < 13:
            return discount_percent.NORMAL_DISCOUNT
        elif age < 17:
            return discount_percent.NORMAL_DISCOUNT

        return discount_percent.NO_DISCOUNT


