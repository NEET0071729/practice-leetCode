import pandas as pd

data = [[1, 3.5], [2, 3.65], [3, 4.0], [4, 3.85], [5, 4.0], [6, 3.65]]
scores = pd.DataFrame(data, columns=['id', 'score']).astype({'id':'Int64', 'score':'Float64'})

# def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
#     scores.sort_values(by = 'score', ascending=False, inplace=True)
#     la = [0] * len(scores.index)
#     scores = scores.reset_index(drop=True)
#     print(scores)
#     scores['rank'] = la
#     l = None
#     m = 1
#     for x in scores.index:
#         if l == scores.at[x, 'score']:
#             scores.at[x, 'rank'] = m
#         else:
#             m += 1
#             scores.at[x, 'rank'] = m
#             l = scores.at[x, 'score']
#     return scores[['score', 'rank']]

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores['rank'] = scores['score'].rank(method='dense', ascending=False)
    scores.sort_values(by= 'rank', inplace=True)
    return scores[['score', 'rank']]


print(order_scores(scores))