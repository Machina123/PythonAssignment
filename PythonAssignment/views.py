from django.http import HttpResponse

def index(request):
    resp_string = ""
    if "spotify" in request.GET:
        if request.GET["spotify"] == "success":
            spoti_auth_data = open("spotify_auth.dat", "r")
            resp_string += spoti_auth_data.read()
            spoti_auth_data.close()
        else:
            resp_string += "Response from Spotify Authentication: error"

    return HttpResponse(resp_string)