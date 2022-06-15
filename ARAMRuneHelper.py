import willump
import json
import asyncio
import webbrowser

async def newChampion(data):
    #Iterate the JSON file to match the received ID to the Champion name
    for champs in champions['data']:
        if int(champions['data'][champs]['key']) is int(data['data']):
            championURL = f"https://poro.gg/champions/{champions['data'][champs]['id']}/aram"
            webbrowser.open(championURL.lower(), new=0, autoraise=True)


async def main():
    global wlp 
    global champions

    # Start the Willump module for interfacing with the League Client
    wlp = await willump.start()

    # Open the JSON file with all the Champion : ID information
    f = open('champions.json', 'r', encoding='utf-8')
    champions = json.load(f)
	
    # Subscribe to the "current champion" event, which is triggered everytime a new champion is locked in
    championSubscription = await wlp.subscribe('OnJsonApiEvent_lol-champ-select_v1_current-champion', default_handler=newChampion)

    while True:
        await asyncio.sleep(10)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        loop.run_until_complete(wlp.close())

