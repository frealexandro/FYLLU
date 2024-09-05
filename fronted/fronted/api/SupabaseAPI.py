import os
import dotenv
from supabase import create_client, Client

class SupabaseAPI:
    dotenv.load_dotenv()

    SUPABASE_URL = os.environ.get("SUPABASE_URL")
    SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

    def __init__(self) -> None:
        if self.SUPABASE_URL is not None and self.SUPABASE_KEY is not None:
            self.supabase: Client = create_client(
                self.SUPABASE_URL, self.SUPABASE_KEY
            )
        else:
            raise ValueError("SUPABASE_URL y SUPABASE_KEY deben estar configurados")

    def email_exists(self, email: str) -> bool:
        try:
            response = self.supabase.table("wailist").select("mail").eq("mail", email).execute()
            print(f"Respuesta de verificación de email: {response}")
            return len(response.data) > 0
        except Exception as e:
            print(f"Error al verificar el email: {str(e)}")
            return False

    def save_email(self, email: str) -> None:
        if not self.email_exists(email):
            data = {"mail": email}
            try:
                print(f"Intentando guardar email: {email}")
                response = self.supabase.table("wailist").insert(data).execute()
                print(f"Respuesta completa de inserción: {response}")
                if hasattr(response, 'data') and len(response.data) > 0:
                    print("Email guardado exitosamente en Supabase")
                else:
                    print("Error al guardar el email en Supabase:", response)
            except Exception as e:
                print(f"Error al guardar el email en Supabase: {str(e)}")
        else:
            print("El email ya existe en la lista de espera")

