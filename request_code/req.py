import requests
import json


def switch_case():
    print("\n1.CREATE\n2.READ\n3.UPDATE\n4.DELETE")
    choice = int(input("Enter Your Choice:"))
    if (choice == 1):
        post()
    elif (choice == 2):
        get()
    elif (choice == 3):
        update()
    elif (choice == 4):
        delete()

# POST REQUEST TO ENTER DATA


def post():
    url = "http://127.0.0.1:8000/enterstudentinfo"

    ro_no = int(input("\nEnter Roll No:"))
    n = input("Enter Name:")
    c = input("Enter Class:")

    res = requests.request("POST", url=url, json={"roll_no": ro_no, "name": n, "cl": c})

    print("Response:", res.json())


# GET REQUEST FOR GETTING STUDENT INFO.
def get():
    url = "http://127.0.0.1:8000/readstudentinfo"
    Roll_no = int(input("\nEnter Roll No:"))
    data_to_get = {"roll_no": Roll_no}
    res = requests.request("GET", url=url, params=data_to_get)
    print("Response:", res.json())

# UPDATING PREVIOUS DATA


def update():
    url = "http://127.0.0.1:8000/updatestudentinfo"
    srn = int(input("\nEnter A Roll No To Update Its Data:"))
    ro_no = int(input("Enter Roll No To Update:"))
    n = input("Enter Name To Update:")
    c = input("Enter Class To Update:")
    res = requests.request("PUT", url=url, params={"rno": srn},
                           json={"roll_no": ro_no, "name": n, "cl": c})
    print("Response:", res.json())


# DELETE OPERATION


def delete():
    url = "http://127.0.0.1:8000/deletestudentinfo"
    r_no = int(input("\nEnter Roll No Of Thr Student :"))
    data_to_delete = {"roll_no": r_no}
    res = requests.request("DELETE", url=url, params=data_to_delete)
    print("Response:", res.json())

#FOR CONTIOUS OPEARTION
while True:

    switch_case()
