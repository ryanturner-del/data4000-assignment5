

# inventory_spotcheck.py
# Assignment 5 — Inventory Reorder Analyzer with API Spot Check

import requests  # third-party library for making HTTP requests (pip install requests)

# ─────────────────────────────────────────────
# SECTION 1: STUDENT KEY & SEED
# ─────────────────────────────────────────────

student_key = input("Student key: ")

# Same seed formula as Exercise 1
seed = sum(ord(ch) for ch in student_key.strip())


# ─────────────────────────────────────────────
# SECTION 2: THRESHOLD LOGIC
# ─────────────────────────────────────────────

# The reorder threshold depends on seed % 3 (remainder when dividing seed by 3)
# This gives one of three possible values: 0, 1, or 2
if seed % 3 == 0:
    threshold = 15
elif seed % 3 == 1:
    threshold = 12
else:
    threshold = 9  # seed % 3 == 2


# ─────────────────────────────────────────────
# SECTION 3: SKU ENTRY LOOP
# ─────────────────────────────────────────────

total_skus = 0    # count of all SKUs entered
reorder_count = 0  # count of SKUs flagged for reorder

while True:

    # ── SKU Input ──────────────────────────────
    while True:
        sku = input("SKU (or DONE): ").strip()

        if sku.upper() == "DONE":
            break  # exit inner loop, will also exit outer loop below

        if sku == "":
            print("  Error: SKU cannot be blank.")
            continue  # reprompt

        break  # valid SKU, exit inner loop

    # Exit outer loop if user typed DONE
    if sku.upper() == "DONE":
        break

    # ── On-Hand Quantity ───────────────────────
    # Must be an integer >= 0 (0 is allowed — means out of stock)
    while True:
        try:
            on_hand = int(input("  On hand: "))

            if on_hand < 0:
                print("  Error: quantity cannot be negative.")
                continue

            break  # valid quantity

        except ValueError:
            print("  Error: please enter a whole number.")

    # ── Reorder Decision ───────────────────────
    # If on_hand is below the threshold, flag this SKU for reorder
    total_skus += 1

    if on_hand < threshold:
        status = "REORDER"
        reorder_count += 1
    else:
        status = "OK"

    print(f"  {sku}: {status} (on hand: {on_hand}, threshold: {threshold})")


# ─────────────────────────────────────────────
# SECTION 4: API SPOT CHECK
# ─────────────────────────────────────────────

# Choose search term based on whether seed is even or odd
if seed % 2 == 0:
    spotcheck_term = "weezer"
else:
    spotcheck_term = "drake"

# Set up the API request parameters
# The iTunes Search API is free and requires no API key
api_url = "https://itunes.apple.com/search"
params = {
    "term": spotcheck_term,
    "entity": "song",
    "limit": 5
}

# Variables to hold results — default to failure state
song_count = None   # will stay None if API fails (printed as N/A)
api_status = "FAILED"

# ── API Request with Exception Handling ────────
try:
    # Send the GET request to iTunes — raises an exception if network fails
    response = requests.get(api_url, params=params, timeout=10)

    # .json() parses the response body as JSON into a Python dictionary
    # Raises an exception if the response isn't valid JSON
    data = response.json()

    # Try to access the "results" key — raises KeyError if it's missing
    results = data["results"]

    # Count only items where "kind" == "song"
    # This is a list comprehension — it loops through results and filters
    song_count = sum(1 for item in results if item.get("kind") == "song")

    api_status = "OK"

except requests.exceptions.RequestException:
    # Covers all network-related failures: no internet, timeout, DNS error, etc.
    api_status = "FAILED"

except (KeyError, ValueError):
    # KeyError: "results" key missing from JSON
    # ValueError: response body wasn't valid JSON at all
    api_status = "INVALID_RESPONSE"


# ─────────────────────────────────────────────
# SECTION 5: OUTPUT
# ─────────────────────────────────────────────

# Format song_count as N/A if the API didn't succeed
songs_display = str(song_count) if song_count is not None else "N/A"

print()
print(f"Seed: {seed}")
print(f"Threshold: {threshold}")
print(f"SKUs entered: {total_skus}")
print(f"Reorder flagged: {reorder_count}")
print(f"Spotcheck term: {spotcheck_term}")
print(f"Songs returned: {songs_display}")
print(f"API status: {api_status}")