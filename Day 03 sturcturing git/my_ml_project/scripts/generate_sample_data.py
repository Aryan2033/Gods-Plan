#!/usr/bin/env python3
"""Generate a sample CSV with 100 records (name, age, salary).

Run from the workspace root or directly; it writes to data/processed/raw/data.csv.
"""
import csv
from random import randint, seed
from pathlib import Path


def generate_rows(n=100, seed_value=42):
    seed(seed_value)
    for i in range(1, n + 1):
        name = f"Person{i:03d} Last{i:03d}"
        age = randint(20, 65)
        salary = randint(30000, 150000)
        yield (name, age, salary)


def main():
    out = Path("data/processed/raw/data.csv")
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["name", "age", "salary"])
        for row in generate_rows(100):
            writer.writerow(row)
    print(f"Wrote {out.resolve()}")


if __name__ == "__main__":
    main()
