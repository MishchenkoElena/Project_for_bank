import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_mask_card_number(card_number: str) -> None:
    assert get_mask_card_number(card_number) == "6831 98** **** 7658"


def test_invalid_card_number() -> None:
    with pytest.raises(ValueError):
        get_mask_card_number("68319824767376582" "" "[]")


def test_zero_card_number() -> None:
    with pytest.raises(ValueError):
        get_mask_card_number("0")


def test_mask_account_number(account_number: str) -> None:
    assert get_mask_account(account_number) == "**4305"


def test_invalid_account_number() -> None:
    with pytest.raises(ValueError):
        get_mask_card_number("736541084301358743" "" "[]")
