
# FastAPI With MongoDB (CRUD Application)

An API made with FastAPI python module to perform CRUD operations on database.

## Features

- Easy to use
- CRUD support
- Fast Response
- Easy to understand documentation


## API Reference

#### Get Students Info.

```http
  GET /readstudentinfo/${roll_no}
```
| Parameter | Type  | Description                                    |
| :-------- | :---- | :----------------------------------------------|
| `roll_no` | `int` | **Required**. Roll No of student to fetch info |

Takes student roll no and returns his/her all info from database.

#### Enter Students Info.

```http
  POST /enterstudentinfo/${roll_no}${name}${cl}
```
| Parameter | Type   | Description                                |
| :-------- | :----- | :------------------------------------------|
| `roll_no` | `int`  | **Required**. Roll No of student to enter. |
| `name`    | `str`  | **Required**. Name of student to enter.    |
| `cl`      | `str`  | **Required**. Class of student to enter.   |

Takes student info to store into database.

#### Update Students Info.

```http
  PUT /updatestudentinfo/${roll_no}${roll_no}${name}${cl}
```
| Parameter | Type   | Description                                              |
| :-------- | :----- | :--------------------------------------------------------|
| `roll_no` | `int`  | **Required**. Roll No of student to update his/her info. |
| `roll_no` | `int`  | **Required**. Roll No of student to update.              |
| `name`    | `str`  | **Required**. Name of student to update.                 |
| `cl`      | `str`  | **Required**. Class of student to update.                |

Takes student info to update previous students info in database.

#### Delete Students Info.

```http
  DELETE /deletestudentinfo/${roll_no}
```
| Parameter | Type  | Description                                             |
| :-------- | :---- | :-------------------------------------------------------|
| `roll_no` | `int` | **Required**. Roll No of student to delete his/her info.|

Takes student roll no and delete his/her info. from database.


## Screenshots

![FastAPI - Docs](https://github.com/vikramsamak/Student-Mangaement-System-FastAPI---MangoDB-CRUD-Application-/blob/2ea6b7277afbbee42d98851b2bff3fef72a754cc/FastAPI%20-Docs.png)


## Feedback

If you have any feedback, please reach out to me at vikramsamak02@gmail.com
## Authors

-[@Vikram Samak]https://github.com/vikramsamak)
-[@Abhimanyu Sharma]https://github.com/0xN1nja




