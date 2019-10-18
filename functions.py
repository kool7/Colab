def train_cats(df):
    for n, c in df.items():
        if is_string_dtype(c): df[n] = c.astype('category').cat.as_ordered()
            
# NOTE: is_string_dtype isn't working in kaggle it is part of pandas api so I imported it as follows in kaggle ,
# pandas.api.types.is_string_type 
            
def add_cats(df, trn):
    for n, c in df.items():
        if trn[n].dtype.name == 'category':
            df[n] = pd.Categorical(c, categories=trn[n].cat.categories, ordered=True)
