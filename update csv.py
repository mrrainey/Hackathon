import pandas

data = pandas.read_csv('train/index.csv')

data = data.drop(columns="mask")

def split_url(row):
    return row.split('/')[1]


data['image'] = data['image'].apply(split_url)

data.to_csv('train/updated_csv.csv', index=False)