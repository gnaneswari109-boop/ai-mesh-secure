import asyncio


async def run_researcher(task: dict):
    await asyncio.sleep(0.5)
    return {
        "task_id": task["task_id"],
        "summary": f"Research complete for {task['name']}",
        "facts": ["Fact 1", "Fact 2"],
    }


async def run_coder(task: dict):
    await asyncio.sleep(0.7)
    return {
        "task_id": task["task_id"],
        "summary": f"Implementation complete for {task['name']}",
        "files": ["main.py", "service.py"],
    }


async def run_summarizer(task: dict):
    await asyncio.sleep(0.4)
    return {
        "task_id": task["task_id"],
        "summary": f"Summary complete for {task['name']}",
        "key_takeaways": ["Takeaway 1", "Takeaway 2"],
    }


async def execute_task(task: dict):
    capability = task["capability"]
    if capability == "research":
        return await run_researcher(task)
    if capability == "code":
        return await run_coder(task)
    if capability == "summary":
        return await run_summarizer(task)
    return {
        "task_id": task["task_id"],
        "summary": f"Completed: {task['name']}",
    }
