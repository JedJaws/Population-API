#!/usr/bin/env python3
#
# Copyright (c) 2022, Michael Shafae
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree. 
#

"""Example of how to use us_state.pckl and ca_county.pckl pickle files."""

from collections import namedtuple
import pickle
import locale

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

CACounty = namedtuple(
    'CACounty', ['name', 'county_seat', 'population', 'area_sq_mi']
)


def _str(item):
    """Handy function to return the named field name of a state or county."""
    return f'{item.name}'


State.__str__ = _str
CACounty.__str__ = _str


def main():
    """Main function"""
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
    with open('ca_county.pckl', 'rb') as file_handle:
        ca_counties = pickle.load(file_handle)

    with open('us_state.pckl', 'rb') as file_handle:
        states = pickle.load(file_handle)

    states.sort(key=lambda x: x.area_sq_mi)
    print(
        f'The largest state or territory by area is {states[-1]} ' \
        f'and the smallest one is {states[0]}.'
    )

    ca_counties.sort(key=lambda x: x.area_sq_mi)
    print(
        f'The largest CA county by area is {ca_counties[-1]}'
        f' and the smallest one is {ca_counties[0]}.'
    )
    
    print('largest county num: ', ca_counties[-1].area_sq_mi)

    total_us_population = sum([s.population for s in states])
    print(f'The total US population is {total_us_population:n}.')
    # territories_only = [s for s in states if s.n_ec_votes == 0]
    states_only = [s for s in states if s.n_rep_votes > 0]
    
    total_pop = 0
    
    least_states = []
    
    states_only.sort(key=lambda x: x.population)
    for i in range(len(states_only)):
        if total_pop < 37956694:
            total_pop = total_pop + states_only[i].population
            least_states.append(states_only[i])
            if total_pop > 41119752:
                total_pop = total_pop - states_only[i].population
                least_states.pop(states_only[i])
                break
                
    ec_sum = 0
    for l in range(len(least_states)):
         ec_sum += least_states[l].n_ec_votes
         
    ec_diff = 0
    if ec_sum < states_only[-1].n_ec_votes:
        ec_diff = states_only[-1].n_ec_votes - ec_sum
    else:
        ec_diff = ec_sum - states_only[-1].n_ec_votes
        
    print('electoral diff is: ', ec_diff)
        
    total_states_only_population = sum([s.population for s in states_only])
    print(
        f'The total US population from states is {total_states_only_population:n}.'
    )
    print(
        'This means that there are '
        f'{total_us_population - total_states_only_population:n} people'
        ' who live in US territories.'
    )
    total_ec_votes = sum([s.n_ec_votes for s in states])
    print(f'The total number of Electoral College votes is {total_ec_votes}.')

    total_ca_population = sum([c.population for c in ca_counties])
    print(f'The total population of California is {total_ca_population:n}.')
    print(
        'California is '
        f'{(total_ca_population / total_us_population) * 100:.2f}% of '
        ' the US total population.'
    )
    
    small_states = 0
    for f in states_only:
        if f.land_area_sq_mi < ca_counties[-1].area_sq_mi:
            small_states += 1
            
    print('num of small states: ', small_states)
    
    ca_counties.sort(key=lambda x: x.population, reverse=True)
    n_counties = 3
        
    q1 = sum([i.population for i in ca_counties[3:6]])
    print(q1)
    
    q2 = 0
    for m in range(2, 5):
        print('counties: ', ca_counties[m])
        q2 = q2 + ca_counties[m].population
        
    print(q2)
    
    less_than_count = 0
    for j in states_only:
        if j.population < q2:
            less_than_count += 1
            
    print(less_than_count)
        
    ca_population_largest_counties = sum(
        [c.population for c in ca_counties[:n_counties]]
    )
    county_names = ', '.join(map(str, ca_counties[:n_counties]))
    print(
        f'The population of the largest {n_counties} counties '
        f'({county_names}) in CA is {ca_population_largest_counties:n} '
        'which is '
        f'{(ca_population_largest_counties / total_ca_population) * 100:.2f}%'
        ' of CA total population or '
        f'{(ca_population_largest_counties / total_us_population) * 100:.2f}%'
        ' of the US population.'
    )

if __name__ == '__main__':
    main()
