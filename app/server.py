from quart import Quart, request, g
from quart_cors import cors
from .invoker.routes import invoker_bp
from .ranger.routes import ranger_bp


app = Quart(__name__)
# app.config.from_object(settings)
app = cors(app, allow_origin=app.config.get("CORS_ALLOWED_ORIGINS"))


@app.before_serving
async def __init__():
    print("Starting the prerequistes from logger")
    _register_blueprints()



def _register_blueprints():
    app.register_blueprint(invoker_bp)
    app.register_blueprint(ranger_bp)
    return

#hypercorn app.server:app