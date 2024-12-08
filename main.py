from src.masks import get_mask_card_number
from src.masks import get_mask_account

user_card_number = input("Введите номер карты")
print(get_mask_card_number(user_card_number))

user_number_account = input("Введите номер счета")
print(get_mask_account("user_number_account"))
