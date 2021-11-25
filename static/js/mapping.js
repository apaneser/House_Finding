console.log("working");

// Create the map object with a center and zoom level.
let map = L.map('mapid').setView([30.26759, -97.74299], 13);

// We create the tile layer that will be the background of our map.
let streets = L.tileLayer('https://api.mapbox.com/styles/v1/mapbox/outdoors-v11/tiles/{z}/{x}/{y}?access_token={accessToken}', {
attribution: 'Map data © <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery (c) <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    accessToken: API_KEY
});

streets.addTo(map);

let homeData = "/static/result.json";

// Grabbing our GeoJSON data.
d3.json(homeData).then(function(data) {
  // Creating a GeoJSON layer with the retrieved data.
  L.geoJson(data, {
    // We turn each feature into a marker on the map.
    pointToLayer: function(feature, latlng) {
      console.log(feature);
      return L.marker(latlng)
      .bindPopup(
        "<h5>Street Address: " + feature.properties.streetaddress + "</h5>" +
        "<h5>City: " + feature.properties.city + "</h5>" +
        "<h5>Zipcode: " + feature.properties.zipcode + "</h5>" +
        "<h5>Home Type: " + feature.properties.hometype + "</h5>" +
        "<h5>Lot Size (SqFt): " + feature.properties.lotsizesqft + "</h5>" +
        "<h5>Living Area (SqFt): " + feature.properties.livingareasqft + "</h5>" +
        "<h5>Bedrooms: " + feature.properties.numofbedrooms + "</h5>" +
        "<h5>Bathrooms: " + feature.properties.numofbathrooms + "</h5>" +
        "<h5>Stories: " + feature.properties.numofstories + "</h5>" +
        "<h3>Latest Price: " + feature.properties.latestprice + "</h3>"
          );
    }

  }).addTo(map);
});

console.log('checking')