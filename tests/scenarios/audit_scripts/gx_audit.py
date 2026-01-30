import pytest
import pandas as pd
import great_expectations as gx
# Import specific expectation classes for better type-hinting and clarity
from great_expectations.expectations import ExpectColumnValuesToNotBeNull

class TestDataIntegrity:

    def test_financial_csv_quality(self, gx_context):
        # 1. Load Data
        csv_path = "data/financial_data.csv"
        df = pd.read_csv(csv_path)

        # 2. Data Source Handling (Stable 1.0 Syntax)
        datasource_name = "finance_pipeline"
        try:
            # context.data_sources is the correct entry point in 1.0
            datasource = gx_context.data_sources.add_pandas(name=datasource_name)
        except Exception:
            datasource = gx_context.data_sources.get(datasource_name)

        # 3. Asset Handling
        asset_name = "monthly_transactions"
        try:
            asset = datasource.add_dataframe_asset(name=asset_name)
        except Exception:
            asset = datasource.get_asset(asset_name)

        # 4. Batch Definition (The "Glue" between logic and data)
        batch_def_name = "default_batch_definition"
        try:
            batch_definition = asset.add_batch_definition_whole_dataframe(name=batch_def_name)
        except Exception:
            batch_definition = asset.get_batch_definition(batch_def_name)

        # 5. Suite Management (Stable 1.0 Syntax)
        suite_name = "transaction_audit_suite"
        # add_or_update() is the idempotent method for suites
        suite = gx_context.suites.add_or_update(gx.ExpectationSuite(name=suite_name))

        # 6. Define Expectations (Class-based approach)
        # We add the expectation object directly to the suite
        suite.expectations = []
        suite.add_expectation(
            ExpectColumnValuesToNotBeNull(column="transaction_id")
        )

        # 7. Validation using the Validator
        # In 1.0, the Validator links the Batch Definition to the Suite
        validator = gx_context.get_validator(
            batch_definition=batch_definition,
            batch_parameters={"dataframe": df},
            expectation_suite_name=suite_name
        )
        
        results = validator.validate()

        # 8. Assertion
        assert results.success, f"Data Audit Failed. Statistics: {results.statistics}"