records = [
    {"product":"Rice","category":"Grocery","region":"West","price":60,"quantity":20,"profit":220},
    {"product":"Milk","category":"Dairy","region":"North","price":50,"quantity":15,"profit":90},
    {"product":"Soap","category":"Personal Care","region":"South","price":35,"quantity":30,"profit":180},
    {"product":"Bread","category":"Bakery","region":"West","price":40,"quantity":25,"profit":120},
    {"product":"Oil","category":"Grocery","region":"East","price":150,"quantity":12,"profit":150},
    {"product":"Cheese","category":"Dairy","region":"South","price":110,"quantity":10,"profit":160},
    {"product":"Shampoo","category":"Personal Care","region":"North","price":180,"quantity":8,"profit":240},
    {"product":"Biscuits","category":"Bakery","region":"East","price":25,"quantity":40,"profit":110},
]

def revenue(r): return r["price"] * r["quantity"]
def group(field):
    result = {}
    for r in records: result[r[field]] = result.get(r[field],0) + revenue(r)
    for k,v in sorted(result.items(), key=lambda kv:kv[1],reverse=True): print(k, v)

def main():
    while True:
        print("\n1.All 2.Total sales 3.Total profit 4.Average sales 5.Highest 6.Lowest 7.By category 8.By region 9.Sales above 10.Profit below 11.Total quantity 12.Exit")
        try:
            c=int(input("Choice: "))
            if c==12: break
            if c==1:
                for r in records: print(r,"sales:",revenue(r))
            elif c==2: print(sum(map(revenue,records)))
            elif c==3: print(sum(r["profit"] for r in records))
            elif c==4: print(sum(map(revenue,records))/len(records))
            elif c==5: print(max(records,key=revenue))
            elif c==6: print(min(records,key=revenue))
            elif c==7: group("category")
            elif c==8: group("region")
            elif c==9:
                threshold=float(input("Sales threshold: "))
                for r in records:
                    if revenue(r)>threshold: print(r)
            elif c==10:
                threshold=float(input("Profit threshold: "))
                for r in records:
                    if r["profit"]<threshold: print(r)
            elif c==11: print(sum(r["quantity"] for r in records))
            else: print("Invalid choice")
        except ValueError: print("Enter valid numeric input")

if __name__ == "__main__": main()
