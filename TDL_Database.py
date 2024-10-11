import sqlite3 as sql

con = sql.connect("TDL.db")
cur = con.cursor()

cur.execute("""

CREATE TABLE IF NOT EXISTS user(
id INTEGER PRIMARY KEY AUTOINCREMENT,
username TEXT,
ph_num TEXT,
password TEXT
)

""")

cur.execute("""

CREATE TABLE IF NOT EXISTS task(
task_id INTEGER PRIMARY KEY AUTOINCREMENT,
user_id INTEGER,
title TEXT,
description TEXT,
creation_date TEXT,
lastmodification_date TEXT,
deadline_date TEXT,
active BOOL,
tags TEXT
)

""")

cur.execute("""

CREATE TABLE IF NOT EXISTS tag(
tag_user_id,
tag_name,
tagged_tasks
)

""")

class DB_User:
    @staticmethod
    def add_user(ph_num, username, password):
        cur.execute("INSERT INTO user (ph_num, username, password) VALUES (?, ?, ?)", (ph_num, username, password)) 
        con.commit()

    @staticmethod
    def get_id(ph_num):
        cur.execute("SELECT id FROM user WHERE ph_num = ?", (ph_num,))
        id = cur.fetchone()[0]
        return id   

    @staticmethod
    def get_username(ph_num):
        cur.execute("SELECT username FROM user WHERE ph_num = ?", (ph_num,))
        username = cur.fetchone()[0]
        return username

    @staticmethod
    def get_password(ph_num):
        cur.execute("SELECT password FROM user WHERE ph_num = ?", (ph_num,))
        password = cur.fetchone()[0]
        return password

