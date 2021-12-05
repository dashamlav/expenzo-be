
class UserType:

    ADMIN = 'adm'
    DEMO = 'dem'
    DEFAULT = 'def'

    Choices = (
        (ADMIN, 'admin'),
        (DEMO, 'demo'),
        (DEFAULT, 'default')
    )
    

class CurrencyType:

    INR = 'inr'
    USD = 'usd'
    EURO = 'eur'
    POUND = 'pnd'

    Choices = (
        (INR, 'INR'),
        (USD, 'USD'),
        (EURO, 'Euro'),
        (POUND, 'Pound')
    )