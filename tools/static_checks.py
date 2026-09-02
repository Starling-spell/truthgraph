from pathlib import Path
s = Path("contracts/TruthGraph.py").read_text(encoding="utf-8")
assert s.startswith('# { "Depends": "py-genlayer:')
assert "py-genlayer:test" not in s and "py-genlayer:latest" not in s
assert "class TruthGraph" in s
print("static checks passed")
