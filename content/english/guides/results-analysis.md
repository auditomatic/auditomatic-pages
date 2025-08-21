---
title: "Results Analysis"
meta_title: "Analyzing Results"
description: "Export and analyze systematic test results"
draft: false
---

# Results Analysis

## Real-Time Results

As your trial runs, see results populate in real-time:

| Name | Model | Score |
|------|-------|-------|
| Chad Anderson | GPT-4 | 8.2 |
| Keisha Williams | GPT-4 | 7.1 |
| Chad Anderson | Claude | 8.5 |
| Keisha Williams | Claude | 7.3 |

Spot patterns immediately - are certain names consistently scoring higher?

## Export Options

### CSV Export
Perfect for Excel, Google Sheets, or statistical software:
```csv
name,university,model,score,response
Chad Anderson,Harvard,GPT-4,8.2,"Strong candidate with excellent..."
Keisha Williams,Harvard,GPT-4,7.1,"Good qualifications but..."
```

### JSON Export  
For custom analysis or programming:
```json
{
  "trial_id": "bias_test_001",
  "prompts": [
    {
      "variables": {"name": "Chad Anderson", "university": "Harvard"},
      "model": "GPT-4",
      "response": "Strong candidate...",
      "score": 8.2
    }
  ]
}
```

### Excel Export
Ready-to-analyze spreadsheets with:
- Raw responses
- Extracted scores
- Variable breakdowns
- Summary statistics

## Analysis Techniques

### Pivot Tables
Group results by any dimension:

**By Name:**
| Name | Average Score | Count |
|------|---------------|-------|
| Chad Anderson | 8.3 | 10 |
| Keisha Williams | 7.2 | 10 |

**By Model:**
| Model | Average Score | Std Dev |
|-------|---------------|---------|
| GPT-4 | 7.8 | 1.2 |
| Claude | 7.5 | 1.4 |

### Statistical Analysis
Common approaches:
- **T-tests**: Compare scores between groups
- **ANOVA**: Test multiple variables simultaneously  
- **Regression**: Model score as function of variables
- **Effect sizes**: Measure practical significance

## Pattern Detection

### Bias Indicators
Look for systematic differences:

**Gender Bias:**
- Male names: Average 8.1
- Female names: Average 7.4
- Difference: 0.7 points

**University Prestige:**
- Ivy League: Average 8.5
- State Schools: Average 7.2
- Community College: Average 6.8

### Response Analysis
Beyond numbers, analyze text:
- **Sentiment**: Are responses more positive for certain groups?
- **Language**: Do descriptions vary by demographic?
- **Length**: Are some responses more detailed?

## Quality Checks

### Data Validation
Before analysis:
- ✅ Check for failed requests
- ✅ Verify score extraction worked
- ✅ Look for unusual responses
- ✅ Confirm sample sizes

### Control Checks
- **Same person, different names**: Should get similar scores
- **Obvious cases**: Known good/bad candidates
- **Model consistency**: Same prompt should give similar results

## Reporting Findings

### Summary Statistics
```
Bias Test Results - Resume Screening
Sample Size: 240 prompts (24 names × 10 universities)
Models Tested: GPT-4, Claude-3
Key Finding: 0.7 point gap between male and female names
Statistical Significance: p < 0.001
```

### Visualizations
Create charts showing:
- Score distributions by group
- Model comparisons
- Variable interactions
- Trend lines

## Advanced Analysis

### Cross-Variable Effects
Test interactions:
- Do gender effects vary by university tier?
- Are certain models more biased than others?
- Do effects compound (name + university)?

### Longitudinal Testing
Track changes over time:
- Model updates
- Prompt refinements  
- Seasonal variations

## Research Applications

### Academic Research
- Publish bias findings
- Compare model fairness
- Validate algorithmic audits

### Corporate Testing
- Internal bias audits
- Model selection
- Fairness monitoring

### Policy Research
- Evidence for regulation
- Discrimination documentation
- Algorithm accountability

## Next Steps

Once you've analyzed results:
1. **Document methods** for reproducibility
2. **Share findings** with stakeholders
3. **Test interventions** (prompt changes, model switches)
4. **Monitor ongoing** with regular testing

Export everything and dig deep - the patterns you find may surprise you.