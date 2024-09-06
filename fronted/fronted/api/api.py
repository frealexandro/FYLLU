
from .SupabaseAPI import SupabaseAPI
from fronted.model.Featured import Featured

SUPABASE_API = SupabaseAPI()



async def featured() -> list[Featured]:
    return SUPABASE_API.featured()