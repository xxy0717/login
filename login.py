import streamlit as st
from passlib.hash import pbkdf2_sha256
import sqlite3

# 创建数据库
conn = sqlite3.connect('users.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              email TEXT,
              password TEXT)''')
conn.commit()

# 注册功能
def register():
    st.header("用户注册")
    email = st.text_input("请输入您的Email：")
    password = st.text_input("请输入密码：", type="password")
    confirm_password = st.text_input("请确认密码：", type="password")
    if st.button("注册"):
        # 验证输入的密码和确认密码是否匹配
        if password != confirm_password:
            st.error("两次输入的密码不匹配！")
        else:
            # 检查是否存在相同的Email
            query = f"SELECT * FROM users WHERE email='{email}'"
            result = c.execute(query).fetchone()
            if result:
                st.error("该Email已被注册，请使用其他Email！")
            else:
                # 对密码进行加密
                hashed_password = pbkdf2_sha256.hash(password)
                # 将新用户插入到数据库中
                query = f"INSERT INTO users (email, password) VALUES ('{email}', '{hashed_password}')"
                c.execute(query)
                conn.commit()
                st.success("注册成功，请登录！")

# 登录功能
def login():
    st.header("用户登录")
    email = st.text_input("请输入您的Email：")
    password = st.text_input("请输入密码：", type="password")
    if st.button("登录"):
        # 检查输入的Email和密码是否与数据库匹配
        query = f"SELECT * FROM users WHERE email='{email}'"
        result = c.execute(query).fetchone()
        if result:
            if pbkdf2_sha256.verify(password, result[2]):
                st.success("登录成功！")
            else:
                st.error("密码不正确，请重新输入！")
        else:
            st.error("该Email未注册，请先注册！")

# 显示界面
def main():
    st.set_page_config(page_title="用户注册和登录")
    st.title("用户注册和登录")
    menu = ["用户注册", "用户登录"]
    choice = st.sidebar.selectbox("请选择功能：", menu)
    if choice == "用户注册":
        register()
    else:
        login()

if __name__ == '__main__':
    main()
