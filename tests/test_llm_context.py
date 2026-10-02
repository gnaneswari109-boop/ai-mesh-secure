import pytest
from app.services.llm.task_context import build_task_prompt, extract_facts, extract_files, extract_takeaways


def test_build_task_prompt():
    task = {
        "task_id": "test-1",
        "name": "Test Task",
        "capability": "research",
        "input_data": {"topic": "AI"},
    }
    prompt = build_task_prompt(task)
    assert "Test Task" in prompt
    assert "research" in prompt
    assert "AI" in prompt


def test_extract_facts():
    text = "Fact 1 about AI\nFact 2 about ML\nFact 3 about DL"
    facts = extract_facts(text)
    assert len(facts) > 0
    assert isinstance(facts, list)


def test_extract_files():
    text = "main.py service.py utils.py"
    files = extract_files(text)
    assert len(files) > 0
    assert any(".py" in f for f in files)


def test_extract_takeaways():
    text = """Key points:
- Takeaway 1 about AI
- Takeaway 2 about ML
* Takeaway 3 about DL"""
    takeaways = extract_takeaways(text)
    assert len(takeaways) > 0
    assert isinstance(takeaways, list)
