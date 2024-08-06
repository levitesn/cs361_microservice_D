from fastapi import FastAPI, HTTPException
from random import choice

app = FastAPI()

# Dictionary of travel tips categorized
travel_tips = {
    "packing": [
        "Roll your clothes instead of folding them.",
        "Use packing cubes to save space.",
        "Pack a reusable water bottle."
    ],
    "safety": [
        "Always keep a copy of your important documents.",
        "Be aware of your surroundings.",
        "Avoid flashing valuables in public."
    ],
    "budget": [
        "Travel during the off-season to save money.",
        "Look for free activities in your destination.",
        "Use public transportation instead of taxis."
    ]
}


@app.get("/random_tip")
async def get_random_tip():
    all_tips = [tip for tips in travel_tips.values() for tip in tips]
    return {"tip": choice(all_tips)}


@app.get("/categorytip/{category}")
async def get_category_tip(category: str):
    if category not in travel_tips:
        raise HTTPException(status_code=404, detail="Category not found")
    return {"tip": choice(travel_tips[category])}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
