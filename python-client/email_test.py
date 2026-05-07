from supabase_config import supabase

email_utilizator = "alegabi0504@gmail.com"
parola = "ParolaTest123!"

try:
    print(f"Se trimite e-mail de confirmare către {email_utilizator}...")

    res = supabase.auth.sign_up({
        "email": email_utilizator,
        "password": parola
    })

    print("✅ SUCCES! Verifică-ți Inbox-ul (sau folderul Spam).")
    print("Ar trebui să primești un mail de la 'noreply@mail.supabase.co'.")

except Exception as e:
    print(f"❌ Eroare la trimitere: {e}")