import pandas as pd
import pytest
# from utils.new_setup_gx import init_finance_audit_context
from utils.setup_gx import init_permanent_context
from great_expectations.expectations import (
    ExpectColumnValuesToNotBeNull,
    ExpectColumnValuesToBeBetween,
    ExpectColumnValuesToMatchRegex
)

class TestFinancialDataAudit:

    def test_csv_audit_full_run(self):
        # 1. Initialize permanent context and components
        # context, batch_definition, suite = init_finance_audit_context()
        context, batch_definition, suite = init_permanent_context()

        # 2. Load the actual CSV data
        csv_path = "data/financial_data.csv"
        df = pd.read_csv(csv_path)

        # 3. Define the "Data Contract" (Expectations)
        # We clear old ones to ensure we are only running the latest rules
        suite.expectations = []
        
        # Rule 1: Transaction IDs must exist
        suite.add_expectation(ExpectColumnValuesToNotBeNull(column="transaction_id"))
        
        # Rule 2: Amounts must be positive (Assuming no reversals in this file)
        suite.add_expectation(ExpectColumnValuesToBeBetween(column="amount", min_value=0))
        
        # Rule 3: Account numbers should follow a specific pattern (Example: ACC-XXXX)
        suite.add_expectation(ExpectColumnValuesToMatchRegex(
            column="account_number", 
            regex=r"^ACC-\d{4}$"
        ))

        # 4. EXECUTION: Using your proven fix
        batch = batch_definition.get_batch(batch_parameters={"dataframe": df})
        results = batch.validate(expect=suite)

        # 5. SDET Report Printing
        print(f"\n--- Financial Audit Report ---")
        print(f"Status: {'SUCCESS' if results.success else 'FAILURE'}")
        print(f"Tests Passed: {results.statistics['successful_expectations']}")
        print(f"Tests Failed: {results.statistics['unsuccessful_expectations']}")
        
        # 6. Assertion for CI/CD Pipeline
        assert results.success, f"Data quality check failed! Issues found: {results.statistics}"