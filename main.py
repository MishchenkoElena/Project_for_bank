from src.widget import get_date, mask_account_card

user_accounting = input("Введите номер банковской карты или счета")
print(mask_account_card("Visa Classic 6831982476737658"))
print(mask_account_card("Счет 73654108430135874305"))
print(get_date("2024-03-11T02:26:18.671407"))
