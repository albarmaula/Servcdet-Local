from flask import Flask, session, url_for, render_template, redirect, request, flash, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask_mysqldb import MySQL
import os
from werkzeug.utils import secure_filename
import uuid as uuid
import numpy as np
import os
import pickle
from tensorflow.keras.preprocessing.image import img_to_array, load_img
from tensorflow.keras.applications import ResNet50, imagenet_utils
from tensorflow.keras.models import load_model
import joblib

app = Flask(__name__)
app.secret_key = "1234567890"

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'servcdet'
mysql = MySQL(app)

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'bmp', 'tiff', 'tif', 'svg', 'webp', 'heic', 'ico', 'raw', 'dng', 'ai', 'eps', 'psd', 'pdf'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

###########################################(MACHINE LEARNING)#############################################################
print("[INFO] Loading The Machine Learning...")
resnet_model = ResNet50(weights="imagenet", include_top=False)
scaler = joblib.load("ml/.2scaler.pkl")
pca = joblib.load("ml/.2pca.pkl")
svm_classifier = joblib.load("ml/.2svm_classifier.pkl")
with open("ml/2le.cpickle", "rb") as f:
    le = pickle.load(f)

def preprocess_image(image_path):
    image = load_img(image_path, target_size=(224, 224))
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image = imagenet_utils.preprocess_input(image)
    features = resnet_model.predict(image)
    features = features.reshape((features.shape[0], -1))
    features = scaler.transform(features)
    features = pca.transform(features)
    return features

#Test ML
@app.route("/detect", methods=["GET", "POST"])
def detect():
    if request.method == "POST":
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            features = preprocess_image(filepath)
            confidence = svm_classifier.predict_proba(features)
            max_confidence = np.max(confidence)
            if max_confidence < 0.6: 
                label = "Gambar tidak sesuai"
                confidence_score = max_confidence * 100
            else:
                prediction = svm_classifier.predict(features)
                label = le.inverse_transform(prediction)[0] 
                confidence_score = confidence[0][prediction[0]] * 100
            os.remove(filepath)
            return render_template("detect.html", label=label, confidence=confidence_score)
    return render_template("detect.html")

###########################################(FUNCTIONS)#############################################################
#Done
@app.route('/change_status_detection', methods=['POST'])
def change_status_detection():
    if "user_id" in session:
        data = request.get_json()
        detection_id = data.get('id')
        if detection_id:
            cursor = mysql.connection.cursor()
            cursor.execute("SELECT status FROM detection WHERE detection_id = %s", (detection_id,))
            current_status = cursor.fetchone()
            if current_status:
                new_status = 'non-aktif' if current_status[0] == 'aktif' else 'aktif'
                cursor.execute("UPDATE detection SET status = %s WHERE detection_id = %s", (new_status, detection_id))
                mysql.connection.commit()
                cursor.close()
                flash('Status berhasil diperbarui!', 'success')
                return jsonify(success=True)
            else:
                flash('ID tidak valid!', 'danger')
                return jsonify(success=False, message="Invalid ID"), 400
        else:
            flash('ID tidak valid!', 'danger')
            return jsonify(success=False, message="Invalid ID"), 400
    else:
        flash('Anda tidak diizinkan untuk melakukan aksi ini!', 'danger')
        return jsonify(success=False, message="Unauthorized"), 403

#Done
@app.route('/uploadpp', methods=['POST'])
def uploadpp():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        if uploaded_file and allowed_file(uploaded_file.filename):
            filename = secure_filename(uploaded_file.filename)
            pic_name = "pp_" + str(uuid.uuid1()) + "_" + filename
            uploaded_file.save(os.path.join(app.config['UPLOAD_FOLDER'], pic_name))
            
            user_id = session.get('user_id')
            cur = mysql.connection.cursor()
            cur.execute("UPDATE user SET profile_picture = %s WHERE user_id = %s", (pic_name, user_id))
            mysql.connection.commit()
            cur.close()
            flash("Foto profil anda telah diubah!", 'success')
            return redirect(url_for('doctor'))
        else:
            flash('Tolong unggah file gambar dengan ekstensi yang benar!', 'danger')
            return redirect(url_for('doctor'))

        
###########################################(THE PAGE)#############################################################
print("[INFO] Loading The Page...")
#Done
@app.route('/')
def index():
    return render_template("index.html")

