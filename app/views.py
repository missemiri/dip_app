from app import app

import os
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from flask import send_from_directory
from . import predict


@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method=="POST":
        file = request.files['file']
        if request.form['file'] == '推論を開始':
            if file.filename == '':
                return render_template("public/index.html", message='ファイルを選択してください')
            else:
                file.save(os.path.join("app/CSV_files", file.filename))
                predict.dip_predict(os.path.join("app/CSV_files", file.filename))
                return redirect(url_for('download'))
        return render_template("public/index.html")
    return render_template("public/index.html")
    


@app.route('/download', methods=['GET', 'POST'])
def download():
    if request.method=="POST":
        if request.form['download'] == '結果をダウンロード':
            download = request.form['download']
            try:
                return send_from_directory(
                    "CSV_files", filename='output.csv', as_attachment=True
                )
            except FileNotFoundError:
                os.abort(404)
        elif request.form['download'] == '戻る':
            return redirect(url_for('hello'))
    return render_template("public/download.html")



