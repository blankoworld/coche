# all the imports
from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash
import peewee

import flask_admin as admin
from flask_admin.contrib.peewee import ModelView

FLASKR_SETTINGS = 'settings.cfg'

# create our little application :)
app = Flask(__name__)
app.config.from_pyfile(FLASKR_SETTINGS, silent=True)

DATABASE_CONNECTION = peewee.SqliteDatabase(app.config['DATABASE'],
    check_same_thread=False)

class BaseModel(peewee.Model):
    class Meta:
        database = DATABASE_CONNECTION

class Contact(BaseModel):
    id = peewee.IntegerField(primary_key=True)
    name = peewee.CharField(max_length=80)
    email = peewee.CharField(max_length=120)
    phone_number = peewee.CharField(max_length=16)

    def __unicode__(self):
        return self.name

class Company(BaseModel):
    id = peewee.IntegerField(primary_key=True)
    name = peewee.CharField(max_length=200)
    description = peewee.TextField(null=False)
    address_street = peewee.CharField(max_length=300)
    address_city = peewee.CharField(max_length=300)
    address_zipcode = peewee.CharField(max_length=10)

    contact = peewee.ForeignKeyField(Contact) # Contact in this company

    def __unicode__(self):
        return self.name

class ContactAdmin(ModelView):
    column_exclude_list = ['id']

class CompanyAdmin(ModelView):
    # Visible columns in the list view
    column_exclude_list = ['id']

    # List of columns that can be sorted. For 'contact' column, use its email
    column_sortable_list = ('name', ('contact', Contact.email), 'address_city')

    # Full text search
    column_searchable_list = ('name', Contact.name)

    # Column filters
    column_filters = ('name',
                      'address_city',
                      Contact.name)

    form_ajax_refs = {
        'contact': {
            'fields': (Contact.name, 'email')
        }
    }

@app.route('/')
def index():
    return '<a href="/manage/">Manage data</a>'

if __name__ == '__main__':
    import logging
    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)

    admin = admin.Admin(app, name='Data Management', url='/manage')

    admin.add_view(ContactAdmin(Contact))
    admin.add_view(CompanyAdmin(Company))

    try:
        Contact.create_table()
        Company.create_table()
    except:
        pass

    app.run() # app.run(host='0.0.0.0') # run server publicly
