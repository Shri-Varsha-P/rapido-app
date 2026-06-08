from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

app = FastAPI()

visitor_count = 0

RIDES = [
    {
        "driver": "Arun",
        "vehicle": "Bike",
        "pickup": "T Nagar",
        "destination": "Guindy",
        "fare": "₹120"
    },
    {
        "driver": "Priya",
        "vehicle": "Auto",
        "pickup": "Velachery",
        "destination": "Tambaram",
        "fare": "₹180"
    },
    {
        "driver": "Rahul",
        "vehicle": "Cab",
        "pickup": "Anna Nagar",
        "destination": "Airport",
        "fare": "₹350"
    }
]

HTML_PAGE = """
<!DOCTYPE html>
<html>

<head>
<title>Rapido Dashboard</title>

<style>

body{
    font-family:Arial;
    background:#fff8e7;
    max-width:1000px;
    margin:auto;
    padding:20px;
}

h1{
    color:#f7b500;
}

.grid{
    display:grid;
    grid-template-columns:repeat(auto-fill,minmax(250px,1fr));
    gap:20px;
}

.card{
    background:white;
    padding:20px;
    border-radius:12px;
    box-shadow:0 2px 8px #ccc;
}

.visitor{
    color:gray;
    margin-bottom:20px;
}

</style>

</head>

<body>

<h1>🏍 Rapido Ride Dashboard</h1>

<div class="visitor">
Visitor #__COUNT__
</div>

<div id="grid" class="grid"></div>

<script>

fetch('/rides')
.then(response => response.json())
.then(data => {

const grid =
document.getElementById('grid');

for(const ride of data.rides){

const card =
document.createElement('div');

card.className='card';

card.innerHTML=`

<h2>${ride.driver}</h2>

<p><b>Vehicle:</b> ${ride.vehicle}</p>

<p><b>Pickup:</b> ${ride.pickup}</p>

<p><b>Destination:</b> ${ride.destination}</p>

<p><b>Fare:</b> ${ride.fare}</p>

`;

grid.appendChild(card);

}

});

</script>

</body>

</html>
"""


@app.get("/rides")
async def get_rides(request: Request):

    client_ip = (
        request.client.host
        if request.client
        else "unknown"
    )

    print(
        f"{client_ip} -> /rides",
        flush=True
    )

    return {
        "rides": RIDES
    }


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    global visitor_count

    visitor_count += 1

    client_ip = (
        request.client.host
        if request.client
        else "unknown"
    )

    print(
        f"{client_ip} -> /",
        flush=True
    )

    return HTMLResponse(
        HTML_PAGE.replace(
            "__COUNT__",
            str(visitor_count)
        )
    )