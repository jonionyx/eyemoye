import pytest
from config import get_config, CURRENT_ENV
from clients.base_client import BaseClient
from datetime import datetime
from utils.helpers import logger
import great_expectations as gx
import os


@pytest.fixture
def user_context(api_client):
    """
    A fixture that creates a user for the test
     and ensures it is deleted after the test finishes.
    """
    created_user_ids = []

    def _create_user(payload):
        response  = api_client.post("/users", json=payload)
        user_id = response.json().get("id")
        if user_id:
            created_user_ids.append(user_id)
        return response
    
    yield _create_user  # The test runs here


    #  --- Teardown Logic ---
    print("\nCleaning up test data")
    for user_id in created_user_ids:
        api_client.delete(f"/users/{user_id}")



def pytest_addoption(parser):
    """Adds a custom command line argument for environment"""

    parser.addoption(
        "--env",
        action="store",
        default=CURRENT_ENV,
        help="Environment to run tests agaonst: dev, staging or prod"
    )
    
# @pytest.fixture(scope="session")
# def env_config(request):
#     """Retrieves the configuration for the selected environment"""

#     env_name = request.config.getoption("--env").lower()
#     if env_name not in ENVIRONMENTS:
#         raise ValueError(f"Invalid environment: {env_name}. Choose from {list(ENVIRONMENTS.keys())}")
#     return ENVIRONMENTS[env_name]


@pytest.fixture(scope="session")
def api_client(request):
    """
    Provides an authenticated instance of the BaseClient.
    Runs once per test session.
    """
    env_name = request.config.getoption("--env", default=CURRENT_ENV)
    config = get_config(env_name)
    
    if not config:
        pytest.exit(f"Failure: Credentials for environment '{env_name}' not found in .env")

    # Initialise with URL and the environment-specific key

    client = BaseClient(
        base_url=config["base_url"],
        api_key=config.get("api_key"),
        timeout=config.get("timeout", 10)
    )

    
    # Logic Switch: If API Key is present, we are altready Authenticated
    
    if config.get("api_key"):
        print(f"----Info: Authenticated via API Key for {env_name}---")
    else:
        #Fall back to Username/Password if no API Key is provided
        username = config.get("username")
        password = config.get("password")

        if not username or not password:
               pytest.exit(f"Blocking Error: No API Key or Credentials found for {env_name}")

        try:
            client.authenticate(username, password)
            print(f"----- Info: Authenticated via Credentials for {env_name}----")
        except Exception as e:
            pytest.exit(f"Blocking Errot: Login failed for {env_name}: {e}")
    return client 



def pytest_html_report_title(report):
    report.title = "API Automation Execution Report"

@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    
    """ Add or remove metadata from the report """
    metadata.pop("JAVA_HOME", None) # Remove unnecessary info
    metadata["Project Name"] = "User Management API" 
    metadata["Execution Time"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Extends the HTML report to include requests/response details on failure.
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])

    if report.when == "call" and report.failed:
        # Assuming you store the last response in the test item
        if hasattr(item, "last_response"):
            res = item.last_response
            log_info = f"\nURL: {res.url}\nStatus: {res.status_code}\nResponse: {res.text}"
            extra.append(pytest_html.extras.text(log_info, name="API Details"))

    report.extra = extra


@pytest.fixture(scope="session", autouse=True)
def init_logger():
    logger.info("Starting Test Session . . .")
    yield
    logger.info("Test Session Completed.")



# @pytest.fixture(scope="session")
# def gx_context():
#     """Initialises the Great Expectations context for the entire test session. """

#     # This will create or load the /gx folder in the root directory

#     return gx.get_context()
