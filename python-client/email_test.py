from supabase_config import supabase

# DATE REALE PENTRU TEST
email_utilizator = "alegabi0504@gmail.com"
parola = "ParolaTest123!"

try:
    print(f"Se trimite e-mail de confirmare către {email_utilizator}...")

    # Această comandă face totul:
    # 1. Creează userul în sistem
    # 2. Trimite e-mailul automat prin serverele Supabase
    res = supabase.auth.sign_up({
        "email": email_utilizator,
        "password": parola
    })

    print("✅ SUCCES! Verifică-ți Inbox-ul (sau folderul Spam).")
    print("Ar trebui să primești un mail de la 'noreply@mail.supabase.co'.")

except Exception as e:
    print(f"❌ Eroare la trimitere: {e}")