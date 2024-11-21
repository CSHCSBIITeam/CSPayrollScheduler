import pandas as pd
from cs_payroll_scheduler.tools.create_payroll_range import date_range
from datetime import timedelta, datetime

class PayrollPeriodGenerators:

    def __init__(self, future_payroll_range: int, past_payroll_range: int) -> None:

        ranges= date_range(future_payroll_range, past_payroll_range)
        
        self.previous_payroll= ranges[0]
        self.current_payroll= ranges[1]
        self.future_payroll= ranges[2]
        self.biweekly_gap_future= ranges[3]
        self.biweekly_gap_past= ranges[4]

    def _calculate_payroll_status(self, row):

        payroll_start = row['Payroll Period Start Date']
        payroll_end = row['Payroll Period End Date']

        today = datetime.now().date()

        previous_period_end= self.current_payroll - timedelta(days=1)
        next_period_start= self.current_payroll + timedelta(days=14)
        
        if payroll_start <= today <= payroll_end:
            return "In Progress"
        elif payroll_end < today and payroll_end == previous_period_end:
            return "Recently Completed"
        elif payroll_start > today and payroll_start == next_period_start:
            return "Upcoming Next"
        elif payroll_end < today:
            return "Completed"
        else:
            return "Future Period"
        
    def _payroll_period(self, row):

        first_term= row['Payroll Period Start Date']
        second_term= row['Payroll Period End Date']

        return f"{first_term.strftime('%b %d')} - {second_term.strftime('%b %d, %y')}"
        
    def generate_periods(self):

        periods_previous= []

        for period in range(self.biweekly_gap_past):

            if period == 0:

                periods_previous.append(self.previous_payroll + timedelta(14))

            else:

                periods_previous.append(periods_previous[period - 1] + timedelta(14))

        periods_future= []

        for period in range(self.biweekly_gap_future):

            if period == 0:

                periods_future.append(self.current_payroll + timedelta(14))

            else:

                periods_future.append(periods_future[period - 1] + timedelta(14))

        periods_previous.extend(periods_future)

        period_df= pd.DataFrame(periods_previous, columns= ['Payroll Period Start Date'])

        period_df['Payroll Period End Date'] = period_df['Payroll Period Start Date'].apply(lambda x: x + timedelta(days= 13))

        period_df['Payroll Status'] = period_df.apply(self._calculate_payroll_status, axis= 1)
        period_df['Payroll Period'] = period_df.apply(self._payroll_period, axis= 1)

        return period_df