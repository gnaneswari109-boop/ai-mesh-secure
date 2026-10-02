def aggregate_results(results: list[dict]):
    merged = {"summary": [], "facts": [], "artifacts": []}
    for item in results:
        if "summary" in item:
            merged["summary"].append(item["summary"])
        if "facts" in item:
            merged["facts"].extend(item["facts"])
        if "files" in item:
            merged["artifacts"].extend(item["files"])
    return merged
