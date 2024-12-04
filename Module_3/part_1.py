from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient("mongodb://localhost:27017/")
db = client["cat_database"]
collection = db["cats"]

#CREATE
def create_cat(name, age, features):
    try:
        cat = {"name": name, "age": age, "features": features}
        result = collection.insert_one(cat)
        print(f"Кіт {name} доданий з _id: {result.inserted_id}")
    except Exception as e:
        print("Помилка створення запису:", e)

#READ
def read_all_cats():
    try:
        cats = collection.find()
        for cat in cats:
            print(cat)
    except Exception as e:
        print("Помилка читання записів:", e)

def read_cat_by_name(name):
    try:
        cat = collection.find_one({"name": name})
        if cat:
            print(cat)
        else:
            print(f"Кота з іменем {name} не знайдено.")
    except Exception as e:
        print("Помилка під час пошуку:", e)

#UPDATE
def update_cat_age(name, new_age):
    try:
        result = collection.update_one({"name": name}, {"$set": {"age": new_age}})
        if result.matched_count:
            print(f"Вік кота {name} оновлено до {new_age}.")
        else:
            print(f"Кота з іменем {name} не знайдено.")
    except Exception as e:
        print("Помилка оновлення віку:", e)

def add_feature_to_cat(name, feature):
    try:
        result = collection.update_one({"name": name}, {"$push": {"features": feature}})
        if result.matched_count:
            print(f"Характеристика '{feature}' додана коту {name}.")
        else:
            print(f"Кота з іменем {name} не знайдено.")
    except Exception as e:
        print("Помилка додавання характеристики:", e)

#DELETE
def delete_cat_by_name(name):
    try:
        result = collection.delete_one({"name": name})
        if result.deleted_count:
            print(f"Кіт {name} видалений.")
        else:
            print(f"Кота з іменем {name} не знайдено.")
    except Exception as e:
        print("Помилка видалення:", e)

def delete_all_cats():
    try:
        result = collection.delete_many({})
        print(f"Видалено {result.deleted_count} записів.")
    except Exception as e:
        print("Помилка видалення всіх записів:", e)

#MAIN MENU
def main():
    while True:
        print("\n Меню:")
        print("ADD - Додати кота")
        print("SHOW ALL - Показати всіх котів")
        print("FIND - Знайти кота за іменем")
        print("UPDATE AGE - Оновити вік кота")
        print("ADD FEATURE - Додати характеристику коту")
        print("DELETE - Видалити кота за іменем")
        print("CLEAR ALL - Видалити всіх котів")
        print("EXIT - Вийти")
        choice = input("Виберіть опцію: ")

        if choice == "ADD":
            name = input("Введіть ім'я кота: ")
            age = int(input("Введіть вік кота: "))
            features = input("Введіть характеристики (через кому): ").split(", ")
            create_cat(name, age, features)
        elif choice == "SHOW ALL":
            read_all_cats()
        elif choice == "FIND":
            name = input("Введіть ім'я кота: ")
            read_cat_by_name(name)
        elif choice == "UPDATE AGE":
            name = input("Введіть ім'я кота: ")
            new_age = int(input("Введіть новий вік: "))
            update_cat_age(name, new_age)
        elif choice == "ADD FEATURE":
            name = input("Введіть ім'я кота: ")
            feature = input("Введіть нову характеристику: ")
            add_feature_to_cat(name, feature)
        elif choice == "DELETE":
            name = input("Введіть ім'я кота: ")
            delete_cat_by_name(name)
        elif choice == "CLEAR ALL":
            delete_all_cats()
        elif choice == "EXIT":
            print("Вихід із програми.")
            break
        else:
            print("Неправильно введено команду або сталася помилка.")

if __name__ == "__main__":
    main()