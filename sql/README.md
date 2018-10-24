Relational databases
====================

This version by [Ben Waugh](https://github.com/benwaugh),
based on material from [Ethan White](https://github.com/ethanwhite),
[Greg Wilson](https://github.com/gvwilson) and the
[Software Carpentry](http://github.com/swcarpentry) team.
This material is provided with a Creative Commons Attribution licence
[CC-BY 3.0](http://creativecommons.org/licenses/by/3.0/).

---

Aims
----

After this lesson you should be able to

* evaluate the pros and cons of using a relational database for a given task,
  compared to a spreadsheet or other solution
* find the information you need to set up and use a relational database for your work
* carry out a simple data analysis using an existing relational database
* import data into a relational database from a text file or spreadsheet
* export processed data from a relational database into a text file or spreadsheet
* use a relational database from within a Python program

---

Introduction
------------

### Objectives

After this section you should be able to

* explain the concepts of a table, a record and a field
* explain the difference between a database and a database manager
* make an informed choice whether to use a relational database for a given task
* find documentation for the software used in this lesson, and other relational database software

### What is a relational database?

* A relational database stores data in a structured form, using tables of *records* (rows) containing
  *fields* (columns).
    * Sounds a bit like a spreadsheet, but read on.
    * Based on the mathematical concept of a *relation*...
    * ...but in practice can view as tables and rows.
    * Data in tables has types, just like in Python, and all values in a field have the same type.
    * A field in one table can provide a reference to a record in a different table, thus encoding
      information about the relationships between items.
* A database *manager* or *database management system (DBMS)* is an application that manages one or
  more databases, and provides an interface for interacting with the data.
    * By analogy we could call Excel a "spreadsheet manager".
    * The DBMS is given instructions in the form of *statements* in a specific language, normally
      *SQL (Structured Query Language)*.
    * A statement that returns data is called a *query*.
    * Queries let us look up data or make calculations based on columns.
    * The queries are distinct from the data, so if we change the data we can just rerun the query. (cf spreadsheet)

### What is not a relational database?

If there is such a thing as a *relational* database, presumably there are *non-relational* databases too...

Non-relational databases:

* Hierarchical.
* Network.
* Object-oriented.
* Key-value store.
* Document-oriented.
* The latter two are often lumped together under the *NoSQL* buzzword, sometimes said to stand
  for "Not *only* SQL".
* These are often used in cases where it is important to be able to access large amounts of data,
  especially when this is distributed across multiple servers, and may not have as rigid a structure as
  required by a relational database.
* They may also in some cases be simpler to use in applications where the relational features are not
  needed.

Ad-hoc data structures:

* You can combine lists, tuples, sets and dictionaries (or their equivalents in other languages) into 
  arbitrarily complex objects.
* It can become awkward and inefficient to use these to track all the relationships between different
  records.
* You still need some form of *persistence* to store these data structures when your software is not running.
* There are *object-relational mapping* packages available if you do need to switch between approaches.

Spreadsheets:

* Often the first tool people reach for to track their data.
* Easy to manipulate small, relatively simple data sets.
* Simplest approach often involves duplicating data across rows: violates *Don't Repeat Yourself* principle.
* Can evolve into complex systems of formulas, macros and functions.
* Can be very hard to understand, as relationships between cells and sheets are not easily visible.
* Size limits: 1 million rows by 16 thousand columns per sheet in Excel 2013.
* Example: [survey.xlsx](data/survey.xlsx)

### When should I use a relational database?

* Your data has a well defined structure.
* Relationships between items are important.
* Spreadsheets or ad-hoc data structures have become hard to use.
* You care about correct reproducible results.

### When should I not use a relational database?

A *spreadsheet* might be better if

* Your data has a fairly well defined structure.
* Relationships between items are simple or unimportant.
* You don't have very much data.
* You are consistently meticulous about checking the formulas in your cells.
* You don't want other people to understand your calculations.
* You don't mind if your results are wrong.
    * See e.g. [Growth in a Time of Debt](http://en.wikipedia.org/wiki/Growth_in_a_Time_of_Debt)
    * Further examples: [How Excel is ruining the world](http://finance.fortune.cnn.com/2013/04/17/rogoff-reinhart-excel-errors/)

A *NoSQL* database might be better if

* Your data is very varied in form.
    * Don't have to force it into a rigid *schema*.
    * You will still have to deal with the complexity in your application.
* You have *vast* quantities of data.
    * But even Twitter uses a relational database (MySQL) to store tweets and other data.
* You only need to access the data in one way, e.g. looking up temperatures for a given region
  but not finding regions with a given range of temperatures.
* You care more about speed than consistency.
    * More typical of social media than scientific research.

### Which relational database manager should I use?

* This lesson uses SQLite:
    * simple to install and use
    * provides most standard SQL features
    * free and open source
    * not suitable for large databases, multiple simultaneous users, or speed-critical applications
* For larger projects options include MySQL, MariaDB, PostgreSQL, Oracle.
* All of these can be accessed using a command-line tool, or via an API in Python or another programming
  language.
* We will use the "SQLite Manager" plug-in for Firefox, because
    * it is easy to install on all common systems;
    * it lets you "browse" the data as well as entering SQL statements.

### Documentation

* [SQLite](http://www.sqlite.org/) web site includes [Getting Started](http://www.sqlite.org/quickstart.html)
  and other documentation.
* [SQLite Manager](https://addons.mozilla.org/en-US/firefox/addon/sqlite-manager/) add-on for Firefox.
* There is a [Python SQLite Tutorial](http://www.pythoncentral.io/series/python-sqlite-database-tutorial/)
  on the [Python Central](http://www.pythoncentral.io/) web site.
* For use from IPython, there are some "magics" for manipulating SQLite and other databases:
    * [SQLite magics for IPython](https://github.com/tkf/ipython-sqlitemagic) (Takafumi Arakaki)
    * [SQL magic for IPython](https://github.com/catherinedevlin/ipython-sql) (Catherine Devlin)
    * [Simple SQLite magic for the IPython Notebook](https://github.com/gvwilson/sqlitemagic/) (Greg Wilson)
* [Popularity Ranking of Relational DBMS](http://db-engines.com/en/ranking/relational+dbms) claims that the
  most popular open-source RDBMSs are
    * [MySQL](http://www.mysql.com/)
    * [PostgreSQL](http://www.postgresql.org/)
    * [SQLite](http://sqlite.org/)

---

An ecological dataset
---------------------

In this lesson we will be using some data from a project studying the effects of rodents and ants
on the plant community in a region of southern Arizona over the last 35 years.
The rodents are sampled on a series of 24 plots, with different 
manipulations of which rodents are allowed to access the plots.

This is a real dataset that has been used in over 100 publications.
It has been simplified a bit for the workshop (thanks to Ethan White)
but you can download the [full dataset](http://esapubs.org/archive/ecol/E090/118/)
and work with it using exactly the same tools we'll learn about today.

---

Selecting data
--------------

### Objectives

After this section you should be able to do the following using the Firefox
"SQLite Manager" plug-in:

* import data into an SQLite database from a spreadsheet or text file
* write a query to select all values for specific fields from a single table
* export processed data from an SQLite database into a spreadsheet text file

### Installation

1. Install Firefox
2. Install the SQLite Manager add on **Tools -> Add-ons -> Search -> SQLite Manager -> Install -> Restart**
3. Open SQLite Manager **Tools -> SQLite Manager**

### Importing data

1. Go to the [data directory](data/) and download the file [mammal_plots_table.csv](data/mammal_plots_table.csv)
1. In SQLite Manager, start a new database **Database -> New Database**
    * give it a meaningful name, e.g. `mammals`
    * choose a suitable directory to store it in
1. Import each CSV file as a table
    * Start the import **Database -> Import**
    * Select the file to import: **Select File**
    * Give the table a name like `plots` (rather than `mammal_plots_table`)
    * Look at the first few lines of the file to work out what options to select
        - First row contains column names
        - Fields enclosed by double quotes if necessary
    * Click **OK**
    * When asked if you want to modify the table, click **OK**
    * Set the data types for each field, by looking at the first few lines of the file:
        - `plot_id` is an `INTEGER`
        - `plot_type` can be stored as a `VARCHAR` (variable length character data)
    * Confirm import by clicking **OK**.
1. Look at the data by selecting the `plots` table and the `Browse & Search` tab.

#### Exercise

* Import the species and surveys tables.

#### Notes

* Some entries have special meaning or human-readable metadata, e.g.
    * `Rodent-not censused`
    * `Zero Trapping Success`
* Some fields are missing in some records.
* Can explicitly tell SQLite which field(s) is the primary key, but haven't done so.

### Selecting data

The `Browse & Search` tab allows limited viewing and selection of data, but for more control (and when
not using the Firefox add-on) we need to learn some SQL. Select the `Execute SQL` tab.

Let's start by using the **surveys** table.
Here we have data on every individual that was captured at the site,
including when they were captured, what plot they were captured on,
their species ID, sex and weight in grams.

Let’s write an SQL query that selects only the year column from the surveys table.

```SQL
    SELECT year FROM surveys;
```

Tthe words SELECT and FROM are capitalized because they are SQL keywords.
SQL is case insensitive, but this is a common convention intended to help readability
by distinguishing keywords from database-specific table and field names.
The semicolon at the end of the statement is required in SQL: a statement can be
split over multiple lines, or several statements can be entered on a single line,
so the semicolon tells the interpreter where each statement ends.
SQLite Manager will let you omit the semicolon, since it can only handle one
statement at a time in the "Enter SQL" field anyway, but you must remember the
semicolon if using the SQLite command line interface.

If we want more information, we can just add to the list of fields, using commas
to separate them:

```SQL
    SELECT day, month, year FROM surveys;
```

Or we can select all of the columns in a table using the wildcard *:

```SQL
    SELECT * FROM surveys;
```

### Exporting data from SQLite Manager

Below the SQL statement field in the "Execute SQL" tab, there is a pull-down menu labelled "Actions".
Select "Save Result (CSV) to File" to create a text file containing the result of your query.

#### Exercise

* Write a query that returns only the `genus` and `species` fields from the `species` table.
* Save the list of genus and species names to a file.

#### Note

* The order of records in the output is arbitrary in SQL.
* Even if a particular DBMS always provides output in a predictable order (or appears to)
  this should not be relied on. It is likely to be different in a different DBMS, or even
  when the same data has been loaded into the same DBMS in a different order.

---

Sorting and filtering data
--------------------------

### Objectives

After this section you should be able to do the following:

* write queries that eliminate duplicate values from data
* write queries that display results in a particular order
* write queries that select records that satisfy user-specified conditions

### Unique values

So, we've all written a query that pulls out the species column from the database,
but what if we want only the unique values so that we can quickly see what
species have been sampled.

```SQL
    SELECT DISTINCT species FROM surveys;
```

If we select more than one column, then the distinct pairs of values are returned

```SQL
    SELECT DISTINCT year, species FROM surveys;
```

#### Exercise

* Write a query that returns the values of the field `plot_type` in the `plots` table,
  listing each plot type only once.

### Sorting

We can also sort the results of our queries by using `ORDER BY`.
For simplicity, let’s go back to our species table and alphabetize it by Genus.

```SQL
    SELECT * FROM species ORDER BY Genus ASC;
```

The keyword `ASC` tells us to order it in ascending order.
We could alternatively use `DESC` to get descending order.

```SQL
    SELECT * FROM species ORDER BY Genus DESC;
```

`ASC` is the default.

We can also sort on several fields at once.
To truly be alphabetical, we might want to order by genus then species.

```SQL
    SELECT * FROM species ORDER BY genus ASC, species ASC;
```

#### Exercise

* Write a query that returns all of the data in the plots table,
sorted alphabetically by plot type and then (within each plot type)
in descending order of the plot ID.

### Filtering

One of the most powerful features of a database is the ability to filter data:
selecting only the data meeting certain criteria.
For example, let’s say we only want data for the species Dipodomys merriami,
which has a species code of DM.
We need to add a `WHERE` clause to our query:

```SQL
    SELECT * FROM surveys WHERE species="DM";
```

We can do the same thing with numbers.
Here, we only want the data since 2000:

```SQL
    SELECT * FROM surveys WHERE year >= 2000;
```

#### Exercise

* Write a query that returns the day, month, year, species ID, and weight
for individuals that weigh more than 75 grams.

We can user more sophisticated conditions by combining tests with `AND` and `OR`.
For example, suppose we want to data on Dipodomys merriami starting in the year 2000:

```SQL
    SELECT * FROM surveys WHERE (year >= 2000) AND (species = "DM");
```

Note that the parentheses aren’t needed but, again, they help with readability.
They also ensure that the computer combines `AND` and `OR` in the way that we intend.

If we wanted to get data for any of the Dipodomys species,
which have species codes DM, DO, and DS we could combine the tests using OR:

```SQL
    SELECT * FROM surveys WHERE (species = "DM") OR (species = "DO") OR (species = "DS");
```

#### Exercise

* Write a query that returns the day, month, year, species ID, and weight
  for individuals caught on plot 1 that weigh more than 75 g.

---

Calculating new values
----------------------

### Objectives

After this section you should be able to do the following:

* write queries that calculate new values for each selected record

We are not restricted to just printing values as they exist in the database: we can also
carry out a range of calculations using built-in SQL operators and functions. For example,
we could use a simple multiplication to correct the data if we discover that the scale
we used was miscalibrated by 2%:

```SQL
SELECT wgt*1.02 FROM surveys;
```

There are many built-in functions, such as `ROUND`, which can be used to round results
to a given precision:

```SQL
SELECT ROUND(wgt*1.02, 2) FROM surveys;
```

We can give a name to a calculated quantity to reduce repetition and thus make it less
likely that we will introduce errors.

```SQL
SELECT (wgt*1.02) AS weight_corr
  FROM
    surveys
  WHERE
    weight_corr > 50;
```

#### Exercise

* Write a query that returns the day, month, year, species ID, and weight
(in kg) for individuals caught on plot 1 that weigh more than 0.079 kg.

---

Missing data
------------

### Objectives

After this section you should be able to

* explain how a relational database represents missing information
* write queries that handle missing information correctly

### Null

In browsing the tables, and looking at your query results, you may have noticed that some fields
have no value in certain records. The absence of a value is represented in SQL by a `NULL` value.
The existence of `NULL` entries can complicate the interpretation of results, but this is not a feature
of SQL so much as a reflection of the complexity or imperfections of the underlying data. In our data,
some animals were not weighed, or sexed, so the corresponding fields are `NULL`.

There may also be more subtle issues to consider in interpreting the data. In this case, some of the
entries in the `species` table correspond to specimens that were only identified to the level of their
genus or above.
Failing to allow for `NULL` or missing values, or errors in the data, can make the results of
an analysis invalid.

To check whether a value is `NULL`, the special syntax `IS NULL` or `IS NOT NULL` is needed.
Trying to compare a `NULL` value with anything for either equality (`=`) or inequality (`!=`)
always results in another `NULL`, which is interpreted as "false" in selection criteria.

#### Exercise

* Write a query to list the plot ID and species for all specimens captured in 1980 whose
  weight was not recorded.

---

Aggregation
-----------

### Objectives

After this section you should be able to

* define "aggregation" and give examples of its use
* write queries that compute aggregated values

### Aggregation functions

Let’s go to the surveys table and find out how many individuals there are.
Using the wildcard simply counts the number of records (rows)

```SQL
    SELECT COUNT(*) FROM surveys;
```

We can also find out the mean weight of all of those individuals.

```SQL
    SELECT AVG(wgt) FROM surveys;
```

There are many other aggregate functions included in SQL including `SUM`, `MAX` and `MIN`.

 
#### Exercise

* Write a query to find the smallest and largest weights recorded for specimens of *Neotoma albigula*.

### Grouping

Now, let's try to see how many individuals were counted in each species.

```SQL
    SELECT species, COUNT(*) FROM surveys;
```

Why does this NOT work?

The database counted all the individuals, but we didn’t specify anything about the species,
so it just picked an arbitrary value and returned it.

If we select fields and aggregate at the same time, values from 
unaggregated fields can be any value: we need to tell the data how to 
aggregate, and we can do that using `GROUP BY` clause

```SQL
    SELECT species, COUNT(*)
    FROM surveys
    GROUP BY species;
```

#### Exercises

* How many individuals were counted in each year?
* How many individuals were counted in each species in each year?

We can order the results of our aggregation by a specific column, 
including the aggregated column.
Let’s count the number of individuals of each species captured,
ordered by the count

```SQL
SELECT species, COUNT(*) AS number
  FROM
    surveys
  GROUP BY
    species
  ORDER BY
    number DESC;
```

#### Exercises

* Write a query that lets us look at which years contained the most individuals and which had the least.
* Write a query that shows us which species had the largest and smallest individuals on average.

---

Combining data
--------------

### Objectives

After this section you should be able to

* write a query that uses information from two or more tables 
* explain what primary and foreign keys are, and why they are useful
* explain what atomic values are, and why database fields should only contain atomic values

### Joining tables

If we want to list the full name of each species in the output of a query on the survey results,
we need to combine data from the `surveys` and `species` tables.

To combine data from two tables we use the `SQL JOIN` command,
which comes after the `FROM` command.

```SQL
    SELECT * FROM surveys JOIN species;
```

But this didn’t do what we wanted because we didn’t tell the database 
manager how the tables are related to each other.
Look at the number of rows it returned!
Simply adding the `JOIN` combines every row of 
one table with every row of the other:
it creates a cross-product of the sets of rows.
When looking at a record from `surveys` where the `species` field has the value `CB`,
we want to combine it only with the record in the `species` table that has the
same value `CB` in the `species_id` field, and leave out the records with all the
other `species_id` values.

To tell SQL how the tables are related, we indicated which columns provide the link
between the two tables using the word ON.

```SQL
    SELECT * FROM surveys JOIN species
        ON surveys.species = species.species_id;
```

`ON` is like `WHERE`: it filters things out according to a test condition.
We use `table.field` to tell the manager what column in which table
we are referring to.

We often won't want all of the fields from both tables,
so anywhere we would have used a field name in a non-join query,
we can use `table.field`. (We can just use the field name where this is
unambiguous, but it is safer to specify the table explicitly.)

For example, what if we wanted information on when individuals of each
species were captured, but instead of their species ID we wanted their
actual species names.

```SQL
    SELECT surveys.year, surveys.month, surveys.day, species.genus, species.species
    FROM surveys
    JOIN species ON surveys.species = species.species_id;
```

#### Exercise

* Write a query that returns the genus, the species, and the weight of every individual captured.


Joins can be combined with sorting, filtering, and aggregation.
So, if we wanted average mass of the individuals on each different
type of treatment, we could do something like

```SQL
    SELECT plots.plot_type, surveys.species, AVG(surveys.wgt)
    FROM surveys
      JOIN plots
      ON surveys.plot = plots.plot_id
    GROUP BY plot_type;
```

#### Exercise

* Modify the query above so that it returns only the average mass of the individuals of
  *Sigmodon hispidus* on each type of plot.

### Joining more than two tables

We can join any number of tables simply by adding more `JOIN` clauses to our query

```SQL
SELECT plots.plot_type, species.genus, species.species, AVG(surveys.wgt)
    FROM surveys
        JOIN plots ON plots.plot_id = surveys.plot
        JOIN species ON species.species_id = surveys.species
    GROUP BY plots.plot_type, surveys.species
```

#### Exercise (advanced)

* Modify the query from the previous exercise so it returns the average mass of individuals
  of all *Sigmodon* species on each type of plot.

### Keys

A *key* is a field (or sometimes a combination of fields) that is used to identify a record
in a table. Each table should (most database designers would agree) have a well-defined
*primary key* that *uniquely* identifies each record in a table. SQLite allows you to specify
which field(s) in a table should be the primary key, and will stop you from entering duplicate
values, although we did not take advantage of this when importing the data for this lesson.

A *foreign key* is a field in one table that can be used to identify a corresponding record
in a different table. In other words it is a primary key for the table it refers to, rather
than the one it appears in.

#### Exercise

* Identify the primary and foreign keys (if any) in each of the three tables `plots`,
  `species` and `surveys`.

---

Programming with databases
--------------------------

### Objectives

After this section you should be able to

* write a simple Python program that uses data in an SQLite database

### The Python `sqlite3` module

This is illustrated in [this IPython notebook](sql.ipynb).

---

Further topics
--------------

This lesson cannot cover every feature of relational databases or SQL, but aims to
provide enough of an introduction to let you judge whether it is worth following
this topic further.

* We have demonstrated how to import data into an SQLite database, but not how to
  *modify* the data in the database or *create tables* using SQL statements.
* *Subqueries* enable the creation of more complex queries that would otherwise
  have to be split into multiple steps.
* *Temporary tables* can be used like variables to store intermediate results.
* *Views* provide "virtual tables" that act like aliases for the results of queries,
  automatically calculating intermediate results when they are needed.
* *Constraints* and *transactions* can be used to help maintain the *integrity* of a database.
* *Performance* can be tested and tuned using *indexes* and *logging*.
* The SQLite *command-line interface* provides a simple tool for interacting with an
  SQLite database without using a web browser.
* An SQL *prepared statement* or *parameterized statement* is a query template, into which
  specific values such as a species of interest or threshold weight value can be substituted.
  These can provide some performance improvement, but most importantly they can protect
  against an *SQL injection* attack where someone passes maliciously crafted input to your
  DBMS (typically via a web interface) to corrupt your data or gain unauthorized access.

---

Tips and hints
--------------

* backing up a database
    * exporting from SQLite manager
    * dumping from other database managers
    * importing using SQLite manager
    * importing from command line
* querying a database
    * build query incrementally
    * test query on subset of data where correct answer is known
    * use the RDBMS, don't read everything and loop in application!
* designing a database
    * normalisation (Don't Repeat Yourself)
    * optimisation: using indexes, denormalisation (if really needed)
* pitfalls (many apply to data in general)
    * incomplete data (NULLs)
    * inconsistent data (especially if data not normalised)
    * biased data (e.g. selection bias)