class DB_Task:
    @staticmethod
    def add_task(user_id, title, description, creation_date, lastmodification_date, deadline_date, active, tags):
        cur.execute("INSERT INTO task (user_id, title, description, creation_date, lastmodification_date, deadline_date, active, tags) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (user_id, title, description, creation_date, lastmodification_date, deadline_date, active, tags))
        con.commit()
    
    @staticmethod
    def edit_task(task_id, title, description, lastmodification_date, deadline_date, active, tags):
        cur.execute(f"UPDATE task SET title = ?, description = ?, lastmodification_date = ?, deadline_date = ?, active = ?, tags = ? WHERE task_id = ?", (title, description, lastmodification_date, deadline_date, active, tags, task_id))
        con.commit()

    @staticmethod
    def show_task(task_id):
        cur.execute("SELECT title, description, creation_date, lastmodification_date, deadline_date, active, tags FROM task WHERE task_id = ?", (task_id,))
        for i in cur.fetchone():
            print(i)
        if cur.fetchone() == None:
            return True
    
    @staticmethod
    def show_tasks(sorting, user_session):
        if sorting[2] == "g":
            if sorting[1] == "a":
                if sorting[0] == "u":
                    print("not yet done:")
                    cur.execute(f"SELECT task_id, title FROM task WHERE user_id = {user_session.id} AND active = {True} ORDER BY lastmodification_date ASC")
                    for task_id, title in cur.fetchall():
                        print(str(task_id) + ") " + title)
                    print("-----------------------------------------------------------------------------")
                    print("done:")
                    cur.execute(f"SELECT task_id, title FROM task WHERE user_id = {user_session.id} AND active = {False} ORDER BY lastmodification_date ASC")
                    for task_id, title in cur.fetchall():
                        print(str(task_id) + ") " + title)
                if sorting[0] == "c":
                    print("not yet done:")
                    cur.execute(f"SELECT task_id, title FROM task WHERE user_id = {user_session.id} AND active = {True} ORDER BY creation_date ASC")
                    for task_id, title in cur.fetchall():
                        print(str(task_id) + ") " + title)
                    print("-----------------------------------------------------------------------------")
                    print("done:")
                    cur.execute(f"SELECT task_id, title FROM task WHERE user_id = {user_session.id} AND active = {False} ORDER BY creation_date ASC")
                    for task_id, title in cur.fetchall():
                        print(str(task_id) + ") " + title)
                if sorting[0] == "e":
                    print("not yet done:")
                    cur.execute(f"SELECT task_id, title FROM task WHERE user_id = {user_session.id} AND active = {True} ORDER BY deadline_date ASC")
                    for task_id, title in cur.fetchall():
                        print(str(task_id) + ") " + title)
                    print("-----------------------------------------------------------------------------")
                    print("done:")
                    cur.execute(f"SELECT task_id, title FROM task WHERE user_id = {user_session.id} AND active = {False} ORDER BY deadline_date ASC")
                    for task_id, title in cur.fetchall():
                        print(str(task_id) + ") " + title)
                if sorting[0] != "u" and sorting[0] != "c" and sorting[0] != "e":
                    print("input invalid")
            if sorting[1] == "d":
                if sorting[0] == "u":
                    print("not yet done:")
                    cur.execute(f"SELECT task_id, title FROM task WHERE user_id = {user_session.id} AND active = {True} ORDER BY lastmodification_date DESC")
                    for task_id, title in cur.fetchall():
                        print(str(task_id) + ") " + title)
                    print("-----------------------------------------------------------------------------")
                    print("done:")
                    cur.execute(f"SELECT task_id, title FROM task WHERE user_id = {user_session.id} AND active = {False} ORDER BY lastmodification_date DESC")
                    for task_id, title in cur.fetchall():
                        print(str(task_id) + ") " + title)
                if sorting[0] == "c":
                    print("not yet done:")
                    cur.execute(f"SELECT task_id, title FROM task WHERE user_id = {user_session.id} AND active = {True} ORDER BY creation_date DESC")
                    for task_id, title in cur.fetchall():
                        print(str(task_id) + ") " + title)
                    print("-----------------------------------------------------------------------------")
                    print("done:")
                    cur.execute(f"SELECT task_id, title FROM task WHERE user_id = {user_session.id} AND active = {False} ORDER BY creation_date DESC")
                    for task_id, title in cur.fetchall():
                        print(str(task_id) + ") " + title)
                if sorting[0] == "e":
                    print("not yet done:")
                    cur.execute(f"SELECT task_id, title FROM task WHERE user_id = {user_session.id} AND active = {True} ORDER BY deadline_date DESC")
                    for task_id, title in cur.fetchall():
                        print(str(task_id) + ") " + title)
                    print("-----------------------------------------------------------------------------")
                    print("done:")
                    cur.execute(f"SELECT task_id, title FROM task WHERE user_id = {user_session.id} AND active = {False} ORDER BY deadline_date DESC")
                    for task_id, title in cur.fetchall():
                        print(str(task_id) + ") " + title)
                if sorting[0] != "u" and sorting[0] != "c" and sorting[0] != "e":
                    print("input invalid")
            if sorting[1] != "a" and sorting[1] != "d":
                print("input invalid")
        if sorting[2] == "n":
            if sorting[1] == "a":
                if sorting[0] == "u":
                    cur.execute(f"SELECT task_id, title FROM task WHERE user_id = {user_session.id} ORDER BY lastmodification_date ASC")
                    for task_id, title in cur.fetchall():
                        print(str(task_id) + ") " + title)
                if sorting[0] == "c":
                    cur.execute(f"SELECT task_id, title FROM task WHERE user_id = {user_session.id} ORDER BY creation_date ASC")
                    for task_id, title in cur.fetchall():
                        print(str(task_id) + ") " + title)
                if sorting[0] == "e":
                    cur.execute(f"SELECT task_id, title FROM task WHERE user_id = {user_session.id} ORDER BY deadline_date ASC")
                    for task_id, title in cur.fetchall():
                        print(str(task_id) + ") " + title)
                if sorting[0] != "u" and sorting[0] != "c" and sorting[0] != "e":
                    print("input invalid")
            if sorting[1] == "d":
                if sorting[0] == "u":
                    cur.execute(f"SELECT task_id, title FROM task WHERE user_id = {user_session.id} ORDER BY lastmodification_date DESC")
                    for task_id, title in cur.fetchall():
                        print(str(task_id) + ") " + title)
                if sorting[0] == "c":
                    cur.execute(f"SELECT task_id, title FROM task WHERE user_id = {user_session.id} ORDER BY creation_date DESC")
                    for task_id, title in cur.fetchall():
                        print(str(task_id) + ") " + title)
                if sorting[0] == "e":
                    cur.execute(f"SELECT task_id, title FROM task WHERE user_id = {user_session.id} ORDER BY deadline_date DESC")
                    for task_id, title in cur.fetchall():
                        print(str(task_id) + ") " + title)
                if sorting[0] != "u" and sorting[0] != "c" and sorting[0] != "e":
                    print("input invalid")
            if sorting[1] != "a" and sorting[1] != "d":
                print("input invalid")
        if sorting[2] != "g" and sorting[2] != "n":
            print("input invalid")

    @staticmethod
    def show_tagged_tasks(tagged_task_ids, sorting, user_session):
        if sorting[2] == "g":
            if sorting[1] == "a":
                if sorting[0] == "u":
                    print("not yet done:")
                    for task_id in tagged_task_ids:
                        cur.execute(f"SELECT title FROM task WHERE user_id = {user_session.id} AND task_id = {task_id} AND active = {True} ORDER BY lastmodification_date ASC")
                        for title in cur.fetchall()[0]:
                            print(str(task_id) + ") " + title)
                    print("-----------------------------------------------------------------------------")
                    print("done:")
                    for task_id in tagged_task_ids:
                        cur.execute(f"SELECT title FROM task WHERE user_id = {user_session.id} AND task_id = {task_id} AND active = {False} ORDER BY lastmodification_date ASC")
                        for title in cur.fetchall()[0]:
                            print(str(task_id) + ") " + title)
                if sorting[0] == "c":
                    print("not yet done:")
                    for task_id in tagged_task_ids:
                        cur.execute(f"SELECT title FROM task WHERE user_id = {user_session.id} AND task_id = {task_id} AND active = {True} ORDER BY creation_date ASC")
                        for title in cur.fetchall()[0]:
                            print(str(task_id) + ") " + title)
                    print("-----------------------------------------------------------------------------")
                    print("done:")
                    for task_id in tagged_task_ids:
                        cur.execute(f"SELECT title FROM task WHERE user_id = {user_session.id} AND task_id = {task_id} AND active = {False} ORDER BY creation_date ASC")
                        for title in cur.fetchall()[0]:
                            print(str(task_id) + ") " + title)
                if sorting[0] == "e":
                    print("not yet done:")
                    for task_id in tagged_task_ids:
                        cur.execute(f"SELECT title FROM task WHERE user_id = {user_session.id} AND task_id = {task_id} AND active = {True} ORDER BY deadline_date ASC")
                        for title in cur.fetchall()[0]:
                            print(str(task_id) + ") " + title)
                    print("-----------------------------------------------------------------------------")
                    print("done:")
                    for task_id in tagged_task_ids:
                        cur.execute(f"SELECT title FROM task WHERE user_id = {user_session.id} AND task_id = {task_id} AND active = {False} ORDER BY deadline_date ASC")
                        for title in cur.fetchall()[0]:
                            print(str(task_id) + ") " + title)
                if sorting[0] != "u" and sorting[0] != "c" and sorting[0] != "e":
                    print("input invalid")
            if sorting[1] == "d":
                if sorting[0] == "u":
                    print("not yet done:")
                    for task_id in tagged_task_ids:
                        cur.execute(f"SELECT title FROM task WHERE user_id = {user_session.id} AND task_id = {task_id} AND active = {True} ORDER BY lastmodification_date DESC")
                        for title in cur.fetchall()[0]:
                            print(str(task_id) + ") " + title)
                    print("-----------------------------------------------------------------------------")
                    print("done:")
                    for task_id in tagged_task_ids:
                        cur.execute(f"SELECT title FROM task WHERE user_id = {user_session.id} AND task_id = {task_id} AND active = {False} ORDER BY lastmodification_date DESC")
                        for title in cur.fetchall()[0]:
                            print(str(task_id) + ") " + title)
                if sorting[0] == "c":
                    print("not yet done:")
                    for task_id in tagged_task_ids:
                        cur.execute(f"SELECT title FROM task WHERE user_id = {user_session.id} AND task_id = {task_id} AND active = {True} ORDER BY creation_date DESC")
                        for title in cur.fetchall()[0]:
                            print(str(task_id) + ") " + title)
                    print("-----------------------------------------------------------------------------")
                    print("done:")
                    for task_id in tagged_task_ids:
                        cur.execute(f"SELECT title FROM task WHERE user_id = {user_session.id} AND task_id = {task_id} AND active = {False} ORDER BY creation_date DESC")
                        for title in cur.fetchall()[0]:
                            print(str(task_id) + ") " + title)
                if sorting[0] == "e":
                    print("not yet done:")
                    for task_id in tagged_task_ids:
                        cur.execute(f"SELECT task_id, title FROM task WHERE user_id = {user_session.id} AND task_id = {task_id} AND active = {True} ORDER BY deadline_date DESC")
                        for title in cur.fetchall()[0]:
                            print(str(task_id) + ") " + title)
                    print("-----------------------------------------------------------------------------")
                    print("done:")
                    for task_id in tagged_task_ids:
                        cur.execute(f"SELECT title FROM task WHERE user_id = {user_session.id} AND task_id = {task_id} AND active = {False} ORDER BY deadline_date DESC")
                        for title in cur.fetchall()[0]:
                            print(str(task_id) + ") " + title)
                if sorting[0] != "u" and sorting[0] != "c" and sorting[0] != "e":
                    print("input invalid")
            if sorting[1] != "a" and sorting[1] != "d":
                print("input invalid")
        if sorting[2] == "n":
            if sorting[1] == "a":
                if sorting[0] == "u":
                    for task_id in tagged_task_ids:
                        cur.execute(f"SELECT title FROM task WHERE user_id = {user_session.id} AND task_id = {task_id} ORDER BY lastmodification_date ASC")
                        for title in cur.fetchall()[0]:
                            print(str(task_id) + ") " + title)
                if sorting[0] == "c":
                    for task_id in tagged_task_ids:
                        cur.execute(f"SELECT title FROM task WHERE user_id = {user_session.id} AND task_id = {task_id} ORDER BY creation_date ASC")
                        for title in cur.fetchall()[0]:
                            print(str(task_id) + ") " + title)
                if sorting[0] == "e":
                    for task_id in tagged_task_ids:
                        cur.execute(f"SELECT title FROM task WHERE user_id = {user_session.id} AND task_id = {task_id} ORDER BY deadline_date ASC")
                        for title in cur.fetchall()[0]:
                            print(str(task_id) + ") " + title)
                if sorting[0] != "u" and sorting[0] != "c" and sorting[0] != "e":
                    print("input invalid")
            if sorting[1] == "d":
                if sorting[0] == "u":
                    for task_id in tagged_task_ids:
                        cur.execute(f"SELECT title FROM task WHERE user_id = {user_session.id} AND task_id = {task_id} ORDER BY lastmodification_date DESC")
                        for title in cur.fetchall()[0]:
                            print(str(task_id) + ") " + title)
                if sorting[0] == "c":
                    for task_id in tagged_task_ids:
                        cur.execute(f"SELECT title FROM task WHERE user_id = {user_session.id} AND task_id = {task_id} ORDER BY creation_date DESC")
                        for title in cur.fetchall()[0]:
                            print(str(task_id) + ") " + title)
                if sorting[0] == "e":
                    for task_id in tagged_task_ids:
                        cur.execute(f"SELECT title FROM task WHERE user_id = {user_session.id} AND task_id = {task_id} ORDER BY deadline_date DESC")
                        for title in cur.fetchall()[0]:
                            print(str(task_id) + ") " + title)
                if sorting[0] != "u" and sorting[0] != "c" and sorting[0] != "e":
                    print("input invalid")
            if sorting[1] != "a" and sorting[1] != "d":
                print("input invalid")
        if sorting[2] != "g" and sorting[2] != "n":
            print("input invalid")

class DB_Tag:
    @staticmethod
    def add_tag(tags, user_session):
        tags_list = tags.split(",")
        for tag in tags_list:
            cur.execute(f"SELECT task_id, tags FROM task WHERE user_id = {user_session.id}")
            tag_task_ids = ""
            f = 0
            for task_id, task_tags in cur.fetchall():
                task_tags_list = task_tags.split(",")
                for task_tag in task_tags_list:
                    if tag == task_tag:
                        f += 1
                        tag_task_ids = str(tag_task_ids) + "," + str(task_id)
            tag_task_ids = tag_task_ids.removeprefix(",")
            if f == 1:
                cur.execute("INSERT INTO tag (tag_user_id, tag_name, tagged_tasks) VALUES (?, ?, ?)", (user_session.id, tag, tag_task_ids))
                con.commit()
            else:
                cur.execute(f"UPDATE tag SET tag_user_id = ?, tagged_tasks = ? WHERE tag_name = ?", (user_session.id, tag_task_ids, tag))
                con.commit()

    @staticmethod
    def show_tags(user_session):
        cur.execute(f"SELECT tag_name FROM tag WHERE tag_user_id = {user_session.id}")
        for tag in cur.fetchall():
            print(tag[0])

    @staticmethod
    def get_tagged_tasks(tag, user_session):
        cur.execute(f"SELECT tagged_tasks FROM tag WHERE tag_name = ? AND tag_user_id = ?", (tag, user_session.id))
        tagged_task_ids = cur.fetchone()[0]
        if tagged_task_ids != None:
            tagged_task_ids = tagged_task_ids.split(",")
        else:
            print("no such tag")  
        return tagged_task_ids