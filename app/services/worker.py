import asyncio


async def execute_researcher(task: dict):
    await asyncio.sleep(0.5)
    return {
        "task_id": task["task_id"],
        "summary": f"Research complete for {task['name']}",
        "facts": ["fact-1", "fact-2", "fact-3"],
    }


async def execute_coder(task: dict):
    await asyncio.sleep(0.7)
    return {
        "task_id": task["task_id"],
        "summary": f"Implementation complete for {task['name']}",
        "files": ["main.py", "service.py"],
    }


async def execute_summarizer(task: dict):
    await asyncio.sleep(0.4)
    return {
        "task_id": task["task_id"],
        "summary": f"Summary complete for {task['name']}",
        "key_takeaways": ["Takeaway 1", "Takeaway 2"],
    }


async def execute_task(task: dict):
    capability = task["capability"]
    if capability == "research":
        return await execute_researcher(task)
    if capability == "code":
        return await execute_coder(task)
    if capability == "summary":
        return await execute_summarizer(task)
    return {
        "task_id": task["task_id"],
        "summary": f"Task complete for {task['name']}",
    }
