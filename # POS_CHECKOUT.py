# POS_CHECKOUT.PY

# pos_checkout.py
# Assignment 5 — Point-of-Sale Checkout System


# Prompt the user for their student key (fairfield 00 fill in rest)
student_key = input("Student key: ")


seed = sum(ord(ch) for ch in student_key.strip())


# These two variables track the running state across all items entered
subtotal = 0.0   # total dollar amount before discount
total_units = 0  # total number of units purchased



# This loop runs forever until the cashier types "DONE"
while True:

    # ── Item Name ──────────────────────────────
    # Inner loop: keep asking until we get a valid name or "DONE"
    while True:
        name = input("Item name (or DONE): ").strip()  # .strip() removes extra spaces

        if name.upper() == "DONE":
            # Exit the outer loop by breaking all the way out
            # We use a flag approach: set name to "DONE" and break inner loop
            break

        if name == "":
            # Reject empty names — reprompt
            print("  Error: item name cannot be blank.")
            continue  # go back to the top of this inner while loop

        # If we reach here, name is valid and not "DONE"
        break

    # If the cashier typed DONE, exit the outer while loop too
    if name.upper() == "DONE":
        break

    # ── Unit Price ─────────────────────────────
    # Inner loop: keep asking until we get a valid float > 0
    while True:
        try:
            # try to convert the input to a float — raises ValueError if it can't
            price = float(input("  Unit price: $"))

            if price <= 0:
                # Price must be positive — reprompt
                print("  Error: price must be greater than 0.")
                continue  # go back to top of this inner while loop

            # Valid price — exit this inner loop
            break

        except ValueError:
            # The user typed something that isn't a number (e.g. "abc")
            print("  Error: please enter a valid number for price.")

    # ── Quantity ───────────────────────────────
    # Inner loop: keep asking until we get a valid int >= 1
    while True:
        try:
            # try to convert input to int — raises ValueError if it can't
            qty = int(input("  Quantity: "))

            if qty < 1:
                # Quantity must be at least 1 — reprompt
                print("  Error: quantity must be at least 1.")
                continue

            # Valid quantity — exit this inner loop
            break

        except ValueError:
            # The user typed something that isn't a whole number (e.g. "two")
            print("  Error: please enter a whole number for quantity.")

    # ── Update Running Totals ──────────────────
    # Now that all three fields are valid, update our running totals
    subtotal += price * qty   # add this item's total cost to the subtotal
    total_units += qty        # add this item's quantity to the unit count

    # Confirm the item was added (helpful for the cashier)
    print(f"  Added: {name} x{qty} @ ${price:.2f} = ${price * qty:.2f}")




# Apply a 10% discount if units >= 10 OR subtotal >= $100, otherwise 0%
if total_units >= 10 or subtotal >= 100:
    discount_percent = 10
else:
    discount_percent = 0

# Calculate the dollar amount of the discount
discount_amount = subtotal * (discount_percent / 100)

# Subtract the discount from the subtotal
total = subtotal - discount_amount



# Check if seed is odd or even using the modulo operator (% gives the remainder)
# seed % 2 == 1 means it's odd (e.g. 7 % 2 = 1)
if seed % 2 == 1:
    perk_applied = True
    total -= 3.00  # subtract $3.00 member perk

    # Total must never go below $0.00
    if total < 0:
        total = 0.0
else:
    perk_applied = False


print()  # blank line before output for readability
print(f"Seed: {seed}")
print(f"Units: {total_units}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Discount: {discount_percent}%")
print(f"Perk applied: {'YES' if perk_applied else 'NO'}")
print(f"Total: ${total:.2f}")