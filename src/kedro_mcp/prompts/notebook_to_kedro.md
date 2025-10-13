# 🤖 AI ASSISTANT INSTRUCTIONS - SOW-DRIVEN CONVERSION

> **CRITICAL**: These instructions create a Statement of Work (SOW) approach for reliable notebook conversion

## 🎯 NOTEBOOK TO KEDRO CONVERSION - SOW ENFORCEMENT

### 🚨 CORE PRINCIPLE: CREATE SOW → GET APPROVAL → DELIVER EXACTLY

The conversion plan functions as a **Statement of Work** with specific deliverables and acceptance criteria.

---

## 6-STEP SOW WORKFLOW

#### ✅ STEP 1: ANALYZE & CREATE STATEMENT OF WORK
**ANNOUNCE:** "Step 1: Creating detailed conversion plan..."

### 📋 PLAN OUTPUTS (TERMINAL + FILE)
When analyzing notebook, produce **two** artifacts:

1) **Executive Summary (Terminal)** - print readable overview:
```
Conversion Plan Summary:
Pipelines (X): [list names with key transformations]
Datasets (Y): [input/intermediate/output with types]
Parameters: [configuration groups identified]
Dependencies: [only actual imports found]
```

2) **Detailed Statement of Work (File)** - comprehensive deliverable specification:
```
<project-root>/<project-name>-YYYY-MM-DD_HHMM_conversion-plan.md
```

### 🔍 SOW ANALYSIS REQUIREMENTS

**DEPENDENCY ANALYSIS - SCAN ACTUAL IMPORTS:**
```python
# VALIDATION CHECKLIST - Scan every cell for:
import pandas as pd          ✓ → kedro-datasets[pandas] 
import matplotlib.pyplot     ✓ → kedro-datasets[matplotlib]
from sklearn import model   ✓ → scikit-learn
import plotly.express        ✓ → kedro-datasets[plotly]
import seaborn              ✓ → seaborn
# Mark each ✓/✗ - NO package added without explicit import found
```

**PARAMETER DECISION FRAMEWORK:**
For each hardcoded value in the notebook, evaluate:

**✅ SHOULD BE CONFIGURABLE** (users will likely experiment with):
- **Experimentation values**: Learning rates, model hyperparameters, feature thresholds
- **Business logic**: Confidence thresholds, approval limits, scoring cutoffs
- **Data processing**: Batch sizes, outlier detection limits, sampling ratios
- **Feature engineering**: Correlation thresholds, scaling parameters, binning criteria
- **Model training**: Train/test splits, cross-validation folds, regularization parameters

**❌ KEEP HARDCODED** (structural constants unlikely to change):
- **Data schema**: Column names, expected data types, table structures
- **Mathematical constants**: PI, e, conversion factors, statistical distributions
- **Business rules fixed by regulation**: Tax rates, compliance thresholds (if legally mandated)
- **String literals**: Error messages, log statements, display text
- **System constraints**: File extensions, API endpoints (if fixed), standard formats
- **Date/time formats**: Standard format strings like '%H:%M:%S'

**DECISION CRITERIA QUESTIONS:**
For each hardcoded value, ask:
1. "Would a data scientist want to experiment with this value?"
2. "Does this value change based on business conditions or model performance?"
3. "Would different datasets or use cases require different values?"
4. "Is this value likely to be tuned during model development?"

If YES to any question → Make it configurable
If NO to all questions → Keep hardcoded

**PARAMETER USAGE METHODS:**
1. **Individual parameters**: `"params:parameter_name"` for single values
2. **Parameter groups**: `"params:group_name"` for related sets (PREFERRED)
3. **All parameters**: `"parameters"` only when function needs many unrelated params

### 📄 STATEMENT OF WORK STRUCTURE

**SOW must include numbered deliverables (NO implementation guidance):**

