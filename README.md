
# Pickled Population Data for California and The United States

There are two pickle files in this repository.
* us_state.pckl
* ca_county.pckl

The file us_state.pckl contains information about United States territories and states. The pickle file contains a list of named tuples. The definition for the named tuple is given below.

```python
State = namedtuple(
    'State',
    [
        'name',
        'area_sq_mi',
        'land_area_sq_mi',
        'water_area_sq_mi',
        'population',
        'n_rep_votes',
        'n_senate_votes',
        'n_ec_votes',
    ],
)
```

The file ca_county.pckl contains information about the counties in the state of California. The pickle file contains a list of named tuples. The dfinition for the named tuple is given below.

```python
CACounty = namedtuple(
    'CACounty', ['name', 'county_seat', 'population', 'area_sq_mi']
)
```

The file example_app.py is an example application using these two pickle files. Running this example will yield the following output.
```
$ ./example_app.py 
The largest state or territory by area is Alaska and the smallest one is District of Columbia.
The largest CA county by area is San Bernardino County and the smallest one is San Francisco.
The total US population is 335,073,176.
The total US population from states is 330,759,736.
This means that there are 4,313,440 people who live in US territories.
The total number of Electoral College votes is 535.
The total population of California is 39,237,836.
California is 11.71% of  the US total population.
The population of the largest 3 counties (Los Angeles County, San Diego County, Orange County) in CA is 16,283,422 which is 41.50% of CA total population or 4.86% of the US population.
```

