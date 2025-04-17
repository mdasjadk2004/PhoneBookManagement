from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# File to store contacts
CONTACTS_FILE = "phonebook.txt"

# Load contacts from file
def load_contacts():
    contacts = []
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as file:
            for line in file:
                name, phone = line.strip().split(",")
                contacts.append({"name": name, "phone": phone})
    return contacts

# Save contacts to file
def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        for contact in contacts:
            file.write(f"{contact['name']},{contact['phone']}\n")

# Merge Sort for sorting contacts by name
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i]["name"].lower() < right[j]["name"].lower():
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

@app.route("/")
def index():
    contacts = load_contacts()
    return render_template("index.html", contacts=contacts)

@app.route("/add", methods=["POST"])
def add_contact():
    name = request.form.get("name")
    phone = request.form.get("phone")
    contacts = load_contacts()
    contacts.append({"name": name, "phone": phone})
    save_contacts(contacts)
    return redirect(url_for("index"))

@app.route("/delete/<int:index>")
def delete_contact(index):
    contacts = load_contacts()
    if 0 <= index < len(contacts):
        contacts.pop(index)
        save_contacts(contacts)
    return redirect(url_for("index"))

@app.route("/sort")
def sort_contacts():
    contacts = load_contacts()
    sorted_contacts = merge_sort(contacts)
    save_contacts(sorted_contacts)
    return redirect(url_for("index"))

@app.route("/search", methods=["POST"])
def search_contact():
    query = request.form.get("query").lower()
    contacts = load_contacts()
    results = [contact for contact in contacts if query in contact["name"].lower() or query in contact["phone"]]
    return render_template("index.html", contacts=results, search_query=query)

if __name__ == "__main__":
    app.run(debug=True)