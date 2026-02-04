
import great_expectations as gx
import os

def init_finance_audit_context():
    project_root = os.getcwd()
    context = gx.get_context(project_root_dir=project_root)
    
    # 1. Datasource
    datasource = context.data_sources.add_or_update_pandas(name="finance_datasource")

    # 2. Financial Asset
    # We define the asset that will hold our CSV data
    asset = datasource.add_or_update_dataframe_asset(name="monthly_audit_asset")

    # 3. Batch Definition
    batch_definition = asset.add_or_update_batch_definition_whole_dataframe(
        name="finance_batch_definition"
    )

    # 4. Financial Suite
    suite_name = "finance_full_audit_suite"
    suite = context.suites.add_or_update(gx.ExpectationSuite(name=suite_name))

    return context, batch_definition, suite