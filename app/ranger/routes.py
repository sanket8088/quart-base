from quart import current_app as app, make_response, request, Blueprint, g

ranger_bp = Blueprint("ranger", __name__, url_prefix="/ranger")

@ranger_bp.route("/", methods = ["GET"])
async def ranger():
    return "Ranger working"