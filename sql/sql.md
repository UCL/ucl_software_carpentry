Relational Databases
====================

Background
----------

### What is a relational database?

* A relational database stores data in a structured form, using tables of *records* (rows) containing
*fields* (columns).
* Data in tables has types, just like in Python, and all values in a field have the same type.
* Queries let us look up data or make calculations based on columns.
* The queries are distinct from the data, so if we change the data we can just rerun the query.

### What are the alternatives?

Non-relational databases:

* The newer examples are often lumped together under the *NoSQL* buzzword, sometimes said to stand
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
* There are *object-relational mapping* packages available if you do need to switch between approaches.

Spreadsheets:

* Often the first tool people reach for to track their data.
* Easy to manipulate small, relatively simple data sets.
* Simplest approach often involves duplicating data across rows: violates *Don't Repeat Yourself* principle.
* Can evolve into complex systems of formulas, macros and functions.
* Can be very hard to understand, as relationships between cells and sheets are not easily visible.
* Size limits: 1 million rows per sheeet in Excel 2010.


Set-up
------

1. Install Firefox
2. Install the SQLite Manager add on **Tools -> Add-ons -> Search -> SQLite Manager -> Install -> Restart**
3. Open SQLite Manager **Tools -> SQLite Manager**

The data
--------

This is data on a small mammal community in southern Arizona over the last 35 years.
This is part of a larger project studying the effects of rodents and ants
on the plant community.
The rodents are sampled on a series of 24 plots, with different 
manipulations of which rodents are allowed to access the plots.

