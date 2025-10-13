> Kedro 1.x (pin ≥1.0), kedro-datasets 3.x (pin). Updated: 2025-10-01  
> Policy level: MUST unless changed via CR.

## Short Context
- Goal: Consistent Kedro usage across projects.
- Pipelines via CLI; nodes are pure, typed; multiple outputs allowed but keep them minimal and named.
- Prefer file-backed datasets; pin dataset class names to installed `kedro-datasets`.
- Group parameters by domain; avoid catch-all `parameters` unless necessary.
- Keep requirements minimal and pinned.
- Environments: `conf/base` for shared defaults, `conf/local` for machine-specific secrets (not committed).
- Acceptance on tasks: 0 critical/high defects; ≥95% checklist pass; deviations logged.

## [SECTION:CONVENTIONS]
1) Naming: snake_case for datasets, nodes, parameters, pipelines.  
2) Datasets: use `Dataset` (not `DataSet`). Prefer explicit types (e.g., `pandas.CSVDataset`).  
3) Nodes: pure functions; inputs/outputs declared; side-effects only via catalog datasets.  
4) Pipelines: small, cohesive; compose in `__default__` as needed.  
5) Code style: type hints, docstrings; keep modules small and focused.

## [SECTION:WORKFLOW]
1) To create a new Kedro project, use only this command: `kedro new --name <PROJ> --tools=none --example=no`  
2) Create pipeline(s): `kedro pipeline create <PIPE>`  
3) Add nodes in Python, wire IO in `conf/base/catalog.yml`.  
4) Params in `conf/base/parameters*.yml` (grouped by pipeline).  
5) Commit small, reviewable diffs; document deviations.

## [SECTION:CATALOG]
1) Prefer explicit, file-backed datasets; keep paths relative to project root.  
2) Versioning: use dataset-level versioning if needed; document rationale.  
3) Resolve class names from installed `kedro-datasets`; keep extras pinned.
4) Use **dataset factories** for groups of datasets with similar type/config to reduce repetition.

Example:
```yaml
raw_sales:
  type: pandas.CSVDataset
  filepath: data/01_raw/sales.csv
```

Factory example:
```yaml
"{name}_data":
  type: pandas.CSVDataset
  filepath: data/01_raw/{name}_data.csv
```
This single entry resolves any dataset named `factory_data`, `process_data`, etc.

## [SECTION:PARAMS]
1) Group into files by domain (e.g., `training.yml`, `features.yml`).  
2) Keep constants inline in code unless schema must be externalised.  
3) Avoid overloading `parameters`; use namespaced groups.

Skeleton:
```yaml
training:
  test_size: 0.2
  random_state: 42
```

## [SECTION:PIPELINES_NODES]
Node skeleton:
```python
def clean_sales(raw: "pandas.DataFrame") -> "pandas.DataFrame":
    """Pure transform; no IO."""
    # ...
    return df
```
Wire in pipeline factory; keep outputs minimal but named.

## [SECTION:CONFIG_ENVIRONMENTS]
- `conf/base`: shared defaults.  
- `conf/local`: secrets/paths per machine; git-ignored.  
- Use `--env <ENV>` only when teams truly need variants; document differences.

## [SECTION:TESTS_QA]
- Unit tests for node logic; smoke test pipeline graph construction.  
- Lint/type-check as CI gates.  
- Acceptance: 0 critical/high; ≥95% checklist pass.

## [SECTION:CHECKLIST]
- [ ] Pipelines created via CLI
- [ ] Nodes pure & typed
- [ ] Catalog explicit & pinned
- [ ] Params grouped
- [ ] Reqs minimal & pinned
- [ ] Deviations documented

## [SECTION:TEMPLATES]
Requirements (minimal):
```
kedro>=1.0,<2
kedro-datasets[pandas]>=3,<4
pandas>=2.0,<3
```
