from .conventions import LibConventions
from datetime import datetime, timedelta

def date_range(payroll_range_future: int, payroll_range_past: int):

    current_date = datetime.now().date()

    previous_date= datetime.strptime(LibConventions.PAYROLL_SEED.value, "%Y-%m-%d").date()

    biweeks = ((current_date - previous_date).days // 7) // 2

    current_payroll= previous_date + timedelta(weeks= biweeks * 2)

    future_payroll= current_payroll + timedelta(weeks=payroll_range_future * 2)

    previous_payroll= current_payroll - timedelta(weeks=payroll_range_past * 2)

    biweekly_gap_future= ((future_payroll - current_payroll).days // 7) // 2

    biweekly_gap_past= ((current_payroll - previous_payroll).days // 7) // 2

    return previous_payroll, current_payroll, future_payroll, biweekly_gap_future, biweekly_gap_past
