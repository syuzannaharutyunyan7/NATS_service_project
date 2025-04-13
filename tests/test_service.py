import sys
import os

project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'nats_service_project'))
sys.path.append(project_path)

import asyncio
import pytest
from service_layer import process_message  

@pytest.mark.asyncio
async def test_process_message():
    await process_message("Test message")
