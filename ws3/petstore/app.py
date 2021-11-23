#!/usr/bin/env python3

import datetime
import logging

import connexion
from connexion import NoContent

# our memory-only pet storage
PETS = {}


def get_pets(limit, animal_type=None):
    return {
        "pets": [
            pet
            for pet in PETS.values()
            if not animal_type or pet["animal_type"] == animal_type
        ][:limit]
    }


def get_pet(pet_id):
    pet = PETS.get(pet_id)
    return pet or ("Not found", 404)


def put_pet(pet_id, body):
    # note: the parameter above for the body *must* be named body.
    pet = body
    exists = pet_id in PETS
    pet["id"] = pet_id
    if exists:
        logging.info("Updating pet %s..", pet_id)
        PETS[pet_id].update(pet)
    else:
        logging.info("Creating pet %s..", pet_id)
        pet["created"] = datetime.datetime.utcnow()
        PETS[pet_id] = pet
    return NoContent, (200 if exists else 201)


def delete_pet(pet_id):
    if pet_id in PETS:
        logging.info("Deleting pet %s..", pet_id)
        del PETS[pet_id]
        return NoContent, 204
    else:
        return NoContent, 404


logging.basicConfig(level=logging.INFO)
app = connexion.App(__name__, port=7070, specification_dir="openapi/", server="gevent")
app.add_api("openapi.yaml")
application = app.app  # expose global WSGI application object

if __name__ == "__main__":
    # run our standalone gevent server
    app.run(port=7070, server="gevent")
