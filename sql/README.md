Using relational databases
==========================

Topics to cover
---------------

* What is a relational database?
    * compare: text file, spreadsheet, hierarchical database, object-oriented
    * relationships between items
    * mathematical idea of *relations*...
    * ...but in practice can view as tables and rows
    * examples: MySQL, Oracle, SQLite
* When should I use a relational database?
    * structured data
    * relationships between items are important
    * ad-hoc data structures become hard to use
* When should I not use a relational database?
    * depends what the alternative is
    * scalability can be limited...
    * ...but probably isn't in your case
    * huge amounts of data, and care more about speed than consistency!
* How can I use a relational database?
    * getting data into or out of a relational database
        * by hand with SQL statements
        * from an application via an API
        * import/export from/to another format
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
