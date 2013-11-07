Python-Social-Network-Analysis
==============================

My attempt at social network analysis displayed with Django web framework, inspired by my dissertation study.


##Setup

```sh
# If you're using Python3, use this command.
$ mkvirtualenv -p 'which python3' sna


$ pip install -r requirements.txt

```

Next, you'll have to update your database settings. 

##Running server



```sh
$ python manage.py runserver
```



MySQL Database Tables
==============================
<pre>
mysql> describe sna_messages;
+-----------+--------------+------+-----+---------+----------------+
| Field     | Type         | Null | Key | Default | Extra          |
+-----------+--------------+------+-----+---------+----------------+
| id        | int(11)      | NO   | PRI | NULL    | auto_increment |
| url       | varchar(500) | NO   |     | NULL    |                |
| thread    | varchar(20)  | NO   |     | NULL    |                |
| tIndex    | varchar(20)  | NO   |     | NULL    |                |
| author    | varchar(100) | NO   |     | NULL    |                |
| cmc       | varchar(50)  | NO   |     | NULL    |                |
| timestamp | datetime     | NO   |     | NULL    |                |
+-----------+--------------+------+-----+---------+----------------+

mysql> describe sna_users;
+---------+--------------+------+-----+---------+----------------+
| Field   | Type         | Null | Key | Default | Extra          |
+---------+--------------+------+-----+---------+----------------+
| id      | int(11)      | NO   | PRI | NULL    | auto_increment |
| uid     | varchar(200) | NO   |     | NULL    |                |
| name    | varchar(500) | NO   |     | NULL    |                |
| F_posts | varchar(3)   | NO   |     | NULL    |                |
| J_posts | varchar(3)   | NO   |     | NULL    |                |
| N_posts | varchar(3)   | NO   |     | NULL    |                |
+---------+--------------+------+-----+---------+----------------+

mysql> describe sna_pairs;
+--------+-------------+------+-----+---------+----------------+
| Field  | Type        | Null | Key | Default | Extra          |
+--------+-------------+------+-----+---------+----------------+
| id     | int(11)     | NO   | PRI | NULL    | auto_increment |
| CMC    | varchar(10) | NO   |     | NULL    |                |
| sender | varchar(10) | NO   |     | NULL    |                |
| target | varchar(10) | NO   |     | NULL    |                |
+--------+-------------+------+-----+---------+----------------+
</pre>
