from app import create_app, db

app = create_app()

if _name_ == '_main_':
    with app.app_context():
        db.create_all()
    app.run(debug=True)