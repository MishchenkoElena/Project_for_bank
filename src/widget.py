from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(user_accounting: str) -> str:
    """Маскировка номера банковской карты или счета"""

    if user_accounting.lower().startswith("счет"):
        return f"Счет {get_mask_account(user_accounting)}"
    else:
        return f"{user_accounting[:-16]} {get_mask_card_number(user_accounting[-16:])}"


def get_date(user_login_date: str) -> str:
    """Преобразование даты"""

    return f"{user_login_date[8:10]}.{user_login_date[5:7]}.{user_login_date[0:4]}"
