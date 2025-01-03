def get_mask_card_number(user_card_number: str) -> str:
    """Маскировка номера банковской карты"""

    if len(user_card_number) != 16:
        raise ValueError("Данные введены некорректно: номер должен состоять из 16 цифр")
    return f"{user_card_number[:4]} {user_card_number[4:6]}** **** {user_card_number[-4:]}"


def get_mask_account(user_number_account: str) -> str:
    """Маскировка номера банковского счета"""

    return f"**{user_number_account[-4:]}"
