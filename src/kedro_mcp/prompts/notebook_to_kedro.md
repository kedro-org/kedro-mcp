> Depends on: `kedro_general_instructions.md`. Read both.  
> Updated: 2025-09-15

## Short Context (≤300 tokens)
- Purpose: Convert a Jupyter notebook into a production-ready Kedro project.  
- Do not move data; reuse paths observed in the notebook.  
- Do not run pipelines to “verify”; produce scaffolding and config only.  
- Approval gate: complete SOW → get “APPROVED” → then implement.  
- Use CLI for scaffolding; follow general conventions.

## [SECTION:SOW] (fill before any code)
1) Goal: Convert `<NOTEBOOK>` → Kedro project `<PROJ>`.  
2) Deliverables:
   - Pipeline plan (names, nodes, inputs/outputs)
   - `conf/base/catalog.yml` skeleton
   - Parameter grouping spec
   - `README.md` summary
   - `requirements.txt` (minimal, pinned)
3) Commands to use:
   - `kedro new --name <PROJ> --tools=none --example=no`
   - `kedro pipeline create <PIPE>` (per plan)
4) Assumptions:
   - Use file paths from the notebook in catalog entries.
   - Nodes are pure; multiple outputs allowed but keep minimal & named.
   - No data downloads/uploads; no execution.
5) Change control:
   - New datasets/pipelines after approval → raise CR-N and pause.

## [SECTION:IMPLEMENTATION_STEPS]
1) Analyse notebook: extract logical steps, IO paths, parameters/constants.  
2) Propose plan: pipelines, node list, IO mapping, parameter groups.  
3) Submit SOW: return only the filled SOW; await “APPROVED”.  
4) Scaffold:
   - Run commands in SOW §3.
   - Create nodes with pure functions.
   - Add catalog entries using observed paths and resolved dataset classes.
   - Create parameters files per grouping spec.
   - Draft minimal README and requirements (from import scan).
5) Hand-off: provide diffs and checklist; record deviations.

## [SECTION:ACCEPTANCE]
- [ ] SOW approved
- [ ] Pipelines created via CLI as per plan
- [ ] Catalog skeleton present & valid
- [ ] Params grouped by domain
- [ ] README updated (project summary, how to run)
- [ ] Requirements minimal & pinned
- [ ] 0 critical/high defects; ≥95% checklist pass; deviations logged

## [SECTION:TEMPLATES]
Catalog (diff):
```diff
+ raw_sales:
+   type: pandas.CSVDataset
+   filepath: data/01_raw/sales.csv
+ clean_sales:
+   type: pandas.ParquetDataset
+   filepath: data/02_intermediate/clean_sales.parquet
```

Params skeleton:
```yaml
features:
  include: ["col_a", "col_b"]
  drop: ["id"]
training:
  test_size: 0.2
  random_state: 42
```

Node skeleton:
```python
def make_features(df: "pandas.DataFrame", params: dict) -> "pandas.DataFrame":
    # use params["features"]["include"] etc.
    return out
```

README outline:
```
# <PROJ>
Purpose, pipelines, how to run:
- kedro build-reqs
- kedro run --pipeline <PIPE>
```

## [SECTION:NOTES_FOR_AGENT]
- Fetch `kedro_general_instructions.md` (Short Context + relevant sections) before executing these steps.  
- If dataset classes differ from examples, resolve from installed `kedro-datasets` and proceed; note in deviations.  
- Do not execute the pipeline; produce scaffolding and configs only.
