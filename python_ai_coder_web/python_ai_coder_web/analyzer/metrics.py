import numpy as np

def analyze_code(code: str) -> dict:
    lines = code.strip().split('\n')
    line_lengths = np.array([len(line) for line in lines if line.strip()])
    return {
        'total_lines': len(lines),
        'avg_line_length': round(np.mean(line_lengths), 2) if line_lengths.size > 0 else 0,
        'max_line_length': int(np.max(line_lengths)) if line_lengths.size > 0 else 0
    }
