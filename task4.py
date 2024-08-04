import pandas as pd
import numpy as np

# Sample data (user ratings for movies)
data = {
    'User': ['User1', 'User2', 'User3'],
    'Movie1': [5, 4, 3],
    'Movie2': [3, 5, 4],
    'Movie3': [4, 3, 5]
}

df = pd.DataFrame(data)

# Calculate similarity (e.g., cosine similarity between users)
def cosine_similarity(user1, user2):
    # Assume ratings are in columns Movie1, Movie2, Movie3
    ratings1 = df.loc[df['User'] == user1].values[:, 1:]
    ratings2 = df.loc[df['User'] == user2].values[:, 1:]
    return np.dot(ratings1, ratings2.T) / (np.linalg.norm(ratings1) * np.linalg.norm(ratings2))

# Recommend movies based on similar users' preferences
def recommend_movies(user):
    similar_users = df['User'][df['User'] != user]
    recommendations = {}
    for other_user in similar_users:
        similarity = cosine_similarity(user, other_user)
        other_user_ratings = df.loc[df['User'] == other_user].values[:, 1:]
        user_ratings = df.loc[df['User'] == user].values[:, 1:]
        recommendations[other_user] = np.sum(similarity * other_user_ratings) / np.sum(np.abs(similarity))
    
    # Sort recommendations by score
    sorted_recommendations = sorted(recommendations.items(), key=lambda x: x[1], reverse=True)
    return sorted_recommendations

user_to_recommend = 'User1'
recommended_movies = recommend_movies(user_to_recommend)
print(f"Recommended movies for {user_to_recommend}:")
for user, score in recommended_movies:
    print(f"{user}: {score:.2f}")