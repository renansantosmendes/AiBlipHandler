import json
import requests_async as requests
import asyncio

class Intent:
    def __init__(self, verbose:bool=True):
        self.intent_name = ''
        self.intent_id = ''
        self.examples = []
        self.count_questions = None
        self.health_score = None
        self.storage_date = None
        self.bot_key = None
        self.verbose = verbose
        self.blip_url = 'https://msging.net/commands'
        
    def _retrieve_examples(self):
        self.header = {
            'Content-Type':'application/json',
            'Authorization':'Key ' + self.bot_key.replace('Key','').replace('key','').strip()
            }
        self.body = {
            "id": "123561215",
            "to": "postmaster@ai.msging.net",
            "method": "get",
            "uri": "/intentions/{}".format(self.intent_id)
        }
        
        r = asyncio.get_event_loop().run_until_complete(self.__send_request())
        print(r.json())
        return r#.json()['status']
    
    async def __send_request(self):
        r = await requests.post(self.blip_url, json.dumps(self.body), headers=self.header)
        return r
    
    def set_bot_key(self, bot_key:str):
        self.bot_key = bot_key
        
    def set_intent_id(self, intent_id:str):
        self.intent_id = intent_id