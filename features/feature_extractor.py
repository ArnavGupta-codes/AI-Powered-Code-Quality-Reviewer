import numpy as np

COMMON_FEATURES = [
    "loc",
    "cyclomatic_avg",
    "cyclomatic_per_func",
    "num_functions",
    "avg_func_len",
    "issue_density",
    "comment_density",
    "token_count",
    "avg_token_len",
    "include_count",
    "todo_count",
]

def to_common_features(lang: str, metrics: dict) -> np.ndarray:
    # Map language-specific keys to common ones
    if lang == "python":
        loc = metrics.get("loc", 0)
        return np.array([
            loc / max(1, 100),
            metrics.get("cyclomatic_avg", 0),
            metrics.get("cyclomatic_avg", 0),  # approximate per-func
            metrics.get("num_functions", 0) / max(1, 10),
            metrics.get("avg_func_len", 0) / max(1, 100),
            (metrics.get("pylint_num_issues", 0) + metrics.get("bandit_num_issues", 0)) / max(1, loc),
            metrics.get("comment_density", 0),
            metrics.get("token_count", 0) / max(1, 500),
            metrics.get("avg_token_len", 0) / max(1, 20),
            0,
            0,
        ], dtype=float)
    elif lang == "cpp":
        loc = metrics.get("loc", 0)
        warnings = metrics.get("clang_tidy_warnings", 0)
        issues = metrics.get("cppcheck_num_issues", 0)
        cyclomatic_avg = metrics.get("cyclomatic_avg", 0)
        cyclomatic_total = metrics.get("cyclomatic_total", 0)
        num_funcs = metrics.get("num_functions", 0)
        avg_func_len = metrics.get("avg_func_len", 0)
        comment_density = metrics.get("comment_density", 0)
        token_count = metrics.get("token_count", 0)
        avg_token_len = metrics.get("avg_token_len", 0)
        include_count = metrics.get("include_count", 0)
        todo_count = metrics.get("todo_count", 0)
        code_quality_issues = metrics.get("code_quality_issues", 0)

        # features with code quality issues added
        return np.array([
            loc / max(1, 100),
            cyclomatic_avg,
            (cyclomatic_total / max(1, num_funcs)) if num_funcs else cyclomatic_avg,
            num_funcs / max(1, 10),
            avg_func_len / max(1, 100),
            (warnings + issues + code_quality_issues) / max(1, loc),  # Combined issue density
            comment_density,
            token_count / max(1, 500),
            avg_token_len / max(1, 20),
            include_count / max(1, 10),
            code_quality_issues / max(1, 5),  # Normalized code quality issues
        ], dtype=float)
    elif lang == "java":
        loc = metrics.get("loc", 0)
        checkstyle = metrics.get("checkstyle_issues", 0)
        comment_density = metrics.get("comment_density", 0)
        token_count = metrics.get("token_count", 0)
        avg_token_len = metrics.get("avg_token_len", 0)
        include_count = metrics.get("include_count", 0)
        todo_count = metrics.get("todo_count", 0)
        
        return np.array([
            loc / max(1, 100),
            metrics.get("cyclomatic_avg", 0),
            metrics.get("cyclomatic_total", 0) / max(1, metrics.get("num_functions", 1)),
            metrics.get("num_functions", 0) / max(1, 10),
            metrics.get("avg_func_len", 0) / max(1, 100),
            checkstyle / max(1, loc),
            comment_density,
            token_count / max(1, 500),
            avg_token_len / max(1, 20),
            include_count / max(1, 10),
            todo_count / max(1, 5),
        ], dtype=float)
    else:
        raise ValueError("Unsupported language")