#Done
@app.route("/logout")
def logout():
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
                    flash('Akun anda tidak dapat digunakan, Silahkan hubungi admin!', 'danger')
                    return redirect(url_for('logout'))
            else:
                flash('Password salah! Silakan coba lagi!', 'danger')
                return redirect(url_for('login'))
        else:
            flash('Email tidak ditemukan! Silakan coba lagi!', 'danger')
            return redirect(url_for('login'))
    else:
        if "user_id" in session:
            return redirect(url_for("user"))
        else:
            return render_template("login.html")
        
###########################################(DOCTOR)#############################################################
#Done
@app.route('/doctor')
def doctor():
    if "user_id" in session:
        role = session.get('role')
        if role == "dokter":
            user_id = session.get('user_id')
            cursor = mysql.connection.cursor()
            cursor.execute("SELECT * FROM user WHERE user_id = %s", (user_id,))
            user_data = cursor.fetchone()
            
            page = request.args.get('page', 1, type=int)
            per_page = 10
            offset = (page - 1) * per_page
            cursor.execute("SELECT COUNT(*) FROM detection WHERE user_id = %s AND status = %s", (user_id, 'aktif'))
            total = cursor.fetchone()[0]
            
            cursor.execute("""
                SELECT d.detection_id, d.image, d.label, d.time, p.username AS patient_username, d.note, u.username AS doctor_username, d.confidence, p.nik
                FROM detection d
                JOIN patient p ON d.patient_id = p.id
                JOIN user u ON d.user_id = u.user_id
                WHERE d.user_id = %s AND d.status = 'aktif' LIMIt %s OFFSET %s
            """, (user_id, per_page, offset))
            detection_data = cursor.fetchall()
            cursor.close()
            return render_template("doctor.html", user_data=user_data, detection_data=detection_data, page=page, per_page=per_page, total=total)
        if role == "admin":
            return redirect(url_for("admin"))
        if role == "superadmin":
            return redirect(url_for("superadmin"))
        else:
            flash('Anda tidak dapat mengakses halaman ini! Silahkan login kembali!', 'danger')
            return redirect(url_for('logout'))
    else:
        flash("Anda belum Login!", 'danger')
        return redirect(url_for("login"))
    
#done
@app.route('/doctor/detection', methods=["GET", "POST"])
def doctor_detect():
    if "user_id" in session:
        role = session.get('role')
        if role == "dokter":
            cur = mysql.connection.cursor()
            cur.execute("SELECT id, username FROM patient")
            patients = cur.fetchall()
            cur.close()

            if request.method == "POST":
                patient_id = request.form['patientDetForm']
                file = request.files['imgDetForm']
                doct_id = session.get('user_id')
                if file.filename == '':
                    flash('Tolong masukkan data formulir secara lengkap!', 'danger')
                if file and allowed_file(file.filename):
                    filename = secure_filename(file.filename)
                    file_name = "det_" + str(uuid.uuid1()) + "_" + filename
                    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file_name)
                    file.save(filepath)
                    features = preprocess_image(filepath)
                    confidence = svm_classifier.predict_proba(features)
                    max_confidence = np.max(confidence)
                    if max_confidence < 0.6:
                        flash('Tolong unggah gambar yang relevan dan/atau berkualitas baik!', 'danger')
                        os.remove(filepath)
                        return redirect(url_for("doctor_detect"))
                    else:
                        prediction = svm_classifier.predict(features)
                        label = le.inverse_transform(prediction)[0]
                        confidence_score = confidence[0][prediction[0]] * 100
                        cur = mysql.connection.cursor()
                        cur.execute("INSERT INTO detection (image, label, patient_id, note, user_id, confidence, status) VALUES (%s,%s,%s,%s,%s,%s,%s)", (file_name, label, patient_id,'', doct_id, confidence_score, 'aktif'))
                        mysql.connection.commit()
                        detection_id = cur.lastrowid
                        cur.close()
                        return redirect(url_for('doctor_detection_result', detection_id=detection_id))
                        flash('Data deteksi telah disimpan!', 'success')
                else:
                    flash('Tolong unggah file gambar dengan ekstensi yang benar!', 'danger')
                    return redirect(url_for("doctor_detect"))
            else:
                return render_template("doctor-detection.html", patients=patients)
        else:
            flash('Anda tidak dapat mengakses halaman ini! Silahkan login kembali!', 'danger')
            return redirect(url_for('logout'))
    else:
        flash("Anda belum Login!", 'danger')
        return redirect(url_for("login"))