This is a real dataset that has been used in over 100 publications.
It has been simplified a bit for the workshop (thanks to Ethan White)
but you can download the [full dataset](http://esapubs.org/archive/ecol/E090/118/)
and work with it using exactly the same tools we'll learn about today.

Importing data
--------------

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

---

***Exercise***

* Import the species and surveys tables.

---

***Notes***

* Some entries have special meaning or human-readable metadata, e.g.
    * `Rodent-not censused`
    * `Zero Trapping Success`
* Some fields are missing in some records.
* Can explicitly tell SQLite which field(s) is the primary key, but haven't done so.

---

Selecting data
--------------

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

---

***Note***

* Line breaks aren't important, but statement must end with a semicolon.

---

We have capitalized the words SELECT and FROM because they are SQL keywords.
SQL is case insensitive, but it helps readability.

If we want more information, we can just add a new column to the list of fields, right after SELECT:

```SQL
    SELECT day, month, year FROM surveys;
```

Or we can select all of the columns in a table using the wildcard *

```SQL
    SELECT * FROM surveys;
```

---

***Exercise***

* Write a query that returns only the species column.

---

***Note***

* The `species` field in the `surveys` table contains an abbreviated identifier rather than the full
  species name.
* No guarantee what order data will be retrieved.
* Will address both points later.

---

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

### Calculated values

We can also do calculations with the values in a query.
For example, if we wanted to look at the mass of each individual
on different dates, but we needed it in kg instead of g we would use

```SQL
    SELECT month, day, year, wgt/1000.0 FROM surveys;
```

When we run the query, the expression ``wgt / 1000.0`` is evaluated for each row
and appended to that row, in a new column. 
Expressions can use any fields, any arithmetic operators (+ - * /)
and a variety of built-in functions (). For example, we could round the values to
make them easier to read.

```SQL
    SELECT plot, species, sex, wgt, ROUND(wgt / 1000.0, 2) FROM surveys;
```


Filtering
---------

One of the most powerful features of a database is the ability to filter data –
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

---

***Exercise***

* Write a query that returns the day, month, year, species ID, and weight
for individuals that weigh more than 75 grams.

---

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

---

***Exercise***

* Write a query that returns the day, month, year, species ID, and weight
(in kg) for individuals caught on plot 1 that weigh more than 0.075 kg.

---

***Note***

* We can give a name to a calculated quantity to reduce repetition and thus make it less likely
  that we will introduce errors.

```SQL
SELECT (wgt/1000.0) AS weight_kg
  FROM
    surveys
  WHERE
    weight_kg > 0.075;
```

---

Exporting results of queries
----------------------------

Getting the result of your query out to work with elsewhere is as easy
as clicking the **Actions** button and choosing **Save Result to File**.

---

***Note***

* Headers are not included in exported CSV file.

---


Building more complex queries
-----------------------------

Now, lets combine the above queries to get data for the 3 Dipodomys species
from the year 2000 on.
This time, let’s use `IN` as one way to make the query easier to understand.
It is equivalent to saying ``WHERE (species = "DM") OR (species = "DO") OR (species = "DS")``,
but reads more neatly:

```SQL
SELECT *
  FROM
    surveys
  WHERE
    (year >= 2000)
    AND
    (species IN ("DM", "DO", "DS"));
```

We started with something simple, then added more clauses one by one,
testing their effects as we went along.
For complex queries, this is a good strategy, to make sure you are getting what you want.
Sometimes it might help to take a subset of the data that you can easily see in a temporary
database to practice your queries on before working on a larger or more complicated database.


Sorting
-------

We can also sort the results of our queries by using `ORDER BY`.
For simplicity, let’s go back to our species table and alphabetize it by Genus.

```SQL
    SELECT * FROM species ORDER BY Genus ASC;
```

The keyword `ASC` tells us to order it in Ascending order.
We could alternately use `DESC` to get descending order.

```SQL
    SELECT * FROM species ORDER BY Genus DESC;
```

`ASC` is the default.

We can also sort on several fields at once.
To truly be alphabetical, we might want to order by genus then species.

```SQL
    SELECT * FROM species ORDER BY genus ASC, species ASC;
```

---

***Exercise***

* Write a query that returns all of the data in the plots table,
sorted alphabetically by plot type and then (within each plot type)
in descending order of the plot ID.

---


Order of execution
------------------

Another note for ordering:
We don’t actually have to display a column to sort by it.
For example, let’s say we want to order by the species ID, but we only want to see genus and species. 

```SQL
    SELECT genus, species FROM species ORDER BY species_id ASC;
```

We can do this because sorting occurs earlier in the computational pipeline than field.

The computer is doing this:

1. filtering rows according to `WHERE`;
2. sorting results according to `ORDER BY`;
3. displaying requested columns or expressions.

Let’s try to combine what we’ve learned so far in a single query.
The order of the clauses is dictated by SQL: `SELECT`, `FROM`, `WHERE`, `ORDER BY`
and we often write each of them on their own line for readability.

---

***Exercise***

* Write a query on the `surveys` table to display the three date fields,
species ID, and weight in kilograms (rounded to two 
decimal places) for rodents captured in 1999, ordered alphabetically by 
the species ID.

---

Missing or inconsistent data
----------------------------

In browsing the tables, and looking at your query results, you may have noticed that some fields
have no value in certain records. The absence of a value is represented in SQL by a `NULL` value.
The existence of `NULL` entries can complicate the interpretation of results, but this is not a feature
of SQL so much as a reflection of the complexity or imperfections of the underlying data. In our data, some animals were not weighed, or sexed, so the corresponding fields are `NULL`.

There may also be more subtle issues to consider in interpreting the data. In this case, some of the
entries in the `species` table correspond to specimens that were only identified to the level of their
genus or above.

---

***Note***

* Failing to allow for `NULL` or missing values, or errors in the data, can make the results of
  an analysis invalid.

---

To check whether a value is `NULL`, the special syntax `IS NULL` or `IS NOT NULL` is needed.
Trying to compare a `NULL` value with anything for either equality (`=`) or inequality (`!=`)
always results in another `NULL`, which is interpreted as "false" in selection criteria.

---

***Exercise***

Modify the previous query to display results only for individuals whose species and weight
were recorded.

---

When joining two tables, one or both of which may contain `NULL` values in the join variable, the
result is that some combinations of values you might expect are not included in the result. This could
occur if, for example, some species in the `species` table never showed up in the `surveys` table,
or a species showed up in a survey without being added to the `species` table.

We don't have time here to follow this up, but the solution involves using an *outer join*.

It is also possible to use *constraints* to prevent the database from ending up in certain types
of inconsistent state, such as having a species in `surveys` that is not included in `species`.


Aggregation
-----------
Aggregation allows us to combine results group records based on value
and calculate combined values in groups.

Let’s go to the surveys table and find out how many individuals there are.
Using the wildcard simply counts the number of records (rows)

```SQL
    SELECT COUNT(*) FROM surveys;
```

We can also find out how all of those individuals weigh.

```SQL
    SELECT SUM(wgt) FROM surveys;
```

Do you think you could output this value in kilograms, rounded to 3 decimal places?

```SQL
    SELECT ROUND(SUM(wgt)/1000.0, 3) FROM surveys;
```

There are many other aggregate functions included in SQL including
`MAX`, `MIN`, and `AVG`.

---
 
***Exercise***

From the surveys table, use one query to output the total weight, average weight, and the min and max weights.

---

Now, let's try to see how many individuals were counted in each species?

```SQL
    SELECT species, COUNT(*) FROM surveys;
```

Why does this NOT work?

The database counted all the individuals,
but we didn’t specify anything about the species,
so it just picked an arbitrary value and returned it.

If we select fields and aggregate at the same time, values from 
unaggregated fields can be any value – we need to tell the data how to 
aggregate, and we can do that using `GROUP BY` clause

```SQL
    SELECT species, COUNT(*)
    FROM surveys
    GROUP BY species;
```

---

***Exercises***

* How many individuals were counted in each year?
* How many individuals were counted in each species in each year?

---

We can order the results of our aggregation by a specific column, 
including the aggregated column.
Let’s count the number of individuals of each species captured,
ordered by the count

```SQL
    SELECT species, COUNT(*)
    FROM surveys
    GROUP BY species
    ORDER BY COUNT(sp_code);
```

---

***Exercises***

* Write a query that lets us look at which years contained the most individuals and which had the least.
* Write a query that shows us which species had the largest and smallest individuals on average.

---


Database Design
---------------

Principles of database *normalization* aim to minimize redundancy and dependency among records,
so relationships are clear and we are less likely to introduce inconsistencies.

* Each field in a database should store a single value.
* Information should not be duplicated in a database.
* Each table should be about a single subject (avoids unnecessary replication).

Also, remembering to *write for people, not computers*:

* When naming fields, you should think about meaning, not presentation.

When we divide our data between several tables,
we need a way to bring it back together again.
The key is to have an identifier in common between tables: shared columns.
This will allow us to join tables, which we will discuss now.

For example, the species ID is included in the `surveys` table,
but we don’t know what the species ID stands for.
That information is stored in the `species` table and can be
linked to if we need it.
This means that we don't have to record the full genus, species,
and taxa information for the several thousand individuals of each species. 

---

***Note***

* When using a spreadsheet, it is common for information to be duplicated in this way. Getting round this 
  involves using *look-up* or *database* functions in the spreadsheet.

---


Joining tables
--------------

To combine data from two tables we use the `SQL JOIN` command,
which comes after the `FROM` command.

```SQL
    SELECT * FROM surveys JOIN species;
```

But this didn’t do what we wanted because we didn’t tell the database 
manager how the tables are related to each other.
Look at the number of rows it returned!
Simply adding the `JOIN` combines every row of 
one table with every row of the other -
it creates a cross-product of the sets of rows.
We need to tell SQL how the tables are related.

To do this we indicated which columns provide the link between
the two tables using the word ON.
What we want is to join the data with the same species codes.

```SQL
    SELECT *
    FROM surveys
    JOIN species ON surveys.species = species.species_id;
```

`ON` is like `WHERE`, it filters things out according to a test condition.
We use the table.colname to tell the manager what column in which table
we are referring to.

We often won't want all of the fields from both tables,
so anywhere we would have used a field name in a non-join query,
we can use *table.colname*

For example, what if we wanted information on when individuals of each
species were captured, but instead of their species ID we wanted their
actual species names.

```SQL
    SELECT surveys.year, surveys.month, surveys.day, species.genus, species.species
    FROM surveys
    JOIN species ON surveys.species = species.species_id;
```

---

***Exercise***

* Write a query that returns the genus, the species, and the weight of every individual captured.

---

***Note***

* In many records, the weight has not been recorded.

---

Joins can be combined with sorting, filtering, and aggregation.
So, if we wanted average mass of the individuals on each different
type of treatment, we could do something like

```SQL
    SELECT plots.plot_type, AVG(surveys.wgt)
    FROM surveys
      JOIN plots
      ON surveys.plot = plots.plot_id
    GROUP BY plots.plot_type;
```

---

***Exercise***

* Modify the query above so that it returns only the average mass of the individuals of
  *Sigmodon hispidus* on each type of plot.
* Modify the query so it returns the average mass of individuals of all *Sigmodon* species
  on each type of plot.

---

Subqueries
----------

Which individual was the heaviest? We can answer this in two steps by finding the greatest mass and
then finding the individual(s) with this value:

```SQL
SELECT MAX(wgt)
  FROM
    surveys;

SELECT *
  FROM
    surveys
  WHERE
    wgt = 280;
```

However, we can also feed the result of the first query into the second by making it into a
*subquery*:

```SQL
SELECT *
  FROM
    surveys
  WHERE
    wgt = (SELECT MAX(wgt)
                  FROM
                      surveys);
```


Creating tables
---------------


Views
-----


Adding data to existing tables
------------------------------


Advanced features
-----------------

For performance:

* indexes
* logging
* tuning

For integrity:

* constraints
* transactions and roll-back


Programming with databases
--------------------------

* Using the Python API for SQLite.
* Importing data without Firefox.

