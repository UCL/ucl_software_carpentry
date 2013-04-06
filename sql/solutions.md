Example SQL queries on mammals survey data
==========================================

---

Write a query that returns only the species column.

```sql
SELECT species FROM surveys;
```

---

Write a query that returns the day, month, year, species ID, and
weight for individuals that weigh more than 75 grams.

```sql
SELECT day, month, year, species, wgt FROM surveys WHERE wgt > 75;
```

---

Write a query that returns the day, month, year, species ID, and
weight (in kg) for individuals caught on plot 1 that weigh more than 0.075 kg.

```sql
SELECT day, month, year, species, wgt/1000.0 
  FROM
    surveys
  WHERE
    plot = 1 AND wgt > 75;
```

Using ```AS``` to name the calculated quantity:

```sql
SELECT day, month, year, species, (wgt/1000.0) AS weight_kg
  FROM
    surveys
  WHERE
    plot = 1 AND weight_kg > 0.075;
```

---

Write a query that returns all of the data in the plots table, sorted
alphabetically by plot type and then (within each plot type) in descending
order of the plot ID.

```sql
SELECT *
  FROM
    plots
  ORDER BY
    plot_type ASC, plot_id DESC;
```

---

Write a query on the `surveys` table to display the three date fields,
species ID, and weight in kilograms (rounded to two 
decimal places) for rodents captured in 1999, ordered alphabetically by 
the species ID.

```sql
SELECT day, month, year, species, round(wgt/1000.0,2)
  FROM surveys
  WHERE year = 1999
  ORDER BY species ASC;
```

---

Modify the previous query to display results only for individuals whose species and weight
were recorded.

```sql
SELECT day, month, year, species, round(wgt/1000.0,2)
  FROM surveys
  WHERE year = 1999
    AND wgt IS NOT NULL
  ORDER BY species ASC;
```

---

From the surveys table, use one query to output the total weight, average weight, and the min and max weights.

```sql
SELECT SUM(wgt), AVG(wgt), MIN(wgt), MAX(wgt)
  FROM
    surveys;
```

---

How many individuals were counted in each year?

```sql
SELECT year, COUNT(*)
  FROM
    surveys
  WHERE
    species IS NOT NULL
  GROUP BY
    year;
```

---

How many individuals were counted in each species in each year?

```sql
SELECT year, species, COUNT(*)
  FROM
    surveys
  WHERE
    species IS NOT NULL
  GROUP BY
    year, species;
```

Write a query that lets us look at which years contained the most individuals and which had the least.

```sql
SELECT year, count(*) AS number
  FROM
    surveys
  WHERE
    species IS NOT NULL
  GROUP BY
    year
  ORDER BY
    number DESC;
```

---

Write a query that shows us which species had the largest and smallest individuals on average.

```sql
SELECT species, AVG(wgt) AS mean_weight
  FROM
    surveys
  WHERE
    species IS NOT NULL
  GROUP BY
    species
  ORDER BY
    mean_weight DESC;
```

---

Write a query that returns the genus, the species, and the weight of every individual captured.

```sql
SELECT species.genus, species.species, surveys.wgt
  FROM
    species
      JOIN surveys
      ON species.species_id = surveys.species;
```

---

Starting with query to find average mass of the individuals on each different type of treatment:

```sql
SELECT plots.plot_type, AVG(surveys.wgt)
  FROM surveys
    JOIN plots
    ON surveys.plot = plots.plot_id
  GROUP BY plots.plot_type;
```

Modify the query above so that it returns only the average mass of the individuals of Sigmodon hispidus on each type of plot.

```sql
SELECT plots.plot_type, AVG(surveys.wgt)
  FROM surveys
    JOIN plots
    ON surveys.plot = plots.plot_id
  WHERE surveys.species = 'SH'
  GROUP BY plots.plot_type;
```

Modify the query so it returns the average mass of individuals of all Sigmodon species on each type of plot.

```sql
SELECT plots.plot_type, AVG(surveys.wgt)
  FROM surveys
    JOIN plots
      ON surveys.plot = plots.plot_id
    JOIN species
      ON species.species_id = surveys.species
  WHERE species.genus = 'Sigmodon'
  GROUP BY plots.plot_type;
```

Not included in lecture notes
-----------------------------

---

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

---

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

