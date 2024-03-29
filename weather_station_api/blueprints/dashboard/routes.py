from flask import Blueprint, render_template, abort
from weather_station_api import models
from weather_station_api.consts import PaginationConsts
from weather_station_api.utils import data_utils, js_modules_utils
from config import ModulesConfig


dashboard = Blueprint("dashboard", __name__, template_folder="templates", static_folder="static", url_prefix="/")


@dashboard.route("/")
def home():
    types = []

    for log in models.Log.__subclasses__():
        types.append({
            "name": log.get_type(),
            "display_name": log.get_display_name()
        })

    return render_template("index.html", logs_types=types)


@dashboard.route("/logs/<log_type>", defaults={"page_id": 1})
@dashboard.route("/logs/<log_type>/<int:page_id>")
def preview_logs_by_type(log_type, page_id):
    log_by_type = models.Log.get_subclass_by_type(log_type)

    if log_by_type:
        paginated_days_data = models.LoggedDay.query.order_by(models.LoggedDay.date.desc())
        paginated_days_data = paginated_days_data.paginate(page=page_id,
                                                           per_page=PaginationConsts.LOGGED_DAY_PER_PAGE)

        daily_logs_struct = data_utils.get_daily_logs_struct(paginated_days_data.items, log_type)
        chart_js_path = js_modules_utils.get_lib_src(ModulesConfig.CHART_JS_NAME)

        return render_template("log_graphs.html",
                               log_type=log_type,
                               logs_pagination=paginated_days_data,
                               paginated_daily_data=daily_logs_struct,
                               chart_js_path=chart_js_path)

    else:
        abort(404)
