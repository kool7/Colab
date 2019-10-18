def train_cats(df):
    for n, c in df.items():
        if is_string_dtype(c): df[n] = c.astype('category').cat.as_ordered()
            
            
def add_cats(df, trn):
    for n, c in df.items():
        if trn[n].dtype.name == 'category':
            df[n] = pd.Categorical(c, categories=trn[n].cat.categories, ordered=True)
