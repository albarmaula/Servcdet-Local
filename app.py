from flask import Flask, session, url_for, render_template, redirect, request, flash
# from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = "1234567890"


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'servcdet'
mysql = MySQL(app)

def get_user_id(username):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT id FROM users WHERE username = %s", (username,))
    user_id = cursor.fetchone()[0]
    cursor.close()
    return user_id

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("index"))

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["emailForm"]
        password = request.form["passForm"]
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM user WHERE email = %s", (email,))
        user = cur.fetchone()
        cur.close()
        
        if user:
            username = user[1]
            hashed_password = user[4]
            if check_password_hash(hashed_password, password):
                session['username'] = user[1]
                flash('Login berhasil!', 'success')
                return redirect(url_for('index'))
            else:
                flash('Password salah. Silakan coba lagi.', 'error')
                return redirect(url_for('login'))
        else:
            flash('Email tidak ditemukan. Silakan coba lagi.', 'error')
            return redirect(url_for('login'))
    else:
        if "username" in session:
            return redirect(url_for("user"))
        else:
            return render_template("login.html")
    return render_template("login.html")

@app.route('/admin')
def admin():
    if "username" in session:
        user = session["username"]
        return redirect(url_for("user", username="Admin!"))
    else:
        flash("You are not logged in!")
        return redirect(url_for("login"))
    
@app.route('/admin/add', methods=["GET", "POST"])
def register():
    if "username" in session:
        user = session["username"]
        if request.method == "POST":
            username = request.form["usernameRegForm"]
            phone = request.form["phoneRegForm"]
            email = request.form["emailRegForm"]
            password = request.form["passRegForm"]
            hashed_password = generate_password_hash(password)
            
            cur = mysql.connection.cursor()
            cur.execute("SELECT * FROM user WHERE email = %s", (email,))
            user = cur.fetchone()
            cur.close()
            
            if user:
                flash('Email sudah digunakan. Silakan gunakan email lain.', 'error')
                return redirect(url_for('register'))
            else:
                cur = mysql.connection.cursor()
                cur.execute("INSERT INTO user (username, phone, email, password, role, status) VALUES (%s, %s, %s, %s, %s, %s)", (username, phone, email, hashed_password, 'dokter', 'aktif'))
                mysql.connection.commit()
                cur.close()
                
                flash('Registrasi berhasil. Silakan login.', 'success')
                session['username'] = user[1]
                flash("Akun dokter telah ditambahkan!")
                return redirect(url_for("user"))
                # return redirect(url_for('admin'))
        else:
            return render_template("admin-add.html")
    else:
        flash("You are not logged in!")
        return redirect(url_for("login"))


@app.route('/user')
def user():
    if "username" in session:
        user = session["username"]
        return render_template("user.html")
    else:
        return redirect(url_for("login"))
    
#nantilah
@app.route('/user/deteksi')
def deteksi():
    if "username" in session:
        user = session["username"]
        if request.method == 'POST':
            # nama_pasien = request.form['nameDetForm']
            # umur_pasien = request.form['ageDetForm']
            # nik_pasien = request.form['idDetForm']
            # no_pasien = request.form['phoneDetForm']
            # image = request.files['imgDetForm']
            
            # # Baca gambar dan ubah menjadi array
            # img = Image.open(io.BytesIO(image.read()))
            # img_array = np.array(img)
            
            # # Contoh: Mendapatkan hasil prediksi (dummy)
            # hasil_prediksi = model.predict([gambar_yang_telah_diproses])[0]
            # label = "Normal" if hasil_prediksi == 0 else "Tidak Normal"
            
            # username = session['username']
            # user_id = get_user_id(username)
            
            # cursor = mysql.connection.cursor()
            # cursor.execute("INSERT INTO detection (image, label, patient_name, patient_phone, patient_age, patient_id, user_id) VALUES (%s, %s, %s, %s, %s, %s, %s)",
            #             (image, label, nama_pasien, no_pasien, umur_pasien, nik_pasien, user_id))
            # mysql.connection.commit()
            # cursor.close()

            # flash('Data berhasil ditambahkan', 'success')
            return redirect(url_for('hasil'))
        else:
            return render_template("user-detection.html")
    else:
        flash("You are not logged in!")
        return redirect(url_for("login"))

@app.route('/user/hasil-deteksi')
def hasil():
    if "username" in session:
        user = session["username"]
        return render_template("user-detection-result.html")
    else:
        flash("You are not logged in!")
        return redirect(url_for("login"))
    
def create_wsgi_app():
    return app

if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='localhost', port=8080)
