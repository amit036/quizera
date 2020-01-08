from app.main import db
from app.main.models.batch import Batch
from flask import jsonify


def add_new_batch(data):
    """method to add new batch to the model Batch
    Args:
        data (dict): data which needs to be stored into Batch table
                    using Batch model
    Returns:
        dict, int: response object containing appropriate response based on the response from save changes,
                    http response code specifying the success or failure of storing data into table
    """
    batch = Batch(
        batch_name=data['batch_name']
    )
    db.session.add(batch)
    db.session.commit()
    response_object = jsonify({"response": "successfully added Batch"})
    return response_object, 200