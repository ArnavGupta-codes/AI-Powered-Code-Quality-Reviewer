import subprocess
import json
from radon.complexity import cc_visit
from radon.metrics import mi_visit

def run_pylint(path: str) -> dict:
    # JSON output with timeout
    try:
        result = subprocess.run(
            ["pylint", "--output-format=json", path],
            capture_output=True, text=True, timeout=2
        )
        try:
            messages = json.loads(result.stdout or "[]")
        except json.JSONDecodeError:
            messages = []
        return {
            "pylint_num_issues": len(messages)
        }
    except (subprocess.TimeoutExpired, FileNotFoundError):
        return {"pylint_num_issues": 0}

def run_bandit(path: str) -> dict:
    try:
        result = subprocess.run(
            ["bandit", "-q", "-f", "json", "-r", path],
            capture_output=True, text=True, timeout=2
        )
        try:
            data = json.loads(result.stdout or "{}")
            issues = data.get("results", [])
        except json.JSONDecodeError:
            issues = []
        return {
            "bandit_num_issues": len(issues)
        }
    except (subprocess.TimeoutExpired, FileNotFoundError):
        return {"bandit_num_issues": 0}

def run_radon(code: str) -> dict:
    cc_blocks = cc_visit(code)
    total_complexity = sum(b.complexity for b in cc_blocks)
    avg_complexity = total_complexity / max(len(cc_blocks), 1)
    mi = mi_visit(code, False)
    return {
        "cyclomatic_total": total_complexity,
        "cyclomatic_avg": avg_complexity,
        "maintainability_index": mi
    }

def analyze_python_file(path: str) -> dict:
    import re
    with open(path, "r", encoding="utf-8") as f:
        code = f.read()
    metrics = {}
    metrics.update(run_pylint(path))
    metrics.update(run_bandit(path))
    metrics.update(run_radon(code))
    metrics["loc"] = len(code.splitlines())
    
    # Add lexical features
    comment_lines = len([l for l in code.splitlines() if l.strip().startswith("#")])
    metrics["comment_density"] = comment_lines / max(1, metrics["loc"])
    
    tokens = re.findall(r"\w+", code)
    metrics["token_count"] = len(tokens)
    metrics["avg_token_len"] = (sum(len(t) for t in tokens) / len(tokens)) if tokens else 0
    
    metrics["include_count"] = len(re.findall(r"^\s*import", code, re.MULTILINE))
    metrics["todo_count"] = len(re.findall(r"TODO|FIXME", code))
    metrics["num_functions"] = len(re.findall(r"def\s+\w+", code))
    metrics["avg_func_len"] = 0  # placeholder
    
    return metrics