```markdown
# KEDRO CONVERSION - STATEMENT OF WORK
## PROJECT DELIVERABLES

### DELIVERABLE 1: PIPELINE IMPLEMENTATION
1.1 data_processing pipeline
    - Task 1.1.1: load_raw_data() → outputs: raw_table
    - Task 1.1.2: clean_data(raw_table, params:data_params) → outputs: cleaned_table  
    - Task 1.1.3: validate_data(cleaned_table) → outputs: valid_table
    
1.2 feature_engineering pipeline  
    - Task 1.2.1: build_features(valid_table, params:feature_flags) → outputs: features
    - Task 1.2.2: join_features(features, external_lookup) → outputs: feature_set

1.3 model_training pipeline
    - Task 1.3.1: split_data(feature_set, params:split_params) → outputs: train_X, train_y, test_X, test_y
    - Task 1.3.2: train_model(train_X, train_y, params:model_params) → outputs: model
    - Task 1.3.3: evaluate_model(model, test_X, test_y) → outputs: metrics

### DELIVERABLE 2: DATA CATALOG CONFIGURATION
2.1 raw_table → pandas.CSVDataset (filepath: data/01_raw/raw_sales_data.csv)
2.2 cleaned_table → pandas.ParquetDataset (filepath: data/02_intermediate/cleaned_sales.parquet)
2.3 valid_table → pandas.ParquetDataset (filepath: data/03_primary/valid_sales.parquet)
2.4 features → pandas.ParquetDataset (filepath: data/04_feature/features.parquet)
2.5 feature_set → pandas.ParquetDataset (filepath: data/04_feature/feature_set.parquet)
2.6 train_X → pandas.ParquetDataset (filepath: data/05_model_input/train_X.parquet)
2.7 train_y → pandas.ParquetDataset (filepath: data/05_model_input/train_y.parquet)
2.8 test_X → pandas.ParquetDataset (filepath: data/05_model_input/test_X.parquet)
2.9 test_y → pandas.ParquetDataset (filepath: data/05_model_input/test_y.parquet)
2.10 model → pickle.PickleDataset (filepath: data/06_models/model.pkl)
2.11 metrics → json.JSONDataset (filepath: data/08_reporting/metrics.json)

### DELIVERABLE 3: PARAMETER CONFIGURATION
3.1 data_params group: outlier_threshold, min_samples, batch_size
3.2 feature_flags group: use_scaling, use_ohe, correlation_threshold
3.3 split_params group: test_size, random_state
3.4 model_params group: learning_rate, n_estimators, max_depth, random_state

### DELIVERABLE 4: VISUALIZATION OUTPUTS
4.1 sales_trend_plot → matplotlib.MatplotlibDataset → data/08_reporting/sales_trend.png
4.2 feature_importance → plotly.JSONDataset → data/08_reporting/feature_importance.html
4.3 model_performance → matplotlib.MatplotlibDataset → data/08_reporting/model_performance.png

### DELIVERABLE 5: DEPENDENCY SPECIFICATIONS
5.1 kedro-datasets[pandas] (RATIONALE: import pandas found in cell X)
5.2 kedro-datasets[matplotlib] (RATIONALE: import matplotlib found in cell Y)
5.3 scikit-learn (RATIONALE: from sklearn import found in cell Z)

TOTAL DELIVERABLES: X pipelines, Y tasks, Z datasets, W parameters, V visualizations, U dependencies
```

### 🔧 TECHNICAL IMPLEMENTATION STANDARDS

**NODE IMPLEMENTATION REQUIREMENTS:**
- Pure functions only (no side effects)
- Multiple inputs allowed, **exactly ONE output** per node
- Clear type hints required
- Use specific parameter references (params:group_name preferred)

**PARAMETER USAGE STANDARDS:**
```python
# ✅ PREFERRED - Parameter groups
inputs=["data", "params:model_params"]
inputs=["features", "params:data_params"] 

# ✅ ACCEPTABLE - Individual parameters
inputs=["data", "params:learning_rate"]

# ❌ USE SPARINGLY - Whole parameters (only if many unrelated params needed)
inputs=["data", "parameters"]
```

