import unittest
import pandas as pd
from cs_payroll_scheduler.main import PayrollPeriodGenerators

class TestScheduler(unittest.TestCase):

    def setUp(self) -> None:
        
        self.payroll_generator= PayrollPeriodGenerators(12,12)

    def test_scheduler(self):

        print(self.payroll_generator.generate_periods())

        self.assertIsInstance(self.payroll_generator.generate_periods(), pd.DataFrame)