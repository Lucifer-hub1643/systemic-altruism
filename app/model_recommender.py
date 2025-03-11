def get_recommendations(username: str, category_id: int = None):
    # Dummy recommendation logic; replace with your deep neural network algorithm later.
    dummy_recommendations = [
        {"id": 1, "title": "Motivational Video 1", "category": "motivation"},
        {"id": 2, "title": "Motivational Video 2", "category": "motivation"},
        {"id": 3, "title": "Inspirational Video 1", "category": "inspiration"},
    ]
    if category_id:
        # Dummy filtering based on category_id.
        return [video for video in dummy_recommendations if video["id"] == category_id]
    return dummy_recommendations
