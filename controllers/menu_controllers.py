from flask import jsonify, request
from config.database import get_db
from models.menu_model import Menus
from sqlalchemy.orm import Session
from datetime import datetime

def get_all_menu():
    db: Session = next(get_db())
    data = db.query(Menus).all()
    return jsonify([{
        "id_menu": k.id_menu,
        "nama": k.nama,
        "kategori": k.kategori,
        "harga": k.harga,
        "image": k.image,
        "deskripsi": k.deskripsi,
    } for k in data])

def add_menu():  
    db: Session = next(get_db())
    body = request.json

    new_data = Menus(
        nama=body["nama"],
        harga=body["harga"],
        kategori=body["kategori"],
        image=body["image"],
        deskripsi=body["deskripsi"],
    )
    db.add(new_data)
    db.commit()
    db.refresh(new_data)

    return jsonify({
        "message": "Data berhasil ditambahkan",
        "data": {
            "id_menu": new_data.id_menu,
            "nama": new_data.nama,
            "kategori": new_data.kategori,
            "harga": new_data.harga,
            "image": new_data.image,
            "deskripsi": new_data.deskripsi,
        }
    }), 201

def update_menu(id_menu):
    db: Session = next(get_db())
    body = request.json

    menu = db.query(Menus).filter(Menus.id_menu == id_menu).first()
    if not menu:
        return jsonify({"message": "Menu tidak ditemukan"}), 404

    # Update field sesuai data yang dikirim
    menu.nama = body.get("nama", menu.nama)
    menu.kategori = body.get("kategori", menu.kategori)
    menu.harga = body.get("harga", menu.harga)
    menu.image = body.get("image", menu.image)
    menu.deskripsi = body.get("deskripsi", menu.deskripsi)

    db.commit()
    db.refresh(menu)

    return jsonify({
        "message": "Data berhasil diperbarui",
        "data": {
            "id_menu": menu.id_menu,
            "nama": menu.nama,
            "kategori": menu.kategori,
            "harga": menu.harga,
            "image": menu.image,
            "deskripsi": menu.deskripsi,
        }
    }), 200


# =========================
# DELETE DATA MENU
# =========================
def delete_menu(id_menu):
    db: Session = next(get_db())
    menu = db.query(Menus).filter(Menus.id_menu == id_menu).first()
    if not menu:
        return jsonify({"message": "Menu tidak ditemukan"}), 404

    db.delete(menu)
    db.commit()

    return jsonify({"message": f"Data menu dengan id {id_menu} berhasil dihapus"}), 200
