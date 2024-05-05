from flask import Flask, session, url_for, render_template, redirect, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask_mysqldb import MySQL
import os
from werkzeug.utils import secure_filename
import uuid as uuid
import hashlib
# import joblib
# import numpy as np
# import pickle
# from sklearn.svm import SVC


app = Flask(__name__)
app.secret_key = "1234567890"

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'servcdet'
mysql = MySQL(app)

# svm_model = joblib.load('svm_model.pkl')
# pca = joblib.load('pca_model.pkl')
# with open('scaler.pkl', 'rb') as f:
#     scaler = pickle.load(f)
    
# def process_image(image):
#     processed_image = resize_image(image)
#     # Konversi gambar ke bentuk yang sesuai untuk model
#     processed_image = convert_to_array(processed_image)
#     # Lakukan normalisasi atau pra-pemrosesan lainnya sesuai kebutuhan model
#     processed_image = apply_preprocessing(processed_image)
#     return processed_image

# @app.route('/detect', methods=['GET', 'POST'])
# def detect():
#     if request.method == 'POST':
#         image = request.files['image']
#         processed_image = process_image(image)
#         normalized_image = scaler.transform(processed_image)
#         transformed_image = pca.transform(normalized_image)
#         prediction = svm_model.predict(transformed_image)
#         return render_template('detect.html', prediction=prediction)
#     return render_template('detect.html', prediction=None)

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#Done
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

#Done
@app.route('/uploadpp', methods=['POST'])
def uploadpp():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            filename = secure_filename(uploaded_file.filename)
            pic_name = "pp_" + str(uuid.uuid1()) + "_" + filename
            uploaded_file.save(os.path.join(app.config['UPLOAD_FOLDER'], pic_name))
            
            user_id = session.get('user_id')
            cur = mysql.connection.cursor()
            cur.execute("UPDATE user SET profile_picture = %s WHERE user_id = %s", (pic_name, user_id))
            mysql.connection.commit()
            cur.close()
            flash("Foto profil anda telah diubah!", 'success')
            return redirect(url_for('user'))

#Done
@app.route('/')
def index():
    return render_template("index.html")

#Done
@app.route("/logout")
def logout():
    flash("Anda berhasil Logout!", 'success')
    session.pop("user_id", None)
    return redirect(url_for("index"))

#Done
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
                session['status'] = user[7] 
                status = session.get('status')
                if status == "aktif":
                    session['user_id'] = user[0]
                    session['username'] = user[1]
                    session['role'] = user[6]
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

#Done
@app.route('/user', methods=["GET", "POST"])
def user():
    if "user_id" in session:
        role = session.get('role')
        if role == "dokter":
            user_id = session.get('user_id')
            cursor = mysql.connection.cursor()
            cursor.execute("SELECT * FROM user WHERE user_id = %s", (user_id,))
            user_data = cursor.fetchone()
            cursor.execute("SELECT * FROM detection WHERE user_id = %s", (user_id,))
            detection_data = cursor.fetchall()
            cursor.close()
            return render_template("user.html", user_data=user_data, detection_data=detection_data)
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

#nantilah
@app.route('/user/hasil-deteksi')
def user_hasil():
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
    
#Done
@app.route('/admin')
def admin():
    if "user_id" in session:
        role = session.get('role')
        if role == "admin":
            user_id = session.get('user_id')
            cursor = mysql.connection.cursor()
            cursor.execute("SELECT * FROM user WHERE user_id = %s", (user_id,))
            user_data = cursor.fetchone()
            cursor.execute("SELECT * FROM user WHERE role = %s", ('dokter',))
            all_user_data = cursor.fetchall()
            cursor.close()
            return render_template("admin.html", user_data=user_data, all_user_data=all_user_data)
        else:
            flash('Anda tidak dapat mengakses halaman ini, silahkan login kembali!', 'danger')
            return redirect(url_for('logout'))
    else:
        flash("Anda belum Login!", 'danger')
        return redirect(url_for("login"))

#Done
@app.route('/admin/user/<int:taken_user_id>', methods=['GET', 'POST'])
def admin_user(taken_user_id):
    if "user_id" in session:
        role = session.get('role')
        if role == "admin":
            if request.method == 'POST':
                if 'new_password' in request.form:
                    password = request.form['new_password']
                    new_password = generate_password_hash(password)
                    
                    cursor = mysql.connection.cursor()
                    cursor.execute("UPDATE user SET password = %s WHERE user_id = %s", (new_password, taken_user_id))
                    mysql.connection.commit()
                    cursor.close()
                    flash("Password akun telah diperbarui!", 'success')
                    return redirect(url_for('admin_user', taken_user_id=taken_user_id))
                else:
                    new_name = request.form['new_name']
                    new_phone = request.form['new_phone']
                    new_email = request.form['new_email']
                    new_status = request.form['new_status']
                    
                    cursor = mysql.connection.cursor()
                    cursor.execute("UPDATE user SET username = %s, phone = %s, email = %s, status = %s WHERE user_id = %s", (new_name, new_phone, new_email, new_status, taken_user_id))
                    mysql.connection.commit()
                    cursor.close()
                    flash("Akun dokter telah diubah!", 'success')
                    return redirect(url_for('admin_user', taken_user_id = taken_user_id))
            else:
                cursor = mysql.connection.cursor()
                cursor.execute("SELECT * FROM user WHERE user_id = %s", (taken_user_id,))
                user_data = cursor.fetchone()
                cursor.execute("SELECT * FROM detection WHERE user_id = %s", (taken_user_id,))
                detection_data = cursor.fetchall()
                cursor.close()
                return render_template("admin-user.html", user_data=user_data, detection_data=detection_data)
        else:
            flash('Anda tidak dapat mengakses halaman ini, silahkan login kembali!', 'danger')
            return redirect(url_for('logout'))
    else:
        flash("Anda belum Login!", 'danger')
        return redirect(url_for("login"))
 
#Done   
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
                    cur.execute("INSERT INTO user (username, phone, email, password, role, status, profile_picture) VALUES (%s, %s, %s, %s, %s, %s, %s)", (username, phone, email, hashed_password, 'dokter', 'aktif', 'NULL'))
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
    
def create_wsgi_app():
    return app

if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='localhost', port=8080)
