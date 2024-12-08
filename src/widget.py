def mask_account_card(user_accounting: str) -> str:
    """Маскировка номера банковской карты или счета"""

    if "MasterCard" or "Maestro" or "Visa" in user_accounting:
        return f" {user_accounting[0:-12]} {user_accounting[-12:-10]}** **** {user_accounting[-4:]}"
    else:
        return f" Счет **{user_accounting[-4:]}"


def get_date(user_login_date: str) -> str:
    """Преобразование даты"""

    return f" {user_login_date[8:10]}.{user_login_date[5:7]}.{user_login_date[0:4]}"