#done
@app.route('/doctor/detection-result', methods=["GET", "POST"])
def doctor_detection_result():
    if "user_id" in session:
        role = session.get('role')
        if role == "dokter":
            user_id = session.get('user_id')
            detection_id = request.args.get('detection_id')
            if request.method == "POST":
                detection_id = request.form['detection_id']
                note = request.form['note']
                cur = mysql.connection.cursor()
                cur.execute('UPDATE detection SET note = %s WHERE detection_id = %s', (note, detection_id))
                mysql.connection.commit()
                cur.close()
                flash('Catatan berhasil diperbarui!', 'success')
                return redirect(url_for('doctor'))
            if detection_id:
                cur = mysql.connection.cursor()
                cur.execute("""
                    SELECT d.detection_id, d.image, d.label, d.time, p.username AS patient_username, d.note, d.user_id, d.confidence, p.nik
                    FROM detection d
                    JOIN patient p ON d.patient_id = p.id
                    WHERE d.detection_id = %s AND d.user_id = %s AND d.status = 'aktif'
                """, (detection_id, user_id))
                detection_data = cur.fetchone()
                cur.close()
                if detection_data:
                    return render_template("doctor-detection-result.html", detection_data=detection_data)
                else:
                    flash('Data deteksi tidak ditemukan!', 'danger')
                    return redirect(url_for('doctor'))
            else:
                flash('ID deteksi tidak ditemukan!', 'danger')
                return redirect(url_for('doctor'))
        else:
            flash('Anda tidak dapat mengakses halaman ini! Silahkan login kembali!', 'danger')
            return redirect(url_for('logout'))
    else:
        flash("Anda belum Login!", 'danger')
        return redirect(url_for("login"))

###########################################(ADMIN)#############################################################
#Done
@app.route('/admin', methods=["GET", "POST"])
def admin():
    if "user_id" in session:
        role = session.get('role')
        if role == "admin":
            if request.method == "POST":
                name = request.form["namePatientForm"]
                nik = request.form["nikPatientForm"]
                phone = request.form["phonePatientForm"]
                birthday = request.form["birthdayPatientForm"]
                status = request.form["statusPatientForm"]
                
                cur = mysql.connection.cursor()
                cur.execute("SELECT * FROM patient WHERE nik = %s", (nik,))
                existing_nik = cur.fetchone()
                
                if existing_nik:
                    flash('Pasien dengan NIK ini sudah digunakan!', 'danger')
                    cur.close()
                    return redirect(url_for('admin'))
                else:
                    cur.execute("INSERT INTO patient (nik, username, phone, birthday, status) VALUES (%s, %s, %s, %s, %s)", (nik, name, phone, birthday, status))
                    mysql.connection.commit()
                    cur.close()
                    
                    flash("Pasien telah ditambahkan!", 'success')
                    return redirect(url_for("admin"))
            else:
                user_id = session.get('user_id')
                cursor = mysql.connection.cursor()
                cursor.execute("SELECT * FROM user WHERE user_id = %s", (user_id,))
                user_data = cursor.fetchone()

                page = request.args.get('page', 1, type=int)
                per_page = 10
                offset = (page - 1) * per_page
                cursor.execute("SELECT COUNT(*) FROM patient")
                total = cursor.fetchone()[0]
                
                cursor.execute("SELECT * FROM patient LIMIT %s OFFSET %s", (per_page, offset))
                patient_data = cursor.fetchall()
                cursor.close()
                return render_template("admin.html", user_data=user_data, patient_data=patient_data, page=page, per_page=per_page, total=total)
        if role == "dokter":
            return redirect(url_for("doctor"))
        if role == "superadmin":
            return redirect(url_for("superadmin"))
        else:
            flash('Anda tidak dapat mengakses halaman ini! Silahkan login kembali!', 'danger')
            return redirect(url_for('logout'))
    else:
        flash("Anda belum Login!", 'danger')
        return redirect(url_for("login"))
    
