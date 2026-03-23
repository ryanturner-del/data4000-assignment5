[README.md](https://github.com/user-attachments/files/26195422/README.md)
# data4000-assignment5

Assignment 5 — Python with AI: Conditionals, Loops, Exceptions, and Libraries

## Requirements

Install the required library before running Exercise 2:

```
pip install requests
```

---

## Exercise 1 — Point-of-Sale Checkout System

**File:** `pos_checkout.py`

### How to run

```
python3 pos_checkout.py
```

### Example run

```
Student key: rturner42
Item name (or DONE): Coffee
  Unit price: $3.50
  Quantity: 4
  Added: Coffee x4 @ $3.50 = $14.00
Item name (or DONE): Notebook
  Unit price: $8.00
  Quantity: 7
  Added: Notebook x7 @ $8.00 = $56.00
Item name (or DONE): DONE

Seed: 874
Units: 11
Subtotal: $70.00
Discount: 10%
Perk applied: NO
Total: $63.00
```

---

## Exercise 2 — Inventory Reorder Analyzer with API Spot Check

**File:** `inventory_spotcheck.py`

### How to run

```
python3 inventory_spotcheck.py
```

### Example run

```
Student key: rturner42
SKU (or DONE): SKU-001
  On hand: 5
  SKU-001: REORDER (on hand: 5, threshold: 12)
SKU (or DONE): SKU-002
  On hand: 20
  SKU-002: OK (on hand: 20, threshold: 12)
SKU (or DONE): DONE

Seed: 874
Threshold: 12
SKUs entered: 2
Reorder flagged: 1
Spotcheck term: weezer
Songs returned: 5
API status: OK
```
