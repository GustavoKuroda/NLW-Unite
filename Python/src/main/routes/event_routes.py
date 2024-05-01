from flask import Blueprint, jsonify, request
from src.http_types.http_request import HttpRequest
from src.data.event_handler import EventHandler

event_route_bp = Blueprint("event_route", __name__)

@event_route_bp.route("/events", methods=["POST"])
def create_event():
    """    Create an event and register it using the HTTP request.

    This function creates an event using the HTTP request body and registers it using the EventHandler.

    Returns:
        tuple: A tuple containing the JSON response body and the HTTP status code.
    """

    http_request = HttpRequest(body=request.json)
    event_handler = EventHandler()
    http_response = event_handler.register(http_request)
    
    return jsonify(http_response.body), http_response.status_code

@event_route_bp.route("/events/<event_id>", methods=["GET"])
def get_event(event_id):
    """    Get event details by event ID.

    This function retrieves event details using the provided event ID by making an HTTP request to the event handler.

    Args:
        event_id (int): The unique identifier of the event.

    Returns:
        tuple: A tuple containing the JSON response body and the HTTP status code.
    """

    event_handler = EventHandler()
    http_request = HttpRequest(param={"event_id": event_id})
    http_response = event_handler.find_by_id(http_request)

    return jsonify(http_response.body), http_response.status_code