# routes.py

from flask import render_template, request, redirect, flash
from app import app, mysql

@app.route('/')
def index():
    # Mendapatkan data keluarga dari database
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM asdos")
    data = cur.fetchall()
    cur.close()
    return render_template('index.html', data=data)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        # Ambil data dari form tambah
        name = request.form['name']
        c1 = request.form['c1']
        c2 = request.form['c2']
        c3 = request.form['c3']
        c4 = request.form['c4']
        c5 = request.form['c5']
        c6 = request.form['c6']

        # Masukkan data ke dalam database
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO asdos (name, c1, c2, c3, c4, c5, c6) VALUES (%s, %s, %s, %s, %s, %s, %s)", (name, c1, c2, c3, c4, c5, c6))
        mysql.connection.commit()
        cur.close()
        flash('Data berhasil ditambahkan', 'success')
        return redirect('/')
    return render_template('add.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    if request.method == 'POST':
        # Ambil data dari form edit
        name = request.form['name']
        c1 = request.form['c1']
        c2 = request.form['c2']
        c3 = request.form['c3']
        c4 = request.form['c4']
        c5 = request.form['c5']
        c6 = request.form['c6']

        # Ubah data dalam database
        cur = mysql.connection.cursor()
        cur.execute("UPDATE asdos SET name = %s, c1 = %s, c2 = %s, c3 = %s, c4 = %s, c5 = %s, c6 = %s WHERE id = %s", (name, c1, c2, c3, c4, c5, c6, id))
        mysql.connection.commit()
        cur.close()
        flash('Data berhasil diubah', 'success')
        return redirect('/')
    else:
        # Tampilkan data keluarga yang akan diubah dalam form
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM asdos WHERE id = %s", (id,))
        data = cur.fetchone()
        cur.close()
        return render_template('edit.html', data=data)

@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    # Hapus data keluarga dari database
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM asdos WHERE id = %s", (id,))
    mysql.connection.commit()
    cur.close()
    flash('Data berhasil dihapus', 'success')
    return redirect('/')

@app.route('/home')
def home():
    return render_template ('home.html')


@app.route('/generate')
def calculate_profile(criteria_weights, criteria_values):
    if len(criteria_weights) != len(criteria_values):
        raise ValueError("Number of criteria weights must match number of criteria values")

    # Hitung nilai total profil
    total_score = sum(weight * value for weight, value in zip(criteria_weights, criteria_values))

    return total_score

# Contoh penggunaan
criteria_weights = [3, 3, 4, 3, 3, 4]  # Bobot untuk masing-masing kriteria 
criteria_values = [4, 5, 4, 3, 3, 3]  # Nilai untuk masing-masing kriteria

# Hitung profil berdasarkan kriteria dan nilai yang diberikan
profile_score = calculate_profile(criteria_weights, criteria_values)

print("Profile Score:", profile_score)
