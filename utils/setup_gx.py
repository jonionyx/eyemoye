import pandas as pd
import great_expectations as gx
import os
from great_expectations.expectations import ExpectColumnValuesToNotBeNull

def init_permanent_context():
    # 1. Force the creation of a permanent context at the project root
    # This creates the /gx folder officially
    project_root = os.getcwd()
    context = gx.get_context(project_root_dir=project_root)
    
    # 2. Setup Data Source
    ds_name = "finance_datasource"
    # In 1.0+, use add_or_update_pandas to handle re-runs seamlessly
    try:
        datasource = context.data_sources.add_pandas(name=ds_name)
    except Exception:
        datasource = context.data_sources.get(ds_name)

    # 3. Setup Asset
    asset_name = "bank_transactions"
    try:
        asset = datasource.add_dataframe_asset(name=asset_name)
    except Exception:
        asset = datasource.get_asset(asset_name)

    # 4. Setup Batch Definition (The permanent link)
    # This saves the definition into your /gx folder
    batch_def_name = "default_batch_definition"
    try:
        batch_definition = asset.add_batch_definition_whole_dataframe(name=batch_def_name)
    except Exception:
        batch_definition = asset.get_batch_definition(batch_def_name)

    # 5. Create Suite
    suite_name = "finance_suite"
    suite = context.suites.add_or_update(gx.ExpectationSuite(name=suite_name))

    suite.expectations = []
    suite.add_expectation(ExpectColumnValuesToNotBeNull(column="transaction_id"))

    print(f"✅ Permanent GX context initialized at {project_root}/gx")
    return context, batch_definition, suite_name

if __name__ == "__main__":
    init_permanent_context()
    print("GX Structure Initialised Successfully")


