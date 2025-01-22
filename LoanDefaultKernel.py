import numpy as np

# Functions for Convert Features Values
# Age Feature
def ConvertAgeValues(Value):
    if 18 <= Value <= 32:
        return 1
    elif 32 < Value <= 46:
        return 2
    elif 46 < Value <= 60:
         return 3
     elif Value > 60:
        return 4

# Income Feature
def ConvertIncomeValues(Value):
    if Value <= 60000:
        return 1
    elif 60000 < Value <= 120000:
        return 2
    elif Value > 120000:
        return 3

    # LoanAmount Feature
def ConvertLoanAmountValues(Value):
    if Value <= 25000:
        return 1
    elif 25000 < Value <= 75000:
        return 2
    elif 75000 < Value <= 200000:
        return 3
    elif Value > 200000:
        return 4

# CreditScore Feature
def ConvertCreditScoreValues(Value):
    if 300 <= Value <= 450:
        return 1
    elif 450 < Value <= 600:
        return 2
    elif 600 < Value <= 750:
        return 3
    elif Value > 750:
        return 4

# MonthsEmployed Feature
def ConvertMonthsEmployedValues(Value):
    if Value <= 30:
        return 1
    elif 30 < Value <= 60:
        return 2
    elif 60 < Value <= 90:
        return 3
    elif 90 < Value <= 120:
        return 4

# LoanTerm Feature
def ConvertLoanTermValues(Value):
    if Value <= 12:
        return 1
    elif 12 < Value <= 24:
        return 2
    elif 24 < Value <= 36:
        return 3
    elif 36 < Value <= 48:
        return 4
    elif 48 < Value <= 60:
        return 5

# InterestRate Feature
def ConvertInterestRateValues(Value):
    if Value <= 5:
        return 1
    elif 5 < Value <= 10:
        return 2
    elif 10 < Value <= 15:
        return 3
    elif 15 < Value <= 20:
        return 4
    elif 20 < Value <= 25:
        return 5

# DTIRate Feature
def ConvertDTIRatioValues(Value):
    if Value <= 0.3:
        return 1
    elif 0.3 < Value <= 0.6:
        return 2
    elif 0.6 < Value <= 0.9:
        return 3