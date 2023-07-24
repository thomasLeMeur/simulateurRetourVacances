import datetime
import json

from enum import Enum
from pydantic import BaseModel, PositiveInt
from jours_feries_france import JoursFeries

ZoneEnum = Enum('ZoneENum', {zone: zone for zone in JoursFeries.ZONES})

class ConfigurationModel(BaseModel):
    date_arret_travail: datetime.date
    nb_jours_arret: PositiveInt
    ponts_inclus: bool
    zone: ZoneEnum

if __name__ == "__main__":
    with open("conf.json", mode="rb") as file:
        config = ConfigurationModel(**json.load(file))
    
    current_date = config.date_arret_travail
    remaining_days_off = config.nb_jours_arret
    while remaining_days_off > 0:
        next_day = current_date + datetime.timedelta(days=1)

        step: int
        # Do not take in account the week-end
        if current_date.isoweekday() in [6, 7]:
            step = 1
        # If tuesday is a bank holday, do not take in account it (+ monday ?)
        elif not config.ponts_inclus and current_date.isoweekday() == 1 and JoursFeries.is_bank_holiday(next_day, zone=config.zone.value):
            step = 2
        # If tuesday is a bank holday, do not take in account it (+ friday ?)
        elif not config.ponts_inclus and current_date.isoweekday() == 4 and JoursFeries.is_bank_holiday(current_date, zone=config.zone.value):
            step = 2
        # Do not take in account bank holday
        elif JoursFeries.is_bank_holiday(current_date, zone=config.zone.value):
            step = 1
        # Else, use a day off
        else:
            step = 1
            remaining_days_off -= 1
        
        current_date = current_date + datetime.timedelta(days=step)
    
    print(f"Arrêt de travail: {config.date_arret_travail}")
    print(f"Nombre de jours d'arrêt: {config.nb_jours_arret}")
    print(f"Le nombre de jours d'arrêt inclus les ponts à poser: {'Oui' if config.ponts_inclus else 'Non'}")
    print(f"=> Le travail reprendra le {current_date}")