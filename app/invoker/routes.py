from quart import current_app as app, make_response, request, Blueprint, g

invoker_bp = Blueprint("invoker", __name__, url_prefix="/invoker")

@invoker_bp.route("/", methods = ["GET"])
async def invo():
    return "Invo working"