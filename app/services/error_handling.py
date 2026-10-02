import asyncio
from typing import Callable, Any


async def execute_with_retry(
    func: Callable, 
    max_retries: int = 3, 
    backoff: float = 1.0
) -> Any:
    """Execute function with exponential backoff retry logic."""
    for attempt in range(max_retries):
        try:
            return await func()
        except Exception as e:
            if attempt < max_retries - 1:
                wait_time = backoff ** attempt
                await asyncio.sleep(wait_time)
            else:
                raise
