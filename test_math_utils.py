from math_utils import calculate_discount
from math_utils import process_payment

def test_calculate_discount():
    # 20% off $100 should be $80. The bug will return $80 (100-20), 
    # WAIT, let's make a better bug.
    pass

# Let's use a Type Error bug, which you highlighted in your EDA!

def test_process_payment():
    # Should successfully add float and string
    assert process_payment(100.0, "5.50") == 105.50
