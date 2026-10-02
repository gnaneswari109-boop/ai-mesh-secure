import asyncio
from app.services.llm.agent_llm import get_llm_response
from app.services.llm.task_context import (
    build_task_prompt,
    extract_facts,
    extract_files,
    extract_takeaways,
)
from app.services.memory import get_memory
from app.services.error_handling import execute_with_retry


async def execute_researcher_with_llm(task: dict):
    """Execute researcher task using Gemini LLM."""
    shared_memory = get_memory(task["task_id"])
    prompt = build_task_prompt(task, shared_memory)
    prompt += "\n\nAs a research expert, provide comprehensive findings and analysis."
    
    result_text = await execute_with_retry(lambda: get_llm_response("researcher", prompt))
    
    return {
        "task_id": task["task_id"],
        "summary": result_text,
        "facts": extract_facts(result_text),
    }


async def execute_coder_with_llm(task: dict):
    """Execute coder task using ChatGPT LLM."""
    shared_memory = get_memory(task["task_id"])
    prompt = build_task_prompt(task, shared_memory)
    prompt += "\n\nAs a senior software engineer, provide implementation details with code examples."
    
    result_text = await execute_with_retry(lambda: get_llm_response("coder", prompt))
    
    return {
        "task_id": task["task_id"],
        "summary": result_text,
        "files": extract_files(result_text),
    }


async def execute_summarizer_with_llm(task: dict):
    """Execute summarizer task using Gemini LLM."""
    shared_memory = get_memory(task["task_id"])
    prompt = build_task_prompt(task, shared_memory)
    prompt += "\n\nAs an executive summary writer, condense the information into key takeaways."
    
    result_text = await execute_with_retry(lambda: get_llm_response("summarizer", prompt))
    
    return {
        "task_id": task["task_id"],
        "summary": result_text,
        "key_takeaways": extract_takeaways(result_text),
    }


async def execute_task_with_llm(task: dict):
    """Main entry point for LLM-based task execution."""
    capability = task["capability"]
    
    try:
        if capability == "research":
            return await execute_researcher_with_llm(task)
        elif capability == "code":
            return await execute_coder_with_llm(task)
        elif capability == "summary":
            return await execute_summarizer_with_llm(task)
        else:
            return {
                "task_id": task["task_id"],
                "summary": f"Unknown capability: {capability}",
            }
    except Exception as e:
        return {
            "task_id": task["task_id"],
            "summary": f"Task execution failed: {str(e)}",
            "error": str(e),
        }
