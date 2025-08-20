---
title: "Prompt Templates"
meta_title: "Creating Prompt Templates"
description: "How to create effective prompt templates in Auditomatic Lite"
draft: false
---

# Prompt Templates

## What are Prompt Templates?

Prompt templates allow you to create reusable prompts with variable placeholders that can be systematically tested with different inputs.

## Creating Templates

Use curly braces to define variables:

```
Hello {name}, please analyze this {topic} and provide your thoughts.
```

## Variable Types

- **Simple**: `{name}` - Direct text replacement
- **Attributed**: Variables with metadata for analysis
- **Conditional**: Logic-based variable insertion

## Best Practices

1. Keep variables clearly named
2. Use consistent naming conventions
3. Test with diverse input sets
4. Consider edge cases

## Examples

### Bias Testing
```
Rate the job candidate {name} for the position of {role}.
```

### Capability Testing
```
Solve this {difficulty} math problem: {problem}
```