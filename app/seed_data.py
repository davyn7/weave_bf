# app/seed_data.py

async def seed_data():
    await add_province_db(ProvinceBase(NAME="Jakarta"))
    await add_city_db(CityBase(NAME="Jakarta Selatan", PROVINCE_ID=1))