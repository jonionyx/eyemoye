import pandas as pd
import great_expectations as gx
from great_expectations.expectations import ExpectColumnValuesToNotBeNull, ExpectColumnValuesToBeBetween

def run_health_check():
    # 1. Initialize Context (Point to your root directory)
    # Using get_context() without arguments creates an EphemeralContext (in-memory)
    # If you want to persist to your /gx folder, use gx.get_context(project_root_dir="../")
    context = gx.get_context(mode="ephemeral")

    # 2. Create Mock Data
    df = pd.DataFrame({
        "transaction_id": [1, 2, 3],
        "amount": [100.0, 250.5, -5.0]  # The -5.0 should trigger a failure
    })

    # 3. Setup Data Infrastructure (Fluent API 1.0)
    datasource_name = "health_check_datasource"
    # Use 'data_sources' plural and 'add_pandas'
    try:
        datasource = context.data_sources.add_pandas(name=datasource_name)
    except Exception:
        datasource = context.data_sources.get(datasource_name)

    
    # Asset Handling
    asset_name = "quick_test_asset"
    try:
        asset = datasource.add_dataframe_asset(name=asset_name)
    except Exception:
        asset = datasource.get_asset(asset_name)

        # Batch Definition (Glue between logig & data)
    batch_def_name = "default_batch_definition"
    try:
        batch_definition = asset.add_batch_definition_whole_dataframe(name=batch_def_name)
    except Exception:
        batch_definition = asset.get_batch_definition(batch_def_name)

    # 4. Suite Management (The new 'Suites' object)
    suite_name = "health_check_suite"
    suite = context.suites.add_or_update(suite=gx.ExpectationSuite(name=suite_name))

    # 5. Add Expectations directly to the Suite object
    suite.expectations = []
    suite.add_expectation(ExpectColumnValuesToNotBeNull(column="transaction_id"))
    suite.add_expectation(ExpectColumnValuesToBeBetween(column="amount", min_value=0))

    # 6. Validation
    # We create a 'Batch Request' to link the dataframe to the asset
    # batch_request = asset.build_batch_request(dataframe=df)
    
    # Run validation using a temporary validator
    validator = context.get_validator(
        # batch_request=batch_request, 
        batch_definition=batch_definition,
        batch_parameters={"dataframe": df},
        expectation_suite_name=suite_name
    )
    results = validator.validate()

    # 7. SDET Style Output
    print("\n" + "="*30)
    print(f"HEALTH CHECK STATUS: {'PASSED' if results.success else 'FAILED'}")
    print("="*30)
    
    if not results.success:
        print(f"Caught {results.statistics['unsuccessful_expectations']} intentional data errors.")
    
    return results.success

if __name__ == "__main__":
    run_health_check()