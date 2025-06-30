import numpy as np

def ObjectToFloat(data, features):
    for feature in features:
        feature_keys   = data[feature].value_counts().index
        feature_values = np.arange(1, len(feature_keys) + 1)
        feature_dict = {}
        for i in range(len(feature_keys)):
            feature_dict[feature_keys[i]] = feature_values[i]
        data[feature] = data[feature].map(feature_dict)
    return data


def getObjectsFeaturesList(df):
    features_for_replace = []
    for f in df:
        if type(df.at[1, f]) == str:
            features_for_replace.append(f)
    return features_for_replace
    
def ExpToFloat(Value):
    return float('%.2f'%Value)
    
def ExpToInteger(Value):
    return int('%d'%Value)