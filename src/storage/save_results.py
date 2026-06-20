import json 
from datetime import datetime

def save_results(results):
    filename = f"results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(f"data/results/{filename}","w") as f :
        json.dump(results,f,indent=4)
    return filename