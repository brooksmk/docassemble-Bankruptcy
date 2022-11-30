def amount_fully_exempt(non_job_income):
  fully_exempt = list()
  total = float(0)
  for item in non_job_income:
    if item.name in ['Workers Compensation', 'Unemployment', 'Social Security', 'Public Assistance (Food Stamps, Cash Assistance)', 'EAEDC', 'Food Stamps', 'Veterans Benefits', 'Pension/Annuity/Retirement']:
            fully_exempt.append(item)
  for item in fully_exempt:
      total = total + float(item.amount(period_to_use=52))
  return total
        
        
def jobs_and_fully_exempt_combined(jobs, non_job_income):
    jobs_and_fully_exempt = list()
    for item in non_job_income:
        if item.name in ['Workers Compensation', 'Unemployment', 'Social Security', 'Public Assistance (Food Stamps, Cash Assistance)', 'EAEDC', 'Food Stamps', 'Veterans Benefits', 'Pension/Annuity/Retirement']:
            jobs_and_fully_exempt.append(item)
    for item in jobs:
        jobs_and_fully_exempt.append(item)
    return jobs_and_fully_exempt

def fully_non_exempt(non_job_income):
    fully_non_exempt = list()
    total = float(0)
    for item in non_job_income:
        if item.name not in ['Workers Compensation', 'Unemployment', 'Social Security', 'Public Assistance (Food Stamps, Cash Assistance)', 'EAEDC', 'Food Stamps', 'Veterans Benefits', 'Pension/Annuity/Retirement']:
            fully_non_exempt.append(item)
    for item in fully_non_exempt:
        total = total + float(item.amount(period_to_use=52))
    return total

def amount_not_exempt(IncomeList):
    total = float(0)
    for item in IncomeList:
        if item.name in ['Workers Compensation', 'Unemployment', 'Social Security', 'Public Assistance (Food Stamps, Cash Assistance)', 'EAEDC', 'Food Stamps', 'Veterans Benefits', 'Pension/Annuity/Retirement']:
            total = total
        else:
            total = total + float(item.amount(period_to_use=52))
    if (float(total) <= 637.50) is False:
        if ((float(total) * .85) > 637.50) is True:
            amount_not_exempt = (float(total) * .15)
        else:
            amount_not_exempt = (float(total) - 637.50)
    else:
        amount_not_exempt = float(0)
    return amount_not_exempt

def exempt_assets(assets):
    for item in assets:
        if item.asset_type == "car":
            if item.disabled_or_over_sixty == True:
                item.amount_not_exempt = item.value - 15000
            else:
                item.amount_not_exempt = item.value - 7500
            if item.amount_not_exempt < 0:
                item.amount_not_exempt = 0
        if item.asset_type == "home":
            if item.homestead_filed == False:
              if (item.value - item.mortgage) >= 125000:
                  item.amount_not_exempt = (item.value - item.mortgage) - 125000
              else:
                  item.amount_not_exempt = 0
            if item.homestead_filed == True:
              if (item.value - item.mortgage) >= 500000:
                  item.amount_not_exempt = (item.value - item.mortgage) - 500000
              else:
                  item.amount_not_exempt = 0
        if item.asset_type == "bank_account":
            if item.value >= 2500:
                item.amount_not_exempt = item.value - 2500
            else:
                item.amount_not_exempt = 0
        if item.asset_type == "jewelry":
            if item.value >= 1225:
                item.amount_not_exempt = item.value - 1225
            else:
                item.amount_not_exempt = 0
        if item.asset_type == "other_valuable_things":
          item.amount_not_exempt = item.value
    return assets




