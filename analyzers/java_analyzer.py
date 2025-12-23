def analyze_java_file(path):
    import re
    # Basic analyzer with lexical features
    with open(path, "r") as f:
        code = f.read()

    loc = len(code.splitlines())
    
    # Lexical features
    comment_lines = len([l for l in code.splitlines() if l.strip().startswith("//") or l.strip().startswith("/*") or l.strip().endswith("*/")])
    comment_density = comment_lines / max(1, loc)
    
    tokens = re.findall(r"\w+", code)
    token_count = len(tokens)
    avg_token_len = (sum(len(t) for t in tokens) / token_count) if token_count else 0
    
    import_count = len(re.findall(r"^\s*import", code, re.MULTILINE))
    todo_count = len(re.findall(r"TODO|FIXME", code))
    method_count = len(re.findall(r"\bpublic\s+\w+\s+\w+\s*\(", code))

    return {
        "loc": loc,
        "checkstyle_issues": 0,
        "comment_density": comment_density,
        "token_count": token_count,
        "avg_token_len": avg_token_len,
        "include_count": import_count,
        "todo_count": todo_count,
        "num_functions": method_count,
        "avg_func_len": 0,
        "cyclomatic_total": 0,
        "cyclomatic_avg": 0,
    }
