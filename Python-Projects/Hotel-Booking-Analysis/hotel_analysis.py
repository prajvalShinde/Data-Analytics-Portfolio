import csv
from pathlib import Path
from collections import Counter
path=Path(__file__).with_name("synthetic_hotel_bookings.csv")
with path.open(newline="") as f: rows=list(csv.DictReader(f))
total=len(rows)
canceled=sum(int(r["is_canceled"]) for r in rows)
print("Total bookings:",total)
print("Canceled bookings:",canceled)
print("Cancellation rate (%):",round(canceled/total*100,2))
print("Average daily rate:",round(sum(float(r["adr"]) for r in rows)/total,2))
print("Bookings by month:",dict(Counter(r["month"] for r in rows)))
