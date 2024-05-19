# routes.py

from flask import render_template, request, redirect, flash
from app import app, mysql

@app.route('/')
def index():
    # Mendapatkan data keluarga dari database
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM asdos ORDER BY bobot DESC")
    data = cur.fetchall()
    cur.close()
    return render_template('index.html', data=data)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        # Ambil data dari form tambah
        name = request.form['name']
        c1 = float(request.form['c1'])
        c2 = float(request.form['c2'])
        c3 = float(request.form['c3'])
        c4 = float(request.form['c4'])
        c5 = float(request.form['c5'])
        c6 = float(request.form['c6'])

        #PERHITUNGANNYA
        bobot = ((((c1 + c2) / 2) * 0.6) + (c3 * 0.4)) * 0.7 + ((((c5 + c6) / 2) * 0.6) + (c4 * 0.4)) * 0.3

        # Masukkan data ke dalam database
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO asdos (name, c1, c2, c3, c4, c5, c6, bobot) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (name, c1, c2, c3, c4, c5, c6, bobot))
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
        cur.execute("UPDATE asdos SET name = %s, c1 = %s, c2 = %s, c3 = %s, c4 = %s, c5 = %s, c6 = %s   WHERE id = %s", (name, c1, c2, c3, c4, c5, c6,  id ))
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



