from bottle import Bottle


def create_spec_route(app: Bottle):
    @app.get("/spec", name="Show all routes and descriptions.")
    def spec():
        routes = app.routes
        response = """<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">"""
        response += "<div class='container'><div class='row'><div class='col-lg-7 col-md-8 col-sm-12 mx-auto'><h3>Route List</h3><table class='table table-responsive table-striped'> <tr> <th> PATH </th> <th> Method </th> <th> Description </th> "
        for route in routes:
            if f"<tr><td> {route.rule} </td> <td>{route.method}</td> <td> {route.name} </td> </tr>" not in response:
                response += f"<tr><td> {route.rule} </td> <td>{route.method}</td> <td> {route.name} </td> </tr>"
        response += "</table></div></div></div>"

        return response