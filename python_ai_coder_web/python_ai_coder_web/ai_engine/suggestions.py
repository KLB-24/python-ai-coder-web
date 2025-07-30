def get_suggestion(code: str) -> str:
    if "for" in code and "range" not in code:
        return "Consider using 'range()' with 'for' loops for clarity."
    if len(code.splitlines()) > 10:
        return "Consider breaking down large functions into smaller ones."
    return "Your code looks clean! No suggestions right now."