**PIPELINE CREATION STANDARDS:**
- Use `kedro pipeline create <name>` CLI only (never manual folder creation)
- Run all `kedro` CLI commands from within an existing Kedro project directory, except for the `kedro new` command
- Follow standard Kedro project structure:  
  - Define all node functions in `nodes.py`.  
  - Create pipelines with these nodes in `pipeline.py`.
- Register all pipelines in pipeline_registry.py

**DATA ORGANIZATION STANDARDS:**
```
data/01_raw/          # Original input files
data/02_intermediate/ # Cleaned, processed data
data/03_primary/      # Business logic datasets  
data/04_feature/      # Feature engineering outputs
data/05_model_input/  # Model training ready
data/06_models/       # Trained models
data/07_model_output/ # Predictions, results
data/08_reporting/    # Visualizations, reports
```

**DATASET TYPE STANDARDS:**
- Use Kedro 1.0+ dataset names only
- Correct casing: pandas.CSVDataset (not CSVDataSet)
- Match dataset type to use case (see reference table)

#### ✅ STEP 2: SOW APPROVAL & SIGN-OFF
**ANNOUNCE:** "Step 2: Plan approval required..."

**USER-FRIENDLY APPROVAL:**
```
Detailed conversion plan saved to ./YYYY-MM-DD_HHMM_conversion-plan.md
Type "details" to review the full plan here.

PLAN OVERVIEW:
- Deliverable 1: X pipelines with Y total tasks  
- Deliverable 2: Z datasets with proper types
- Deliverable 3: W parameter groups 
- Deliverable 4: V visualization outputs
- Deliverable 5: U dependencies (with justification)

Proceed to implement this plan? (yes/no)
```

**APPROVAL RULES:**
- If **yes** → SOW approved, proceed to implementation
- If **no** → Revise plan based on feedback
- If **details** → Show full SOW, ask again
- **NO IMPLEMENTATION until explicit approval**

#### ✅ STEP 3: PROJECT SETUP
**ANNOUNCE:** "Step 3: Setting up project structure..."

```bash
kedro new --name <project_name> --tools data,lint,test --example n --telemetry no
```
**ALWAYS include 'data' tool for folder structure**

#### ✅ STEP 4: SOW IMPLEMENTATION WITH PROGRESS TRACKING
**ANNOUNCE:** "Step 4: Implementing approved plan with progress updates..."

### 📊 DELIVERABLE TRACKING

**Progress dashboard (update after each milestone):**
```
📋 PROJECT PROGRESS:

DELIVERABLE 1 - PIPELINE IMPLEMENTATION:
□ Pipeline 1.1 (data_processing): CREATED ✓/✗  
  □ Task 1.1.1 (load_raw_data): COMPLETED ✓/✗
  □ Task 1.1.2 (clean_data): COMPLETED ✓/✗  
  □ Task 1.1.3 (validate_data): COMPLETED ✓/✗
□ Pipeline 1.2 (feature_engineering): CREATED ✓/✗
  □ Task 1.2.1 (build_features): COMPLETED ✓/✗
  □ Task 1.2.2 (join_features): COMPLETED ✓/✗

DELIVERABLE 2 - DATA CATALOG:
□ Item 2.1 (raw_table): CONFIGURED ✓/✗
□ Item 2.2 (cleaned_table): CONFIGURED ✓/✗  
□ Item 2.3 (valid_table): CONFIGURED ✓/✗

DELIVERABLE 3 - PARAMETER CONFIGURATION:
□ Item 3.1 (data_params): CREATED ✓/✗
□ Item 3.2 (feature_flags): CREATED ✓/✗

DELIVERABLE 4 - VISUALIZATIONS:
□ Item 4.1 (sales_trend_plot): CONFIGURED ✓/✗
□ Item 4.2 (feature_importance): CONFIGURED ✓/✗

COMPLETION STATUS: [X/TOTAL] deliverables finished
```

