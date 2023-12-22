from io import BytesIO
import json
from app.utils.schema import  ItemRecordResponse
import os
from supabase import create_client, Client


class SupabaseService:
    def __init__(self):
        # This will be called once when the app starts (put the expensive init here)

        print('---- supabase_service init-----')

        # Supabase Initialization
        url: str = os.environ.get("SUPABASE_URL")
        key: str = os.environ.get("SUPABASE_KEY")
        self.supabase: Client = create_client(url, key)

  
    def record_item(self, data: json) -> ItemRecordResponse:
       
        res, count = self.supabase.table('responses').insert({"response": data}).execute()

        print('data: ', data)
        print('res', res)
        return res