@app.route('/admin/patient/<int:taken_patient_id>', methods=["GET", "POST"])
def admin_patient(taken_patient_id):
    if "user_id" in session:
        role = session.get('role')
        if role == "admin":
            if request.method == 'POST':
                new_name = request.form['new_name']
                new_nik = request.form['new_nik']
                new_phone = request.form['new_phone']
                new_birthday = request.form['new_birthday']
                new_status = request.form['new_status']
                
                cursor = mysql.connection.cursor()
                cursor.execute("UPDATE patient SET username = %s, phone = %s, nik = %s, birthday = %s, status = %s WHERE id = %s", (new_name, new_phone, new_nik, new_birthday, new_status, taken_patient_id))
                mysql.connection.commit()
                cursor.close()
                flash("Data pasien telah diubah!", 'success')
                return redirect(url_for('admin_patient', taken_patient_id=taken_patient_id))
            else:
                cursor = mysql.connection.cursor()
                cursor.execute("SELECT * FROM patient WHERE id = %s", (taken_patient_id,))
                patient_data = cursor.fetchone()
                
                page = request.args.get('page', 1, type=int)
                per_page = 10
                offset = (page - 1) * per_page
                cursor.execute("SELECT COUNT(*) FROM detection WHERE patient_id = %s", (taken_patient_id,))
                total = cursor.fetchone()[0]

                cursor.execute("""
                    SELECT d.detection_id, d.image, d.label, d.time, p.username AS patient_username, d.note, u.username AS doctor_username, d.confidence, p.nik
                    FROM detection d
                    JOIN patient p ON d.patient_id = p.id
                    JOIN user u ON d.user_id = u.user_id
                    WHERE d.patient_id = %s AND d.status = 'aktif' LIMIt %s OFFSET %s
                """, (taken_patient_id, per_page, offset))
                detection_data = cursor.fetchall()
                
                cursor.close()
                return render_template("admin-patient.html", taken_patient_id=taken_patient_id, patient_data=patient_data, detection_data=detection_data, page=page, per_page=per_page, total=total)
        else:
            flash('Anda tidak dapat mengakses halaman ini! Silahkan login kembali!', 'danger')
            return redirect(url_for('logout'))
    else:
        flash("Anda belum Login!", 'danger')
        return redirect(url_for("login"))

###########################################(SUPERADMIN)#############################################################
#Done   
@app.route('/superadmin/add', methods=["GET", "POST"])
def register():
    if "user_id" in session:
        role = session.get('role')
        if role == "superadmin":
            if request.method == "POST":
                username = request.form["usernameRegForm"]
                phone = request.form["phoneRegForm"]
                email = request.form["emailRegForm"]
                role = request.form["roleRegForm"]
                password = request.form["passRegForm"]
                hashed_password = generate_password_hash(password)
                
                cur = mysql.connection.cursor()
                cur.execute("SELECT * FROM user WHERE email = %s", (email,))
                user = cur.fetchone()
                cur.close()
                
                if user:
                    flash('Email sudah digunakan! Silakan gunakan email lain!', 'danger')
                    return redirect(url_for('register'))
                else:
                    cur = mysql.connection.cursor()
                    cur.execute("INSERT INTO user (username, phone, email, password, role, status, profile_picture) VALUES (%s, %s, %s, %s, %s, %s, %s)", (username, phone, email, hashed_password, role, 'aktif', 'user-black.png'))
                    mysql.connection.commit()
                    cur.close()
                    
                    flash("Akun pengguna telah ditambahkan!", 'success')
                    return redirect(url_for("superadmin"))
            else:
                return render_template("superadmin-add.html")
        else:
            flash('Anda tidak dapat mengakses halaman ini! Silahkan login kembali!', 'danger')
            return redirect(url_for('logout'))
    else:
        flash("Anda belum Login!", 'danger')
        return redirect(url_for("login"))
    
