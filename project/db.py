import sqlite3
import os
import json


class DatabaseDriver(object):
    def __init__(self):
        self.conn = sqlite3.connect("TeamProject.db", check_same_thread=False)
        self.create_curriculum_table()

    def create_curriculum_table(self):
        try:
            self.conn.execute(
                """
               CREATE TABLE curriculum (
                   DATE INTEGER PRIMARY KEY ,
                   TEACHER TEXT NOT NULL,
                   CLASS1 TEXT ,
                   CLASS2 TEXT ,
                   CLASS3 TEXT ,
                   CLASS4 TEXT ,
                   CLASS5 TEXT ,
                   CLASS6 TEXT ,
                   CLASS7 TEXT 
               );
               """
            )
        except Exception as e:
            print(e)

    def insert_curriculum_table(self, Date, Teacher, CLASS1, CLASS2, CLASS3, CLASS4, CLASS5, CLASS6, CLASS7):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO task (DESCRIPTION, DONE) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);",
            (Date, Teacher, CLASS1, CLASS2, CLASS3, CLASS4, CLASS5, CLASS6, CLASS7)
        )
        self.conn.commit()
        return cursor.lastrowid

    def get_curriculum_by_date(self, Date):
        cursor = self.conn.execute(
            "SELECT * FROM curriculum WHERE Date = ?", (Date,))
        for row in cursor:
            return {
                "date": row[0],
                "Teacher": row[1],
                "class1": row[2],
                "class2": row[3],
                "class3": row[4],
                "class4": row[5],
                "class5": row[6],
                "class6": row[7],
                "class7": row[8]

            }

        return None

    def update_curriculum_by_date(self, Date, Teacher, Class1, Class2, Class3, Class4, Class5, Class6, Class7):
        self.conn.execute(
            """
           UPDATE curriculum
           SET Teacher = ?, Class1 = ?,Class2 = ?, Class3 = ?, Class4 = ?, Class5, Class6 = ?, Class7 = ?
           WHERE Date = ?;
           """,
            (Teacher, Class1, Class2, Class3, Class4, Class5, Class6, Class7, Date),
        )
        self.conn.commit()

    def delete_curriculum_by_date(self, Date):
        self.conn.execute(
            """
           DELETE FROM curriculum
           WHERE Date = ?;
           """,
            (Date,),
        )
        self.conn.commit()
