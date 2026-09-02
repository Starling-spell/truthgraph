# TruthGraph

TruthGraph is a reusable GenLayer Intelligent Contract that turns uncertain external information into versioned, auditable knowledge claims. Validators independently reconstruct five proof lanes—source, identity, temporal, semantic, and contradiction—and consensus binds the complete vector and score before a claim becomes `VERIFIED`.

Claims and proof records are versioned. Failed evaluations do not destroy a claim, and new versions preserve the prior history. The contract stores bounded proof packets, not free-form validator narratives.

## Flow

`submit_claim` → `evaluate` (validator consensus) → `VERIFIED`/`REJECTED` → `new_version`.

## Checks

```powershell
genvm-lint check contracts/TruthGraph.py
python tools/static_checks.py
```
