import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OrdinalEncoder
df = pd.DataFrame(
    {
        "cargo" : ["gerente", "analista", "asistente", "gerente", "analista", "asistente"],
        
        "departamento" : ["ventas", "marketing", "RH", "ventas", "marketing", "RH"],
        
        "ubicacion" : ["norte", "sur", "este", "oeste", "norte", "sur"]
    }   
)
print(df)

#ONE-HOT-ENCODING
model = OneHotEncoder()
df_model = pd.DataFrame(model.fit_transform(df).toarray(), columns=model.get_feature_names_out(df.columns))

print(df_model)

df_pandas = pd.get_dummies(df)
print(df_pandas)


#LABEL-ENCODING
model2 = LabelEncoder()
df_label = df.copy()
df_label["cargo"] = model2.fit_transform(df_label["cargo"])
df_label["departamento"] = model2.fit_transform(df_label["departamento"])
df_label["ubicacion"] = model2.fit_transform(df_label["ubicacion"])
print(df_label)

#FAST_VERSION
model3 = OrdinalEncoder()
df_OE = df.copy()
df_OE[["cargo", "departamento", "ubicacion"]] = model3.fit_transform(df_OE[["cargo", "departamento", "ubicacion"]])

print(df_OE)

#SELF FUNCTION
def label_encoder(df, columns):
    for column in columns:
        unique_values = df[column].unique()
        value_to_int = {value : i for i, value in enumerate(unique_values)}
        df[column + "_encoded"] = df[column].replace(value_to_int)
    return df

df_label_custom = label_encoder(df, ["cargo", "departamento", "ubicacion"])
print(df_label_custom)