### 📊 IMPLEMENTATION PHASES

**Phase A: Pipeline Structure Setup**
```bash
# Create each pipeline using CLI only
kedro pipeline create data_processing    # Deliverable 1.1
kedro pipeline create feature_engineering # Deliverable 1.2
kedro pipeline create model_training     # Deliverable 1.3

# VALIDATION: Verify all planned pipelines exist
ls src/<project>/pipelines/
```

**Phase B: Task Implementation** 
- Complete each numbered task from Deliverable 1
- Follow technical implementation standards
- Cross-reference: Task outputs match Deliverable 2 dataset names
- Update progress after each pipeline completion

**Phase C: Data Catalog Setup**
- Configure each dataset from Deliverable 2
- Use exact Kedro 1.0+ dataset types specified
- Verify filepaths match specifications
- Ensure correct naming conventions

**Phase D: Parameter Configuration**
- Create parameter groups from Deliverable 3 using decision framework
- Structure parameters.yml with proper grouping
- Validate all specified parameters present
- Verify parameter references in tasks

**MILESTONE CHECKPOINTS:**
```
⚠️  MILESTONE REVIEW:
Deliverable [X] Status: [Y/Z] items completed
Any incomplete items? → Complete before proceeding
All items finished? → Move to next deliverable
```

#### ✅ STEP 5: PRE-DELIVERY QUALITY ASSURANCE
**ANNOUNCE:** "Step 5: Quality assurance review before testing..."

**COMPREHENSIVE QA REVIEW:**
```
🔍 QUALITY ASSURANCE CHECKLIST:

DELIVERABLE 1 REVIEW - PIPELINE IMPLEMENTATION:
✓ Pipeline count: [actual] vs [planned] → MATCH/MISMATCH
✓ Task count: [actual] vs [planned] → MATCH/MISMATCH  
✓ Task names: All match specifications → YES/NO
✓ Parameter usage: Uses technical standards → YES/NO
✓ Single outputs: All tasks have exactly one output → YES/NO

DELIVERABLE 2 REVIEW - DATA CATALOG:
✓ Dataset count: [actual] vs [planned] → MATCH/MISMATCH
✓ Dataset types: All use Kedro 1.0+ names → YES/NO
✓ Type casing: Correct format (pandas.CSVDataset) → YES/NO
✓ File paths: All match specifications → YES/NO
✓ Folder structure: Follows data organization standards → YES/NO

DELIVERABLE 3 REVIEW - PARAMETER CONFIGURATION:
✓ Parameter groups: [actual] vs [planned] → MATCH/MISMATCH  
✓ Parameter keys: All specified keys present → YES/NO
✓ Decision quality: Parameters follow decision framework → YES/NO
✓ Usage: Tasks reference parameters correctly → YES/NO

DELIVERABLE 4 REVIEW - VISUALIZATIONS:
✓ Visualization count: [actual] vs [planned] → MATCH/MISMATCH
✓ Output types: Correct dataset types → YES/NO
✓ File paths: All match specifications → YES/NO

DELIVERABLE 5 REVIEW - DEPENDENCIES:
✓ Dependency count: [actual] vs [planned] → MATCH/MISMATCH
✓ Package list: Exactly matches plan → YES/NO
✓ No extras: Zero unauthorized additions → YES/NO

QUALITY SCORE: [X/TOTAL] = [percentage]%

🚨 REQUIREMENT: 100% quality score before delivery
Any issues found? → Fix and re-review
Perfect score? → Ready for final testing
```

#### ✅ STEP 6: FINAL DELIVERY & ACCEPTANCE
**ANNOUNCE:** "Step 6: Final delivery testing..."

