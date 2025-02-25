import json

FILE_NAME = "recipes.json"

def load_recipes():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_recipes(recipes):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(recipes, file, indent=4, ensure_ascii=False)
def add_recipe(recipes):
    name = input("ชื่อเมนู: ")
    if name in recipes:
        print("❌ เมนูนี้มีอยู่แล้ว!")
        return
    
    ingredients = input("ส่วนผสม (คั่นด้วย ,): ").split(",")
    steps = input("ขั้นตอนการทำ (คั่นด้วย |): ").split("|")
    nutrition = input("ข้อมูลโภชนาการ: ")

    recipes[name] = {
        "ingredients": [ing.strip() for ing in ingredients],
        "steps": [step.strip() for step in steps],
        "nutrition": nutrition.strip()
    }
    
    save_recipes(recipes)
    print(f"✅ เพิ่มเมนู {name} สำเร็จ!")
def edit_recipe(recipes):
    name = input("ใส่ชื่อเมนูที่ต้องการแก้ไข: ")
    if name not in recipes:
        print("❌ ไม่พบเมนูนี้")
        return
    
    print("เลือกสิ่งที่ต้องการแก้ไข:")
    print("1. ส่วนผสม\n2. ขั้นตอนการทำ\n3. โภชนาการ\n4. ยกเลิก")
    choice = input("เลือก (1-4): ")

    if choice == "1":
        ingredients = input("ส่วนผสมใหม่ (คั่นด้วย ,): ").split(",")
        recipes[name]["ingredients"] = [ing.strip() for ing in ingredients]
    elif choice == "2":
        steps = input("ขั้นตอนใหม่ (คั่นด้วย |): ").split("|")
        recipes[name]["steps"] = [step.strip() for step in steps]
    elif choice == "3":
        nutrition = input("ข้อมูลโภชนาการใหม่: ")
        recipes[name]["nutrition"] = nutrition.strip()
    elif choice == "4":
        return
    else:
        print("❌ กรุณาเลือกให้ถูกต้อง")

    save_recipes(recipes)
    print(f"✅ แก้ไขเมนู {name} สำเร็จ!")

def delete_recipe(recipes):
    name = input("ใส่ชื่อเมนูที่ต้องการลบ: ")
    if name in recipes:
        del recipes[name]
        save_recipes(recipes)
        print(f"🗑 ลบเมนู {name} สำเร็จ!")
    else:
        print("❌ ไม่พบเมนูนี้")
FAVORITE_FILE = "favorites.json"

def load_favorites():
    try:
        with open(FAVORITE_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_favorites(favorites):
    with open(FAVORITE_FILE, "w", encoding="utf-8") as file:
        json.dump(favorites, file, indent=4, ensure_ascii=False)

def add_favorite(recipe_name, favorites, recipes):
    if recipe_name in recipes and recipe_name not in favorites:
        favorites.append(recipe_name)
        save_favorites(favorites)
        print(f"⭐ เพิ่ม {recipe_name} ลงในเมนูโปรดแล้ว!")
    else:
        print("❌ ไม่พบเมนูนี้ หรืออาจอยู่ในเมนูโปรดอยู่แล้ว")

def show_favorites(favorites):
    print("\n📌 เมนูโปรดของคุณ:")
    for recipe in favorites:
        print(f"- {recipe}")

from rich.console import Console
from rich.table import Table

console = Console()

def show_all_recipes(recipes):
    table = Table(title="📖 สูตรอาหารทั้งหมด", show_lines=True)
    table.add_column("ชื่อเมนู", style="cyan", justify="left")
    table.add_column("ส่วนผสม", style="green")
    table.add_column("โภชนาการ", style="yellow")

    for name, details in recipes.items():
        table.add_row(name, ", ".join(details['ingredients']), details['nutrition'])

    console.print(table)

def main():
    recipes = load_recipes()
    favorites = load_favorites()

    while True:
        print("\n--- 📌 โปรแกรมสอนทำอาหาร ---")
        print("1. เพิ่มสูตรอาหาร")
        print("2. แก้ไขสูตรอาหาร")
        print("3. ลบสูตรอาหาร")
        print("4. แสดงสูตรอาหารทั้งหมด")
        print("5. ค้นหาสูตรอาหาร")
        print("6. เพิ่มเมนูโปรด")
        print("7. แสดงเมนูโปรด")
        print("8. ออกจากโปรแกรม")

        choice = input("เลือกเมนู (1-8): ")

        if choice == "1":
            add_recipe(recipes)
        elif choice == "2":
            edit_recipe(recipes)
        elif choice == "3":
            delete_recipe(recipes)
        elif choice == "4":
            show_all_recipes(recipes)
        elif choice == "5":
            keyword = input("ใส่คำค้นหา: ")
            results = [name for name in recipes if keyword in name or any(keyword in ing for ing in recipes[name]["ingredients"])]
            if results:
                print("\n📋 พบเมนูที่เกี่ยวข้อง:")
                for name in results:
                    print(f"- {name}")
            else:
                print("❌ ไม่พบเมนูที่ต้องการ")
        elif choice == "6":
            recipe_name = input("ใส่ชื่อเมนูที่ต้องการเพิ่มในเมนูโปรด: ")
            add_favorite(recipe_name, favorites, recipes)
        elif choice == "7":
            show_favorites(favorites)
        elif choice == "8":
            print("👋 ออกจากโปรแกรมแล้ว")
            break
        else:
            print("❌ กรุณาเลือกเมนูที่ถูกต้อง")

if __name__ == "__main__":
    main()
4