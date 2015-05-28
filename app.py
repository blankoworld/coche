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
    contact_id = peewee.IntegerField(primary_key=True)
    contact_nom = peewee.CharField(max_length=120)
    contact_prenom = peewee.CharField(max_length=120)
    contact_adresse_rue = peewee.CharField(max_length=254)
    contact_adresse_cp = peewee.CharField(max_length=10)
    contact_adresse_ville = peewee.CharField(max_length=120)
    contact_numero_prive = peewee.CharField(max_length=13)
    contact_numero_bureau = peewee.CharField(max_length=13)
    contact_courriel = peewee.CharField(max_length=254)
    contact_note = peewee.TextField()

    def __unicode__(self):
        return "%s %s" % (self.contact_prenom, self.contact_nom)

class Entreprise(BaseModel):
    entreprise_id = peewee.IntegerField(primary_key=True)
    entreprise_libelle = peewee.CharField(max_length=200)
    entreprise_rue = peewee.CharField(max_length=254)
    entreprise_cp = peewee.CharField(max_length=10)
    entreprise_ville = peewee.CharField(max_length=120)
    entreprise_telephone = peewee.CharField(max_length=13)
    entreprise_fax = peewee.CharField(max_length=13)
    entreprise_courriel = peewee.CharField(max_length=254)
    entreprise_site_web = peewee.CharField(max_length=500)
    entreprise_note = peewee.TextField()

    def __unicode__(self):
        return self.entreprise_libelle

class ContactAdmin(ModelView):
    column_exclude_list = ['contact_id']

class EntrepriseAdmin(ModelView):
    # Visible columns in the list view
    column_exclude_list = ['entreprise_id']

    # List of columns that can be sorted.
    column_sortable_list = ('entreprise_ville', 'entreprise_libelle')

    # Column filters
    column_filters = ('entreprise_ville',
                      'entreprise_cp',
                      'entreprise_libelle')

@app.route('/')
def index():
    return '<a href="/manage/">Manage data</a>'

if __name__ == '__main__':
    import logging
    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)

    admin = admin.Admin(app, name='Data Management', url='/manage')

    admin.add_view(ContactAdmin(Contact))
    admin.add_view(EntrepriseAdmin(Entreprise))

    try:
        Contact.create_table()
        Entreprise.create_table()
    except:
        pass

    app.run() # app.run(host='0.0.0.0') # run server publicly
