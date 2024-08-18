import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.cluster import KMeans
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

childrenBooks = pd.read_csv("children_books.csv")
stories = pd.read_csv("children_stories.csv", encoding='ISO-8859-1')

childrenBooks["Inerest_age"] = childrenBooks["Inerest_age"].str.extract('(\d+)').astype(float)
childrenBooks['Reading_age'] = childrenBooks['Reading_age'].str.extract('(\d+)').astype(float)

stories['cats'] = stories['cats'].str.extract('(\d+)').astype(float)

oneHotEncoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
oneHEncodeAuthor = oneHotEncoder.fit_transform(childrenBooks[['Author']])
authorEncodedDF = pd.DataFrame(oneHEncodeAuthor, columns=oneHotEncoder.get_feature_names_out(['Author']))
childrenBooks = pd.concat([childrenBooks, authorEncodedDF], axis=1)
childrenBooks.drop(['Author'], axis=1, inplace=True)

X = childrenBooks.drop(columns=['Title', 'Desc'])
y = childrenBooks['Title']

scaler = StandardScaler()
xScaled = scaler.fit_transform(X)

kmeans = KMeans(n_clusters=5, n_init=10, random_state=42)
clusters = kmeans.fit_predict(xScaled)

childrenBooks['Cluster'] = clusters

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
randomFmodel = RandomForestClassifier(n_estimators=100, random_state=42)
randomFmodel.fit(X_train, y_train)

def recommendStories(user_interest_age, user_reading_age):
    userinputEncoded = pd.DataFrame({
        'Inerest_age': [user_interest_age],
        'Reading_age': [user_reading_age]
    })

    for col in X.columns:
        if col not in userinputEncoded.columns:
            userinputEncoded[col] = 0

    userinputEncoded = userinputEncoded[X.columns]

    user_input_scaled = scaler.transform(userinputEncoded)
    
    userCluster = kmeans.predict(user_input_scaled)[0]
    
    recommendedStories = childrenBooks[childrenBooks['Cluster'] == userCluster]
    
    return recommendedStories[['Title', 'Desc']]

def preprocessData(data):
    scaler = StandardScaler()
    scaledData = scaler.fit_transform(data)
    return scaledData, scaler

def trainModels(X, y):
    kmeans = KMeans(n_clusters=5, n_init=10, random_state=42)
    clusters = kmeans.fit_predict(X)

    randomFmodel = RandomForestClassifier(n_estimators=100, random_state=42)
    randomFmodel.fit(X, y)

    return kmeans, randomFmodel
