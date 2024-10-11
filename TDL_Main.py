import re
import datetime as dt
import TDL_Database as db
import sys

class User:
    def __init__(self, id : int, username : str, ph_num : str, password : str):
        self.id = id
        self.username = username
        self.ph_num = ph_num
        self.password = password

class Tag:
    def __init__(self, tag_name : str, tagged_tasks : str):
        self.tag_name = tag_name
        self.tagged_tasks = tagged_tasks

class Task:
    def __init__(self, task_id : int, user_id : int, title : str, desc : str, creation_date : str, lastmodification_date : str, deadline_date : str, active : bool, tags : str):
        self.task_id = task_id
        self.user_id = user_id
        self.title = title
        self.desc = desc
        self.creation_date = dt.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        self.lastmodification_date = dt.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        self.deadline_date = deadline_date
        self.active = True
        self.tags = tags

class Pattern:
    ph_num_patt = r'^(09|00989|\+989)\d{9}$'
    username_patt = r'^[a-zA-Z0-9_.-]{3,24}$'
    password_patt = r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$'

class Validator:
    @staticmethod
    def check_ph_num(ph_num):
        if re.search(Pattern.ph_num_patt,ph_num) != None:
            return True
        else:
            return False

    @staticmethod
    def check_username(username):
        if re.search(Pattern.username_patt,username) != None:
            return True
        else:
            return False

    @staticmethod
    def check_password(password):
        if re.search(Pattern.password_patt,password) != None:
            return True
        else:
            return False

    @staticmethod
    def check_signup(ph_num, username, password, re_password):
        if Validator.check_ph_num(ph_num):
            pass
        else:
            print("invalid phone number")
        if Validator.check_username(username):
            pass
        else:
            print("invalid username")
        if Validator.check_password(password):
            pass
        else:
            print("invalid password")
        if password == re_password:
            pass
        else:
            print("passwords do not match")
        return True

    @staticmethod
    def check_login(ph_num, password):
        if Validator.check_ph_num(ph_num):
            pass
        else:
            print("invalid phone number")
        if Validator.check_password(password):
            pass
        else:
            print("invalid password")
        return True

class Terminal:
    @staticmethod
    def menu1():
        print("1) login\n2) signup")
        choice = int(input("choose an option: "))
        
        if choice == 1:
            ph_num = input("phone_number: ")
            password = input("password: ")
            if Validator.check_login:
                if db.DB_User.get_password(ph_num) == password:
                    id = db.DB_User.get_id(ph_num)
                    username = db.DB_User.get_username(ph_num)
                    user_session = User(id, ph_num, username, password)
                    print("welcome" + " " + str(username))
                    Terminal.menu2(user_session)
                else:
                    print("phone number and password do not match")
                    Terminal.menu1()
            else:
                Terminal.menu1()
        
        if choice == 2:
            ph_num = input("phone number: ")
            username = input("username(between 3 and 24 characters long and only include '_.-', lowercase and uppercase letters and numbers): ")
            password = input("password(atleast 8 characters long, only include lowercase and uppercase letters, numbers and special characters'#?!@$%^&*-' and atleast one lowercase, uppercase letter and special character): ")
            re_password = input("confirm password: ")
            if Validator.check_signup(ph_num, username, password, re_password):
                db.DB_User.add_user(ph_num, username, password)
                id = db.DB_User.get_id(ph_num)
                user_session = User(id, ph_num, username, password)
                print("successfully signed up")
                print("welcome" + " " + str(username))
                Terminal.menu2(user_session)
            else:
                Terminal.menu1()
        
        if choice != 1 and choice != 2:
            print("invalid input")
            Terminal.menu1()
    
    @staticmethod
    def menu2(user_session):
        print("1) create task\n2) edit task\n3) show tasks list\n4) show tagged tasks\n5) show tags\n6) exit")
        choice = int(input("choose an option: "))
        
        if choice == 1:
            user_id = user_session.id
            title = input("title: ")
            desc = input("desc: ")
            creation_date = dt.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
            lastmodification_date = dt.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
            deadline_choice = int(input("1)has a deadline\n2)no deadline\nyour choice: "))
            if deadline_choice == 1:
                deadline_date = input("deadline(year/month/day, e.g., 2023/05/16): ")
            if deadline_choice == 2:
                deadline_date = None
            if deadline_choice != 1 and deadline_choice !=2:
                print("invalid input")
            active = True
            tags = input("enter tags('tag1,tag2,... , e.g., work,school,home):")
            db.DB_Task.add_task(user_id, title, desc, creation_date, lastmodification_date,deadline_date, active, tags)
            if tags != "":
                db.DB_Tag.add_tag(tags, user_session)
            print("task successfully added")
            Terminal.menu2(user_session)
        
        if choice == 2:
            task_id = int(input("task id: "))
            title = input("new title: ")
            desc = input("new desc: ")
            lastmodification_date = dt.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
            deadline_choice = int(input("1)has a deadline\n2)no deadline\nyour choice: "))
            if deadline_choice == 1:
                deadline_date = input("deadline(year/month/day, e.g., 2023/05/16): ")
            if deadline_choice == 2:
                deadline_date = None
            if deadline_choice != 1 and deadline_choice !=2:
                print("invalid input")
            activity_state = int(input("1)active\n2)inactive\nyour choice: "))
            if activity_state == 1:
                active = True
            if activity_state == 2:
                active = False
            if activity_state != 1 and activity_state !=2:
                print("input invalid")
            tags = input("enter tags('tag1,tag2,... , e.g., work,school,home):")
            db.DB_Task.edit_task(task_id, title, desc, lastmodification_date, deadline_date, active, tags)
            if tags != "":
                db.DB_Tag.add_tag(tags, user_session)
            print("task successfully edited")
            Terminal.menu2(user_session)
        
        if choice == 3:
            sorting = input("sorting(u = last edit date, c = creation date, e = deadline date | a = ascending, d = descending | g = grouped by done or not yet done, n = not grouped by done or not yet done | e.g., cag): ")
            db.DB_Task.show_tasks(sorting, user_session)
            print("-----------------------------------------------")
            task_id = input("task id: ")
            db.DB_Task.show_task(task_id)
            Terminal.menu2(user_session)

        if choice == 4:
            tag = input("tag: ")
            sorting = input("sorting(u = last edit date, c = creation date, e = deadline date | a = ascending, d = descending | g = grouped by done or not yet done, n = not grouped by done or not yet done | e.g., cag): ")
            tagged_task_ids = db.DB_Tag.get_tagged_tasks(tag, user_session)
            db.DB_Task.show_tagged_tasks(tagged_task_ids, sorting, user_session)
            print("-----------------------------------------------")
            Terminal.menu2(user_session)

        if choice == 5:
            db.DB_Tag.show_tags(user_session)
            print("-----------------------------------------------")
            Terminal.menu2(user_session)

        if choice == 6:
            sys.exit()

Terminal.menu1()