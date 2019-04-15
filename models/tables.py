import datetime

db.define_table('movies',
    Field('movie_title'),
    Field('movie_description', 'text'),
    Field('movie_cover', 'upload'),
    Field('movie_release_date', 'datetime', default=datetime.datetime.now())
)