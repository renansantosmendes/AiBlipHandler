import asyncio
from Intent import Intent

if __name__ == '__main__':
    print('Testing AiBLiP')
    key1 = 'Key cGFnc2VndXJvZXhwZXJpbWVudG9zOnNua09LQWJxNU11ZExoZkxKMFJJ'
    intent = Intent()
    intent.set_bot_key(key1)
    intent.set_intent_id('alterar_dados')
    intent._retrieve_examples()
    print('Finished...')