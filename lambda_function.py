import json
from datetime import datetime, timezone


def lambda_handler(event, context):
    """Simple demo Lambda deployed by a GitHub Actions OIDC pipeline."""
    message = "Hello from a GitHub Actions deployed Lambda!"
    response = {
        "message": message,
        "deployed_by": "github-actions",
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(response),
    }
