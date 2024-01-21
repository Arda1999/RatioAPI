
from flask import Flask, jsonify, request, make_response, abort
from flask_restx import Api, Resource, reqparse
import os
from werkzeug.datastructures import FileStorage
from functools import wraps
import csv
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\Codes\RatioAPI\data\sample_db.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////usr/src/app/data/sample_db.db'

app.config['CSV_DIR'] = './csv'
 
db = SQLAlchemy()
db.init_app(app)


class Customers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False)


api = Api(app, version='1.0.0', title='Customers API', description='API for managing customers')
main = api.namespace('/', description='GET/POST to database.')

api.add_namespace(main)


@main.route('/write-objects')
class GetDatabase(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('csv', type=FileStorage, location='files')
    @api.doc(parser=parser) 
    def post(self):
        if len(request.files) != 0:
            if 'csv' in request.files:
                f = request.files['csv']
                filename = f.filename
                if filename != '':
                    file_ext = os.path.splitext(filename)[1]
                    if not file_ext == '.csv':
                        return make_response('Not a valid CSV file!', 400)
                    
                    f.save(filename)
                else:
                    return make_response('Missing csv field in the body!', 400)
            else:
                return make_response('Missing csv field in the body!', 400)
        else:
            return make_response('Incomplete request body!', 400)

        with open(filename, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            header = next(reader, None)
        print(header)
        if header != ['name', 'email']:

            return make_response("CSV Header mismatch.",400)
        else:
            with open(filename, 'r') as csvfile:
                csv_reader = csv.DictReader(csvfile)
                for row in csv_reader:
                    # Veritabanına ekle
                    new_customer = Customers(name=row['name'], email=row['email'])
                    db.session.add(new_customer)
                    db.session.commit()
        return make_response("User/s succesfull added.",200)

@main.route('/read-objects/')
class ReadObjectsResource(Resource):
    def get(self):
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 100, type=int)

        customers = Customers.query.paginate(page=page, per_page=per_page)

        customers_list = [{'name': customer.name, 'email': customer.email} for customer in customers.items]
        pagination = {
            'page': customers.page,
            'per_page': customers.per_page,
            'total_pages': customers.pages,
            'total_objects': customers.total,
        }

        return {'customers': customers_list, 'pagination': pagination}

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)