#! /bin/bash


# This script is deprecated. Use 'deploy_ovh' instead.
exit 1

# Clearly working well.

./my_blog.py
cp php/*.php /var/www/html/laurent/blog/php/
cp html/*.html /var/www/html/laurent/blog/html/
cp src/*.php /var/www/html/laurent/blog/src/
cp src/generic_head.src /var/www/html/laurent/blog/src/
cp rss.xml /var/www/html/laurent/blog/
cp php/articles.css /var/www/html/laurent/blog/php/