#Done
@app.route('/superadmin')
def superadmin():
    if "user_id" in session:
        role = session.get('role')
        if role == "superadmin":
            user_id = session.get('user_id')
            cursor = mysql.connection.cursor()
            cursor.execute("SELECT * FROM user WHERE user_id = %s", (user_id,))
            user_data = cursor.fetchone()

            active_page = request.args.get('active_page', 1, type=int)
            inactive_page = request.args.get('inactive_page', 1, type=int)
            per_page = 10

            active_offset = (active_page - 1) * per_page
            cursor.execute("SELECT COUNT(*) FROM user WHERE status = %s", ('aktif',))
            active_total = cursor.fetchone()[0]
            cursor.execute("SELECT * FROM user WHERE status = %s LIMIT %s OFFSET %s", ('aktif', per_page, active_offset))
            active_users = cursor.fetchall()

            inactive_offset = (inactive_page - 1) * per_page
            cursor.execute("SELECT COUNT(*) FROM user WHERE status = %s", ('non-aktif',))
            inactive_total = cursor.fetchone()[0]
            cursor.execute("SELECT * FROM user WHERE status = %s LIMIT %s OFFSET %s", ('non-aktif', per_page, inactive_offset))
            inactive_users = cursor.fetchall()

            cursor.close()
            return render_template("superadmin.html", user_data=user_data, active_users=active_users, inactive_users=inactive_users, active_page=active_page, inactive_page=inactive_page, per_page=per_page, active_total=active_total, inactive_total=inactive_total)
        else:
            flash('Anda tidak dapat mengakses halaman ini! Silahkan login kembali!', 'danger')
            return redirect(url_for('logout'))
    else:
        flash("Anda belum Login!", 'danger')
        return redirect(url_for("login"))
    
#Done
@app.route('/superadmin/user/<int:taken_user_id>', methods=['GET', 'POST'])
def superadmin_user(taken_user_id):
    if "user_id" in session:
        role = session.get('role')
        if role == "superadmin":
            if request.method == 'POST':
                if 'new_password' in request.form:
                    password = request.form['new_password']
                    new_password = generate_password_hash(password)
                    cursor = mysql.connection.cursor()
                    cursor.execute("UPDATE user SET password = %s WHERE user_id = %s", (new_password, taken_user_id))
                    mysql.connection.commit()
                    cursor.close()
                    flash("Password telah diperbarui!", 'success')
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
                    flash("Data pengguna telah diubah!", 'success')
                    return redirect(url_for('superadmin_user', taken_user_id=taken_user_id))
            else:
                cursor = mysql.connection.cursor()
                cursor.execute("SELECT * FROM user WHERE user_id = %s", (taken_user_id,))
                user_data = cursor.fetchone()

                active_page = request.args.get('active_page', 1, type=int)
                inactive_page = request.args.get('inactive_page', 1, type=int)
                per_page = 10
                
                active_offset = (active_page - 1) * per_page
                cursor.execute("SELECT COUNT(*) FROM detection WHERE user_id = %s AND status = 'aktif'", (taken_user_id,))
                active_total = cursor.fetchone()[0]
                
                cursor.execute("""
                    SELECT d.detection_id, d.image, d.label, d.time, p.username AS patient_username, d.note, u.username AS doctor_username, d.confidence, p.nik, d.status
                    FROM detection d
                    JOIN patient p ON d.patient_id = p.id
                    JOIN user u ON d.user_id = u.user_id
                    WHERE d.user_id = %s AND d.status = 'aktif' LIMIT %s OFFSET %s
                """, (taken_user_id, per_page, active_offset))
                active_detections = cursor.fetchall()

                inactive_offset = (inactive_page - 1) * per_page
                cursor.execute("SELECT COUNT(*) FROM detection WHERE user_id = %s AND status = 'non-aktif'", (taken_user_id,))
                inactive_total = cursor.fetchone()[0]
                
                cursor.execute("""
                    SELECT d.detection_id, d.image, d.label, d.time, p.username AS patient_username, d.note, u.username AS doctor_username, d.confidence, p.nik,  d.status
                    FROM detection d
                    JOIN patient p ON d.patient_id = p.id
                    JOIN user u ON d.user_id = u.user_id
                    WHERE d.user_id = %s AND d.status = 'non-aktif' LIMIT %s OFFSET %s
                """, (taken_user_id, per_page, inactive_offset))
                inactive_detections = cursor.fetchall()
                
                cursor.close()
                return render_template("superadmin-user.html", user_data=user_data, active_detections=active_detections, inactive_detections=inactive_detections, active_page=active_page, inactive_page=inactive_page, per_page=per_page, active_total=active_total, inactive_total=inactive_total, taken_user_id=taken_user_id)
        else:
            flash('Anda tidak dapat mengakses halaman ini! Silahkan login kembali!', 'danger')
            return redirect(url_for('logout'))
    else:
        flash("Anda belum Login!", 'danger')
        return redirect(url_for("login"))
    
print("[INFO] Done :)")

def create_wsgi_app():
    return app

if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='localhost', port=8080)
