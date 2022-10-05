CREATE TABLE category (
	id	INTEGER NOT NULL,
	name	VARCHAR(64),
	description	VARCHAR(500) NOT NULL,
	image	VARCHAR(60) NOT NULL,
	PRIMARY KEY(id),
	UNIQUE(name)
);

# c1 = Category(name='Rice', description='yummy rice', image='beefnoodle.jpg');
# c2 = Category(name='Noodle', description='tasty noodles', image=Braisedporkonrice.jpg');
 c3 = Category(name='Other ', description='other food', image='bubbletea.jpg');
 
INSERT INTO category(1,'Rice','yummy rice','beefnoodle.jpg');

INSERT INTO foods
VALUES (1, 'beefnoodle',
'It’s delicious. Tender beef, a rich and slightly spicy broth, fresh noodles, a little bok choy, and that absolutely necessary fistful of Chinese pickled mustard greens along with fresh scallions and cilantro.'
,'beefnoodle.jpg');

INSERT INTO foods
VALUES (2, 'Braisedporkonrice',
'I don’t think there’s any debate on this issue. Lu rou fan one of THE most beloved Taiwanese comfort foods. Second only perhaps to a piping bowl of beef noodle soup (and even then, a very close second).'
,'Braisedporkonrice.jpg');

INSERT INTO foods
VALUES (3, 'bubbletea',
'Mention tapioca iced tea or famously known as bubble tea to almost any Asian and I can guarantee you that they will know about this tea. This very popular bubble tea is originally from Taiwan. You can find this bubble tea almost anywhere around the world now. Seriously, it is spreading like a virus.'
,'bubbletea.jpg');

INSERT INTO foods
VALUES (4, 'chickenrice',
'Taiwanese chicken rice originated from Chiayi, a city in the southern part of Taiwan.  Traditionally its made with turkey, as its cheaper and more available back in the day.  If you visit Chiayi in Taiwan, you will see restaurants and food stalls selling turkey/chicken rice every where.'
,'chickenrice.jpg');

INSERT INTO foods
VALUES (5, 'oystervermicellinoodle',
'Oyster vermicelli or oyster misua (traditional Chinese: 蚵仔麵線; Taiwanese Hokkien: ô-á mī-sòaⁿ) is a kind of noodle soup originated in Taiwan.'
,'oystervermicellinoodle.jpg');

INSERT INTO foods
VALUES (6, 'pinapplecake',
'Asian-style pineapple tart, pineapple cookie, or pineapple cake is one of the most popular items you will see during Chinese New Year celebration.'
,'pinapplecake.jpg');

INSERT INTO foods
VALUES (7, 'shavedice',
'Your new favorite summer treat: Taiwanese snow ice'
,'shavedice.jpg');

INSERT INTO foods
VALUES (8, 'stinkytofu',
'Stinky tofu has two major secrets. One is that the tofu becomes stinky, but it is not stinky. '
,'stinkytofu.jpg');

INSERT INTO foods
VALUES (9, 'taiwanfriedchocken',
'This Taiwanese fried chicken (táiwān yán sū jī) has all the traits of a good fried chicken: juicy, crispy, and addictive.'
,'taiwanfriedchocken.jpg');

INSERT INTO foods
VALUES (10, 'XiaoLongBao',
'Chinese soup dumplings, sometimes also referred to as Shanghai Soup Dumplings, xiaolongbao, tang bao, or “soupy buns” (as it is hilariously translated on some menus), are a steamed dumpling consisting of a paper thin wrapper enveloping a seasoned pork filling and hot, flavorful soup.'
,'XiaoLongBao.jpg');
	