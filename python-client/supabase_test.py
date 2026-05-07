from supabase_config import supabase

print("Se încearcă scrierea în Cloud...")

date_test = {
    "name": "testName",
    "surname": "testsur",
    "cnp": "9999999999999",
    "phone": "0700000000"
}

try:
    rezultat = supabase.table("profiles").insert(date_test).execute()
    print("✅ SUCCES! Datele au fost trimise.")
    print("Verifică acum tabelul 'profiles' în browser!")
except Exception as e:
    print(f"❌ EROARE: {e}")