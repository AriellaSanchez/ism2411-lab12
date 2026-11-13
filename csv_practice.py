#reflection questions: 1.Python's better at repeating the same task on many files, handling larger files, and automating. Excel's better for quick looks, visual editing, and people who don't code.    2.An audit trail of processed orders, a daily job log, or record of who made what changes. Append mode is the right tool because writing normally would wipe earlier entries each time.

print("--Exercise 2--")
import csv
with open("data/sales.csv", newline="") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

print("--Exercise 3--")
import csv
with open("data/sales.csv", newline="") as f:
    reader = csv.reader(f)
    header = next(reader)
    print(header)
    for row in reader:
        print(row)

print("--Exercise 4--")
total_revenue = 0
with open("data/sales.csv", newline="") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        product = row[0]
        price = float(row[1])
        quantity = int(row[2])
        total = price * quantity
        total_revenue += total
        print(f"{product}: {quantity} units x ${price:.2f} = ${total:.2f}")
print(f"Total revenue: ${total_revenue:.2f}")

print("--Exercise 5--")
original_count = 0
written_count = 0
with open("data/sales.csv", newline="") as f_in, open("data/cleaned.csv", "w", newline="") as f_out:
    reader = csv.reader(f_in)
    writer = csv.writer(f_out)
    next(reader)
    writer.writerow(["Product", "Price", "Qty", "Total"])
    for row in reader:
        original_count += 1
        product = row[0]
        price = float(row[1])
        qty = int(row[2])
        total = price * qty
        if total > 100:
            writer.writerow([product, f"{price:.2f}", qty, f"{total:.2f}"])
            written_count += 1
print(f"Rows written: {written_count} of {original_count} in the original")

print("--Exercise 6--")
total_revenue_dict = 0
with open("data/sales.csv", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])
        total = price * quantity
        total_revenue_dict += total
        print(f"{product}: {quantity} units x ${price:.2f} = ${total:.2f}")
print(f"Total revenue: ${total_revenue_dict:.2f}")

print("--Exercise 7--")
summary = {}
with open("data/sales.csv", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        product = row["product"]
        revenue = float(row["price"]) * int(row["quantity"])
        summary[product] = summary.get(product, 0) + revenue
for product in sorted(summary):
    print(f"{product}: ${summary[product]:.2f}")

print("--Exercise 8--")
from datetime import datetime
log_total = 0
with open("data/sales.csv", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        log_total += float(row["price"]) * int(row["quantity"])
with open("data/run_log.txt", "a") as log:
    log.write(f"{datetime.now()} - total revenue: ${log_total:.2f}/n")
print("Logged this run to data/run_log.txt")
