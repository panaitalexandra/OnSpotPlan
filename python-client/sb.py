from supabase_config import supabase

response = supabase.table("utilizatori").select("*").execute()
print(response.data)