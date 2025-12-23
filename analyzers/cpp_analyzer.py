import subprocess
import os
import re
from lizard import get_reader_for


def analyze_cpp_file(path):
    """Analyze C++ file using lizard for complexity + clang-tidy + cppcheck."""
    with open(path, "r") as f:
        code = f.read()

    loc = len(code.splitlines())
    
    # Extract cyclomatic complexity using lizard
    cyclomatic_total, cyclomatic_avg, num_functions, avg_func_len = _get_complexity_lizard(path)

    clang_tidy_warnings = _run_clang_tidy(path)
    cppcheck_issues = _run_cppcheck(path)

    # Additional simple lexical features
    comment_lines = len([l for l in code.splitlines() if l.strip().startswith("//") or l.strip().startswith("/*") or l.strip().endswith("*/")])
    comment_density = comment_lines / max(1, loc)

    tokens = re.findall(r"\w+", code)
    token_count = len(tokens)
    avg_token_len = (sum(len(t) for t in tokens) / token_count) if token_count else 0

    include_count = len(re.findall(r"^\s*#include", code, re.MULTILINE))
    todo_count = len(re.findall(r"TODO|FIXME", code))
    
    # Code quality patterns (bad practices detection)
    global_vars = len(re.findall(r"^(static\s+)?\w+\s+\w+\s*[=;]", code, re.MULTILINE))
    deep_nesting = len(re.findall(r"if.*if.*if", code))  # 3+ nested ifs
    memory_issues = len(re.findall(r"new\s+|delete\s+", code))  # Dynamic memory
    unsafe_patterns = len(re.findall(r"gets\s*\(|scanf|strcpy|strcat", code))  # Unsafe functions
    code_quality_issues = global_vars + deep_nesting + memory_issues + unsafe_patterns

    return {
        "loc": loc,
        "cyclomatic_total": cyclomatic_total,
        "cyclomatic_avg": cyclomatic_avg,
        "num_functions": num_functions,
        "avg_func_len": avg_func_len,
        "clang_tidy_warnings": clang_tidy_warnings,
        "cppcheck_num_issues": cppcheck_issues,
        "comment_density": comment_density,
        "token_count": token_count,
        "avg_token_len": avg_token_len,
        "include_count": include_count,
        "todo_count": todo_count,
        "code_quality_issues": code_quality_issues,
    }


def _get_complexity_lizard(path):
    """Use lizard to extract cyclomatic complexity."""
    try:
        reader = get_reader_for(path)
        if reader:
            file_reader = reader(open(path))
            total = 0
            count = 0
            total_len = 0
            for func in file_reader.function_list:
                total += func.cyclomatic_complexity
                count += 1
                # lizard's function object has 'length' (lines) or 'nloc'
                length = getattr(func, 'length', None) or getattr(func, 'nloc', None) or 0
                try:
                    total_len += int(length)
                except Exception:
                    total_len += 0
        
            if count > 0:
                avg = total / count
                avg_len = total_len / count if count > 0 else 0
                return float(total), float(avg), int(count), float(avg_len)
    except Exception as e:
        pass
    
    # Fallback: count control flow keywords as complexity heuristic
    with open(path, "r") as f:
        code = f.read()
    
    complexity = (
        code.count("if") + code.count("for") + code.count("while") +
        code.count("switch") + code.count("case") +
        code.count("&&") + code.count("||") +
        code.count("?") + code.count("catch")
    )
    funcs = max(1, code.count("{"))
    return float(complexity), float(complexity / funcs), 0, 0.0


def _run_clang_tidy(path):
    """Run clang-tidy and count warnings."""
    try:
        result = subprocess.run(
            ["clang-tidy", path],
            capture_output=True,
            text=True,
            timeout=5
        )
        # Count lines with "warning:" in output
        return len([line for line in result.stdout.split("\n") if "warning:" in line])
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return 0


def _run_cppcheck(path):
    """Run cppcheck and count issues."""
    try:
        result = subprocess.run(
            ["cppcheck", "--quiet", path],
            capture_output=True,
            text=True,
            timeout=5
        )
        # Count lines with error/warning
        lines = [line for line in result.stdout.split("\n") if ":" in line and line.strip()]
        return len(lines)
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return 0
