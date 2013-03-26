Example SQL queries on mammals survey data
==========================================

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
