
class ExpenseCategory:
    BANKING = 'bank'
    CLOTHING = 'clo'
    ENTERTAINMENT = 'ent'
    ELECTRONICS = 'elec'
    FASHION = 'fash'
    FOOD = 'food'
    GIFT = 'gift'
    GROCERY = 'gro'
    HOUSEHOLD = 'hh'
    JEWELRY = 'jew'
    MISCELLANEOUS = 'misc'
    MEDICAL = 'med'
    OTHER = 'oth'
    TRAVEL = 'tra'
    
    Choices = (
        (BANKING, 'banking'),
        (CLOTHING, 'clothing'),
        (ENTERTAINMENT, 'entertainment'),
        (ELECTRONICS, 'electronics'),
        (FASHION, 'fashion'),
        (FOOD, 'food'),
        (GIFT, 'gift'),
        (GROCERY, 'grocery'),
        (HOUSEHOLD, 'household'),
        (JEWELRY, 'jewelry'),
        (MISCELLANEOUS, 'miscellaneous'),
        (MEDICAL, 'medical'),
        (OTHER, 'other'),
        (TRAVEL, 'travel'),
    )

class TransactionType:
    CASH = 'cash'
    CREDIT_CARD = 'cc'
    DEBIT_CARD = 'dc'
    NET_BANKING = 'netb'
    UPI = 'upi'

    Choices = (
        (CASH , 'cash'),
        (CREDIT_CARD , 'credit card'),
        (DEBIT_CARD, 'debit card'),
        (NET_BANKING , 'net banking'),
        (UPI , 'upi'),
    )


