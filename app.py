from flask import Flask, session, url_for, render_template, redirect, request, flash
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

def get_user_data(user_id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM user WHERE user_id = %s", (user_id,))
    user_data = cursor.fetchone()
    cursor.close()
    return user_data

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/logout")
def logout():
    flash("Anda berhasil Logout!", 'success')
    session.pop("user_id", None)
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
            hashed_password = user[5]
            if check_password_hash(hashed_password, password):
                session['status'] = user[9] 
                status = session.get('status')
                if status == "aktif":
                    session['user_id'] = user[0]
                    session['username'] = user[1]
                    session['role'] = user[8]
                    flash('Login berhasil!', 'success')
                    return redirect(url_for('index'))
                else:
                    flash('Akun anda tidak dapat digunakan, silahkan hubungi admin!', 'danger')
                    return redirect(url_for('logout'))
            else:
                flash('Password salah. Silakan coba lagi.', 'danger')
                return redirect(url_for('login'))
        else:
            flash('Email tidak ditemukan. Silakan coba lagi.', 'danger')
            return redirect(url_for('login'))
    else:
        if "user_id" in session:
            return redirect(url_for("user"))
        else:
            return render_template("login.html")

@app.route('/admin')
def admin():
    if "user_id" in session:
        role = session.get('role')
        if role == "admin":
            return render_template("admin.html")
        else:
            flash('Anda tidak dapat mengakses halaman ini, silahkan login kembali!', 'danger')
            return redirect(url_for('logout'))
    else:
        flash("Anda belum Login!", 'danger')
        return redirect(url_for("login"))
    
@app.route('/admin/add', methods=["GET", "POST"])
def register():
    if "user_id" in session:
        role = session.get('role')
        if role == "admin":
            if request.method == "POST":
                username = request.form["usernameRegForm"]
                phone = request.form["phoneRegForm"]
                email = request.form["emailRegForm"]
                password = request.form["passRegForm"]
                domisili = request.form["locRegForm"]
                hashed_password = generate_password_hash(password)
                
                cur = mysql.connection.cursor()
                cur.execute("SELECT * FROM user WHERE email = %s", (email,))
                user = cur.fetchone()
                cur.close()
                
                if user:
                    flash('Email sudah digunakan. Silakan gunakan email lain.', 'danger')
                    return redirect(url_for('register'))
                else:
                    cur = mysql.connection.cursor()
                    cur.execute("INSERT INTO user (username, phone, location, email, password, role, status) VALUES (%s, %s, %s, %s, %s, %s, %s)", (username, phone, domisili, email, hashed_password, 'dokter', 'aktif'))
                    mysql.connection.commit()
                    cur.close()
                    
                    flash("Akun dokter telah ditambahkan!", 'success')
                    return redirect(url_for('admin'))
            else:
                return render_template("admin-add.html")
        else:
            flash('Anda tidak dapat mengakses halaman ini, silahkan login kembali!', 'danger')
            return redirect(url_for('logout'))
    else:
        flash("Anda belum Login!", 'danger')
        return redirect(url_for("login"))


@app.route('/user')
def user():
    if "user_id" in session:
        user_id = session['user_id']
        role = session.get('role')
        if role == "dokter":
            cursor = mysql.connection.cursor()
            cursor.execute("SELECT * FROM user WHERE user_id = %s", (user_id,))
            user_data = cursor.fetchone()  # Mengambil data pengguna dari database
            cursor.close()
            return render_template("user.html", user_data=user_data)
        if role == "admin":
            return redirect(url_for("admin"))
        else:
            flash('Anda tidak dapat mengakses halaman ini, silahkan login kembali!', 'danger')
            return redirect(url_for('logout'))
    else:
        flash("Anda belum Login!", 'danger')
        return redirect(url_for("login"))
    
#nantilah
@app.route('/user/deteksi')
def deteksi():
    if "user_id" in session:
        role = session.get('role')
        if role == "dokter":
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
            flash('Anda tidak dapat mengakses halaman ini, silahkan login kembali!', 'danger')
            return redirect(url_for('logout'))
    else:
        flash("Anda belum Login!", 'danger')
        return redirect(url_for("login"))

@app.route('/user/hasil-deteksi')
def hasil():
    if "user_id" in session:
        role = session.get('role')
        if role == "dokter":
            return render_template("user-detection-result.html")
        else:
            flash('Anda tidak dapat mengakses halaman ini, silahkan login kembali!', 'danger')
            return redirect(url_for('logout'))
    else:
        flash("Anda belum Login!", 'danger')
        return redirect(url_for("login"))
    
def create_wsgi_app():
    return app

if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='localhost', port=8080)
