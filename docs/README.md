The Impact LGBTQ+ Group's website
===============================

This is the private repo for Impact's website. If you are reading this it is because you have been invited. Welcome and
thanks for getting involved!

Overview
--------
The goal of this project is to create and maintain a website for the LGBTQ+ Group Impact. Its overall design is to be 
mostly static with some dynamic content, not all of which is available to the general public.

Therefore we are using Django to serve the dynamic content side with plans to use a proxy (like 
[nginx](https://www.nginx.com/)) to serve the static content with Django taking over for the other sections.

Contributing
------------
So you want to get involved and help out? Brilliant. There are a few things you need to know before getting started.


Contributing to the Django part
--------------------------------
Firstly you _need_ knowledge of python and [Django](https://django-simple-menu.readthedocs.io/en/latest/)
(Documentation link). If you already have knowledge of python then learning Django should not be too difficult. 


Contributing to the static part
-------------------------------
The static part of the site is written in pure HTML and CSS. The CSS pre-process [Stylus](https://stylus-lang.com/) is
used in this project however. It is designed to massivly ease CSS development and is very powerful, it can however be
used as pure CSS (That is to say, normal CSS can be used), so no knowledge of stylus is needed to edit and contribute 
(but you should learn it :D).

All static files are found under [static](/static/) in their relative directories. Here are some quick directory links
- HTML: [html](/static/html/)
- CSS: [css](/static/css/) 

If you can help and want to do so after reading the above please read [CONTRIBUTING](CONTRIBUTING.md) for project 
specific instructions on github pull requests and issues. 

License
-------
This project is licensed under the [GNU GPLv3](https://www.gnu.org/licenses/gpl-3.0.en.html)
>   This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
>
>   This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

