#!/usr/bin/env python3

# Deterministic calculation: 7607637697 * 30mg
result_mg = 7607637697 * 30
print(f"7607637697 * 30 = {result_mg} mg")

# Convert mg to other units
result_g = result_mg / 1000
result_kg = result_g / 1000
result_tons = result_kg / 1000

print(f"\nConversions:")
print(f"{result_mg:,} mg")
print(f"{result_g:,} g")
print(f"{result_kg:,} kg")
print(f"{result_tons:,} tons")