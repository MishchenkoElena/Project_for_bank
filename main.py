from src.masks import get_mask_account
from src.masks import get_mask_card_number
from src.widget import mask_account_card
from src.widget import get_date

user_accounting = input("Введите номер банковской карты или счета")
print(mask_account_card('Visa Classic 6831982476737658'))
print(get_date('2024-03-11T02:26:18.671407'))