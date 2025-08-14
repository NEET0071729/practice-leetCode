import pandas as pd

data = [['1', '1', '10', '1', 'completed', '2013-10-01'], ['2', '2', '11', '1', 'cancelled_by_driver', '2013-10-01'], ['3', '3', '12', '6', 'completed', '2013-10-01'], ['4', '4', '13', '6', 'cancelled_by_client', '2013-10-01'], ['5', '1', '10', '1', 'completed', '2013-10-02'], ['6', '2', '11', '6', 'completed', '2013-10-02'], ['7', '3', '12', '6', 'completed', '2013-10-02'], ['8', '2', '12', '12', 'completed', '2013-10-03'], ['9', '3', '10', '12', 'completed', '2013-10-03'], ['10', '4', '13', '12', 'cancelled_by_driver', '2013-10-03']]
trips = pd.DataFrame(data, columns=['id', 'client_id', 'driver_id', 'city_id', 'status', 'request_at']).astype({'id':'Int64', 'client_id':'Int64', 'driver_id':'Int64', 'city_id':'Int64', 'status':'object', 'request_at':'object'})

data = [['1', 'No', 'client'], ['2', 'Yes', 'client'], ['3', 'No', 'client'], ['4', 'No', 'client'], ['10', 'No', 'driver'], ['11', 'No', 'driver'], ['12', 'No', 'driver'], ['13', 'No', 'driver']]
users = pd.DataFrame(data, columns=['users_id', 'banned', 'role']).astype({'users_id':'Int64', 'banned':'object', 'role':'object'})

def trips_and_users(trips: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame:
    trips['request_at'] = pd.to_datetime(trips['request_at'])
    start_date = pd.to_datetime('2013-10-01')
    end_date = pd.to_datetime('2013-10-03')
    users_dr = users[users['role'] == 'driver']
    users_cl = users[users['role'] == 'client']
    trips = trips[(trips['request_at']>=start_date) & (trips['request_at']<=end_date)]
    ans = trips.merge(users_cl, how='left', left_on='client_id', right_on='user_id', suffixes=('_l', '_r'), sort=False)
    ans.rename(columns= {'driver_id_l': 'driver_id'}, inplace=True)
    ans = ans.merge(users_dr, how='left', left_on='driver_id', right_on='user_id', suffixes=('_l2', '_r2'), sort=False)
    ans = ans[ans['banned_r_l2'] == 'No' | ans['banned_r2'] == 'No']
    print(ans)

print(trips_and_users(trips, users))