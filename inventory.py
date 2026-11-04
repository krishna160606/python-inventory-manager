import os

class InventoryManager:
    def __init__(self, filename="inventory.txt"):
        self.filename = filename
        self.inventory = {}
        self.load_inventory()

    def add_item(self, item_id, name, qty, price):
        self.inventory[item_id] = {"name": name, "qty": qty, "price": price}
        self.save_to_file()
        print(f"✅ Added: {name} (Qty: {qty}, Price: ₹{price})")

    def update_stock(self, item_id, qty):
        if item_id in self.inventory:
            self.inventory[item_id]["qty"] += qty
            self.save_to_file()
            print(f"🔄 Updated {self.inventory[item_id]['name']} stock by {qty}.")
        else:
            print("❌ Item ID not found!")

    def view_inventory(self):
        if not self.inventory:
            print("📦 Inventory is empty.")
            return
        
        print("\n--- Current Inventory ---")
        print(f"{'ID':<10} | {'Name':<15} | {'Qty':<5} | {'Price':<8}")
        print("-" * 45)
        for item_id, data in self.inventory.items():
            print(f"{item_id:<10} | {data['name']:<15} | {data['qty']:<5} | ₹{data['price']:<8}")
        print("-" * 45)

    def save_to_file(self):
        with open(self.filename, "w") as f:
            for item_id, data in self.inventory.items():
                f.write(f"{item_id},{data['name']},{data['qty']},{data['price']}\n")

    def load_inventory(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                for line in f:
                    parts = line.strip().split(",")
                    if len(parts) == 4:
                        self.inventory[parts[0]] = {
                            "name": parts[1],
                            "qty": int(parts[2]),
                            "price": float(parts[3])
                        }

if __name__ == "__main__":
    ims = InventoryManager()
    ims.add_item("P001", "Python Books", 15, 450.0)
    ims.add_item("P002", "Notebooks", 50, 60.0)
    
    ims.view_inventory()
    
    ims.update_stock("P001", 5)
    ims.view_inventory()
