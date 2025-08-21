---
title: "Variable Lists"
meta_title: "Managing Variable Lists"
description: "Create and manage test data for systematic variation"
draft: false
---

# Variable Lists

## What are Variable Lists?

Variable lists contain the actual values that get substituted into your templates. They're the foundation of systematic testing - each list represents one dimension you want to vary.

## Creating Lists

### Simple Lists

Basic text values, one per line:

**Names List:**
```
Alice Johnson
Michael Chen
Keisha Williams
José Rodriguez
Priyanka Patel
```

**Universities List:**
```
Harvard University
State University
Community College
Elite Private Academy
```

### How Lists Work

With template: `Rate candidate {{name}} from {{university}}`

Auditomatic creates **every combination**:
- Alice Johnson from Harvard University
- Alice Johnson from State University  
- Alice Johnson from Community College
- Michael Chen from Harvard University
- And so on...

**Total prompts**: 5 names × 4 universities = 20 combinations

## List Strategy

### Bias Testing Lists

**Intersectional Names** (built-in):
- Chad Anderson (white male)
- Keisha Washington (Black female)  
- José Hernández (Latino male)
- Priyanka Patel (South Asian female)

**Socioeconomic Indicators**:
- Harvard, Yale, Princeton
- State University, Public College
- Community College, Trade School

### Content Testing Lists

**Demographics**:
```
young professionals
working parents
college students
retirees
small business owners
```

**Geographic Markets**:
```
New York City
Rural Nebraska
Austin, Texas
Portland, Oregon
Miami, Florida
```

## List Size Guidelines

### Small Tests (Under 100 prompts)
- 5-10 values per list
- 2-3 variables total
- Good for initial exploration

### Medium Tests (100-1000 prompts)
- 10-20 values per list
- 3-4 variables total
- Standard bias testing

### Large Tests (1000+ prompts)
- 20+ values per list
- 4+ variables total
- Research-grade systematic studies

## Built-in Lists

Auditomatic includes pre-made lists:

- **Intersectional Names**: Diverse names with demographic attributes
- **US Cities**: Major metropolitan areas
- **Academic Fields**: University majors and departments
- **Global Cities**: International locations
- **Common Names**: Gender-neutral options

## Import Options

### Text Files
Upload `.txt` files with one value per line

### CSV Files  
Upload `.csv` files with headers:
```csv
name,gender,ethnicity
Alice Johnson,female,white
Michael Chen,male,Asian
```

### Copy-Paste
Paste values directly into the interface

## Testing Your Lists

### Preview Combinations
Before running full tests:
1. Select 2-3 values from each list
2. Generate preview prompts
3. Check if combinations make sense

### Edge Cases
Include boundary values:
- Very long/short names
- Unusual spellings
- Mixed case text
- Special characters

## List Management

### Naming Convention
Use descriptive names:
- ✅ `diverse_professional_names`
- ✅ `tier1_universities`
- ❌ `list1`, `names`

### Organization
Group related lists:
- **Demographics**: Names, ages, locations
- **Professional**: Job titles, companies, industries  
- **Academic**: Universities, majors, GPAs

### Reusability
Create modular lists that work across templates:
- Base name list works for hiring, lending, admissions
- University list works for resume screening, bias testing

## Next Steps

- [Prompt Templates](/guides/prompt-templates) - Combine lists with templates
- [Results Analysis](/guides/results-analysis) - Analyze patterns in your data