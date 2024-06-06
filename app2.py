
from flask import Flask, jsonify, render_template, request, url_for
import pymysql
import db_auth as au

app = Flask(__name__)

conn = pymysql.connect(host=au.host, user=au.user, passwd=au.password, database=au.database)
# conn = pymysql.connect(host=host, user=user, passwd=password, database=database)
cursor = conn.cursor()


@app.route("/")
def index():
    return "<h1 style='red'>O_O</h1>"

@app.route("/admin/new_product/")
def testPage():
    name = ""
    return render_template('admin_new_product.html', name=name)

@app.route("/admin/new_product/get/",  methods=['POST', 'GET'])
def newProduct():
    fname = request.form['firstname']
    sql_p = "INSERT INTO users_tbl (email, full_name, password) VALUES (%s, %s, %s)"
    cursor.execute(sql_p, ('email_example', fname, 'very-secret'))
    conn.commit()
    sql_2 = "SELECT * FROM users_tbl"
    cursor.execute(sql_2)
    result = cursor.fetchall()
    return render_template('test.html', name=result)

@app.route("/template1/")
def test():
    # name = url_for('static/template1/images', filename='happy-bearded-young-man.jpg') 
    name = ''
    return render_template('template1_templatemo_portfolio/index.html', name=name)


# -------------------------------------------- insta CRM app /begining/
@app.route("/instagram_crm")
def login_crm():
    return render_template('template2_insta_crm/login.html')

@app.route("/instagram_crm/users")
def users_crm():
    return render_template('template2_insta_crm/users.html')

@app.route("/instagram_crm/admin_acc")
def admin_crm():
   return render_template('template2_insta_crm/admin_acc.html')

@app.route("/instagram_crm/admin_see_chat")
def adminSeeChat_crm():
   return render_template('template2_insta_crm/admin_ans_to_user.html')
# -------------------------------------------- insta CRM app /end/

