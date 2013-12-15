philly-councilmatic
===================

#Designs/Wireframes
-------------------
Provided by TK Rodgers [here](https://docs.google.com/file/d/0B1ikPJfvXCSlYVdmUDNQdmFBSWc/edit?pli=1). Much thanks!


Getting set up on Heroku
========================

Provision your project

    heroku apps:create <city>-councilmatic

Promote your desired database. Running `heroku pg` will list your added
databases. Choose the one you want to use. If there are none there, add
one with `heroku addons:add heroku-postgresql`. Note that if you want to
use location queries and such, you must at least install the Yanari DB:
`heroku addons:add heroku-postgresql:standard-yanari`.

    heroku pg:promote HEROKU_POSTGRESQL_<color>_URL

If you do want to use location functionality, enable PostGIS.

    heroku pg:psql
    CREATE EXTENSION postgis;
    \q

Sync DB
Migrate
Copy over the database?
-- Load in current councilmember data

Copy desired search URL to SEARCH_URL
Commit and push
Start a scrape

Make sure the legislation settings are right
Set up periodic scrapes (you can use Scheduler)

    bin/update_data