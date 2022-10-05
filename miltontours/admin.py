'''
CREATING A NEW DATABASE
-----------------------
Read explanation here: https://flask-sqlalchemy.palletsprojects.com/en/2.x/contexts/

In the terminal navigate to the project folder just above the miltontours package
Type 'python' to enter the python interpreter. You should see '>>>'
In python interpreter type the following (hitting enter after each line):
    from miltontours import db, create_app
    db.create_all(app=create_app())
The database should be created. Exit python interpreter by typing:
    quit()
Use DB Browser for SQLite to check that the structure is as expected before 
continuing.

ENTERING DATA INTO THE EMPTY DATABASE
-------------------------------------

# Option 1: Use DB Browser for SQLite
You can enter data directly into the cities or tours table by selecting it in
Browse Data and clicking the New Record button. The id field will be created
automatically. However be careful as you will get errors if you do not abide by
the expected field type and length. In particular the DateTime field must be of
the format: 2020-05-17 00:00:00.000000

# Option 2: Create a database seed function in an Admin Blueprint
See below. This blueprint needs to be enabled in __init__.py and then can be 
accessed via http://127.0.0.1:5000/admin/dbseed/
Database constraints mean that it can only be used on a fresh empty database
otherwise it will error. This blueprint should be removed (or commented out)
from the __init__.py after use.

Use DB Browser for SQLite to check that the data is as expected before 
continuing.
'''

from email.mime import image
from flask import Blueprint
from . import db
from .models import Food, Category,Order
import datetime


bp = Blueprint('admin', __name__, url_prefix='/admin/')

# function to put some seed data in the database
@bp.route('/dbseed/')

