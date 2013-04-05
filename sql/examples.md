Example SQL queries on mammals survey data
==========================================

Write a query that returns only the species column:
```sql
SELECT species FROM surveys;
```

Exercise: Write a query that returns the day, month, year, species ID, and
weight for individuals that weigh more than 75 grams.
```sql
SELECT day, month, year, species, wgt FROM surveys WHERE wgt > 75;
```

Exercise: Write a query that returns the day, month, year, species ID, and
weight (in kg) for individuals caught on plot 1 that weigh more than 0.075 kg.

```sql
SELECT day, month, year, species, wgt/1000.0 FROM surveys WHERE plot = 1 AND wgt
> 75;
```

```sql
SELECT day, month, year, species, (wgt/1000.0) AS wkg FROM surveys WHERE plot =
1 AND wkg > 0.075;
```

Exercise: Write a query that returns all of the data in the plots table, sorted
alphabetically by plot type and then (within each plot type), in descending
order of the plot ID.
```sql
SELECT * FROM plots ORDER BY plot_type ASC, plot_id DESC;
```

Exercise: Let’s try to combine what we’ve learned so far in a single query.
Let’s go back to the surveys table and lets say that we want to display the
three date fields, species ID, and weight in kilograms (rounded to two decimal
places), for rodents captured in 1999, ordered alphabetically by the species ID.
```sql
SELECT day, month, year, species, round(wgt/1000.0,2)
  FROM surveys
  WHERE year = 1999
  ORDER BY species ASC;
```

Add condition so only show cases where species is recorded:
```sql
SELECT day, month, year, species, round(wgt/1000.0,2)
  FROM surveys
  WHERE year = 1999
    AND species IS NOT NULL
  ORDER BY species ASC;
```

Find the full name of the species with the largest mean weight:
```sql
SELECT species.genus, species.species, meanweights.meanweight FROM 
  (SELECT species AS species, AVG(wgt) AS meanweight
      FROM surveys
      GROUP BY species
      ORDER BY meanweight DESC) AS meanweights
  JOIN species ON species.species_ID = meanweights.species
LIMIT 1
;
```

Modify the query so it returns the average mass of individuals of all *Sigmodon* species
on each type of plot.
```sql
SELECT plots.plot_type, AVG(surveys.wgt)
    FROM 
      surveys
        JOIN plots
          ON surveys.plot = plots.plot_id
        JOIN species
          ON surveys.species = species.species_id
    WHERE species.genus = 'Sigmodon'
    GROUP BY plots.plot_type;
```

