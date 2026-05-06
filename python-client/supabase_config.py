from supabase import create_client

URL = "https://jvrgvusbfdvuaymucuud.supabase.co"
KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imp2cmd2dXNiZmR2dWF5bXVjdXVkIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzgwNjc3NzUsImV4cCI6MjA5MzY0Mzc3NX0.g7j3mfFvS636trP5f-j9MF44fOBKzkXcFaey-T1Mpjg"

supabase = create_client(URL, KEY)
