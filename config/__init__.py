"""Configuration package for the application."""
import json
from typing import Dict

import boto3

from src.pkg import env


def get_remote() -> Dict[str, str]:
    """Get remote configuration from AWS Secrets Manager."""

    stage = env.get_str("STAGE")

    if stage not in ["dev", "prod"]:
        return {}

    client = boto3.client("secretsmanager")
    response = client.get_secret_value(SecretId="secret-name")

    secrets = json.loads(response["SecretString"])

    return secrets
