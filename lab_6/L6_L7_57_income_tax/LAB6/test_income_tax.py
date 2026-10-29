import pytest
from income_tax import taxable_income, tax_due, refund_status


# taxable_income tests

def test_new_regime():
    assert taxable_income(1000000, "new", 0) == 925000


def test_old_regime():
    assert taxable_income(1000000, "old", 100000) == 850000


def test_old_regime_investment_cap():
    assert taxable_income(1000000, "old", 200000) == 800000


def test_negative_gross_income():
    with pytest.raises(ValueError):
        taxable_income(-1, "new", 0)


def test_unknown_regime():
    with pytest.raises(ValueError):
        taxable_income(1000000, "other", 0)


def test_taxable_income_below_zero():
    assert taxable_income(50000, "new", 0) == 0


# tax_due tests

def test_below_exemption():
    assert tax_due(200000, 30) == 0


def test_age_60_exemption():
    assert tax_due(300000, 60) == 0


def test_age_80_exemption():
    assert tax_due(500000, 80) == 0


def test_invalid_taxable_amount():
    with pytest.raises(ValueError):
        tax_due(-1, 30)


def test_first_tax_slab():
    assert tax_due(400000, 30) == 7500


def test_second_tax_slab():
    assert tax_due(600000, 30) == 32500


# refund_status tests

def test_refund_on_time():
    assert refund_status(20000, 15000, True) == "refund"


def test_refund_delayed():
    assert refund_status(20000, 15000, False) == "refund delayed"


def test_pay_balance_on_time():
    assert refund_status(10000, 15000, True) == "pay balance"


def test_pay_balance_with_penalty():
    assert refund_status(10000, 15000, False) == "pay balance with penalty"


def test_settled():
    assert refund_status(15000, 15000, True) == "settled"