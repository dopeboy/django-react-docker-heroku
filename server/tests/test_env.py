"""Sanity test environment setup."""
import os.path

from django.conf import settings
from django.test import TestCase


class EnvTestCase(TestCase):
    """Environment test cases."""

    def test_env_file_exists(self):
        """Test environment file exists."""
        env_file = os.path.join(settings.DEFAULT_ENV_PATH, '.env')
        assert os.path.exists(env_file)