**DELIVERY TESTING:**
1. **Pre-test confirmation**: "Implementation complete and QA passed. Test the full pipeline? (yes/no)"
2. **Wait for approval** before testing
3. **Execute delivery test**: `kedro run`
4. **Validate deliverables**

**ACCEPTANCE CRITERIA:**
```
🎯 DELIVERY ACCEPTANCE TEST:

FUNCTIONALITY VERIFICATION:
□ All planned pipelines executed successfully: ✓/✗
□ All specified datasets created in correct locations: ✓/✗  
□ All visualization outputs generated: ✓/✗
□ No execution errors: ✓/✗
□ Data flows correctly through all pipelines: ✓/✗

DELIVERABLE VERIFICATION:
[For each Deliverable 2 item]:
□ Item 2.1 (raw_table): FILE EXISTS at specified location ✓/✗
□ Item 2.2 (cleaned_table): FILE EXISTS at specified location ✓/✗
□ Item 2.10 (model): FILE EXISTS at specified location ✓/✗

[For each Deliverable 4 item]:  
□ Item 4.1 (sales_trend_plot): VISUALIZATION EXISTS ✓/✗
□ Item 4.2 (feature_importance): VISUALIZATION EXISTS ✓/✗

PROJECT ACCEPTANCE: [X/TOTAL] criteria met
```

**SUCCESS CRITERIA:**
- [ ] 100% SOW deliverables completed
- [ ] `kedro run` executes successfully  
- [ ] All specified outputs generated and verified
- [ ] Zero deviations from approved plan

---

## 🚫 PROJECT VIOLATIONS - ZERO TOLERANCE

### SOW Compliance Issues
- ❌ **Any deviation** from approved SOW without change order
- ❌ **Skip any numbered deliverable** 
- ❌ **Multiple outputs from single task** (violates technical standards)
- ❌ **Wrong dataset types** (must use specified Kedro 1.0+ types)

### Implementation Standard Violations
- ❌ **Manual pipeline creation** (must use `kedro pipeline create`)
- ❌ **Incorrect parameter usage** (must follow technical standards)
- ❌ **Functions with side effects** (violates pure function standard)
- ❌ **Wrong dataset naming** (CSVDataSet vs CSVDataset)

### Parameter Decision Violations
- ❌ **Make structural constants configurable** (column names, schema definitions)
- ❌ **Leave obvious experiment values hardcoded** (learning rates, thresholds)
- ❌ **Ignore decision framework** when classifying parameters

### Quality Violations
- ❌ **Proceed with <100% QA score**
- ❌ **Skip milestone checkpoints**
- ❌ **Ignore specification mismatches**

---

## 📚 IMPLEMENTATION REFERENCE

### Kedro 1.0+ Dataset Specifications (Deliverable 2)
| Data Type | Kedro 1.0+ Dataset | Use Case | SOW Reference |
|-----------|-------------------|----------|---------------|
| CSV files | `pandas.CSVDataset` | Raw input data | Item 2.1 |
| Parquet files | `pandas.ParquetDataset` | Processed data | Items 2.2-2.9 |
| Static plots | `matplotlib.MatplotlibDataset` | PNG visualizations | Item 4.1 |
| Interactive plots | `plotly.JSONDataset` | HTML charts | Item 4.2 |
| JSON data | `json.JSONDataset` | Metadata, results | Item 2.11 |
| Pickle files | `pickle.PickleDataset` | Models | Item 2.10 |

### Parameter Decision Examples
```
✅ MAKE CONFIGURABLE:
- learning_rate = 0.01 (experimentation value)
- confidence_threshold = 0.8 (business logic tuning)
- batch_size = 32 (performance optimization)
- test_size = 0.2 (data splitting experimentation)

❌ KEEP HARDCODED:
- column_names = ["age", "income"] (data schema)
- PI = 3.14159 (mathematical constant)
- "Model training complete" (display message)
- file_extension = ".csv" (system constraint)
```

---

*SOW-driven implementation - Reliable delivery guaranteed*