def dbseed():
    category1 = Category(name='Rice', image='beefnoodle.jpg', \
        description=''' It’s delicious. Tender beef, a rich and slightly spicy broth, fresh noodles, a little bok choy, and that absolutely necessary fistful of Chinese pickled mustard greens along with fresh scallions and cilantro.''')
    category2 = Category(name='Noodle', image='Braisedporkonrice.jpg', \
        description=''' I don’t think there’s any debate on this issue. Lu rou fan one of THE most beloved Taiwanese comfort foods. Second only perhaps to a piping bowl of beef noodle soup (and even then, a very close second).''')
    category3 = Category(name='Other', image='bubbletea.jpg', \
        description=''' Mention tapioca iced tea or famously known as bubble tea to almost any Asian and I can guarantee you that they will know about this tea. This very popular bubble tea is originally from Taiwan. You can find this bubble tea almost anywhere around the world now. Seriously, it is spreading like a virus.''')
     
    try:
        db.session.add(category1) #db.session.add(city1)
        db.session.add(category2) #db.session.add(city2)
        db.session.add(category3) #db.session.add(city3)
        db.session.commit()   #db.session.commit()
    except:
        return 'There was an issue adding the cities in dbseed function'

    # t1 = Tour(city_id=city1.id, image='t_cuddle.jpg', price=59.99,\
    #    date=datetime.datetime(2020, 5, 17),\
    #    name='Cuddle koalas',\
    #    description= 'Lone Pine Koala Sanctuary is the world\'s first and largest koala sanctuary and is home to more than 130 koalas. Hand-feed their kangaroos and wild lorikeets, be entertained by a platypus or - best of all - get cuddly with a beautiful koala. Duration 0900-1400 (5hrs), begins at entrance to Koala Plaza') 
    
    # 1 noodle, 2 rice, 3 other


    f1 = Food(category_id=category1.id, image='beefnoodle.jpg', price=19.99,\
        date=datetime.datetime(2020, 5, 17),\
        name='Beefnoodle',\
        description= 'It’s delicious. Tender beef, a rich and slightly spicy broth, fresh noodles, a little bok choy, and that absolutely necessary fistful of Chinese pickled mustard greens along with fresh scallions and cilantro.') 
    
    f2 = Food(category_id=category1.id, image='oystervermicellinoodle.jpg', price=9.99,\
        date=datetime.datetime(2020, 5, 17),\
        name='Oystervermicellinoodle',\
        description= 'Oyster vermicelli or oyster misua (traditional Chinese: 蚵仔麵線; Taiwanese Hokkien: ô-á mī-sòaⁿ) is a kind of noodle soup originated in Taiwan.')



    f3 = Food(category_id=category2.id, image='Braisedporkonrice.jpg', price=6.99,\
        date=datetime.datetime(2020, 5, 17),\
        name='Braied pork on rice',\
        description= 'I don’t think there’s any debate on this issue. Lu rou fan one of THE most beloved Taiwanese comfort foods. Second only perhaps to a piping bowl of beef noodle soup (and even then, a very close second).')
    
    f4 = Food(category_id=category2.id, image='chickenrice.jpg', price=6.99,\
        date=datetime.datetime(2020, 5, 17),\
        name='Chicken Rice',\
        description= 'Taiwanese chicken rice originated from Chiayi, a city in the southern part of Taiwan.  Traditionally its made with turkey, as its cheaper and more available back in the day.  If you visit Chiayi in Taiwan, you will see restaurants and food stalls selling turkey/chicken rice every where.')
    

    f5 = Food(category_id=category3.id, image='bubbletea.jpg', price=6.99,\
        date=datetime.datetime(2020, 5, 17),\
        name='Bubble Tea',\
        description= 'Mention tapioca iced tea or famously known as bubble tea to almost any Asian and I can guarantee you that they will know about this tea. This very popular bubble tea is originally from Taiwan. You can find this bubble tea almost anywhere around the world now. Seriously, it is spreading like a virus.')
    
    f6 = Food(category_id=category3.id, image='pinapplecake.jpg', price=2.99,\
        date=datetime.datetime(2020, 5, 17),\
        name='Pinapplecake',\
        description= 'Asian-style pineapple tart, pineapple cookie, or pineapple cake is one of the most popular items you will see during Chinese New Year celebration.')
    
    f7 = Food(category_id=category3.id, image='shavedice.jpg', price=6.99,\
        date=datetime.datetime(2020, 5, 17),\
        name='Shavedb Ice',\
        description= 'Your new favorite summer treat: Taiwanese snow ice')
    
    f8 = Food(category_id=category3.id, image='stinkytofu.jpg', price=6.99,\
        date=datetime.datetime(2020, 5, 17),\
        name='Stinky Tofu',\
        description= 'Stinky tofu has two major secrets. One is that the tofu becomes stinky, but it is not stinky. ')
    
    f9 = Food(category_id=category3.id, image='taiwanfriedchocken.jpg', price=6.99,\
        date=datetime.datetime(2020, 5, 17),\
        name='Taiwan fride chicken',\
        description= 'This Taiwanese fried chicken (táiwān yán sū jī) has all the traits of a good fried chicken: juicy, crispy, and addictive.')
    
    f10 = Food(category_id=category3.id, image='XiaoLongBao.jpg', price=6.99,\
        date=datetime.datetime(2020, 5, 17),\
        name='XiaoLongBao',\
        description= 'Chinese soup dumplings, sometimes also referred to as Shanghai Soup Dumplings, xiaolongbao, tang bao, or “soupy buns” (as it is hilariously translated on some menus), are a steamed dumpling consisting of a paper thin wrapper enveloping a seasoned pork filling and hot, flavorful soup.')
    
    
    try:
        db.session.add(f1)
        db.session.add(f2)
        db.session.add(f3)
        db.session.add(f4)
        db.session.add(f5)
        db.session.add(f6)
        db.session.add(f7)
        db.session.add(f8)
        db.session.add(f9)
        db.session.add(f10)


        db.session.commit()
    except:
        return 'There was an issue adding a tour in dbseed function'

    return 'DATA LOADED'


