import pathlib

def detect_language(path: str) -> str:
    ext = pathlib.Path(path).suffix
    if ext in [".py"]:
        return "python"
    if ext in [".cpp", ".cc", ".cxx", ".hpp", ".h"]:
        return "cpp"
    if ext in [".java"]:
        return "java"
    raise ValueError("Unsupported file type")
