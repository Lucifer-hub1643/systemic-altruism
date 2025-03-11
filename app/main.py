from fastapi import FastAPI, Query, HTTPException
from typing import List, Optional
from app.model_recommender import get_recommendations

app = FastAPI(title="Video Recommendation Engine")

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI! Your app and Base are set up."}

@app.get("/feed", response_model=List[dict])
async def get_feed(
    username: str = Query(...),
    category_id: Optional[int] = None,
    page: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1)
):
    try:
        recommendations = get_recommendations(username, category_id)
        # Apply pagination to the recommendations list
        start = (page - 1) * page_size
        end = start + page_size
        paginated = recommendations[start:end]
        if not paginated:
            raise HTTPException(status_code=404, detail="No recommendations found for the given page parameters.")
        return paginated
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
