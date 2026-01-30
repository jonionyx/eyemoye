import pytest
import pandas as pd
from utils.setup_gx import init_permanent_context

def test_gx_system_is_functional():
    # 1. Get our initialized components
    context, batch_definition, suite_name = init_permanent_context()
    suite = context.suites.get(name=suite_name)

    # 2. Create fresh test data (with a deliberate error)
    df = pd.DataFrame({"transaction_id": [101, 102, None]}) 

    # 3. THE FIX: Get a 'Batch' object directly from the definition
    # This automatically includes all the datasource/connector metadata GX is complaining about
    batch = batch_definition.get_batch(batch_parameters={"dataframe": df})

    # 4. Run Validation directly on the Batch
    # This is the most stable way to validate in GX 1.0+
    results = batch.validate(expect=suite)
    
    print(f"\nAudit Success: {results.success}")
    
    # Assertions
    assert isinstance(results.success, bool)
    assert results.success is False, "Audit should have failed due to None value"
    # assert "ExpectColumnValuesToNotBeNull" in str(results)