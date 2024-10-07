```sql
SELECT * FROM AirlineSafety LIMIT 10;
```

```sql
INSERT INTO AirlineSafety VALUES (
            Air Canada, 1865253802, 2, 0, 0, 
            2, 0, 0);
```

```sql
UPDATE AirlineSafety SET 
            airline=Air Canada, avail_seat_km_per_week=2000000000, 
            incidents_85_99=3, fatal_accidents_85_99=1, 
            fatalities_85_99=5, incidents_00_14=2, 
            fatal_accidents_00_14=0, fatalities_00_14=0 
        WHERE id=1;
```

```sql
DELETE FROM AirlineSafety WHERE id=1;
```

```sql
SELECT * FROM AirlineSafety LIMIT 5;
```

