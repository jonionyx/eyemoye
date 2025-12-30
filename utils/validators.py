from jsonschema import validate
from jsonschema.exceptions import ValidationError


def validate_json_schema(instance, schema):
    """
    Validates a JSON response against a predefined schema.
    Raises an informative error if validation fails.
    """

    try:
        validate(instance=instance, schema=schema)
    except ValidationError as e:
        # We raise a custom message to make debugging easier in the logs
        pytest_fail_msg = f"Schema validation failed! \nMessage: {e.message} \nPath: {list(e.path)}"
        raise AssertionError(pytest_fail_msg)
    

def validate_performance(response, max_ms=5000):
    """Fails the test if the response time exceeds the limit"""

    latency_ms = response.elapsed.total_seconds() * 1000
    assert latency_ms <= max_ms, f"Performance SLA failed: {latency_ms: .0f}ms exceeds. {max_ms}ms"

