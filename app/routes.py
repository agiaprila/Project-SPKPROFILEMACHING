# routes.py

from flask import render_template, request, redirect, flash
from app import app, mysql

def calculate_bobot(gap):
    mapping = {
        0: 5.0,
        1: 4.5,
        -1: 4.0,
        2: 3.5,
        -2: 3.0,
        3: 2.5,
        -3: 2.0,
        4: 1.5,
        -4: 1.0
    }
    return mapping.get(gap, 0)  # Default value 0 if gap is not in the mapping

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

        #gap
        gap_1 = c1-3
        gap_2 = c2-3
        gap_3 = c3-4
        gap_4 = c4-3
        gap_5 = c5-3
        gap_6 = c6-4


        # Hitung bobot untuk masing-masing nilai bobot
        bobot_c1 = calculate_bobot(gap_1)
        bobot_c2 = calculate_bobot(gap_2)
        bobot_c3 = calculate_bobot(gap_3)
        bobot_c4 = calculate_bobot(gap_4)
        bobot_c5 = calculate_bobot(gap_5)
        bobot_c6 = calculate_bobot(gap_6)

        bobot = ((((bobot_c1 + bobot_c2) / 2) * 0.6) + (bobot_c3 * 0.4)) * 0.7 + ((((bobot_c5 + bobot_c6) / 2) * 0.6) + (bobot_c4 * 0.4)) * 0.3

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



