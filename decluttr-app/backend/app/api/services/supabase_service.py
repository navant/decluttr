from app.utils.schema import  ItemRecordResponse, Item
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

  
    def record_item(self, item: Item) -> ItemRecordResponse:
       
        res, count = self.supabase.table('responses').insert({"response": item.model_dump()}).execute()

        print("Result, count:",  res, count)

        item_record_response = ItemRecordResponse(data="TODO: improve return datatype" )
        return item_record_response