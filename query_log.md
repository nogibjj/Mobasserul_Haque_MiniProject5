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

```sql
SELECT * FROM AirlineSafety LIMIT 10;
```

```sql
SELECT * FROM AirlineSafety WHERE airline = 'Air Canada';
```

```sql
INSERT INTO AirlineSafety VALUES (
            Air Canada, 1865253802, 2, 0, 0, 
            2, 0, 0);
```

```sql
UPDATE AirlineSafety SET 
            airline=Air Canada, avail_seat_km_per_week=1900000000, 
            incidents_85_99=3, fatal_accidents_85_99=1, 
            fatalities_85_99=5, incidents_00_14=1, 
            fatal_accidents_00_14=0, fatalities_00_14=0 
        WHERE id=1;
```

```sql
INSERT INTO AirlineSafety VALUES (
            Airline A, 500000, 5, 0, 0, 
            2, 0, 0);
```

```sql
INSERT INTO AirlineSafety VALUES (
            Airline B, 700000, 8, 1, 10, 
            3, 0, 0);
```

```sql
INSERT INTO AirlineSafety VALUES (
            Airline C, 800000, 10, 2, 20, 
            5, 1, 1);
```

```sql
SELECT * FROM AirlineSafety LIMIT 5;
```

```sql
INSERT INTO AirlineSafety VALUES (
            Airline A, 500000, 5, 0, 0, 
            2, 0, 0);
```

```sql
INSERT INTO AirlineSafety VALUES (
            Airline B, 700000, 8, 1, 10, 
            3, 0, 0);
```

```sql
INSERT INTO AirlineSafety VALUES (
            Airline C, 800000, 10, 2, 20, 
            5, 1, 1);
```

```sql
SELECT * FROM AirlineSafety LIMIT 5;
```

```sql
UPDATE AirlineSafety SET 
            airline=Updated Airline A, avail_seat_km_per_week=600000, 
            incidents_85_99=3, fatal_accidents_85_99=0, 
            fatalities_85_99=1, incidents_00_14=0, 
            fatal_accidents_00_14=0, fatalities_00_14=0 
        WHERE id=1;
```

```sql
SELECT * FROM AirlineSafety LIMIT 5;
```

```sql
DELETE FROM AirlineSafety WHERE id=2;
```

```sql
SELECT * FROM AirlineSafety LIMIT 5;
```

```sql
SELECT * FROM AirlineSafety WHERE avail_seat_km_per_week > 600000;
```

```sql
SELECT * FROM AirlineSafety LIMIT 5;
```

```sql
INSERT INTO AirlineSafety VALUES (
            Airline A, 500000, 5, 0, 0, 
            2, 0, 0);
```

```sql
INSERT INTO AirlineSafety VALUES (
            Airline B, 700000, 8, 1, 10, 
            3, 0, 0);
```

```sql
INSERT INTO AirlineSafety VALUES (
            Airline C, 800000, 10, 2, 20, 
            5, 1, 1);
```

```sql
SELECT * FROM AirlineSafety LIMIT 5;
```

```sql
UPDATE AirlineSafety SET 
            airline=Updated Airline A, avail_seat_km_per_week=600000, 
            incidents_85_99=3, fatal_accidents_85_99=0, 
            fatalities_85_99=1, incidents_00_14=0, 
            fatal_accidents_00_14=0, fatalities_00_14=0 
        WHERE id=1;
```

```sql
SELECT * FROM AirlineSafety LIMIT 5;
```

```sql
DELETE FROM AirlineSafety WHERE id=2;
```

```sql
SELECT * FROM AirlineSafety LIMIT 5;
```

```sql
SELECT * FROM AirlineSafety WHERE avail_seat_km_per_week > 600000;
```

```sql
SELECT * FROM AirlineSafety LIMIT 5;
```

```sql
INSERT INTO AirlineSafety VALUES (
            New Airline, 1000000, 2, 0, 0, 
            1, 0, 0);
```

