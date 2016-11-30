How to install CEQANET 2.01

Building Development Environment

1) Install Ubuntu 16.04 Desktop

2) Install git - sudo apt-get install git

3) Make directory in home dir - mkdir ceqanet

4) Clone CEQANet git repo - git clone https://github.com/elehmer/ceqanet.git

5) Install virtualenv - sudo apt-get install virtualenv

6) Create virtualenv - cd ~/ceqanet; virtualenv env

7) Install pip - sudo apt-get install python-pip

8) Install postgresql-9.5 and postgis 2.2 - sudo apt-get install postgresql; sudo apt-get install postgresql-server-dev-9.5; sudo apt-get install postgresql-9.5-postgis-2.2

9) Run Makefile - cd ~/ceqanet/ceqanet; make

10) Install libgeos - sudo apt-get install libgeos-dev

11) Edit postgres pg_hba.conf - sudo vi /etc/postgresql/9.5/main/pg_hba.conf. Change (local all all) connection method to trust.

12) Add postgres ceqa role - sudo su - postgres; createuser ceqa

13) Acquire the ceqanet database

14) Create db - sudo su - postgres; createdb ceqanet -O ceqa

15) Add postgis extention to db - sudo su - postgres; psql -d ceqanet -c "CREATE EXTENSION POSTGIS"

16) load postgres dump into db - sudo su - postgres; psql -d ceqanet -f ~ceqadev/ceqanet/ceqanet-11-11-16.dmp

17) open terminal and cd to ~ceqadev/ceqanet/ceqanet

18) activate virtualenv - source ../env/bin/activate

19) run django dev server - python manage.py runserver

20) open browser and point to - http://localhost:8000
